from cryptography.fernet import Fernet
from key_gen import key_gen
from timev import tverify
import pickle

def decrypt(passw,fe):
    
    key=key_gen(passw)
    with open(fe,'rb') as f:
        d=pickle.load(f)
    
    try:
        data=d['Data']
        fer = Fernet(key)
        decrypted = fer.decrypt(data)
    except:
        print('Invaild Password retry once again.')  
    
    fs=fe.split('\\')
    fp=fs[0]
    for i in range(1,len(fs)-1):
        fp= '\\'.join((fp,fs[i]))
    f=[d['Name'],d['Ext']]
    fn=f[0]+'_de.'+f[1]
    fp='\\'.join((fp,fn))

    with open(fp,'wb') as f:
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

