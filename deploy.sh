#!/bin/bash


echo "Creating the volume..."

kubectl apply -f ./deploy/persistent-volume.yml
kubectl apply -f ./deploy/persistent-volume-claim.yml

echo "Creating the flask deployment and service..."

kubectl create -f ./deploy/deploy.yml
kubectl create -f ./deploy/deploy-service.yml


echo "Adding the ingress..."

minikube addons enable ingress
kubectl apply -f ./deploy/minikube-ingress.yml