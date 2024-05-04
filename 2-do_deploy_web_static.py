#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""

from fabric.api import put, run
import os
env.hosts = ['54.242.185.103', '18.235.248.173']


def do_deploy(archive_path):
    """Deploy the archive to web servers"""
    if (archive_path is None):
        return False
# extracts the filename from the provided path.
    filename = os.path.basename(archive_path)
    without_extension, _ = os.path.splitext(filename)

    put(archive_path, '/tmp/')
    run(f'tar -xzf {filename} -C '
        f'/data/web_static/releases/{without_extension}')
    run(f'rm --delete {filename}')
    run(f'sudo ln -sf /data/web_static/releases/{without_extension} '
        f'/data/web_static/current')
    return True
