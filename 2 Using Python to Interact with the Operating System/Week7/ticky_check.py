#!/usr/bin/env python3

import re

'''
For each log entry, you'll have to first check if it matches the INFO or ERROR message formats. You should use regular expressions for this. When you get a successful match, add one to the corresponding value in the per_user dictionary. If you get an ERROR message, add one to the corresponding entry in the error dictionary by using proper data structure.
'''

# per_user = {user1 : {'INFO': count, 'ERROR': count}...}


per_user = {}
errors = {}

file = open('syslog.log')

for line in file.readlines():
    # get the message. Either INFO or ERROR
    pattern = r'(?:INFO|ERROR) [\w\s\[\]()\.#\']+'
    l = re.search(pattern, line)
    s,e = l.span()
    message = line[s:e]

    # get the user associated with the message
    pattern2 = r'\([\w\.]+\)'
    l2 = re.search(pattern2, message)
    s,e = l2.span()
    user = message[s+1:e-1]

    if user not in per_user:
            per_user[user] = {'INFO':0, 'ERROR':0}

    if message.startswith('INFO'):
        per_user[user]['INFO'] += 1

    else:
        # it's an error message
        err_message = message[6:message.find('(')].strip()
        
        per_user[user]['ERROR'] += 1

        if err_message not in errors:
            errors[err_message] = 1

        else:
            errors[err_message] += 1

per_user = {k:per_user[k] for k in sorted(per_user)}
errors = {k : errors[k] for k in sorted(errors, key = lambda i: errors[i])[::-1]}

with open('user_statistics.csv', 'a') as csvf:
    csvf.write('Username,INFO,ERROR')

    for user in per_user:
        s = '\n' + user + "," + str(per_user[user]['INFO']) + ',' + str(per_user[user]['ERROR'])
        csvf.write(s)

with open('error_message.csv', 'a') as e:
    e.write("Error,Count")

    for error in errors:
        s = '\n' + error + ',' + str(errors[error])
        e.write(s)

file.close()
