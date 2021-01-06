class batting:
    def __init__(self,bname):
        self.batsman=bname
        self.b_stats={'batsman':bname,'runs':0,'balls':0,'4s':0,'6s':0,'S/R':0.0,'status':'BAT','strike':False}
        self.runs=0
        self.balls=0
        self.fours=0
        self.six=0
        self.strikerate=0.0


    def stats_change(self):
        self.b_stats['runs']=self.runs
        self.b_stats['balls']=self.balls
        self.b_stats['4s']=self.fours
        self.b_stats['6s']=self.six
        self.b_stats['S/R']=round(self.calc_strikerate(),2)
    
    def inc_runs(self,run):
        self.runs+=run
        self.balls+=1
        if(run==6):
            self.six+=1
        elif(run==4):
            self.fours+=1
        self.stats_change()
    
    def calc_strikerate(self):
        self.strikerate=(self.runs/self.balls)*100
        return self.strikerate
    
    def rotate_strike(self):
        self.b_stats['strike']=not self.b_stats['strike']  #striker:False   1        non-strike:True

    def out(self):
        self.balls+=1
        self.b_stats['status']='OUT'
        self.b_stats['strike']=False
        self.stats_change()