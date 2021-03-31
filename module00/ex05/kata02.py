import string
from datetime import datetime
import time

# (hour, minutes, year, month, day)
# 09/25/2019 03:30
dt_obj = datetime(3,30,2019,9,25)
date_str = dt_obj.strftime("%H:%M %Y-%m-%d")
print (date_str)