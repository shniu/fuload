#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
from subprocess import Popen
import signal
from os.path import abspath, dirname, join

from daemon import Daemon

def handler(signo, frame):
    for child in WorkerManager._childs:
        try:
            child.send_signal(signo)
        except:
            pass

class WorkerManager:
    _childs = []

    def fork(self,exe_args,num):
        for i in range(0,num):
            p = Popen(exe_args)
            WorkerManager._childs.append(p)

        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)

        #for child in WorkerManager._childs:
            #child.send_signal(signal.SIGUSR1)

    def wait():
        for child in WorkerManager._childs:
            child.wait()

if __name__ == "__main__":
    mng = WorkerManager()
    mng.fork("./fl_slave_worker",2)
    mng.wait()