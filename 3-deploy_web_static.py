#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents
# of the web_static folder and deploy it to servers
""" Fabric script to deploy """
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['35.185.87.254', '52.72.127.245']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"
env.warn_only = True


def deploy():
    """ Do all in one step """
    file_path = do_pack()
    if os.path.exists(file_path):
        deploy = do_deploy(file_path)
        return deploy
    else:
        return False


def do_pack():
    """ compress files """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + file_path + " web_static")
    if os.path.exists(file_path):
        return file_path
    else:
        return False


def do_deploy(archive_path):
    """ upload to web servers and deploy """
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
    try:
        # get file name without extension
        filename = os.path.splitext(os.path.basename(archive_path))[0]
        # upload to /tmp dir to server
        put(local_path=archive_path, remote_path="/tmp")
        # create destination directory
        run("mkdir -p /data/web_static/releases/" + filename + "/")
        # uncompress tar file to a directory
        run("sudo tar -xzf /tmp/" + filename + ".tgz" +
            " -C /data/web_static/releases/" + filename + "/")
        # Delete file uploaded
        run("rm /tmp/" + filename + ".tgz")

        # move files to a previous folder
        run("mv /data/web_static/releases/" + filename +
            "/web_static/* /data/web_static/releases/" + filename + "/")

        # delete that folder
        run("rm -rf /data/web_static/releases/" + filename +
            "/web_static")

        # delete symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")
        # create a new symbolic link
        run("ln -s /data/web_static/releases/" + filename +
            "/ /data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False
