# K8S Example

## Navigate To:
* [Description](#description)
* [Usage](#Usage)
* [Oracle Install Linkerd](https://oracle.github.io/cloudtestdrive/AppDev/cloud-native/livelabs/individual/kubernetes/kubernetes-complete/index.html?lab=linkerd-install)


## Description 

This is a basic example using Kubernetes (Kind Cluster) to deploy multi container pod using a Deployment. This lab is conform by a frontend container wich is running a API based on FastAPI which use the GET Method to request the addtion of one to the second container aka Backend.

## Usage 

### Generate images

Run the next commands:
```
docker build -f Dockerfile_backend -t roid/backend:v1  .
docker build -f Dockerfile_frontend -t roid/frontend:v1  .
docker build -f Dockerfile_frontend_dual_pod -t roid/frontenddualpod:v1  .
```

### Deploy lab

1. Deploy single pod app
    - Run:
    `kubectl apply -f deployment_single_pod.yml`
2. Deploy multi pod app
    - Run:
    `kubectl apply -f deployment-dual-pod.yml`



