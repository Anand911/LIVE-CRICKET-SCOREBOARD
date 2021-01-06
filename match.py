from os import system
from datetime import datetime
from matchclass import matchstats
from batting import batting
from bowling import bowling
from pickle import dump,load
import time
t_score=0
t_wickets=0
bat_stats=[]
bowl_stats=[]
bowl_list=[]
save_data=[]
def disp_players(team):
    count=0
    for players in team[1:]:
        count=count+1
        print(str(count)+'.'+players)

def is_valid(ch):
    valid_inputs=('0','1','2','3','4','5','6','W','EXIT','Nb','Wd','Lb','b')
    if ch in valid_inputs:
        return True
    else:
        return False
def save(fname,match_stats,bat_stats,bowl_stats):
    stats=[]
    stats.append(match_stats)
    stats.append(bat_stats)
    stats.append(bowl_stats)
    with open(fname,'wb') as ifile:
        dump(stats,ifile)

def scoreboard(match_stats,bat_stats,bowl_stats):
    if(match_stats['status']=='1st innings'):
        print('\t\t\t',match_stats['1st_innings'])
    elif(match_stats['status']=='2nd innings'):
        print('\t\t\t',match_stats['1st_innings'])
        print('\t\t\t',match_stats['2nd_innings'])
        print('\tTARGET: ',match_stats['target'])
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
def go_bat(match,team):
    print('BATTING ',team[0])
    disp_players(team)
    ch=int(input('\nCHOOSE STRIKER:'))
    ch1=int(input('CHOOSE NON-STRIKER:'))
    STRIKER=team[ch] #virat #striker
    NON_STRIKER=team[ch1] #rohit
    #creation of strike
    bat_temp1=batting(STRIKER) 
    bat_temp1.b_stats['strike']=True
    bat_stats.append(bat_temp1.b_stats)
    #creation of non-strike
    bat_temp2=batting(NON_STRIKER)
    bat_stats.append(bat_temp2.b_stats)
    scoreboard(match.match_stats,bat_stats,bowl_stats)
    return team,bat_temp1,bat_temp2

def go_bowl(match,team):
    print('BOWLING '+team[0])
    disp_players(team)
    b_ch=int(input('CHOOSE THE BOWLER: '))
    #creation of bowler
    bowl_temp=bowling(team[b_ch])
    #bowling object append
    bowl_list.append(bowl_temp)
    #bowling dict append
    bowl_stats.append(bowl_temp.b_stats)
    scoreboard(match.match_stats,bat_stats,bowl_stats)
    return team,bowl_temp

def strike_rotate(striker,nonstrike,spos,npos):
    striker.rotate_strike()
    nonstrike.rotate_strike()
    temp=striker
    striker=nonstrike
    nonstrike=temp
    temp1=spos
    spos=npos
    npos=temp1
    return striker,nonstrike,spos,npos

def choose_bowler(bowl,bowler):
    bowl=list(bowl)
    bowl.remove(bowler.bname)
    disp_players(bowl)
    b_ch=int(input('CHOOSE THE BOWLER'))
    for bowlers in bowl_list:
        if bowlers.bname==bowl[b_ch] and bowl[b_ch]!=bowler.bname:
            bowler=bowlers
            break
    else:
        bowler=bowling(bowl[b_ch])
        bowl_list.append(bowler)
    return bowler
    
def check_result(result,bat,bowl,match):
    if result=='WIN':
        result='{0} WON BY {1} WICKETS'.format(bat[0],10-match.twickets)
        won=bat[0]
    elif result=='DRAW':
        result='DRAW MATCH'
        won=None
    elif result=='LOSE':
        result='{0} WON BY {1} RUNS'.format(bowl[0],(match.target-match.truns-1))
        won=bowl[0]
    return result,won
    

def innings(match,fname,bat,bowl,tovers,over,striker,nonstrike,bowler):
    system('cls')
    with open(fname,'rb+') as ifile:
        stats=load(ifile)
    match_stats,bat_stats,bowl_stats=stats
    #time.sleep(30)
    for batsman in bat_stats:
        if batsman['status']=='BAT' and batsman['strike']:
            spos=bat_stats.index(batsman) #batstats-[striker,nonstriker]
                #print(spos)
        elif batsman['status']=='BAT' and not batsman['strike']:
            npos=bat_stats.index(batsman)
    bat.remove(striker.batsman)
    bat.remove(nonstrike.batsman)
    game=True
    ball_by_ball=[]
    #time.sleep(30)
    while(over!=tovers):
        for bowlers in bowl_stats:
            if bowlers['bowler']==bowler.bname:
                bpos=bowl_stats.index(bowlers)
            #print(bpos)
        print('=================================================================================================\n')
        scoreboard(match_stats,bat_stats,bowl_stats)
        disp_over=over+0.1 
        for balls in range(6):
            print('\nENTER THE DATA IN ',round(disp_over,1),'(0,1,2,3,4,5,6,W-Wicket,EXTRAS: Nb-No ball,Wd-wide,Lb-Leg Byes,b-byes,EXIT): ',end="")
            ch=input()
            while(True):
                if is_valid(ch):
                    if ch=='EXIT' and balls!=0:
                        print('You can Exit only in the begining of an over!')
                    else:
                        break  
                ch=input('ENTER A VALID DATA:')
            #exit by saving Data
            if ch=='EXIT' and balls==0:
                save_data=[]
                save_data.append(match)
                save_data.append(striker)
                save_data.append(nonstrike)
                save_data.append(bowler)
                match.match_stats['status']=match.match_stats['status']+'(save)'
                sav='savedData/save_'+match.mcode+'.txt'
                print(bat_stats)
                save(fname,match.match_stats,bat_stats,bowl_stats)
                with open(sav,'wb') as sfile:
                    dump(save_data,sfile)
                game=False
                break
            #extras
            extras=('Nb','Wd','Lb','b')
            while(ch in extras):
                if ch in extras:
                    extra=ch.lower()
                    if extra=='nb' or extra=='wd':
                        ch1=int(input('ENTER IF ANY RUNS WERE SCORED(0 IF NOT): '))
                        bowler.extras(ch1+1)
                        match.extras(ch1+1)
                    elif extra=='lb' or extra=='b':
                        ch1=int(input('ENTER RUNS SCORED: '))
                        bowler.extras(ch1)
                        match.extras(ch1)
                    this_ball=ch+'-'+str(ch1)
                    ball_by_ball.append(this_ball)
                    print('\nENTER THE DATA IN ',round(disp_over,1),'(0,1,2,3,4,5,6,W-Wicket,EXTRAS: Nb-No ball,Wd-wide,Lb-Leg Byes,b-byes): ',end="")
                    ch=input()
                    while(True):
                        if is_valid(ch):
                            if extra=='nb' and ch=='W':
                                print('IT IS A NO BALL!!')
                            else:
                                break
                        ch=input('ENTER A VALID DATA:')
            system('cls')
            if ch=='W' or ch=='w':
                ball_by_ball.append(ch)
                striker.out()
                bowler._wickets()
                allout=match.update_wicket(round(disp_over,1))
                bat_stats[spos]=striker.b_stats
                bat_stats[npos]=nonstrike.b_stats
                bowl_stats[bpos]=bowler.b_stats
                save(fname,match.match_stats,bat_stats,bowl_stats)
                #allout condition
                if allout:
                    print('=================================================================================================\n')
                    scoreboard(match.match_stats, bat_stats, bowl_stats)
                    print('ALL-OUT!! END OF INNINGS!!\n')
                    game=False
                    break
                disp_players(bat)
                ch=int(input('CHOOSE A BATSMAN:'))
                striker=batting(bat[ch])
                bat.remove(striker.batsman)
                striker.b_stats['strike']=True
                bat_stats.append(striker.b_stats)
                for batsman in bat_stats:
                    if batsman['status']=='BAT' and batsman['strike']:
                        spos=bat_stats.index(batsman)
                    elif batsman['status']=='BAT' and not batsman['strike']:
                        npos=bat_stats.index(batsman)
            else:
                run=int(ch)
                ball_by_ball.append(ch)
                striker.inc_runs(run)
                bowler._runs_conceded(run)
                match.update_score(run,round(disp_over,1))
                if(run%2!=0):
                    striker,nonstrike,spos,npos=strike_rotate(striker, nonstrike, spos, npos)
                bat_stats[spos]=striker.b_stats
                bat_stats[npos]=nonstrike.b_stats
            bowl_stats[bpos]=bowler.b_stats
            disp_over=disp_over+0.1

            if (round(disp_over-over,1))==0.6:
                disp_over=over+1
            print('=================================================================================================\n')
            scoreboard(match.match_stats, bat_stats, bowl_stats)
            #display ball by ball
            print('\n\n\t\t\t',end="[")
            for ball in ball_by_ball:
                print(ball,end=' ')
            print(']')
            match.update_ball_by(ball_by_ball)
            save(fname,match.match_stats,bat_stats,bowl_stats)
            match_stats=match.match_stats
            '''if its 2nd innings we have to display runs to win ,target etc'''
            if(match_stats['status']=='2nd innings'):
                balls_left,runs_to_win=match.calc_balls_left()
                result=match.result_check(balls_left)
                if result is not None:
                    result,won=check_result(result,bat,bowl,match)
                    print('\n\n\t\t\t'+result)
                    match.match_stats['won']=won
                    match.match_stats['result']=result
                    bat_stats[spos]=striker.b_stats
                    bat_stats[npos]=nonstrike.b_stats
                    bowl_stats[bpos]=bowler.b_stats
                    save(fname,match.match_stats,bat_stats,bowl_stats)
                    game=False
                    break
                else:
                    match.match_stats['runs_to_win']='{0} NEEDS {1} RUNS OF {2} BALLS!!'.format(bat[0],runs_to_win,balls_left)
                    print('\t\t\t'+match.match_stats['runs_to_win'])
                    save(fname,match.match_stats,bat_stats,bowl_stats)
        #after an over
        
        ball_by_ball.append('|')
        if(not game):
            break
        striker,nonstrike,spos,npos=strike_rotate(striker, nonstrike, spos, npos)
        over+=1
        if(over!=tovers):
            print('\nOVER COMPLETED!!')
            bowler=choose_bowler(bowl,bowler)
            for bowlers in bowl_stats:
                if bowlers['bowler']==bowler.bname:
                    break
            else:
                bowl_stats.append(bowler.b_stats)
    if(match.match_stats['status'])=='1st innings':
        match.target=match.truns+1
        match.match_stats['target']=match.target
        match.delete_ball_by()
        match.match_stats['status']='2nd innings'
        save(fname,match.match_stats,bat_stats,bowl_stats)
    elif(match.match_stats['status'])=='2nd innings':
        match.match_stats['status']='completed'
        match.delete_ball_by()
        save(fname,match.match_stats,bat_stats,bowl_stats)



def start_match(mcode,team,won_toss,toss,overs):
    team1,team2=zip(*team)
    tname1=team1[0]
    tname2=team2[0]
    match=matchstats(mcode, tname1, tname2, overs)
    match.match_stats['date_time']=datetime.now().replace(second=0,microsecond=0)
    if won_toss==tname1:
        match.match_stats['status']='1st innings'
        if toss=='BAT':
            match.set_score('score1','1st_innings',tname1)
            bat,striker,nonstriker=go_bat(match,team1)
            bowl,bowler=go_bowl(match,team2)
        elif toss=='BOWL':
            match.set_score('score1','1st_innings',tname2)
            bat,striker,nonstriker=go_bat(match,team2)
            bowl,bowler=go_bowl(match,team1)
    if won_toss==tname2:
        match.match_stats['status']='1st innings'
        if toss=='BAT':
            match.set_score('score1','1st_innings',tname2)
            bat,striker,nonstriker=go_bat(match,team2)
            bowl,bowler=go_bowl(match,team1)
        elif toss=='BOWL':
            match.set_score('score1','1st_innings',tname1)
            bat,striker,nonstriker=go_bat(match,team1)
            bowl,bowler=go_bowl(match,team2)
    stats=[] #matchstats,batstats-[striker,nonstriker],bowlstats-[bowler]
    stats.append(match.match_stats)
    stats.append(bat_stats)
    stats.append(bowl_stats)
    fname='innings/1innings_'+mcode+'.txt' 
    with open(fname,'wb') as ifile:
        dump(stats,ifile)
    #1st innings
    innings(match,fname, list(bat), bowl, overs,0, striker, nonstriker,bowler)
    #2nd_innings
    if match.match_stats['status']=='2nd innings':
       match.score_reset()
       bat_stats.clear()
       bowl_stats.clear()
       stats=[]
       temp=bat
       bat,striker,nonstriker=go_bat(match,bowl)
       bowl,bowler=go_bowl(match,temp)
       match.set_score('score2','2nd_innings',bat[0])
       stats.append(match.match_stats)
       stats.append(bat_stats)
       stats.append(bowl_stats)
       fname='innings/2innings_'+mcode+'.txt'
       with open(fname,'wb') as ifile:
           dump(stats,ifile)
       innings(match,fname, list(bat), bowl, overs,0, striker, nonstriker,bowler)

def remove_bat(team,striker,nonstrike,bat_stats):
    print(team)
    for batsman in bat_stats:
        if batsman['status']=='OUT':
            team.remove(batsman['batsman'])
    return team


def match_load(mcode,team1,team2):
    global bat_stats
    fname='savedData/save_'+mcode+'.txt'
    with open(fname,'rb') as sfile:
        save_data=load(sfile)
        print(save_data)
    match,striker,nonstrike,bowler=save_data
    print(match.match_stats)
    if match.match_stats['status']=='1st innings(save)':
        match.match_stats['status']='1st innings'
        fname='innings/1innings_'+mcode+'.txt'
        with open(fname,'rb') as ifile:
            bat_stats=load(ifile)[1]
        if match.match_stats['score1'][0]==team1[0]:
            bat=team1
            bowl=team2
        else:
            bat=team2
            bowl=team1
        innings(match,fname,remove_bat(list(bat),striker, nonstrike, bat_stats), bowl, match.overs,match.match_stats['score1'][3], striker, nonstrike,bowler)
        if match.match_stats['status']=='2nd innings':
           match.score_reset()
           bat_stats.clear()
           bowl_stats.clear()
           stats=[]
           temp=bat
           bat,striker,nonstriker=go_bat(match,bowl)
           bowl,bowler=go_bowl(match,temp)
           match.set_score('score2','2nd_innings',bat[0])
           stats.append(match.match_stats)
           stats.append(bat_stats)
           stats.append(bowl_stats)
           fname='innings/2innings_'+mcode+'.txt'
           with open(fname,'wb') as ifile:
               dump(stats,ifile)
           innings(match,fname, list(bat), bowl, match.overs,0, striker, nonstriker,bowler)
    #load from Second innings
    elif match.match_stats['status']=='2nd innings(save)':
        match.match_stats['status']='2nd innings'
        fname='innings/2innings_'+mcode+'.txt'
        with open(fname,'rb') as ifile:
            bat_stats=load(ifile)[1]
        if match.match_stats['score2'][0]==team1[0]:
            bat=team1
            bowl=team2
        else:
            bat=team2
            bowl=team1
        innings(match,fname,list(bat), bowl, match.overs,match.match_stats['score2'][3], striker, nonstrike,bowler)
         


       


