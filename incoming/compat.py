'''
    incoming.compat
    ~~~~~~~~~~~~~~~

    Python 2/3 compatibility code.
'''

import sys

PY2 = sys.version_info[0] == 2

if PY2:
    string_type = str
    iteritems = lambda x: iter(list(x.items()))
else:
    string_type = str
    iteritems = lambda x: iter(list(x.items()))
