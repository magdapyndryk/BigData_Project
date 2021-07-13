liczba_wyrazow = int(input('Podaj liczbę wyrazów: '))
if liczba_wyrazow >= 1 and liczba_wyrazow <= 3000:
    print ('Liczba wyrazów w Twoim słowniku: ' + str(liczba_wyrazow))
else:
    print ('Błąd. Wprowadź ponownie liczbę wyrazów.')

slownik = []
    
for i in range(liczba_wyrazow):
    slowo = input()
    slownik.append(slowo)
    
#slownik = ['pies', 'siep', 'kot', 'tok', 'pieknie', 'uzod', 'duzo', 'ozud', 'kot']
slownik_set = set(slownik)
pogrupowane_anagramy = {}
for string in list(slownik_set):
    posortowane_stringi = str(sorted(string))
    if posortowane_stringi in pogrupowane_anagramy:
        pogrupowane_anagramy[posortowane_stringi].append(string)
    else:
        pogrupowane_anagramy[posortowane_stringi] = [string]

for string in list(pogrupowane_anagramy.values()):
    print(string)