import datetime

def tverify(etday,nd):
    tday=datetime.date.today()
    tdelta=datetime.timedelta(days=nd)
    etmday=etday+tdelta
    
    if tday>=etmday :
        return False
    else:
        return True