#!/usr/bin/env python
# -*- coding: latin-1 -*-
#
# Copyright 2009-2012 Ghent University
#
# This file is part of VSC-tools,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/VSC-tools
#
# VSC-tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# VSC-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VSC-tools. If not, see <http://www.gnu.org/licenses/>.
#
"""Basic setup.py for deploying the shared setup files.

This is required to bootstrap the building of RPMs from our
Python tool repositories.
"""

import os
from distutils.core import setup
import glob

setup(name="shared_setup",
      version="0.2",
      description="A common setup tool for building RPMs for our systems.",
      long_description="""All our python tools are built in the same fashion.
- we like to have a single place to maintain the code
- we like to deploy everything in the same manner
- we like to build RPMs someplace centrally
""",
      license="GPL",
      author="HPC UGent",
      author_email="hpc-admin@lists.ugent.be",
      scripts=glob.glob(os.path.join("bin", "*")),
      package_dir={'vsc': 'lib/vsc'},
      packages=['vsc', 'vsc.install'],
      namespace_packages=['vsc'],
      url="http://www.ugent.be/hpc")
