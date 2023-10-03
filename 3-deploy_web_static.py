#!/usr/bin/python3
# Script is a Fabfile to create and distribute an archive to a web server
import os.path
from datetime import datetime
from fabric.api import env, run, local, put


env.hosts = ["34.203.33.204", "35.153.50.26"]

def __pack():
    """
    Create a tar gzipped archive of the directory web_static
    """
    date = datetime.utcnow()
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second

    file_output = "versions/web_static_{}{}{}{}{}{}.tgz".format(year,
                                                                month,
                                                                day,
                                                                hour,
                                                                minute,
                                                                second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_output)).failed is True:
        return None
    return file_output

def __deploy(archive_path):
    """
    Distributes an archive to web server.
    """
    if os.path.isfile(archive_path) is False:
        return False
    f = archive_path.split("/")[-1]
    name = f.split(".")[0]

    if put(archive_path, "/tmp/{}".format(f)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(f, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(f)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True

def deploy():
    """
    Create and distribute an archive to a web server
    """
    f = __pack()
    if f is None:
        return False
    return __deploy(f)
