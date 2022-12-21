print("----------------- Program Kasir Sederhana Ekorkode -----------------")
pembeli = input("Masukkan nama pembeli: ")
Tanggal_pembeli = input("Masukan tgl pembelian: ")


def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Steak - Rp 175000")
   print("2. Salmon - Rp 240000")
   print("3. Sushi - Rp 98000")
   print("4. Chiken Katsu - Rp 74000")
   print("5. Caviar - Rp 630000")
   print("6. Burger - Rp 57000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*175000
       print (porsi," porsi Steak = Rp", totalmkn)
       mkn=("Steak")
   elif nomor==2:
       totalmkn=porsi*240000
       print (porsi," porsi Salmon = Rp", totalmkn)
       mkn=("Salmon")
   elif nomor==3:
       totalmkn=porsi*98000
       print (porsi, " porsi Sushi = Rp", totalmkn)
       mkn=("Sushi")
   elif nomor==4:
       totalmkn=porsi*74000
       print (porsi, " porsi Chiken Katsu = Rp", totalmkn)
       mkn=("Chiken Katsu")
   elif nomor==5:
       totalmkn=porsi*630000
       print (porsi, " porsi Caviar = Rp", totalmkn)
       mkn=("Caviar")
   elif nomor==6:
       totalmkn=porsi*57000
       print (porsi, " porsi Burger = Rp", totalmkn)
       mkn=("Burger")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Berry Ice Tea - Rp 70000")
   print("2. Coffee Latte - Rp 65000")
   print("3. Coktail - Rp 120000")
   print("4. Vodka - Rp 300000")
   print("5. Smoties Orange - Rp 85000")
   print("6. Americano - Rp 95000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*70000
       print (gelas," Gelas Berry Ice Tea = Rp", totalmnm)
       mnm=(" Berry Ice Tea")
   elif nomor==2:
       totalmnm=gelas*65000
       print (gelas, " Gelas Coffee Latte = Rp", totalmnm)
       mnm=("Coffee Latte")
   elif nomor==3:
       totalmnm=gelas*120000
       print (gelas, " Gelas Coktail = Rp", totalmnm)
       mnm=("Coktail")
   elif nomor==4:
       totalmnm=gelas*300000
       print (gelas, " Gelas Vodka = Rp", totalmnm)
       mnm=("Vodka")
   elif nomor==5:
       totalmnm=gelas*85000
       print (gelas, " Gelas Smoties Orange = Rp", totalmnm)
       mnm=("Smoties Orange")
   elif nomor==6:
       totalmnm=gelas*95000
       print (gelas, " Gelas Americano = Rp", totalmnm)
       mnm=("Americano")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")