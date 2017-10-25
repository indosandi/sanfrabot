# SANFRABOT
Repo ini berisi source code dari [sanfrabot](https://t.me/sanfrabot). Sanfrabot adalah chat bot di dalam aplikasi pengirim pesan Telegram. Bot ini berfungsi sebagai aplikasi transportasi online di mana bot mampu mengubungkan pengemudi dan penumpang. Mencari pengemudi semudah berinteraksi dengan [sanfrabot](https://t.me/sanfrabot). 

Sasaran pengguna dari [sanfrabot](https://t.me/sanfrabot) adalah masyarakat di daerah non-perkotaan seperti sub-urban, desa, kota kecil, dll. Karena siapapun boleh menggunakan [sanfrabot](https://t.me/sanfrabot), chatbot ini cocok digunakan oleh masyarakat dengan karakter ikatan antar individu masih kuat. Salah satu tujuan pembuatan [sanfrabot](https://t.me/sanfrabot) adalah membangun ekonomi kerakyatan dan men-demokratisasi transportasi online. 

Beberapa keunikan [sanfrabot](https://t.me/sanfrabot):
1. Fitur negosiasi harga antara penumpang dan pengemudi. 
2. Fitur penumpang bisa memilih pengemudi yang setuju dengan harga/negosiasi.
3. Menggunakan aplikasi Telegram sehingga bisa digunakan di daerah pelosok di mana koneksi internet tidak terlalu stabil.
4. Gratis dan tanpa potongan.

Developer-developer lokal diharapkan bisa berkontribusi dengan melakukan pull-request atau dengan open issue buat non-developer (tester, bug reporting, feature request, creating tutorial, etc).

Sanfrabot merupakan salah satu implementasi dari kertasrapi foundation yang bergerak dengan spirit:
"Membuka akses teknologi dan ilmu pengetahuan seluas-luasnya kepada semua kalangan masyarakat sehingga mempercepat transfer idea dan interaksinya demi mencapai kesempatan yang sama dalam berkarya"


# TATA CARA INSTALL
Sejak awal [sanfrabot](https://t.me/sanfrabot) didesain mampu meng-handle load dengan skalabilitas horisontal. Dengan demikian, arsitektur [sanfrabot](https://t.me/sanfrabot) natively distributed services. Ada tiga services berbeda yaitu: rabbitmq (distributed queue), redis (nosql database), dan [sanfrabot](https://t.me/sanfrabot) code. Ketiga component tersebut bisa dideploy di server yang berbeda atau di satu server. Cara paling mudah yaitu menggunakan cloud service seperti cloudamqp.com dan redislab. 

Gambar di atas adalah arsitektur dari backend [sanfrabot](https://t.me/sanfrabot). Penjelasan tentang arsitektur [sanfrabot](https://t.me/sanfrabot) dijelaskan dibawah ini:
1. No 1 adalah telegram api. Sumber data berasal dari telegram api
2. No 2. adalah pusher.py. Python proses ini mengambil data dari telegram server dan memasukannya ke rabbitmq queue. Ada wrapper pusher.py yaitu rbtpusher.sh. Dengan menjalakan wrapper tersebut maka shell script akan merestart python process ( puhser.py) jika fail. 
3. No 3. adalah rabbitmq. Disini data disimpan temporaryly agar bisa dikonsumsi oleh python worker in parallel fashion.
4. No 4. adalah main.py. Python proses ini membaca data kemudian memproses dan menyimpan data ke database redis. Setelah data chat di proses kemudian proses ini akan mengirim respon ke masing-masing user. Process ini dapat dispawn secara parallel sebanyak-banyaknya sampai cpu load maximum. 
5. No 5. adalah redis database. No sql database untuk menyimpan state dan data. Selain itu, untuk mencari driver di radius 1-2 meter, digunakan redis geo library.

Selain component-component di atas, [sanfrabot](https://t.me/sanfrabot) menggunakan google API untuk melakukan reverse geocoding dan static map. Token dari google API dibutuhkan untuk melakukan reverse geocoding. 

Semua rangkaian diatas bisa dideploy di multiple location. Selama variable-variable yang menunjuk ke system di atas diberikan, maka [sanfrabot](https://t.me/sanfrabot) is good to go. Isi variable-variable di dalam file setup.sh dan set setup.sh ke environment variables (source setup.sh). Berikut adalah penjelasan tentang variable-variable tersebut:

GMAP: google token untuk melakukan geocoding
botToken: token telegram bot API
redisHost: host redis 
redisPort: redis port number
password: redis password
GSTATICMAP: google token untuk melakukan static map
rbtHost: host rabbitmq
rbtPass: password rabbitmq
rbtUser: rabbitmq user
rbtVhost: rabbitmq virtual host
rbtPort: rabbitmq port 

Langkah berikutnya yaitu install all dependencies python 2.7 ( disarankan menggunakan venv)
```python 
pip install -r requirements.txt
```

Langkah berikutnya yaitu jalankan pusher dan grabber (main code dari [sanfrabot](https://t.me/sanfrabot))
``` shell
python pusher.py & # pusher
python main.py & # grabber, bisa menjalankan beberapa worker at the same time
```

Langkah di atas bisa diganti dengan shell script. 
```shell
nohup sh rbtpusher.sh & # dapat melakukan restart ulang otomatis
source rbtconsumer.sh # menjalankan 30 worker sekaligus secara otomotis
```

Jika ingin kill all worker:
```shell
source killMain.sh # kill semua worker
```

Yah, selesai deh. Padahal masih pengen pusingin orang. Kalo mau tambah pusing boleh baca wiki-nya

Pusing-pusing tapi tetep perkuat komunitas open source ya

