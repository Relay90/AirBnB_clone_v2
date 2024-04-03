#!/usr/bin/python3
"""Fabric script to delete out-of-date archives"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your web server IPs
env.user = 'ubuntu'  # Replace with your SSH username
env.key_filename = ['/path/to/your/ssh/private_key']  # Replace with the path to your SSH private key


def do_clean(number=0):
    """Delete out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1

    with cd('/data/web_static/releases'):
        # Get list of archives sorted by modification time
        archives = run('ls -tr').split()

        # Keep only the most recent 'number' of archives
        archives_to_keep = archives[-number:]

        # Delete archives not in the 'archives_to_keep' list
        for archive in archives:
            if archive not in archives_to_keep:
                run('rm -f {}'.format(archive))

    with cd('/home/ubuntu/AirBnB_clone_v2/versions'):
        # Get list of archives sorted by modification time
        archives = run('ls -tr').split()

        # Keep only the most recent 'number' of archives
        archives_to_keep = archives[-number:]

        # Delete archives not in the 'archives_to_keep' list
        for archive in archives:
            if archive not in archives_to_keep:
                run('rm -f {}'.format(archive))
