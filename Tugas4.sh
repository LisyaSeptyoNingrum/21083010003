echo "Program Ganjil"
echo "By : Lisya"
echo "-------------------------------"

echo -n "Masukkan batas bawah : "
read a

echo -n "Masukkan batas atas : "
read b

echo "-------------------------------"

for ((angka=a; angka<=b; angka=angka+2))
do
  echo $angka
done
