#!/usr/bin/python3
# Script is a Fabfile to delete out-of-date archives.
import os
from fabric.api import *


env.hosts = ["34.203.33.204", "35.153.50.26"]

def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    number = 1 if int(number) == 0 else int(number)

    arc = sorted(os.listdir("versions"))
    [arc.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arc]

    with cd("/data/web_static/releases"):
        arc = run("ls -tr").split()
        arc = [a for a in arc if "web_static_" in a]
        [arc.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arc]
