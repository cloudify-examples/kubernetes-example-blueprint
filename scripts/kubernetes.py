#!/usr/bin/env python

import os
import subprocess
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from cloudify.exceptions import NonRecoverableError
from fabric.api import run, put

work_environment = os.environ.copy()


def start_app(command, config_path, filepath_agent):

    filepath_manager = ctx.download_resource(config_path)
    put(filepath_manager, filepath_agent)
    fabric_command = '{0} {1}'.format(command, filepath_agent)
    ctx.logger.info('Command: {0}'.format(fabric_command))
    run(fabric_command)
    return
