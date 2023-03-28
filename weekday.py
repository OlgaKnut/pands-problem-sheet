# weekday.py
# Author: Olga Knutova
# Description: outputs whether or not today is a weekday

import datetime
### https://www.delftstack.com/howto/python/python-datetime-day-of-week/
from datetime import datetime
day = datetime.today().weekday()
if day < 5:
    print ("Unfortunatly today is a weekday. Go to work!")
else: print ("It is the weekend! Enjoy!")
