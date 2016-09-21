# coding: utf-8

import os
from datetime import timedelta


class Config(object):

    XNM = 2016
    XQM = 3


config = {
    'develop': Config,
    'test': Config,

    'default': Config
}
