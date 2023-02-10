import datetime

from datetime import datetime

import base64
datetime_str = '09/19/22 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')



a = 'eW91ciB0ZXh0'
re = base64.b64decode(a)

print(re, re.decode('utf-8'))

# print(type(datetime_object))
# print(datetime_object)  # printed in default format



# now = datetime.now() # current date and time

# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)

# print()
# print(datetime.utcnow())

# di = {"name": "rawi"}
# print(di.get("name"))
# print(di.get("nam"))
# print(type("rawi") == str)
# print("rawi".__contains__("r"))
# print(":".join(["H0lberton","School","98!"]))
# print(":".join(["H0lberton"]))
s = "/api/v1/stat*"
print(s.__contains__('*'))
s_split = s.split("/")[-1][:-1]
last = s_split[-1]
last_last = last[:-1]
print(s_split)
# print(last)
# print(last_last)
path = "/api/v1/stats"
ex = ["/api/v1/stat*", "/api/v1/status/", "/api/v1/users"]
for route in ex:
  if route.__contains__("*"):
    if route[:-1] in path:
       print(False)