for started the app in local go to deploy directory in tar_app
docker-compose -f "deploy/docker-compose.yml" up -d --build

data from container will be saved in /tmp/data


docker push kapilsahu1038/tarapp:latest
minikube with hyerkit has some problem in pulling image from dockerhub