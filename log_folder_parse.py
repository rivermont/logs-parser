from log_parser import *
from os import listdir, stat
from os.path import join, isfile


def thing():
	with open('data.txt', 'w+', encoding='utf_8') as f:
		for k in data:
			k.whitelist_ips(['192.168.0.201', '192.168.0.101', '24.40.136.85'])
			for j in k.get_foreign_requests():
				f.write(j + '\n')


def thing2():
	with open('data.txt', 'w+', encoding='utf_8') as f:
		for k in data:
			k.whitelist_ips(['192.168.0.201', '192.168.0.101', '24.40.136.85'])
			for j in k.get_bad_requests():
				f.write(j + '\n')


folder = input('Folder to parse logs from: ')
a = input('Number of top files to exclude: ')

files = listdir(folder)

dat = {}
sizes = []
data = []

for f in files:
	size = stat(folder + '/' + f).st_size
	dat.update({size: f})
	sizes.append(size)

sizes.sort(reverse=True)

for i in sizes[int(a):]:
	if isfile(join(folder, dat[i])):
		print('Processing {0}'.format(dat[i]))
		data.append(parse_file(folder + '/' + dat[i], 's'))

thing2()
