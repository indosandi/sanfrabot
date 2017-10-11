import support.emojis as emo
def pilihSiapa():
    return emo.welcomeGirl+" Silahkan pilih: \n"+emo.rightArrow+"Pengemudi " \
           +emo.pengemudi+"\n"+emo.rightArrow+"Penumpang "+emo.pengguna+"\n"+emo.rightArrow+" Feedback"+emo.envelope

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
    text = emo.welcomeGirl + ' Silahkan diketik nama-nya\n'
    text += "ketik /reset untuk cancel dan kembali ke awal"
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

    text = emo.welcomeGirl + "jika info sudah lengkap bisa cari ojek atau dilengkapi dulu ya\n"
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

def userSendInfo(name,no,harga):
    text = emo.bell+ emo.bell+emo.bell+ '\n'
    text +=emo.pengguna+ 'Penumpang ' + name + ' memilih anda\n'
    text = text +emo.smartphone+ 'No hp :' + no + '\n'
    text = text +emo.pursu+ 'HARGA:' + harga + '\n'
    text = text +emo.whiteExcl+emo.whiteExcl+ 'Silahkan hubungi penumpang'+emo.whiteExcl+emo.whiteExcl
    return text

def driverSendInfo(name,no,deskripsi,harga):
    text = emo.bell+ emo.bell+ emo.bell+ '\n'
    text +=emo.pengemudi+ 'Pengemudi: ' + name + ' \n'
    text = text +emo.smartphone+ 'No hp: ' + no + ' \n'
    text = text +emo.pursu+ 'HARGA: ' + harga + ' \n'
    text = text +emo.pageup+'Deskripsi:' + deskripsi+ '\n'
    text = text +emo.whiteExcl+emo.whiteExcl+ 'Silahkan hubungi pengemudi'+emo.whiteExcl+emo.whiteExcl
    return text

def orderToDriver(harga,dist):
    text = emo.sirine+ emo.sirine+ emo.sirine+ '\n'
    text += 'ORDER!!!!!\n'
    if harga=='0':
        text = text + 'HARGA: Tidak ditetapkan\n'
    else:
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
    text=emo.welcomeGirl+' Order sudah dikirim ke ' + jmlahDriver + ' drivers. Mereka bisa setuju atau menawar harga.\n'
    text+=" Silahkan tunggu response dari pengemudi"
    return text

def ketikHarga():
    text=emo.welcomeGirl+' Masukan harga yang diinginkan'
    return text

def inputSalah():
    text=emo.welcomeGirl+' Ada input yang salah. Bisa dilanjutkan atau kembali ke awal dengan /reset'
    return text

def lokasiDariLengkap():
    text=emo.welcomeGirl+' Berikut adalah beberapa cara memasukan lokasi:\n\n'
    text+=emo.rightArrow+' Paling mudah yaitu ketik alamat dan kirim, saya akan cari alamat di map (peta)\n\n'
    text+=emo.rightArrow+' Selain itu bisa juga dengan menekan tombol "Kirim lokasi" untuk mengakses GPS\n\n'
    text+=emo.rightArrow+' Jika ingin membuka map (peta), tekan tombol attachment('+emo.paperclip+') dibawah dan pilih location. Lokasi bisa dipilih ' \
              'di map atau di-search\n\n'
    text+=emo.rightArrow+' Yg paling sy suka yaitu menggunakan foursquare untuk realtime location, ketik "@foursquare alamat-yg-dituju", tunggu sampe menu di atasnya muncul kemudian pilih'
    return text

def lokasiKeLengkap():
    text=emo.welcomeGirl+' Berikut adalah beberapa cara memasukan lokasi:\n\n'
    text+=emo.rightArrow+' Paling mudah yaitu ketik alamat dan kirim, saya akan cari alamat di map (peta)\n\n'
    text+=emo.rightArrow+' Jika ingin membuka map (peta), tekan tombol attachment('+emo.paperclip+') dibawah dan pilih location. Lokasi bisa dipilih ' \
              'di map atau di-search\n\n'
    text+=emo.rightArrow+' Yg paling sy suka yaitu menggunakan foursquare untuk realtime location, ketik "@foursquare alamat-yg-dituju", tunggu sampe menu di atasnya muncul kemudian pilih'
    return text

def lokasiDari():
    text=emo.welcomeGirl+' Tekan tombol "Kirim lokasi".\n'
    text+=emo.rightArrow+' Untuk mengetahui cara-cara mudah mengirim lokasi ketik atau klik /lokasi'
    return text

def lokasiKe():
    text=emo.welcomeGirl+' Masukan alamat tujuan.\n'
    text+=emo.rightArrow+' Untuk mengetahui cara-cara mudah mengirim lokasi ketik atau klik /lokasi'
    return text

def feedback():
    text=emo.welcomeGirl+' Silahkan beri saran, pertanyaan, atau laporan '
    return text

def feedbackAfter():
    text=emo.welcomeGirl+' Terima kasih sudah kami terima'
    return text

def lihatDriver():
    text=emo.welcomeGirl+' Sebelum mencari ojek, kita bisa melihat pengemudi di sekitar dulu\n'
    text+=emo.rightArrow+' Tekan "Lihat" untuk melihat pengemudi di sekitar\n'
    text+=emo.rightArrow+' Tekan "Order" untuk membuat order baru dan langsung mencari pengemudi. ' \
                         'Pengemudi akan mendapatkan ' \
                         'notif ketika anda menekan tombol ini'
    return text

def lihatDriverImg(number):
    text=emo.welcomeGirl+str(number)+' lokasi pengemudi ditampilkan di atas'
    return text

def errorServ():
    text=emo.bowing+ " service error"
    return text

def tungguOrder():
    text=emo.welcomeGirl+" "
    return text
