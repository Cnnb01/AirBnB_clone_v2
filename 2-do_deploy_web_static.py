#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""

from fabric.api import *
import os


env.hosts = ['54.242.185.103', '18.235.248.173']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Deploy the archive to web servers"""
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        # run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        return True
    return False
