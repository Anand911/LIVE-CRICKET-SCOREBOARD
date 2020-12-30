from pickle import load
from randgenrator import rand
from match import start_match
from os import system
import time
mcode=''
symbol='*'
def scoreboard(match_stats,bat_stats,bowl_stats):
    print('_________________________________________________________________________________________________\n')
    score_board_format1=f"\t\t\t{'BATTING':<15}{'RUNS':^10}{'BALLS':^8}{'4s':^7}{'6s':^7}{'S/R':^7}{'STATUS':>9}"
    score_board_format2="\t\t\tBOWLING    OVER    MAIDEN    WICKET    RUNS    ECONOMY"
    print(score_board_format1)
    score_format="\t\t\t{batsman:<15}{runs:^8}{balls:^8}{4s:^9}{6s:^8}{S/R:^8}{status:>6}"
    score_format_strike="\t\t       *{batsman:<15}{runs:^8}{balls:^8}{4s:^9}{6s:^8}{S/R:^8}{status:>6}"
    bowl_format="\t\t\t{bowler:<10}{over:^10}{maiden:^8}{wickets:^8}{runs:^8}{econ:>7}"
    #score_format.format(item for item in lis1 )
    for batsman in bat_stats:
        if batsman['strike']:
            print(score_format_strike.format(**batsman))
        else:
            print(score_format.format(**batsman))
    print('_________________________________________________________________________________________________\n')
    print(score_board_format2)
    if bowl_stats is not None:
        for bowler in bowl_stats:
            print(bowl_format.format(**bowler))
def user():
	with open('mcode.txt','r') as mfile:
		mcodes=mfile.read().split('\n')
	print('=================================================================================================\n')
	count=1
	for mcode in mcodes[:len(mcodes)-1]:
		print('Match Number: ',count)
		count+=1
		fname='innings/1innings_'+mcode+'.txt'
		with open(fname,'rb') as ifile:
			stats=load(ifile)
		match_stats1=stats[0]
		if count>=5:
			print(match_stats1['date_time'])
		print('\t\t\t',match_stats1['team1']+' vs '+match_stats1['team2'],'\n')
		if(match_stats1['status']=='1st innings'):
			print('\t\t\t',match_stats1['1st_innings'])
		else:
			fname='innings/2innings_'+mcode+'.txt'
			with open(fname,'rb') as ifile:
				stats=load(ifile)
			match_stats2=stats[0]
			print('\t\t\t',match_stats1['1st_innings'])
			print('\t\t\t',match_stats2['2nd_innings'],end='')
			print('\tTARGET: ',match_stats2['target'])
			if(match_stats2['status']=='completed'):
				print('\t\t\t',match_stats2['result'])
		print('=================================================================================================\n')
	num=int(input('\nEnter the Match No. to view(0 to go BACK):'))
	mcode=mcodes[num-1]
	ch=1
	while True:
		if num==0:
			break
		if ch==1:
			matchview(mcode)
		elif ch==0:
			break
		ch=int(input('ENTER 1 TO REFRESH 0 TO GO BACK:'))
	
def matchview(mcode):
	system('cls')
	with open('mcode.txt','r') as mfile:
		mcodes=mfile.read().split('\n')
	if mcode in mcodes:
		print('\t\t\tMATCH LOADING....')  #iDWz
		time.sleep(2)
		system('cls')
		fname='innings/1innings_'+mcode+'.txt'
		with open(fname,'rb') as ifile:
			stats=load(ifile)
		match_stats1,bat_stats1,bowl_stats1=stats
		if(match_stats1['status']=='1st innings'):
			print('\t\t\t',match_stats1['1st_innings'])
			scoreboard(match_stats1, bat_stats1, bowl_stats1)
		else:
			fname='innings/2innings_'+mcode+'.txt'
			with open(fname,'rb') as ifile:
				stats=load(ifile)
			match_stats2,bat_stats2,bowl_stats2=stats
			print('\t\t\t',match_stats1['1st_innings'])
			print('\t\t\t',match_stats2['2nd_innings'],end='')
			print('\tTARGET: ',match_stats2['target'])
			print('\n\t\t',match_stats1['score1'][0])
			scoreboard(match_stats1, bat_stats1, bowl_stats1)
			print('=================================================================================================\n')
			print('\n\t\t',match_stats2['score2'][0])
			scoreboard(match_stats2, bat_stats2, bowl_stats2)
			if(match_stats2['status']=='completed'):
				print('\n\n\t\t\t',match_stats2['result'])
	else:
		pass
def authenticate(uid,pswd):
	with open('admin.dat','rb') as u_file:
		creds=load(u_file)
		if uid is not None:
			if uid==creds['userid'] and pswd==creds['password']:
				creds={}
				return True
		else:
			return False
def get_toss(team1_name,team2_name):
	print('WHO WON THE TOSS:\n1.'+team1_name+'\n2.'+team2_name)
	ch=int(input())
	if(ch==1):
		won_toss=team1_name
	elif(ch==2):
		won_toss=team2_name
	print(won_toss+' won the toss and choose to:\n1.BAT first\n2.BOWL first')
	ch=int(input())
	if(ch==1):
		toss='BAT'
	elif(ch==2):
		toss='BOWL'
	return won_toss,toss

def load_match():
	mcode=input('Enter the Match code: ')
	with open('mcode.txt','r') as mfile:
		mcodes=mfile.read().split('\n')
		print(mcodes)
	if mcode in mcodes:
		print('\t\t\tMATCH LOADING....')  #iDWz
		time.sleep(2)
		fname='team_'+mcode+'.txt'
		with open(fname,'r') as tfile:
			team=tfile.read().split('\n')
		pos=team.index('TEAM')
		team1=team[0:pos]
		team1_name=team1[0]
		team2=team[pos+1:]
		team2_name=team2[0]
		print('\t\t\t\t '+team1_name+' vs '+team2_name)
		for i in range(12):
			print('\t\t\t'+team1[i]+'\t\t\t'+team2[i])
		won_toss,toss=get_toss(team1_name,team2_name)
		if toss is not None:
			print(won_toss+' won the toss and choose to '+toss)
		team=zip(team1,team2)
		start_match(mcode,team,won_toss,toss,2)
		#1
		# continue_match(mcode,team)
	else:
		print('\t\t\tNo Match Exist')

def create_match():
	mcode=rand(4)
	with open('mcode.txt','a') as mfile:
		mfile.write(mcode+'\n')
	over=int(input('ENTER THE NUMBER OF OVERS: '))
	#get team details
	team=[]
	for teams in range(2):
		if(teams==1):
			team.append('TEAM')
		t=input('\nENTER TEAM NAME: ')
		team.append(t)
		print(' ENTER PLAYERS OF TEAM '+t+'(ADD (c) for Captain and (wk) for WicketKeeper) :')
		for players in range(11):
			print('PLAYER ',players+1,end=" ")
			p=input('\t\t\t')
			team.append(p)
	fname='teams/team_'+mcode+'.txt'
	str_team='\n'.join(team)
	with open(fname,'w') as tfile:
		tfile.write(str_team)
	pos=team.index('TEAM')
	team1=team[0:pos]
	team1_name=team1[0]
	team2=team[pos+1:]
	team2_name=team2[0]
	system('cls')
	print('\nMATCH CODE=',mcode,'\n\n')
	time.sleep(1)
	print('\t\t\t\t '+f"{team1_name:<6}vs{team2_name:>6}")
	for i in range(12):
		print('\t\t\t'+f"{team1[i]:<20}{team2[i]:>20}")
	won_toss,toss=get_toss(team1_name,team2_name)
	print(won_toss+' won the toss and choose to'+toss)
	team=zip(team1,team2)
	start_match(mcode,team,won_toss,toss,over)

def delete_match():
	system('cls')
	mcode=input('Enter The match Code to be deleted: ')
	with open('mcode.txt','r') as mfile:
		mcodes=mfile.read().split('\n')
	if mcode in mcodes:
		ch=input('\nARE YOU SURE YOU WANT TO DELETE THIS MATCH(*ALL THE DATA WILL BE LOST)(y/n):')
		if ch=='y':
			fname1='team_'+mcode+'.txt'
			fname2='1innings_'+mcode+'.txt'
			fname3='2innings_'+mcode+'.txt'
			mcodes.remove(mcode)
			mcodes_str='\n'.join(mcodes)
			with open('mcode.txt','w') as mfile:
				mfile.write(mcodes_str)
			print('\t\t\tDELETED SUCESSFULLY!!')
		else:
			print('\t\t\tMATCH NOT DELETED!!')
def admin():
	print('\t\t\tADMIN MODE')
	user=''
	pwd=''
	user=input('\n\t\t\tUSERID: ')
	pwd=input('\n\t\t\tPASSWORD:')
	is_authenticated=authenticate(user, pwd)
	if is_authenticated:
		print('\t\t\tLOGIN SUCCESSFULL!!')
		time.sleep(2)
		system('cls')
		while True:
			print('\t\t\tADMIN PAGE')
			print('\t\t\t1.CREATE MATCH\n\t\t\t2.DELETE MATCH\n\t\t\t3.BACK')
			ch=int(input('\t\t\tENTER A CHOICE:'))
			if(ch==1):
				create_match()
			elif ch==2:
				delete_match()
			elif ch==3:
				break
	else:
		print('\t\t\tWRONG CREDENTIALS!!')
		

