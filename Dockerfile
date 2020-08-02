# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /app

# add the src directory to the container as /app
ADD ./src /app

#copy requirement file 
COPY requirements.txt /tmp

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r /tmp/requirements.txt 

# unblock port 80 for the Flask app to run on
EXPOSE 5001

# execute the Flask app
CMD ["python", "app.py"]

# ENTRYPOINT ["/bin/bash"]