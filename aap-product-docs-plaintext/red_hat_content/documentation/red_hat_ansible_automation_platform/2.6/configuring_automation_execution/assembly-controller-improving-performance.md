# Chapter 3. Performance tuning for automation controller




Tune your automation controller to optimize performance and scalability. When planning your workload, ensure that you identify your performance and scaling needs, adjust for any limitations, and monitor your deployment.

Automation controller is a distributed system with many components that you can tune, including the following:

- Task system in charge of scheduling jobs
- Control Plane in charge of controlling jobs and processing output
- Execution plane where jobs run
- Web server in charge of serving the API
- WebSocket system that serve and broadcast WebSocket connections and data
- Database used by many components


