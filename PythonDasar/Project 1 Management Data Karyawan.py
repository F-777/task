import csv
import os
namafile = r'C:\xampp\htdocs\python\pythondasar\data_karyawan.csv'
def init_csv():
  if not os.path.exists(namafile):
    with open(namafile, mode = 'w', newline = '') as file:
      writer = csv.writer(file)
      writer.writerow(['ID', 'Nama', 'Jabatan', 'Gaji'])
def tambah_karyawan(id, nama, jabatan, gaji):
  with open(namafile, mode = 'a', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow([id, nama, jabatan, gaji])
  print('Berhasil menambahkan data karyawan baru.')
def hapus_karyawan(id):
  rows = []
  with open(namafile, mode = 'r', newline = '') as file:
    reader = csv.reader(file)
    rows = list(reader)
  with open(namafile, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(rows[0])
    found = False
    for row in rows[1:]:
      if row[0] != id:
        writer.writerow(row)
      else:
        found = True
      if found == True:
        print(f'Data karyawan dengan ID {id} berhasil dihapus.')
      else:
        print(f'Data karyawan dengan ID {id} tidak ditemukan.')
def update_karyawan(id, nama=None, jabatan=None, gaji=None):
  rows = []
  updated = False
  with open(namafile, mode = 'r', newline = '') as file:
    reader = csv.reader(file)
    rows = list(reader)
  with open(namafile, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(rows[0])
    for row in rows[1:]:
      if row[0] == id:
        if nama is not None:
          row[1] = nama
        if jabatan is not None:
          row[2] = jabatan
        if gaji is not None:
          row[3] = gaji
        updated = True
      writer.writerow(row)
  if updated:
    print(f'Data karyawan dengan ID {id} berhasil diperbarui.')
  else:
    print(f'Data karyawan dengan ID {id} tidak dapat diperbarui.')
def tampilkan_karyawan():
  with open(namafile, mode = 'r', newline = '') as file:
    reader = csv.reader(file)
    for row in reader:
      print(f'ID:{row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')
def tampilkan_karyawan_berdasar_id(id):
  show_id = False
  with open(namafile, mode = 'r', newline = '') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      if row[0] == id:
        show_id = True
        print(f'ID:{row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')
        break
  if not show_id:
    print(f'Tidak dapat menemukan karyawan dengan ID {id}.')
def menu():
  while True:
    print('\n Pilihan:')
    print('1. Menambahkan Karyawan')
    print('2. Menghapus Karyawan')
    print('3. Update Karyawan')
    print('4. Tampilkan Karyawan')
    print('5. Tampilkan Karyawan berdasarkan ID')
    print('6. Keluar')
    inputUser = input('Masukan Angka yang ingin anda lakukan(1-6): ')
    if inputUser == '1':
      id = input('Masukan ID: ')
      nama = input('Masukan Nama Karyawan: ')
      jabatan = input('Masukan Jabatan: ')
      gaji = input('Masukan Gaji: ')
      tambah_karyawan(id, nama, jabatan, gaji)
    elif inputUser == '2':
      id = input('Masukan ID karyawan yang ingin dihapus: ')
      hapus_karyawan(id)
    elif inputUser == '3':
      id = input('Masukan ID karyawan yang akan diperbarui: ')
      nama = input('Masukan nama baru (kosongkan jika tidak diubah): ')
      jabatan = input('Masukan jabatan baru (kosongkan jika tidak diubah): ')
      gaji = input('Masukan gaji baru (kosongkan jika tidak diubah): ')
      update_karyawan(id, nama if nama else None, jabatan if jabatan else None, gaji if gaji else None)
    elif inputUser == '4':
      tampilkan_karyawan()
    elif inputUser == '5':
      id = input('Masukan ID karyawan yang ingin Anda cari: ')
      tampilkan_karyawan_berdasar_id(id)
    elif inputUser == '6':
      print('Keluar dari program.')
      break
    else:
      print('Silahkan masukan angka dari pilihan yang valid.')
if _name_ == '_main_':
  init_csv()
menu()