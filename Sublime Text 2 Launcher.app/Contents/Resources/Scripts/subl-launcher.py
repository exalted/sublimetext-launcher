#!/usr/bin/env python

import sys
from urlparse import urlparse
from urlparse import parse_qs
from urllib import unquote
import subprocess

x = parse_qs(urlparse(unquote(sys.argv[1])).path)
path = urlparse(x['?url'][0]).path
line = x['line'][0]
subprocess.call(['/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl', '%s:%s' % (path, line)])
