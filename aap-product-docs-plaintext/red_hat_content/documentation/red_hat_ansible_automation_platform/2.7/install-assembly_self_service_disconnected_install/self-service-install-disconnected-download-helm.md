# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Download the helm chart package

Download the Helm chart package and modify the internal image references to point to your disconnected registry. This prepares the installation package for the air-gapped environment.

### Procedure

1.  Add the OpenShift Helm charts repository and update your local cache:


```
helm repo add openshift-helm-charts https://charts.openshift.io/
helm repo update
```

2.  Pull the required version of the chart:


```
helm pull openshift-helm-charts/redhat-rhaap-portal --version x.y.z
```
The chart is saved as a `.tgz` file (for example, `redhat-rhaap-portal-1.0.1.tgz`).

3.  Extract the chart files:


```
tar -xvf redhat-rhaap-portal-x.y.z.tgz
```
This creates a directory with a name similar to `redhat-rhaap-portal-1.0.1/`.

4.  In the `redhat-rhaap-portal/values.yaml` file, replace all `image:` references with the full path to the images in your disconnected registry.
5.  Repack the chart with your modifications:


```
helm package redhat-rhaap-portal-x.y.z
```
A new `.tgz` file is created containing your changes.

