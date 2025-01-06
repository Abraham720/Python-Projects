menu_makanan = {
    1:{
        'nama makanan' : "Nasi Goreng",
        'harga' : 18000
        },

    2:{
        'nama makanan' : "Nasi Goreng Spesial",
        'harga' : 22000
        },

    3:{
        'nama makanan' : "Mie Goreng",
        'harga' : 18000
        },

    4:{
        'nama makanan' : "Mie Goreng Spesial",
        'harga' : 22000
        },

    5:{
        'nama makanan' : "Kwetiaw Goreng",
        'harga' : 19000
        },

    6:{
        'nama makanan' : "Capcay",
        'harga' : 15000
        }
}

menu_minuman = {
    1:{
        'nama minuman' : 'Teh Tawar',
        'harga' : 3000
    },
    2:{
        'nama minuman' : 'Teh Manis',
        'harga' : 5000
    },
    3:{
        'nama minuman' : 'Teh Lemon',
        'harga' : 8000
    },
    4:{
        'nama minuman' : 'Es Jeruk',
        'harga' : 10000
    }
}
menu_dipesan_makanan = []
menu_dipesan_minuman = []
print('Menu Makanan kami yang tersedia :\n1.',menu_makanan[1]['nama makanan'],'\n2.',menu_makanan[2]['nama makanan'],'\n3.',menu_makanan[3]['nama makanan'],'\n4.',menu_makanan[4]['nama makanan'],'\n5.',menu_makanan[5]['nama makanan'],'\n6.',menu_makanan[6]['nama makanan'])

def mesen_makan():
    pemesanan_makanan = input('Makanan apa yang ingin anda pesan? (Tuliskan nomornya, 0 untuk berhenti)')
    while pemesanan_makanan != 'minum':
        pemesanan_makanan = int(pemesanan_makanan)
        if pemesanan_makanan == 0:
            break
        elif pemesanan_makanan < 7 and pemesanan_makanan > 0:
            print('Makanan yang telah anda pesan adalah ', menu_makanan[pemesanan_makanan]['nama makanan'], '\n')
            menu_dipesan_makanan.append(pemesanan_makanan)

        pemesanan_makanan = input('Makanan apa yang ingin anda pesan? (Tuliskan nomornya, 0 untuk berhenti)')

def mesen_minum():
    print('Dengan ini anda mulai memesan minuman')
    pemesanan_minuman = input('Minuman mana yang ingin anda pesan? (Tuliskan nomornya, 0 untuk berhenti)')
    while pemesanan_minuman != '0' and pemesanan_minuman != 'makan':
        pemesanan_minuman = int(pemesanan_minuman)
        if pemesanan_minuman == 0:
            break
        elif pemesanan_minuman < 7 and pemesanan_minuman > 0:
            print('Minuman yang telah anda pesan adalah ', menu_minuman[pemesanan_minuman]['nama minuman'])
            menu_dipesan_minuman.append(pemesanan_minuman)
    
    if pemesanan_minuman == 'makan':
        mesen_makan()

        pemesanan_minuman = input('Minuman mana yang ingin anda pesan? (Tuliskan nomornya, 0 untuk berhenti)')

mesen_makan()
mesen_minum()



