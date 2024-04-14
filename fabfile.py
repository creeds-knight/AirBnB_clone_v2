#!/usr/bin/python3
"""this script automates the deployment of web_static using Fabric.
"""

from fabric.api import env, run, put, local, cd, lcd, put
from fabric import task
from fabric import task, Connection, Config

env.hosts = ['54.237.49.126']
env.user = 'ubuntu'
env.key_filename = '/home/kathy2470/.ssh/id_rsa', '/home/kathy2470/.ssh/key.pem'

def deploy():
    """
    Deploy web_static to the server.
    """

    run('mkdir -p /data/web_static/releases/')
    run('mkdir -p /data/web_static/shared/')

    local_path = './web_static'
    remote_path = '/data/web_static/releases/'
    put(local_path, remote_path)

    current_release = run('ls -t /data/web_static/releases/ | head -n 1').strip()
    run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.format(current_release))

    run('chown -R ubuntu:ubuntu /data/')
    run('chmod -R 755 /data/')
