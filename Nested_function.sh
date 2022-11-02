#mendeklrasikan fungsi
nama() {
    echo "Siapa namamu?"
    read nama
    npm                            # <----- Memanggil fungsi didalam fungsi (fungsi bersarang)
}
npm() {
    echo "Sebutkan NPM mu"
    read npm
    echo -e "Hai $nama dengan NPM $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}


#memanggil fungsi
nama
