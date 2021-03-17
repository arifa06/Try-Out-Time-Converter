# Perhitungan Detik
def timeConverter():
    SS = int(input('Masukkan Detik : '))
    if 1 < SS < 359999:
        HH = int(SS/3600)
        SS = int(SS-(3600*HH))
        MM = int(SS/60)
        SS = int(SS-(60*MM))
        print('Konversi',str(HH)+':'+str(MM)+':'+str(SS))
    else:
        print('Invalid Input')

timeConverter()
timeConverter()