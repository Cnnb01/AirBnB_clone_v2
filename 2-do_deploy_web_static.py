#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""

from fabric.api import *
import os
from datetime import datetime


env.hosts = ['54.242.185.103', '18.235.248.173']
env.user = "ubuntu"


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_path = f"versions/web_static_{timestamp}.tgz"

    local('mkdir -p versions')

    created_archive = local(f"tar cf {archive_path} web_static")

    if created_archive:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """Deploy the archive to web servers"""
    if (archive_path is None):
        return False
# extracts the filename and folder name
    filename = os.path.basename(archive_path)
    folder_name = os.path.splitext(filename)[0]

    remote_tmp_path = f'/tmp/{filename}'
    remote_extract_path = f'/data/web_static/releases/{folder_name}'

    # Upload the archive to /tmp/ directory
    put(archive_path, remote_tmp_path)

    # Create the release directory
    run(f'mkdir -p {remote_extract_path}')

    # Extract the archive
    run(f'tar -xzf {remote_tmp_path} -C {remote_extract_path}')

    # Delete the uploaded archive
    run(f'rm {remote_tmp_path}')

    # Move contents to proper location and remove old directory
    run(f'mv -f {remote_extract_path}/web_static/* {remote_extract_path}/')
    run(f'rm -rf {remote_extract_path}/web_static')

    # Update symbolic link
    run(f'rm -rf /data/web_static/current')
    run(f'ln -s {remote_extract_path} /data/web_static/current')
    return True
