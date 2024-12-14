mulai_berhitung = input('Mari mulai? Y/N ')
mulai_berhitung =  mulai_berhitung.lower()
num_total = 0

while mulai_berhitung == 'y':
    num_1 = int(input('Masukkan angka yang pertama '))

    num_2 = int(input('Masukkan angka yang kedua '))

    diapakan = input('Angka ingin diapakan? (+, -, x, :) ')
    if diapakan == '+':
        num_total = num_1 + num_2
        hasil = 'Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total
        print('Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total)

    elif diapakan == '-':
        num_total = num_1 - num_2
        hasil = 'Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total
        print('Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total)

    elif diapakan == 'x':
        num_total = num_1 * num_2
        hasil = 'Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total
        print('Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total)

    elif diapakan == ':':
        num_total = num_1 / num_2
        hasil = 'Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total
        print('Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total)

    else:
        print('masukin tandanya yang bener dong')
    hasil = 'Total dari perhitungan ', num_1, '', diapakan,'', num_2,'Adalah', num_total

    mulai_berhitung = input('Ingin berlanjut? Y/N ')
    mulai_berhitung =  mulai_berhitung.lower()

print('\nTerimakasih telah berkenan untuk menggunakan kalkulator sederhana ini :D')
