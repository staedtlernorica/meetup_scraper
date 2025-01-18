# import re

# text = 'https://www.meetup.com/mracx-multisport/events/304155079/?eventOrigin=group_events_list&_gl=1*14y06o4*_up*MQ..*_ga*MjkwMzg1MDM0LjE3MzM4Njc2NDg.*_ga_NP82XMKW0P*MTczMzg2NzY0Ny4xLjAuMTczMzg2NzY0Ny4wLjAuMA..'

# m = re.search('/events/\d+/', text)

# print(m.group().split('/')[2])
# print(type(m.group()))


import re

# a = "https://www.meetup.com/mracx-multisport/events/303075566/?eventOrigin=group_events_list"
# b = re.split('\/\?', a)

# print(b[0] + '/')


with open('all past mracx events.txt', 'r') as file:
    data = file.read()
events = eval(data)
o = []
for i in events:
    o.append(re.split('\/\?', i)[0] + '/')

# with open('formatted past events.txt', 'w') as file:
#     file.write('[\n')
#     [file.write(f"    '{item}',\n") for item in o]
#     file.write(']\n')