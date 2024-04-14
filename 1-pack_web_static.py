#!/usr/bin/python3
""" A fabric script that archives the contents of web_static"""

from fabric.api import run, env, local
import os
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive """

    if not os.path.exists('versions'):
        os.mkdir('versions')

    now = datetime.now()
    timestmp = now.strftime("%H%m%d%H%M%S")
    archive_name = f"web_static_{timestmp}.tgz"
    command = f"tar -cvzf versions/{archive_name} web_static"

    result = local(command, capture=False)

    if result.succeeded is True:
        return os.path.join('versions', archive_name)
    else:
        return None
