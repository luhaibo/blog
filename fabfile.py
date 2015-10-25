from __future__ import print_function, unicode_literals
from future.builtins import open

import os
import re
import sys
from contextlib import contextmanager
from functools import wraps
from getpass import getpass, getuser
from glob import glob
from importlib import import_module
from posixpath import join

real_project_name="mmysit"
from mezzanine.utils.conf import real_project_name

from fabric.api import abort, env, cd, prefix, sudo as _sudo, run as _run, \
    hide, task, local
from fabric.context_managers import settings as fab_settings
from fabric.contrib.console import confirm
from fabric.contrib.files import exists, upload_template
from fabric.contrib.project import rsync_project
from fabric.colors import yellow, green, blue, red
from fabric.decorators import hosts




