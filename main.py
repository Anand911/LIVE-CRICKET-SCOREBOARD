from userinterface import user,admin
from os import system

while True:
	system('cls')
	print('\t\t\t**LIVE CRICKET SCORE BOARD**')
	print('\n\t\t\t1.VIEW SCORE')
	print('\n\t\t\t2.ADMIN(UPDATE SCORE)')
	print('\n\t\t\t3.EXIT')
	ch=int(input('\n\t\t\tENTER A CHOICE: '))
	if ch==1:
		system('cls')
		user()
	if ch==2:
		system('cls')
		admin()
	if ch==3:
		break

