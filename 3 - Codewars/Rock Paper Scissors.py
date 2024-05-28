import random
Tabela = ['R', 'P', 'S']
W_gracz = 0
W_komp = 0

Dlugosc_gry = int(input('Podaj ile partii chcesz rozegrać '))

for i in range(0,Dlugosc_gry):
    Wybor = input('Podaj swój wybór (R,P,S) ')
    Z_tab = int(random.randrange(0,2))

    if Wybor == 'R' and Z_tab == 0:
        print(f'Remis!, Przeciwnik wylosował {Tabela[Z_tab]}')
    elif Wybor == 'P' and Z_tab == 1:
        print(f'Remis!, Przeciwnik wylosował {Tabela[Z_tab]}')
    elif Wybor == 'S' and Z_tab == 2:
        print(f'Remis!, Przeciwnik wylosował {Tabela[Z_tab]}')
    elif Wybor == 'R' and Z_tab == 1:
        print(f'Przegrałeś!, Przeciwnik wylosował {Tabela[Z_tab]}')
        W_komp += 1
    elif Wybor == 'R' and Z_tab == 2:
        print(f'Wygrałeś!, Przeciwnik wylosował {Tabela[Z_tab]}')
        W_gracz += 1
    elif Wybor == 'P' and Z_tab == 0:
        print(f'Wygrałeś!, Przeciwnik wylosował {Tabela[Z_tab]}')
        W_gracz += 1
    elif Wybor == 'P' and Z_tab == 2:
        print(f'Przegrałeś!, Przeciwnik wylosował {Tabela[Z_tab]}')
        W_komp += 1
    elif Wybor == 'S' and Z_tab == 0:
        print(f'Przegrałeś!, Przeciwnik wylosował {Tabela[Z_tab]}')
        W_komp += 1
    elif Wybor == 'S' and Z_tab == 1:
        print(f'Wygrałeś!, Przeciwnik wylosował {Tabela[Z_tab]}')
        W_gracz += 1
    else:
        print('Nie ma takiej figury!')

print('Końcowy wynik to ', W_gracz, ':', W_komp)
