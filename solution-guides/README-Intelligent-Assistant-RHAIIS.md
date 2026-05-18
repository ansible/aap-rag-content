{% raw %}
# Configuring Ansible Lightspeed intelligent assistant with Red Hat AI Inference Server on RHEL <!-- omit in toc -->

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(56.4263% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/VIH1fhi64QjLKTnOc9ri?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Plugging Red Hat AI Inference Server into Ansible Lightspeed intelligent assistant" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

The Ansible Lightspeed intelligent assistant is a generative AI service embedded directly into the Ansible Automation Platform UI. It offers on-demand expertise to help you administer and manage your automation, while removing some of the friction associated with onboarding, troubleshooting, and maintaining the platform. It provides direct access to trusted documentation and insights, helping you get up to speed with the platform faster, simplify administration, and resolve issues faster.

## Deployment Requirements

- Ansible Automation Platform 2.5 or later running on OpenShift Container Platform (using the Ansible Automation Platform operator).
- A self-hosted Large Language Model (LLM) running through one of the Red Hat AI options:
  - RHEL AI
  - Red Hat AI Inference Server (covered in this article)
  - Red Hat OpenShift AI

This self-hosted approach is ideal for organizations with strict security, compliance, or customization needs. It allows you to maintain full control over your data, model behavior, and costs, ensuring that no sensitive content is exposed while optimizing LLM performance for higher throughput, reduced latency, and cost-effective inference.

**NOTE:** You can also deploy your LLM on RHEL AI using Red Hat Ansible Certified Content Collections. [Click here](https://access.redhat.com/articles/7118390) for instructions on getting started.

## Setting up GPUs for Model Serving

LLMs, as the name suggests, are computationally intensive models that demand substantial processing power to operate. AI accelerators, such as GPU cards, therefore are essential as they significantly accelerate inference processing time and enable efficient parallel computation.

Red Hat AI Inference Server can be deployed on any RHEL machine with supported GPU acceleration, whether bare metal, virtualized, or a cloud instance. For this demonstration, we used an Amazon AWS g6.2xlarge instance, which provides NVIDIA L4 Tensor Core GPUs. On RHEL 9, `nvidia-smi` may report the device as A10G, but this corresponds to the L4 GPU offering in AWS. Depending on your hardware and RHEL version, your steps may vary -- please refer to the official [NVIDIA documentation](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/index.html) for details.

Note that AI Inference Server is compatible with a wide range of hardware accelerators, including other NVIDIA options such as T4, A100, L40S, H100, and H200, as well as AMD ROCm-based devices like the MI210 and MI300X. If you are interested in the second group of devices, please check the [Red Hat AI Inference Server documentation](https://docs.redhat.com/en/documentation/red_hat_ai_inference_server/3.2/html/getting_started/index), as some steps may vary.

One of the pre-requisites for deploying AI Inference Server is installing and configuring the NVIDIA drivers in the host machine. In order to achieve this, you can follow the steps stated in the official [NVIDIA Driver Installation Guide](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/index.html). Below are the exact steps we followed on our AWS g6.2xlarge test environment (RHEL 9 + NVIDIA L4 Tensor Core GPU):

~~~
# 1. Install EPEL (if not already available)
sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm

# 2. Enable NVIDIA CUDA repo
sudo tee /etc/yum.repos.d/cuda-rhel-x86_64.repo > /dev/null <<EOF
[cuda-rhel-x86_64]
name=NVIDIA CUDA Repository
baseurl=https://developer.download.nvidia.com/compute/cuda/repos/rhel9/x86_64
enabled=1
gpgcheck=0
EOF

# 3. Install NVIDIA driver and CUDA toolkit
sudo dnf install -y @nvidia-driver:latest-dkms cuda-toolkit

# 4. Install dependencies
sudo dnf install -y podman

# 5. Reboot to load driver
sudo reboot
~~~

**NOTE:** These steps are specific to our AWS g6.2xlarge (RHEL 9) test environment. If you are using different GPUs or RHEL versions, package names, driver versions, or repo setup may vary.

Once configured, you need to install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) to enable GPU access inside containers. This ensures the inference server can use hardware acceleration.

Begin by enabling the toolkit repository, which is required for accessing the necessary installation packages:
~~~
$ curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
~~~

Once enabled, you should be able to download and install the NVIDIA Container Toolkit packages:
~~~
$ sudo dnf install -y nvidia-container-toolkit
~~~

Now let the toolkit CLI taking care of generating the Container Device interface (CDI) specs for the NVIDIA devices available:
~~~
$ sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia
~~~

Once the NVIDIA Container Toolkit is installed, and the CDI specs have been created, you should be able to use the GPU to run the Red Hat AI Inference Server on top of it. To check that the GPUs are accessible from the container runtime, run the following command:

~~~
$ podman run --rm -it \
--security-opt=label=disable \
--device nvidia.com/gpu=all \
nvcr.io/nvidia/cuda:12.4.1-base-ubi9 \
nvidia-smi
~~~

The output from the previous command should list all available GPUs in the Linux machine.

[image=[src="images/list_of_gpus.png", title="List of available GPUs", alt="List of GPUs", size="LG - Large", data-cp-size="100%", data-cp-align="center", caption="List of available GPUs", lightbox="true"]]

## Configure Red Hat AI Inference Server

Once you have configured the GPUs to be accessible, you can proceed with setting up AI Inference Server. This will enable you to serve LLMs efficiently using the available hardware acceleration. Let's start by creating a volume that will be used to store the cache for AI Inference Server and give it the right permissions:
~~~
$ mkdir -p rhaiis-cache && chmod a+rwX rhaiis-cache
~~~

Then, [obtain your Hugging Face token](https://huggingface.co/docs/hub/en/security-tokens) and paste it into the following command. This will save the token as an environment variable. Additionally, in order to enable authentication when connecting to the model, it is necessary to create an API key. The variables will be loaded into your current shell session:
~~~
$ echo "export HF_TOKEN=<your_HF_token>" >> private.env && \
echo "export API_KEY=<your_api_key>" >> private.env && \
source private.env
~~~

The inference server container image will be pulled from Red Hat's registry. First, you will need to log in to registry.redhat.io with your account credentials.
~~~
$ podman login registry.redhat.io
~~~

Finally, you're ready to run our inference server container. The following command injects the Hugging Face token and your API key as environment variables and mounts the previously created volume to cache model files for faster loading. It also pulls the LLM that we specified in the --model parameter. For the purposes of this article, we're using a Granite 3.3 (8b) model as backend for the Ansible lightspeed intelligent assistant, but you can [check the documentation](https://docs.redhat.com/en/documentation/red_hat_ai_inference_server/3.2/html/validated_models/index) for the latest updates on other validated models.

Because this demonstration was run on an AWS g6.2xlarge instance (NVIDIA L4/A10G GPU), we configured the engine with a --max-model-len of 8192 tokens. This parameter help ensure the model runs within the GPU's available memory without hitting allocation errors. Your values may differ depending on GPU size, model choice, and workload, so always adjust accordingly.

Here is the full command:
~~~
$ podman run --rm -it \
--device nvidia.com/gpu=all \
--security-opt=label=disable \
--shm-size=8GB -p 8000:8000 \
--env "VLLM_API_KEY=$API_KEY" \
--env "HUGGING_FACE_HUB_TOKEN=$HF_TOKEN" \
--env "HF_HUB_OFFLINE=0" \
--env=VLLM_NO_USAGE_STATS=1 \
-v ./rhaiis-cache:/opt/app-root/src/.cache \
registry.redhat.io/rhaiis/vllm-cuda-rhel9:3.0.0 \
--model RedHatAI/granite-3.3-8b-instruct \
--max-model-len 8192
--enable-auto-tool-choice \
--tool-call-parser granite
~~~

**NOTE:** The inference server powering Ansible Lightspeed intelligent assistant requires the `--enable-auto-tool-choice` and `--tool-call-parser` options when starting the container. These flags prepare the model server to handle tool-related requests. While the assistant does not rely on tool calling in its default configuration, these options ensure compatibility with current and future features of Ansible Lightspeed.

When the command execution finishes the container will prompt "INFO: Application startup complete" and it will start serving the Granite model. To perform a simple test, open a new terminal session and execute the following query against the endpoint. Remember to specify the API key you created before:
~~~
$ curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <your_api_key>" \
    -d '{
      "prompt": "What is the capital of France?",
      "max_tokens": 50
}' http://0.0.0.0:8000/v1/completions | jq
~~~

Now, look for the text field in the response which should contain something like: "The capital of France is Paris". If you received a similar response, it means the LLM is being served correctly and you can start making queries and experimenting with it. However, let's take it one step further…

## Connecting the AI Inference Server to Ansible Lightspeed intelligent assistant

Instead of making requests directly to the API, let's configure Ansible Lightspeed intelligent assistant to connect to the self-hosted inference server. This enables all prompts and completions in the Ansible Automation Platform UI to be powered by the model you're serving.

First, ensure that the inference server endpoint is reachable from the Ansible Automation Platform cluster or node. In our case, since the inference server was running on an AWS instance, we configured security group rules to allow inbound TCP traffic on port 8000.

**NOTE:** Detailed instructions for configuring Ansible Lightspeed intelligent assistant on OpenShift, including creating the chatbot secret and updating the AAP CR, are available in the Ansible Automation Platform [documentation for Ansible Lightspeed intelligent assistant](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform/deploying-chatbot-operator).

Now it's time to start working from our Ansible Automation Platform(AAP) deployment on OpenShift. Start by creating a key/value secret in the same namespace as your AAP custom resource (the namespace where the operator installed AAP). The secret must include the chatbot_model, chatbot_url, and chatbot_token.

~~~
apiVersion: v1
kind: Secret
metadata:
  name: chatbot-configuration-secret
  namespace: <aap-namespace>   # e.g., aap
type: Opaque
stringData:
  chatbot_model: RedHatAI/granite-3.3-8b-instruct
  chatbot_url: http://<inference_server_host_ip>:8000/v1
  chatbot_token: <your_api_key>
~~~

Now edit the AAP custom resource (Operator → Installed Operators → Ansible Automation Platform → Locate and select the Ansible Automation Platform custom resource → YAML) and set:
~~~
spec:
  lightspeed:
    disabled: false
    chatbot_config_secret_name: chatbot-configuration-secret
~~~
Save the CR. The operator will reconcile and deploy/update the Ansible Lightspeed service.

The Ansible Lightspeed intelligent assistant should now be ready for prompting in Ansible Automation Platform UI.

---

## Next Steps

| | |
|---|---|
| <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible/trial"><strong>Try Ansible Automation Platform</strong></a> | Start a free 60-day trial and build your first automation workflows |
| <a target="_blank" href="https://www.redhat.com/en/services/consulting"><strong>Red Hat Consulting</strong></a> | Work with Red Hat experts to design, implement, and scale AI-powered automation |
| <a target="_blank" href="https://www.redhat.com/en/services/training-and-certification"><strong>Training and Certification</strong></a> | Build team skills with hands-on courses and industry-recognized certifications |

---

<img width="400" src="https://raw.githubusercontent.com/rhpds/showroom-lb2961-ai-driven-ansible-automation/refs/heads/main/solution_images/aap_logo.png">
{% endraw %}
