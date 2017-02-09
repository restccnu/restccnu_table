# coding: utf-8

import os
from datetime import timedelta


class Config(object):

    XNM = os.getenv("RESTCCNU_XNM")
    XQM = os.getenv("RESTCCNU_XQM")

config = {
    'develop': Config,
    'test': Config,

    'default': Config
}
