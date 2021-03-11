import pickle
import datetime

with open(r'C:\Users\nihal\Desktop\art\rect833.enc','rb') as f:
    data=pickle.load(f)

nd=data['Nd']
etday=data['Date']
date=datetime.date.today()

tday=datetime.date.today()
tdelta=datetime.timedelta(days=nd)
etmday=etday+tdelta
tmday=tday+tdelta

print('\t',tmday)
print('\t',etmday)
print('\t',date)
print(etmday==tmday)