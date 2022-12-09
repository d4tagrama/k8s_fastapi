# K8S Example

## Navigate To:
* [Description](#description)
* [Installation](#installation)
* [Oracle Install Linkerd](https://oracle.github.io/cloudtestdrive/AppDev/cloud-native/livelabs/individual/kubernetes/kubernetes-complete/index.html?lab=linkerd-install)


## Description 

This is a basic example using Kubernetes (Kind Cluster) to deploy multi container pod using a Deployment. This lab is conform by a frontend container wich is running a API based on FastAPI which use the GET Method to request the addtion of one to the second container aka Backend.

## Instalation 

`kubectl apply -f deployment_multicontainer.yml`


