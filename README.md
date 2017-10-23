# SANFRABOT
Repo ini berisi source code dari sanfrabot. Sanfrabot adalah chat bot di dalam aplikasi pengirim pesan Telegram. Bot ini berfungsi sebagai aplikasi transportasi online di mana bot mampu mengubungkan pengemudi dan penumpang. Mencari pengemudi semudah berinteraksi dengan sanfrabot. 

Sasaran pengguna dari sanfrabot adalah masyarakat di daerah non-perkotaan seperti sub-urban, desa, kota kecil, dll. Karena siapapun boleh menggunakan sanfrabot, chatbot ini cocok digunakan oleh masyarakat dengan karakter ikatan antar individu masih kuat. Salah satu tujuan pembuatan sanfrabot adalah membangun ekonomi kerakyatan dan men-demokratisasi transportasi online. 

Beberapa keunikan sanfrabot:
1. Fitur negosiasi harga antara penumpang dan pengemudi. 
2. Fitur penumpang bisa memilih pengemudi yang setuju dengan harga.
3. Menggunakan aplikasi Telegram sehingga bisa digunakan di daerah pelosok di mana koneksi internet tidak terlalu stabil.
4. Gratis dan tanpa potongan.

Developer-developer lokal diharapkan bisa berkontribusi dengan melakukan pull-request atau dengan open issue buat non-developer (tester, bug reporting, feature request, creating tutorial, etc).

Sanfrabot merupakan salah satu implementasi dari kertasrapi foundation yang bergerak dengan spirit:
"Membuka akses teknologi dan ilmu pengetahuan seluas-luasnya kepada semua kalangan masyarakat sehingga mempercepat transfer idea dan interaksinya demi mencapai kesempatan yang sama dalam berkarya"


# TATA CARA INSTALL
Sejak awal sanfrabot didesain mampu meng-handle load dengan skalabilitas horisontal. Dengan demikian, arsitektur sanfrabot natively distributed services. Ada tiga services berbeda yaitu: rabbitmq (distributed queue), redis (nosql database), dan sanfrabot code. Ketiga component tersebut bisa dideploy di server yang berbeda atau di satu server. Cara paling mudah yaitu menggunakan cloud service seperti cloudamqp.com dan redislab. 

Kode sanfrabot dibagi menjadi dua, satu yaitu mengambil data dari telegram server kemudian mem-push ke rabbitmq, dan kedua yaitu mengambil data dari rabbitmq untuk diproses lebih lanjut. Proses kedua bisa diparalesasi tergantung dari seberapa besar load yang diterima. Selain component tersebut, sanfrabot menggunakan google API untuk melakukan reverse geocoding dan static map. Token dari google API dibutuhkan untuk melakukan reverse geocoding. 

1. Lengkapi variable konfigurasi dan set ke environment variables
Variable-variable konfigurasi disimpan dalam file setup.sh. Semua variable harus dilengkapi agar system bisa berjalan dengan baik

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


Setelah jadikan variable sebagai environment variable
source setup.sh

2. Install all dependencies python 2.7
Kemudian install all dependencies ( disarankan menggunakan venv)
pip install -r requirements.txt

3. Jalankan pusher dan grabber (main code dari sanfrabot)
Siap dijalankan untuk push data from telegram ke rabbitmq 
python pusher.py
untuk grab data from rabbitmq ke worker ( anda bisa menjalankan beberapa worker at the same time)
python main.py

Langkah ke tiga bisa diganti dengan shell script. 
nohup sh rbtpusher.sh & # dapat melakukan restart ulang otomatis
sh rbtconsumer.sh # menjalankan 30 worker sekaligus secara otomotis

Jika ingin kill all worker:
source killMain.sh # kill semua worker
