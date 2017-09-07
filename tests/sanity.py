#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This Modularity Testing Framework helps you to write tests for modules
# Copyright (C) 2017 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# he Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors: Dominika Hodovska <dhodovsk@redhat.com>
#

from avocado import main
from moduleframework import module_framework
from ftplib import FTP
import time


class FTPSanityTest(module_framework.AvocadoTest):
    """
    :avocado: enable
    """

    def setUp(self):
        super(self.__class__,self).setUp()
        self.start()
        time.sleep(2)
        self.run('touch /etc/vsftpd/user_list')
        self.ftp = FTP('localhost')
        self.ftp.login()

    def tearDown(self):
        super(self.__class__, self).tearDown()
        self.ftp.quit()

    def test_list_files(self):
        self.ftp.cwd('forest')
        out = self.ftp.retrlines('LIST')
        if 'spruce.txt' not in out:
            raise AssertionError('Failed to list files')

    def test_put_file(self):
        file = open('files/alien.txt', 'rb')
        self.ftp.storlines('STOR alien.txt', file)
        file.close()

    def test_get_file(self):
        self.ftp.cwd('forest')
        file = open('pine.txt', 'wb')
        self.ftp.retrlines('RETR pine.txt', file.write)
        file.close()

if __name__ == '__main__':
    main()