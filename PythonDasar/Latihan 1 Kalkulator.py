while True:
  print('='*50)
  print('Pilih Operasi:')
  print('1. Penjumlahan')
  print('2. Pengurangan')
  print('3. Perkalian')
  print('4. Pembagian')
  try:
    inputUser = int(input('Masukan Pilihan Operasi (1/2/3/4): '))
    num1 = float(input('Masukan Angka Pertama: '))
    num2 = float(input('Masukan Angka Kedua: '))
    print('')
    if inputUser == 1:
      hasil = num1 + num2
      print(f'Hasil Penjumlahan: {hasil}')
    elif inputUser == 2:
      hasil = num1 - num2
      print(f'Hasil Pengurangan: {hasil}')
    elif inputUser == 3:
      hasil = num1 * num2
      print(f'Hasil Perkalian: {hasil}')
    elif inputUser == 4:
      if num1 == 0 and num2 == 0:
        print('Tidak terhingga.')
      elif num2 == 0:
        print('Error: Pembagian tidak diperbolehkan menggunakan 0.')
      else:
        hasil = num1 / num2
        print(f'Hasil Pembagian: {hasil}')
    else:
      print('Masukkan angka operasi dengan benar.')
  except ValueError:
    print('')
    print('Masukkan Angka dengan benar.')
    print('')
    kondisi = input('Apakah Anda ingin keluar(y/n)? ')
    if kondisi == 'y':
      break