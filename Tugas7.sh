#mendeklarasikan fungsi
panjang() {
    echo "Masukkan panjang : "
    read p
}

lebar() {
    echo "Masukkan lebar : "
    read l
}

luas() {
    echo "Program Menghitung Luas Bidang Persegi"
    panjang
    lebar
    let l=$p*$l
    echo "Luas = $l"
}



#memanggil fungsi
luas
