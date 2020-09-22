#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shlex
import signal
import subprocess
from time import sleep

import allure
import pytest


@pytest.fixture(scope='module', autouse=True)
def record():
    cmd = shlex.split('scrcpy --record test.mp4')
    p = subprocess.Popen(cmd)
    yield
    os.popen('taskkill.exe/pid:' + str(p.pid))
    sleep(1)
    with open('test.mp4', 'rb') as f:
        content = f.read()
    allure.attach(content, attachment_type=allure.attachment_type.MP4)