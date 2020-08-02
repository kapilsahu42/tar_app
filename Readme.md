# For starting the app in local go to deploy directory in tar_app
docker-compose -f "deploy/docker-compose.yml" up -d --build
data from container will be saved in /tmp/data


# Test directory contains tar_app.postman_collection which can be used 
#to import in postman for testing 

# test_tar_app.py is the pytest file which can be run after local deployment 
# for testing 


# for deployment to minikube run deploy.sh


# docker image can be found in dockerhub as kapilsahu1038/tarapp:latest

Note : minikube with hyerkit has some problem in pulling image from dockerhub