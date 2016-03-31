# Authors: Amit Kapoor and Bargava Subramanian
# Copyright (c) 2016 Amit Kapoor 
# License: MIT License

"""
    This script will check if the environment setup is correct for the workshop.

    To run, please execute the following command from the command prompt
               >>> python check_env.py
    
    The output will indicate if any of the libraries are missing or need to be updated. 

    This script is inspired from https://github.com/fonnesbeck/scipy2015_tutorial/blob/master/check_env.py
"""

from __future__ import print_function

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

import sys
try:
    import importlib
except ImportError:
    print(FAIL, "Python version 2.7 is required, but %s is installed." % sys.version)
from distutils.version import LooseVersion as Version

def import_version(pkg, min_ver, fail_msg=""):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        if((pkg=="spacy" or pkg=="wordcloud") and (mod > 0)):
            print(OK, '%s ' % (pkg))
        else:
        #else:
            version = getattr(mod, "__version__", 0) or getattr(mod, "VERSION", 0)
            if Version(version) < min_ver:
                print(FAIL, "%s version %s or higher required, but %s installed."
                    % (lib, min_ver, version))
            else:
               print(OK, '%s version %s' % (pkg, version))
    except ImportError:
        print(FAIL, '%s not installed. %s' % (pkg, fail_msg))
    return mod


# first check the python version
print('Using python in', sys.prefix)
print(sys.version)
pyversion = Version(sys.version)
if pyversion < "3":
    print(FAIL, "Python version 3 is required, but %s is installed." % sys.version)
elif pyversion >= "2":
    if pyversion == "2.7":
        print(FAIL, "Python version 2.7 is installed. Please upgrade to version 3." )
else:
    print(FAIL, "Unknown Python version: %s" % sys.version)

print()
requirements = {

    'IPython'    : '4.0.3',
    'jupyter'    :'1.0.0',
    'matplotlib' :'1.5.0',
    'numpy'      : '1.10.4',
    'pandas'     : '0.17.1',
    'scipy'      : '0.17.0',
    'sklearn'    : '0.17',
    'seaborn'    :'0.6.0',
    'statsmodels':'0.6.1'
}

# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)


    
