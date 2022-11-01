# list manipulasi

#indexnya dari awal itu dimulai dari 0 seperti
#            0 (-4)   1 (-3)   3 (-2)    4 (-1)
himpunan = [ "apel", "pepaya", "mangga", "jambu" ]


# misalnya  kita memanggil  data dari list ini

buah2 = himpunan [2]
print ( "buah yang ke2 (index 2) ", buah2)

#misal kita panggil data terakhir
last_fruit = himpunan [ -1] # karna suatu saat kemungkinan kita tidak tau seberapa panjng list data kita
print ( "buah terakhir = ", last_fruit)

#menghitung panjang data list
jumlah_list = len(himpunan)
print ("jumlah data", jumlah_list)

#MEMANIPULASI LIST
# misal menambahkan item dalam himpunan data

himpunan.insert(3,"rambutan")
print (himpunan)

#misal menambah item di akhir list
himpunan.append ("langsat")
print (himpunan)



