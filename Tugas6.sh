#deklarasi array
declare -a arrIPS

#input jumlah element dalam array
echo -n "Masukkan banyak nilai yang akan diinputkan : "
read n

#input nilai dalam array
for ((i=0; i<n; i=i+1))
do
  read arrIPS[$i]
done

#proses perhitungan nilai IPK
sumIPS=0
for i in ${arrIPS[@]};
do
  let sumIPS+=$i;
  let hasil=$sumIPS/$n;
done

#cetak output
echo ""
echo -e "IPS Mahasiswa : $sumIPS / $n"
echo -e "IPK Mahasiswa : $hasil"
