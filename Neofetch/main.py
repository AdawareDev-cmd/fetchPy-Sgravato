import colors
import os
import socket
import uptime


hostpc = socket.gethostname()
username = os.environ.get('USERNAME')


colors.red(''' .----------------. Hostname: %s''' % hostpc)
colors.green('''|          _       |User: %s''' % username )
colors.yellow('''|      _.-'|'-._   |Ram: ''')
colors.blue('''| .__.|    |    |  |Uptime: %s''' % uptime.uptime())
colors.magenta('''|     |_.-'|'-._|  |Ciao''')
colors.cyan('''| '--'|    |    |  |''')
colors.white('''| '--'|_.-'`'-._|  |''')
colors.red('''| '--'          `  |''')
colors.green(''' \'----------------\'''')
colors.reset()

