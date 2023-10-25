#Exercise 3: Print Date and Time

#'datetime' contains the Date and Time.
# Adding '.now' to datetime (which makes it datetime.now), presents the present date and time.
from datetime import datetime
now=datetime.now()

#A format for showing the date and time is added, one of the formats has been inserted in the following command:
Date1=now.strftime("%d/%m/%Y %H:%M:%S")

print("Today's Date and Time: ",Date1)