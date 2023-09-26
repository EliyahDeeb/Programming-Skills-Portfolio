#Exercise 3: Print Date and Time

from datetime import datetime
now=datetime.now()

Date1=now.strftime("%d/%m/%Y %H:%M:%S")
print("Today's Date and Time: ",Date1)