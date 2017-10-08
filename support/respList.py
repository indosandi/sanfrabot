import support.emojis as emo
def pilihSiapa():
    return emo.welcomeGirl+" Silahkan pilih: \n"+emo.rightArrow+"Pengemudi " +emo.pengemudi+"\n"+emo.rightArrow+"Penumpang "+emo.pengguna

def infoPengemudi():
    text=emo.welcomeGirl+"jika info sudah lengkap bisa langsung mangkal atau dilengkapi dulu ya\n"
    text+='Ketik /reset untuk ke awal'
    return text
def driverData(nama,no,ojek,lokasi,desc):
    outStr = []
    outStr.append(emo.pengemudi+" Pengemudi:")
    outStr.append(emo.rightArrow+'Nama: ' + nama)
    outStr.append(emo.rightArrow+'Phone: ' + no)
    outStr.append(emo.rightArrow+'Kendaraan: ' + ojek)
    outStr.append(emo.rightArrow+'Lokasi terakhir: ' + lokasi)
    outStr.append(emo.rightArrow+'Deskripsi: ' + desc)
    strOut = ""
    for s in outStr:
        strOut = strOut + s + '\n'
    # strOut=strOut+'Ketik /reset untuk ke awal'
    return strOut+'\n\n'+infoPengemudi()

def ubahInfo():
    text=emo.welcomeGirl+" Silahkah pilih yang ingin dilengkapi"
    return text

def ubahHp():
    text=emo.welcomeGirl+' Tekan tombol "kirim no" ya'
    return text

def ubahNama():
    text=emo.welcomeGirl+' Silahkan diketik nama-nya '
    return text

def userData(no,nama,dari,ke,harga,ojek):
    outStr = []
    outStr.append(emo.pengguna+" Info kamu :")
    outStr.append(emo.rightArrow+'Nama: ' + nama)
    outStr.append(emo.rightArrow+'Phone: ' + no)
    outStr.append(emo.rightArrow+'Dari : ' + dari)
    outStr.append(emo.rightArrow+'Ke : ' + ke)
    outStr.append(emo.rightArrow+'harga : ' + harga)
    outStr.append(emo.rightArrow+'Kendaraan: ' + ojek)
    strOut = ""
    for s in outStr:
        strOut = strOut + s + '\n'

    text = emo.welcomeGirl + "jika info sudah lengkap bisa langsung cari ojek atau dilengkapi dulu ya\n"
    text += 'Ketik /reset untuk ke awal'
    return strOut+'\n\n'+text

def userHarga():
    text=emo.welcomeGirl+' Masukan harga ya \n'
    text+=emo.rightArrow+'Contoh: 10rb ya pak, kan ga jauh\n'
    text+=emo.rightArrow+'Contoh: 20rb pak, tp kalo macet sy tambah 5rb lagi deh\n'
    text+=emo.info+' Jika tidak tau harga ketik "0" '
    return text

def userKendaraan():
    text=emo.welcomeGirl+' Silahkan dipilih tipe kendaraan'
    return text

def driverDeskripsi():
    text=emo.welcomeGirl+"Deskripsikan kendaraan selengkapnya \n(no polisi, warna, merek, dll) "
    return text

def driverMangkal():
    text=emo.welcomeGirl+'Mangkal sudah siap, tinggal tunggu order saja.\n'
    text+=emo.info+' Jangan lupa perbarui lokasi mangkal ya'
    return text

def updateMangkal():
    text=emo.welcomeGirl+'lokasi mangkal sekarang'
    return text

def driverGetOrder():
    text=emo.welcomeGirl+'Selamat anda mendapatkan order'+emo.terumpet+emo.terumpet+', tekan "Kembali" untuk ke menu awal'
    return text

def userGetOrder():
    text=emo.welcomeGirl+'Selamat anda mendapatkan pengemudi'+emo.terumpet+emo.terumpet+', tekan "Kembali" untuk ke menu awal'
    return text

def userSendInfo(name,no):
    text = emo.bell+ emo.bell+emo.bell+ '\n'
    text +=emo.pengguna+ 'Penumpang ' + name + ' memilih anda\n'
    text = text +emo.smartphone+ 'No hp :' + no + '\n'
    text = text +emo.whiteExcl+emo.whiteExcl+ 'Silahkan hubungi penumpang'+emo.whiteExcl+emo.whiteExcl
    return text

def driverSendInfo(name,no,deskripsi):
    text = emo.bell+ emo.bell+ emo.bell+ '\n'
    text +=emo.pengemudi+ 'Pengemudi: ' + name + ' \n'
    text = text +emo.smartphone+ 'No hp: ' + no + ' \n'
    text = text +emo.pageup+'Deskripsi:' + deskripsi+ '\n'
    text = text +emo.whiteExcl+emo.whiteExcl+ 'Silahkan hubungi pengemudi'+emo.whiteExcl+emo.whiteExcl
    return text

def orderToDriver(harga,dist):
    text = emo.sirine+ emo.sirine+ emo.sirine+ '\n'
    text += 'ORDER!!!!!\n'
    text = text + 'HARGA: ' + harga + '\n'
    text = text + 'jarak ke penumpang ' + dist + ' KM\n'
    return text

def hargaInfo():
    text=emo.welcomeGirl+' Disini harga ditentukan oleh penumpang dan pengemudi'
    return text

def noDriver():
    text=emo.shrugGirl+' Tidak ada driver ditemukan. Coba sesaat lagi atau ganti kendaraan'
    return text

def orderHowMany(jmlahDriver):
    text=emo.welcomeGirl+' Order akan dikirim ke ' + jmlahDriver + ' drivers. Mereka bisa setuju atau menawar harga'
    return text

def ketikHarga():
    text=emo.welcomeGirl+' Masukan harga yang diinginkan'
    return text