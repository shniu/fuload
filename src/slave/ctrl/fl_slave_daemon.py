#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#  Author:          dantezhu - http://www.vimer.cn
#  Email:           zny2008@gmail.com
#  FileName:        fl_slave_daemon.py
#  Description:     通过daemon继承的子类
#  Version:         1.0
#  LastChange:      2010-12-13 11:36:55
#  History:         
#=============================================================================
'''
import sys
import os
from os.path import abspath, dirname, join
from daemon import Daemon

from fl_slave_ctrl import SlaveCtrl
from fl_slave_conf import DAEMON_PIDFILE,DAEMON_STDIN,DAEMON_STDOUT,DAEMON_STDERR

mpath = abspath(dirname(__file__))

class SlaveDaemon(Daemon):
    def _run(self):
        os.chdir(mpath)

        srv = SlaveCtrl()
        srv.start()

if __name__ == "__main__":
    daemon = SlaveDaemon(DAEMON_PIDFILE,DAEMON_STDIN,DAEMON_STDOUT,DAEMON_STDERR)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
