#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This file is part of PyHunspell.

PyHunspell is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyHunspell is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyHunspell.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import subprocess as sp
from distutils.core import setup, Extension

try:
    cflags = sp.check_output('pkg-config --cflags hunspell '.split()).split()
    ldflags = sp.check_output('pkg-config --libs hunspell '.split()).split()
    for flag in ldflags:
        if flag.startswith('-L'):
            lib_dir = flag[2:]
except sp.CalledProcessError:
    sys.stderr.write('Cannot find pkg-config for hunspell.\n'
    'Try setting the PKG_CONFIG_PATH variable.')
    sys.exit(1)

main = Extension('hunspell', 
	define_macros = [('_LINUX',None)],
	sources = ['hunspell.c'],
    extra_link_args = ldflags + ['-Wl,-rpath,'+lib_dir],
	extra_compile_args = cflags + ['-Wall'])

setup(name = "hunspell",
	version = "0.1",
	description = "Module for the Hunspell spellchecker engine",
	author="Sayamindu Dasgupta",
	author_email="sayamindu@gmail.com",
	url="http://code.google.com/p/pyhunspell",
	ext_modules = [main])
