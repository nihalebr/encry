import os
from encrypt import encrypt
from decrypt import verify
passw=input("Enter the password:")
fn=input("Enter the file name:")
eod=input("Do you want to decyprt or encrypt (e or d):")
de=input("Do you want to delete the orginal file (y or n):")
if eod=='e':
    ent=input("Do you wnat to encrpyt for paricular time (y or n):")
    if ent=='y':
        nd=int(input('Enter no of day for encryption to last:'))
        encrypt(passw,fn,nd)
    else:
        encrypt(passw,fn)
elif eod=='d':
    verify(passw,fn)
if de=='y':
    os.remove(fn)