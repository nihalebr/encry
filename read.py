import pickle
import datetime

fpath=r'C:\Users\nihal\Desktop\art\anto.enc'
with open(fpath,'rb') as f:
    data=pickle.load(f)
fs=fpath.split('\\')
fp=fs[0]
for i in range (1,len(fs)-1):
    fp= '\\'.join((fp,fs[i]))
f=[data['Name'],data['Ext']]
fn=f[0]+'_de.'+f[1]
fp='\\'.join((fp,fn))
print(data)
