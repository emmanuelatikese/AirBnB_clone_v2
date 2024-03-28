#!/usr/bin/python3
'''fabric on the first try'''

import os
import fabric.api import local
import datetime import datetime


def do_pack():
    try:
        if not os.path.exists("versions"):
            os.makedir("versions")
        arch_dt = datetime.strftime("%Y%m%d%H%M%S")
        arch_name = f"web_static_{arch_dt}.tgz"
        local("tar -czvf versions/{} web_static".format(arch_name))
        return "versions/{}".format(arch_name)
    except Exception as e:
        return None
