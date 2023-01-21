#!/usr/bin/python3
<<<<<<< HEAD
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ Creates a .tgz archive from web_static folder"""
    string_date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "versions/web_static_{}.tgz".format(string_date)

    try:
        if not isdir('versions'):
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(archive))
        return archive
    except:
        return None
=======
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generate a tar archives """
    date_recent = datetime.now().strftime("%Y%m%d%H%M%S")
    path_ruth = "versions/web_static_{}.tgz".format(date_recent)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(path_ruth))
        return path_ruth
    except:
        return None
Foot
>>>>>>> 01b4f5dc7ab3aa1f6d252b0b5481adc2d2a4425e
