PODATEK_17 = 0.1775
PODATEK_32 = 0.32
KWOTA_WOLNA_OD_PODATKU = 8000
KWOTA_OBNIZAJACA_DO_8000 = KWOTA_WOLNA_OD_PODATKU * PODATEK_17
DANINA_SOLIDARNOSCIOWA = 0.04

def oblicz_podatek(podstawa):
    if(podstawa <= 8000):
        return 0
    elif(podstawa > 8000 and podstawa <= 13000):
        return podstawa*PODATEK_17-(KWOTA_OBNIZAJACA_DO_8000-871.7*(podstawa-KWOTA_WOLNA_OD_PODATKU)/5000)
    elif(podstawa > 13000 and podstawa <= 85528):
        return (podstawa*PODATEK_17)-548.3
    elif(podstawa > 85528 and podstawa <= 127000):
        return podstawa*PODATEK_32-(548.3-548.3*(podstawa-85528)/41472)
    elif(podstawa > 127000 and podstawa <= 1000000):
        return podstawa*PODATEK_32
    else:
        return podstawa*PODATEK_32+(DANINA_SOLIDARNOSCIOWA*(podstawa-1000000))
    
def wykonaj_obliczenie():
    imie_i_naziwsko = input('Podaj nazwisko i imię: ')
    podstawa = float(input('Podaj kwotę podstawy w zł: '))
    podatek = oblicz_podatek(podstawa)
    print("Podatek: " + str(podatek))

for x in range(3):
    wykonaj_obliczenie()