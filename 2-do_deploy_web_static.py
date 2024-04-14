#!/usr/bin/python3
""" Fabric script to distribute an archive to my web servers"""
from fabric.api import env, put, run
from os.path import exists


env.hosts = ['34.227.101.220', '52.86.118.253']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """ Distributes an archive to the web severs """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1]
        foldername = filename.split('.')[0]
        # Create a directory for new version
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            filename, foldername))
        run('rm /tmp/{}'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(foldername))
        print("New version deployed")
        return True

    except Exception as e:
        print(e)
        return False
