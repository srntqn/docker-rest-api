# How to use

## Local development server

Start server:

```bash
python server.py
```

## Minikube and skaffold

Install additional software:

1. [Docker](https://docs.docker.com/install/)
2. [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
3. [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl)
4. [Skaffold](https://github.com/GoogleContainerTools/skaffold#install)

Start minikube and development skaffold server:

```bash
minikube start
skaffold dev
```

Configure port-forwarding (if not enabled in skaffold by default):

```bash
kubectl port-forward docker-py 5000:5000
```