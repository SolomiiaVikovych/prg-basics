###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('enter username ')
password = input('enter password ')

# pattern (criteria) for username and password
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[A-Za-z0-9_]{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print('everything is ok ')
else:
   if not username_match:
      print('invalid username')
   if not password_match:
      print('invalid password')
       