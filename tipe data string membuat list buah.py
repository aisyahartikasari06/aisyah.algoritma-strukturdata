#membuat list
list_buah = ['duren', 'pisang', 'jambu', 'apel']
print('list_buah:', list_buah)

#
print(list_buah[0])
print(list_buah[1])
print(list_buah[2])
print(list_buah[3])

#slicing list
print(list_buah[1:3])

#mengubah data dalam list
list_buah[3] = 'jeruk'
print(list_buah)

#tambah data kedalam list
list_buah.append('alpukat')
print(list_buah)

list_buah.insert(4, 'kamu')
print(list_buah)

#menghapus item dari list
list_buah.pop() #menhapus data di akhir
print(list_buah)

list_buah.remove('kamu')
print(list_buah)

del list_buah[1]
print(list_buah)

#mengurutkan data
list_buah.insert(3, 'ayam')
print(list_buah)

list_buah.sort()
print(list_buah)