from log_folder_parse import *

a = set([])

for l in data:
	a.add(l.get_bad_user_agents())

with open('bad_agents.txt', 'w+') as f:
	for x in a:
		f.write(x + '\n')

a = set([])

for l in data:
	a.add(l.get_bad_requests())

with open('bad_requests.txt', 'w+') as f:
	for x in a:
		f.write(x + '\n')

print('Done.')

