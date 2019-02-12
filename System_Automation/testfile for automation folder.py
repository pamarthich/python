import os
import time
import datetime
import pipes
import sys
import paramiko

db_name = 'test'
date = time.strftime('%Y-%m-%d')
dump_cmd = "mysqldump --databases " + db_name + " -u root -p > " + db_name+"_"+date+".sql"
print(type(dump_cmd))
print(dump_cmd)
