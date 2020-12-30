from pickle import dump
creds={'userid':'pyadmin','password':'pycharm123'}
with open('admin.dat','wb') as u_file:
	dump(creds, u_file)

