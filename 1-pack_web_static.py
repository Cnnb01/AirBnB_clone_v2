#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime


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
