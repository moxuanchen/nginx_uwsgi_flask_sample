# -*- coding: utf-8 -*-

from core.app import create_app
from flask_script import Manager, Server

manager = Manager(create_app())


if __name__ == "__main__":
    manager.add_command('server', Server)
    manager.run()

