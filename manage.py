# -*- coding: utf-8 -*-

import sys
print sys.path

from core.app import create_app
from flask_script import Manager, Server

app = create_app()
manager = Manager(app)


"""
if __name__ == "__main__":
    manager.add_command('server', Server)
    manager.run()
"""

