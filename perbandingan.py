#bismilla
import time 
import sys
from time import sleep as jeda
from os import system as sistem
sistem('pip install requests')
import requests

from requests import Session
s = Session()

def p(s):
  for c in s + '\n' :
    sys.stdout.write(c)
    sys.stdout.flush()
    jeda(1. / 200)

p("""
____    _   _ __  __ _   _ ____
|  _ \ | | | |  \/  | | | / ___|
| |_) || | | | |\/| | | | \___ \

|  _ < | |_| | |  | | |_| |___) |
|_| \_\ \___/|_|  |_|\___/|____/
""")
print("\nWELCOME TO TOOLS RUMUS PERBANDINGAN\n")
jeda(1)
print("tools ini tentang mencari perbandingan di tabel yang mencari waktu, unit, orang")
jeda(0.4)

try:
  print("masukan terlebih dahulu waktu, unit, pekerja di tabel pertama")
  opsiW = int(input("waktu: "))
  opsiU = int(input("unit: "))
  opsiP = int(input("orang: "))
  jeda(1)
  print("selesai sekarang ingin mencari apa?")
  jeda(1)
  data = input("ingin mencari apa[waktu/unit/orang] ")
except:
  print("hanya boleh angka")

try:
  uh = data
except:
  print("jangan langsung enter sebelum nulis data")

try:
  if (uh == "waktu"):
    print("mencari waktu di tabel perbandingan")
    jeda(1)
    print("perhatikan di tabel ke 2 mu lalu masukan unit dan orang")
    unitWU = int(input("unit: "))
    kerjaWP = int(input("orang: "))
    hasilW = int(opsiW * opsiP) / opsiU * (unitWU/kerjaWP)
    print("####HASIL####")
    print("waktu: ",hasilW)
    print("###############")
  elif (uh == "unit"):
    print("mencari unit di tabel perbandingan")
    jeda(1)
    print("perhatikan di tabel ke 2 mu lalu masukan waktu dan pekerja")
    unitUW = int(input("waktu: "))
    kerjaUP = int(input("orang: "))
    hasilU = int(unitUW / (opsiW * ((opsiP/opsiU)/kerjaUP)))
    print("####HASIL####")
    print("unit: ",hasilU)
    print("##############")
  elif (uh == "orang"):
    print("mencari orang di tabel perbandingan")
    jeda(1)
    print("perhatikan di tabel ke 2 mu lalu masukan waktu dan unit")
    unitPW = int(input("waktu: "))
    kerjaPU = int(input("unit: "))
    cara1 = int(opsiW * opsiP) / opsiU * (kerjaPU/unitPW)
    print("####HASIL####")
    print("waktu: ",cara1)
    print("#############")
  else:
    print(data,"tidak ada dalam data")
    print("hanya ada pilihan waktu, unit, dan orang")
except:
  print("hanya boleh angka")
