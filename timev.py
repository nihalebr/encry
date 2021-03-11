import datetime

def tverify(etday,nd):
    tday=datetime.date.today()
    tdelta=datetime.timedelta(days=nd)
    etmday=etday+tdelta
    tmday=tday+tdelta
    
    if tmday==etmday:
        return True
    else:
        return False