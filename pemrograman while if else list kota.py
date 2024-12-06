listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 
    'Jogjakarta', 'Semaranag', 'Makasar'
]

kotayangdicari = input('masukan nama kota yang dicari: ')
i = 0
while i < len(listkota):
    if listkota[i].lower() == kotayangdicari.lower():
        print('ketemu di index', i)
        break
    print('bukan', listkota[i])
    i += 1
else:
    print('maaf, kota yang anda cari tidak ditemukan.')