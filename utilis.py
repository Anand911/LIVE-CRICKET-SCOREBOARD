from os import system
from pickle import load
import time
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
			elif(match_stats2['runs_to_win'] is not None):
				print('\n\n\t\t\t',match_stats2['runs_to_win'])
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
