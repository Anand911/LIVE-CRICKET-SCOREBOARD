innings_format='{team} : {total}/{wickets}  ||  {over}|{overs}\n\t\t\t{ball_by}'
class matchstats:
    
    def __init__(self,mcode,team1,team2,overs):
        self.match_stats={'mcode':mcode,'date_time':None,'team1':team1,'team2':team2,'overs':overs,'status':None,'score1':[None,0,0,0,overs,None],'score2':[None,0,0,0,overs,None],'runs_to_win':None,'1st_innings':None,'2nd_innings':None}
        self.mcode=mcode
        self.team1=team1
        self.team2=team2
        self.truns=0
        self.twickets=0
        self.over=0
        self.overs=overs
        self.score=''
        self.innings=''
        self.target=0
        self.balls=0
    
    def set_score(self,score,innings,bat):
        self.match_stats[score][0:4]=bat,self.truns,self.twickets,self.over
        score_list=self.match_stats[score]
        self.score=score
        self.innings=innings
        self.match_stats[innings]=innings_format.format(team=score_list[0],total=score_list[1],wickets=score_list[2],over=score_list[3],overs=score_list[4],ball_by='')
    
    def innings_view(self):
        score_list=self.match_stats[self.score]
        self.match_stats[self.innings]=innings_format.format(team=score_list[0],total=score_list[1],wickets=score_list[2],over=score_list[3],overs=score_list[4],ball_by=score_list[5])
    
    def update_score(self,run,disp_over):
        self.truns+=run
        self.balls+=1
        self.over=disp_over
        self.match_stats[self.score][1]=self.truns
        self.match_stats[self.score][3]=self.over
        self.innings_view()
    def update_ball_by(self,ball_by_ball):
        ball_str='['
        for ball in ball_by_ball:
            ball_str=ball_str+' '+ball
        ball_str+=']'
        self.match_stats[self.score][5]=ball_str
        self.innings_view()
    def delete_ball_by(self):
        self.match_stats[self.score][5]=''
        self.innings_view()
    
    def extras(self,run):
        self.truns+=run
        self.match_stats[self.score][1]=self.truns
        self.innings_view()

    def score_reset(self):
        self.truns=0
        self.over=0
        self.twickets=0
        self.balls=0

    def calc_balls_left(self):
        balls_left=(self.overs*6)-self.balls
        runs_to_win=self.target-self.truns
        return balls_left,runs_to_win
    def result_check(self,balls_left):
        if self.truns>=self.target:
            return 'WIN'
        elif self.truns==(self.target-1) and balls_left==0:
            return 'DRAW'
        elif self.truns<self.target and balls_left==0:
            return 'LOSE'
        else:
            return None
    
    def update_wicket(self,disp_over):
        self.twickets+=1
        self.balls+=1
        self.over=disp_over
        self.match_stats[self.score][2]=self.twickets
        self.match_stats[self.score][3]=self.over
        self.innings_view()
        if(self.twickets==10):
            return True
        else:
            return False






        
