# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fabric.api import cd, env, run


env.hosts = ["webmanager@haribo.tag.sk:6791"]
env.shell = "/bin/zsh -l -c"


def deploy():
    with cd("/var/www/tag.sk/polska/"):
        run("git pull")
