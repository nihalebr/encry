import pickle
import datetime

print(datetime.date.today())
with open(r'C:\Users\nihal\Desktop\ffmpeg-4.enc','rb') as f:
    data=pickle.load(f)
print(data)