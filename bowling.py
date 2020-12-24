
class bowling:
    def __init__(self,bname):
        self.b_stats={'bowler':bname,'over':0,'maiden':0,'wickets':0,'runs':0,'econ':0.0,'status':True}
        self.bname=bname
        self.overs = 0
        self.runs_conceded = 0
        self.wickets = 0
        self.maiden=0
        self.economy=0.0
        self.status=True
        self.balls=0
        self.runs_per_over=0
        self.count=1
        self.prev=False

    def _maiden(self):
        if(self.runs_per_over== 0):
            return True
        else:
            return False
    def _runs_conceded(self,run):
        self.runs_conceded+=run
        self.balls+=1
        self.economy=round(self._economy(),2)
        self.runs_per_over+=run
        self.overs+=0.1
        if self.count==6:
            if self._maiden():
                self.maiden+=1
            self.overs=int(self.overs+0.4)
            self.runs_per_over=0
            self.count=1
        else:
            self.count+=1
        self.stats_change()
        
    def _wickets(self):
        self.wickets+=1
        self.balls+=1
        self.overs+=0.1
        if self.count==6:
            self.overs=int(self.overs+0.4)
            self.runs_per_over=0
            self.count=1
        else:
            self.count+=1
        self.stats_change()


    def stats_change(self):
        self.b_stats['over']=round(self.overs,1)
        self.b_stats['maiden']=self.maiden
        self.b_stats['runs']=self.runs_conceded
        self.b_stats['econ']=self.economy
        self.b_stats['wickets']=self.wickets
    def _economy(self):
        economy_result = self.runs_conceded/(self.balls/6)
        return economy_result
    
    def extras(self,run):
        self.runs_conceded+=run
        #self.economy=round(self._economy(),2)
        self.runs_per_over+=run
        self.stats_change()