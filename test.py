from pickle import load
mcode='PeAJ'
fname='innings/1innings_'+mcode+'.txt'
with open(fname,'rb') as ifile:
    stats=load(ifile)
match_stats1,bat_stats1,bowl_stats1=stats
print(match_stats1)