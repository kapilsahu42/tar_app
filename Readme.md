### Problem statement is below

    Implement file store to import and export tar files using micro service architecture and deploy minikube environment using docker and Kubernetes tools
        Expose REST API to import the tar files into store
        Expose REST API to pull the tar file
        Expose REST API to list the store files
        Content can be stored in persistent store or file system

 

### Non-Function Requirements: 
    Documentation using Swagger
    Unit test
    Docker-compose tests 


### For starting the app in local go to deploy directory in tar_app
docker-compose -f "deploy/docker-compose.yml" up -d --build
data from container will be saved in /tmp/data


### Test directory contains tar_app.postman_collection which can be used to import in postman for testing 

### test_tar_app.py is the pytest file which can be run after local deployment for testing 


### for deployment to minikube 
do sh deploy.sh in root directory


### docker image can be found in dockerhub as kapilsahu1038/tarapp:latest

Note : minikube with hyerkit has some problem in pulling image from dockerhub

Note : application api will be exposed to  http://{minikube_ip}:5001/

Note : Applictaion uses sqlite for saving username and passowrd for generating Tokens for API calls 


### swagger dynamic-html documenation in /swagger_doc directory 

### TO DO
docker-compose test 
       