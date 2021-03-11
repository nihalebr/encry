from cryptography.fernet import Fernet
from key_gen import key_gen
import datetime
import pickle

def encrypt(passw,fe,nd=0):
    key=key_gen(passw)
    
    with open(fe,'rb') as f:
        data=f.read()
    
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    fn=fe.split('.')
    name=fn[0]
    ext=fn[1]
    
    time=datetime.datetime.now()
    date=datetime.date.today()
    
    file={'Date':date,'Time':time,'Data':encrypted,'Name':name,'Ext':ext,'Nd':nd}
    
    fp=fn[0]+'.enc'
    fname=r'{}'.format(fp)
    with open(fname,'wb') as f:
        f.write(pickle.dumps(file))