import os
import sys

total = []

def clear_screen():
    os.system('celar' if(os.name=='nt') else'clear')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali")
    clear_screen()

def keluar():
    print("+----------------------------------------------+")
    print("|     SILAHKAN LAKUKAN PEMBAYARAN UKHTI !!     |")
    print("+----------------------------------------------+")
    print("|                                              |")
    print("|        Klik Menu Lakukan Pembayaran !!       |")
    print("|                                              |")
    print("+----------------------------------------------+")

def exit():
    print("+------------------------------------------------------+")
    print("|                                                      |")
    print("|           Terima Kasih Atas Kunjungan Anda           |")
    print("|                                                      |")
    print("+------------------------------------------------------+")

def menu_awal():
    while(True):
        print("+------------------------------------------------------+")
        print("|              Assalamu'alaikum Ukhti :)               |")
        print("+------------------------------------------------------+")
        print("|                                                      |")
        print("|           Selamat Datang di El-Lisya Hijab           |")
        print("|                Big Purchase, Big Bonus               |")
        print("|                                                      |")
        print("+------------------------------------------------------+")
        print("                      El-Lisya Home                     ")
        print("--------------------------------------------------------")
        print("    1. Koleksi Hijab By El-Lisya                        ")
        print("    2. Aneka Aksesoris Hijab By El-Lisya                ")
        print("    3. Lihat Daftar Diskon By El-Lisya Hijab            ")
        print("    4. Lakukan Pembayaran                               ")
        print("    5. Keluar                                           ")
        print("--------------------------------------------------------")
        try:
            a=int(input("Masukkan menu yang anda pilih (1-5) : "))
            print()
            if(a==1):
                koleksi_hijab()
                kembali()
            elif(a==2):
                aksesoris()
                kembali()
            elif(a==3):
                daftar_diskon()
                kembali()
            elif(a==4):
                akhir()
                kembali()
            elif(a==5):
                exit()
                break
            else:
                print("Masukkan kembali menu yang anda pilih (1-5) : ")
                kembali()
                continue
        except ValueError:
            print("Masukkan angka sesuai yang ada di daftar menu !!")
            kembali()
            continue

def koleksi_hijab():
    print("+-----------------------------------------------------+")
    print("|              Koleksi Hijab By El-Lisya              |")
    print("+-----------------------------------------------------+")
    print("  No. |             Daftar Hijab             |  Harga  ")
    print("-------------------------------------------------------")
    print("  1.  | Hijab Segi-empat Polos Premium       |  40000  ")
    print("  2.  | Hijab Segi-empat Motif Premium       |  50000  ")
    print("  3.  | Hijab Pashmina Diamond               |  55000  ")
    print("  4.  | Hijab Pashmina Plisket               |  65000  ")
    print("  5.  | Hijab Syar'i                         |  75000  ")
    print("  6.  | Hijab Sport Premium                  |  35000  ")
    print("-------------------------------------------------------")
    nanya=input("Apakah anda ingin membeli ? [y/t] : ")
    if(nanya=="y"):
        kode=int(input("Masukkan nomor barang : "))
        if(kode==1):
            jumlah1=int(input("Masukkan jumlah barang : "))
            total1=40000*jumlah1
            total.append(total1)
            tanya()
        elif(kode==2):
            jumlah2=int(input("Masukkan jumlah barang : "))
            total2=50000*jumlah2
            total.append(total2)
            tanya()
        elif(kode==3):
            jumlah3=int(input("Masukkan jumlah barang : "))
            total3=55000*jumlah3
            total.append(total3)
            tanya()
        elif(kode==4):
            jumlah4=int(input("Masukkan jumlah barang : "))
            total4=65000*jumlah4
            total.append(total4)
            tanya()
        elif(kode==5):
            jumlah5=int(input("Masukkan jumlah barang : "))
            total5=75000*jumlah5
            total.append(total5)
            tanya()
        elif(kode==6):
            jumlah6=int(input("Masukkan jumlah barang : "))
            total6=35000*jumlah6
            total.append(total6)
            tanya()
        return
    else:
        menu_awal()

def aksesoris():
    print("+-----------------------------------------------------+")
    print("|          Aneka Aksesoris Hijab By El-Lisya          |")
    print("+-----------------------------------------------------+")
    print("   No. |           Daftar Aksesoris         |   Harga  ")
    print("-------------------------------------------------------")
    print("   1.  | Bros Muatiara Premium              |   25000  ")
    print("   2.  | Ring Hijab                         |   25000  ")
    print("   3   | Tuspin Hijab Mutiara Premium       |   20000  ")
    print("   4.  | Inner Bandana                      |   30000  ")
    print("   5.  | Inner Ninja Premium                |   35000  ")
    print("-------------------------------------------------------")
    nanya=input("Apakah anda ingin membeli ? [y/t] : ")
    if(nanya=="y"):
        kode=int(input("Masukkan nomor barang : "))
        if(kode==1):
            jumlah1=int(input("Masukkan jumlah barang : "))
            total1=25000*jumlah1
            total.append(total1)
            tanya()
        elif(kode==2):
            jumlah2=int(input("Masukkan jumlah barang : "))
            total2=25000*jumlah2
            total.append(total2)
            tanya()
        elif(kode==3):
            jumlah3=int(input("Masukkan jumlah barang : "))
            total3=20000*jumlah3
            total.append(total3)
            tanya()
        elif(kode==4):
            jumlah4=int(input("Masukkan jumlah barang : "))
            total4=30000*jumlah4
            total.append(total4)
            tanya()
        elif(kode==5):
            jumlah5=int(input("Masukkan jumlah barang : "))
            total5=35000*jumlah5
            total.append(total5)
            tanya()
        return
    else:
        menu_awal()

def dafar_diskon():
    print("+---------------------------------------------------+")
    print("|          Daftar Diskon By El-Lisya Hijab          |")
    print("+---------------------------------------------------+")
    print("   No. |       Jumlah Belanja       | Jumlah Diskon  ")
    print("-----------------------------------------------------")
    print("   1.  | Belanja > Rp 100000,-      |       5%       ")
    print("   2.  | Belanja > Rp 200000,-      |      10%       ")
    print("   3.  | Belanja > Rp 300000,-      |      15%       ")
    print("   4.  | Belanja > Rp 400000,-      |      20%       ")
    print("-----------------------------------------------------")

def tanya():
    print("-------------------------------------------------------")
    tanya=input("Apakah anda ingin menambah barang lagi ? [y/t] : ")
    print("-------------------------------------------------------")
    if(tanya=="y"):
        menu_awal()
    elif(tanya=="t"):
        keluar()
    else:
        print("Pilihan yang anda masukkan salah")
        return tanya()

def akhir():
    for harga in total:
        print("-----------------------------------------------------")
        print("SubTotal                    : ", sum(total))
        diskon=0
        a=sum(total)
        if(a>100000):
            diskon=a*5/100
        elif(a>200000):
            diskon=a*10/100
        elif(a>300000):
            diskon=a*15/100
        elif(a>400000):
            diskon=a*20/100
        else:
            diskon=0
        print("Potongan Harga              : ", diskon)
        totalakhir=a-diskon
        print("Total                       : ", totalakhir)
        print("-----------------------------------------------------")
        bayar=int(input("Jumlah Pembayaran           :  "))
        kembalian=bayar-totalakhir
        print("Kembalian                   : ", kembalian)
        print("+---------------------------------------------------+")
        print("|                                                   |")
        print("|                 Terima Kasih Ukhti                |")
        print("|                                                   |")
        print("+---------------------------------------------------+")

menu_awal()
