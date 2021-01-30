# ProvisioningControl
The client (NUC or Fixed Node) side of setting up an AERPAW experiment


Basic Idea: A minimal web server (aerpawNodeControl.py) listens for HTTP GET requests
on port 1887 (the year NCSU was founded, naturally).

```/v1/fetchContainer/ContainerNameGoesHere``` - loads a snapshot of the desired container into the local docker

```/v1/startContainer/ContainerNameGoesHere``` - starts the specified container running (docker run)

```/v1/startContainerWithMount/ContainerNameGoesHere/DataContainerNameGoesHere``` - runs the specified container with a data container
mounted into the container as "/data". Allows easy input of experiment configuration and output of experiment data

```/v1/dumpContainer/ContainerNameGoesHere``` - dumps container data to /home/aerpaw/dataContainers/ContainerNameGoesHere.docker.tar

```/v1/emitContainer/ContainerNameGoesHere``` - returns the contents of /home/aerpaw/dataContainers/ContainerNameGoesHere.docker.tar

```/v1/killContainer/ContainerNameGoesHere``` - brings a swift and violent death to a running container

