#!/usr/bin/python3
from os import path, makedirs
from fabric.api import local
from datetime import datetime


def do_pack():
	'''This is all about creating achieve'''

    try:
        if not path.exists("versions"):
            makedirs("versions")
        arch_dt = datetime.strftime("%Y%m%d%H%M%S")
        arch_name = "web_static_{}.tgz".format(arch_dt)
        local("tar -czvf versions/{} web_static".format(arch_name))
        return "versions/{}".format(arch_name)
    except Exception as e:
        return None
