# ALIF81_DevOps

## Build de l'image

```bash
docker build -t py3.14-fastapi .
docker tag 1dsd512s0d antonind5/py3.14-fastapi:latest
docker push antonind5/py3.14-fastapi:latest
docker run -dit -p 8000:8000 antonind5/py3.14-fastapi:latest
```

## Déploiement avec kubernetes

```bash
# On créé un cluster kubernetes
minikube start

# L'url du dashboard minikube (ex: https://127.0.0.1:59828) pour avoir le dashboard

# On vérifie que le cluster est actif
minikube status
kubectl cluster-info

# On regarde l'ensemble des nodes dans le cluster
kubectl get nodes

# On déploie les applications
kubectl apply -f deployment.yaml
# kubectl delete deployments devops-cours
kubectl describe deployment nginx-deployment

# On affiche les pods pour l'un des app déployées
kubectl get pods
kubectl get pods -l app=fastapi

# On crée un service qui va permettre d'exposer un ensemble de ports pour le déploiement
kubectl apply -f service.yaml
minikube service fastapi-service

# On crée un loadbalancer service
kubectl delete services fastapi-service
kubectl apply -f service.yaml
kubectl apply -f loadbalencer_service.yaml
minikube service loadbalancer
```