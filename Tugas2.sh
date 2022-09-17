echo "Program Menghitung Artimatika Sederhana"
echo "----------------------------------------------------------"
echo "By : Lisya"
echo "----------------------------------------------------------"

echo -n "Masukkan angka pertama, sebagai (a) : "
read a

echo -n "Masukkan angka kedua, sebagai (b) : "
read b

echo "----------------------------------------------------------"

echo "Proses perhitungan yang dapat dieksekusi : "
echo "1. Penjumlahan"
echo "2. Pengurangan"
echo "3. Perkalian"
echo "4. Pembagian"
echo "5. Modulus (sisa pembagian)"
echo "6. Perbandingan nilai"
echo -n "Masukkan angka yang mewakili proses eksekusi : "
read proses

if [[ $proses = 1 ]]
then
  let c=$a+$b
  echo "a + b"
  echo "$a + $b = $c"

elif [[ $proses = 2 ]]
then
  let d=$a-$b
  echo "a - b"
  echo "$a - $b = $d"

elif [[ $proses = 3 ]]
then
  let e=$a*$b
  echo "a * b"
  echo "$a * $b = $e"

elif [[ $proses = 4 ]]
then
  let f=`expr $a / $b`
  echo "a / b"
  echo "$a / $b = $f"

elif [[ $proses = 5 ]]
then
  let g=$(($a % $b))
  echo "a % b"
  echo "$a % $b = $g"

else
  if [ $a == $b ]
  then
    echo "Nilai a sama dengan nilai b"
  elif [ $a -gt $b ]
  then
    echo "Nilai a lebih besar dari nilai b"
  else
    echo "Nilai a lebih kecil dari nilai b"

  fi
fi
