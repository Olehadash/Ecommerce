#!C:\Users\User\source\repos\Ecommerce\Ecommerce\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pipenv==9.0.1','console_scripts','pipenv'
__requires__ = 'pipenv==9.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pipenv==9.0.1', 'console_scripts', 'pipenv')()
    )
