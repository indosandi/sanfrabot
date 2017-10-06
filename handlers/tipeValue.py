tipe={}
tipe['motor']='motor'
tipe['mobil']='mobil'

listTipe=tipe.values()

def checkIfIn(key):
    if key in listTipe:
        return True
    else:
        return False
