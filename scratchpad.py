import re

text = 'https://www.meetup.com/mracx-multisport/events/304155079/?eventOrigin=group_events_list&_gl=1*14y06o4*_up*MQ..*_ga*MjkwMzg1MDM0LjE3MzM4Njc2NDg.*_ga_NP82XMKW0P*MTczMzg2NzY0Ny4xLjAuMTczMzg2NzY0Ny4wLjAuMA..'

m = re.search('/events/\d+/', text)

print(m.group().split('/')[2])
print(type(m.group()))