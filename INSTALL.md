# Installing aerpawNodeAgent
aerpawNodeAgent is a small python program and some scripts that
allow an aerpaw client node to load and execute containers, return
the data produced by the job, and finally clean up after the
experiments are done running.

## Installation Steps

1. Copy aerpawNodeAgent.py, fetchContainer, and
startContainer to /usr/local/bin

1. Copy aerpawNodeAgent.json to /etc

1. Edit aerpawNodeAgent.json and change the "containerStore" URL to a
more production-oriented value. "http://152.14.188.11" is a good
choice (that points to aerpaw-ops-server). Note that there must *not*
be a trailing slash.

1. Create the directory hierarchy for fetching
and running containers and virtual machines. See below...

1. Optionally, install the python virtual environment package
"venv". This isn't necessary because the only python modules used are
the ones that come with a basic python3 installation. This could
become a good idea if you know you're going

1. cp aerpawNodeAgent.initsh /etc/init.d/aerpawNodeAgent

1. /etc/init.d/aerpawNodeAgent start

