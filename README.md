# ProvisioningControl
The client (NUC or Fixed Node) side of setting up an AERPAW experiment


##Basic Idea

A minimal web server (aerpawNodeControl.py) listens for HTTP GET requests
on port 1887 (the year NCSU was founded, naturally). Basic workflow is

1. Fetch the container. When an experiment is created, a user-supplied container is made
available to the AERPAW reservation system. This is a tar file and is created by the user, in
their own personal development server somewhere, doing a "docker save".

2. Start the container running. Whatever the user specified as the ENTRYPOINT parameter will
begin executing. An area of disk storage will be provided to the running container and
mounted as "/data". As a good rule of thumb, don't write more than a few hundred gigabytes
here without checking with the operations people first.

3. When the "docker run" command terminates, either because the ENTRYPOINT program completed
or because there was some grave error, the "emitDataVolume" command can be used to
copy that filesystem directory back (as a tar file)

4. Finally, even if the container has ceased running, call the "killContainer" command
to shut down (if needed) and delete the container. A "docker prune" will be done to clean up
any residue left behind. It's good to get in the habit of using this - if you're loading
multiple containers and then running them all in one flight then disk space could run out
otherwise.


## REST Entrypoints

```/v1/fetchContainer/ContainerNameGoesHere``` - loads a snapshot of the desired container into the local docker

```/v1/startContainer/ContainerNameGoesHere``` - starts the specified container running (docker run)

```/v1/emitDataVolume/ContainerNameGoesHere``` - returns the contents of the directory that was mounted to the running container as /data. The contents of the resulting tar file is returned
as the HTTP payload (right after the header and the mandatory blank line, naturally).

```/v1/deleteDataVolume/ContainerNameGoesHere``` - deletes the filesystem directory used for
the /data mount point. Handy for freeing up disk space if you're going to run more than one
experiment before landing and re-imaging the device.

```/v1/killContainer/ContainerNameGoesHere``` - brings a swift and violent death to a running container and deletes all traces of it. It's the Sigourney Weaver Option.

