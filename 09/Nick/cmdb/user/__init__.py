#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/12/6日19点35分
from flask import Flask
import os

# flask框架定义
app = Flask(__name__)
# session_key定义
# app.secret_key = os.urandom(32)
app.secret_key = '\xabv\xb2\x00\xb8\xd3\xde\xac\x84=\xf8*\xaa\xad\xf5%\x83\xd0\x08P]pG\x18\xa9:\xf8pm\x8f\x18\xb1'

import views