#!/usr/bin/python3
# Script is a fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
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
