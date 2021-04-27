#Rihar del tito-71200648
#Universitas Kristen Duta Wacana
#Dictionaries


'''buatlah sebuah menu setelah itu berikan menu apa saja yang dapat
dibeli oleh inputan uang user yang ada 

jumlah_menu = banyaknya menu yang akan diinput
uang_user = uang inputan user
menu_baru = inputan keys
harga = inputan values

input : jumlah_menu = banyak menu yang akan diinput  ; uang_user = uang inputan user ; menu_baru = inputan keys ; harga = inputan values

proses :
membuat dict kosong 
melakukan input jumlah_menu dan uang_user
perulangan untuk mengetahui jumlah menu 
inputan memasukkan keys dan values
perulangan dan percanbangan bila menu <= uang_user
akan ditampilkan 

output :
menampilkan daftar menu yang dapat di beli dengang uang_user yang ada

'''
menu = dict()
jumlah_menu = int(input('masukkan banyak menu :'))
uang_user = int(input('masukkan uang anda :'))
jumlah = 0 

for banyak in range(jumlah_menu):
    menu_baru = str(input('masukkan menu :'))
    harga = int(input('masukkan harga menu ;'))
    banyak = menu[menu_baru]=harga
for banyak2 in menu :
    if menu[banyak2] <= uang_user :
        jumlah +=1
        print(jumlah,'.',banyak2,menu[banyak2])
print('menu yang bisa dibeli berjumlah',jumlah,'dengan uang Rp.',uang_user)
