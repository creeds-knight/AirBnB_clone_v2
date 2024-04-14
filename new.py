from fabric import Connection
import os
from datetime import datetime


c = Connection('ubuntu@34.227.101.220')

c.local('ls -l')
