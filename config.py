#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

"""
    config.py
    ~~~~~~~~~~~

    basic configuration

    :copyright: (c) 2013.
    :license: BSD, see LICENSE for more details.
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# configuration page num
PER_PAGE = 10

# configuration mysql
#SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % ('luhaibo', 'luhaibo', '127.0.0.1', 'pythonpub1')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
USERNAME = 'luhaibo'
PASSWORD = 'luhaibo'

UPLOAD_FOLDER = './static/upload/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

RECAPTCHA_PUBLIC_KEY = '6Ld4rwITAAAAAKUD5AntlHi7HL36W2vHJQOIjQmA'
RECAPTCHA_PRIVATE_KEY = '6Ld4rwITAAAAAFE8nTS852QbsqCBx1mN8D4BqenE'
