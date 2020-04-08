#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents
# of the web_static folder from AirBnB Clone repo.
""" Fabric script to deploy """
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + file_path + " web_static")
    if os.path.exists(file_path):
        pass
    else:
        return None
