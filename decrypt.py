from cryptography.fernet import Fernet
from key_gen import key_gen
from timev import tverify
import pickle

def decrypt(passw,fe):
    
    key=key_gen(passw)
    with open(fe,'rb') as f:
        d=pickle.load(f)
    
    data=d['Data']
    fer = Fernet(key)
    decrypted = fer.decrypt(data)
    
    fn=[d['Name'],d['Ext']]
    fname=fn[0]+'_de.'+fn[1]
    with open(fname,'wb') as f:
        f.write(decrypted)

def verify(pasw,fn):
    
    with open(fn,'rb') as f:
        d=pickle.load(f)
    
    etday=d['Date']
    nd=d['Nd']
    
    if nd==0:
        decrypt(pasw,fn)
    elif tverify(etday,nd):
        decrypt(pasw,fn)
    else:
        print('The encryption period expried.')

