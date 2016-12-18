# kubernetes-example-blueprint

Use Cloudify to deploy Mongo using Kubernetes

## Requirements

* An existing Kubernetes cluster networked with a Cloudify Manager.
* A host with the kubectl executable installed, and is configured to control the Kubernetes cluster, and that is accessible via SSH and only requires username, IP, and SSH key to authenticate.

## How to install

If you have already initialized your Cloudify CLI to connect to the Cloudify Manager, you can run:

`cfy install -p ~/Desktop/example-kubernetes/blueprint.yaml -i kubernetes_master_ip=[Kubernetes Cluster Master IP]`
