#!/usr/bin/python3
"""
This fabfile distributes an archive to my web servers
"""

import os
from fabric.api import *
from datetime import datetime


env.hosts = ['54.242.185.103', '18.235.248.173']
env.user = "ubuntu"


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_filename = f"versions/web_static_{timestamp}.tgz"

    local('mkdir -p versions')

    created_archive = local(f"tar -cvzf {archive_filename} web_static")

    if created_archive:
        return archive_filename
    else:
        return None


def do_deploy(archive_path):
    '''use os module to check for valid file path'''
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        return True
    return False


def deploy():
    """
    Create and archive and get its path
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
