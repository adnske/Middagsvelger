import random
import calendar
from datetime import date

# variabler
mat = ()
middager = []
dato = date.today()

dagNo = calendar.day_name[dato.weekday()]

# oppretter lister for ulike type middager, har to for å få en lettere oversikt over sunne/usunne.
sunneMiddager = ['Spagetti', 'Fiskegrateng', 'Kylling', 'Gryterett', 'Suppe']
usunneMiddager = ['Pizza', 'Hamburger', 'Taco']

#Legger begge listene inn i middager listen
middager.extend(sunneMiddager)
middager.extend(usunneMiddager)

#Oppretter lister med ingrediensene som hører til de forskjellige middagene.
spagetti = ['spaggeti', 'saus', 'kjøttdeig']
fiskegrateng = ['fiskegrateng', 'poteter', 'brokkoli']
kylling = ['kyllingfilet', 'ris', 'grønnsaker']
gryterett = ['toro-gryterett', 'kjøttdeig', 'mais', 'løk']
tomatsuppe = ['tomatsuppe', 'egg', 'melk', 'ost']
taco = ['kjøttdeig', 'mais', 'krydder', 'tortilla', 'rømme', 'saus', 'ost']
pizza = ['pizzadeig', 'ost', 'tomatsaus', 'pepperoni']
hamburger = ['burgerbrød', 'hamburger', 'ost', 'mais', 'sylteagurk', 'ketchup']

#Lister for å skille mellom hverdag og helg.
manTors = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
helg = ['Saturday', 'Sunday']


#matcher input mot listene manTors, helg og stringen "fredag".
#Setter deretter variabelen mat til å være lik en tilfeldig valgt matrett i middager.
if dagNo in manTors:
    mat = random.choice(middager[0:5])

elif dagNo in helg:
    mat = random.choice(middager[5:7])

elif dagNo == 'Friday':
    mat = (middager[7])



#Printer ut svaret på hva som skal spises, og henter ingrediensene fra listen til de forskjellige middagene.
if mat == 'Spagetti':
    print('Du skal spise', mat, 'og du må derfor kjøpe:', ', '.join(spagetti))

elif mat == 'Fiskegrateng':
    print('Du skal spise', mat, 'og du må derfor kjøpe:', ', '.join(fiskegrateng))

elif mat == 'Kylling':
    print('Du skal spise', mat, 'og du må derfor kjøpe:', ', '.join(kylling))

elif mat == 'Gryterett':
    print('Du skal spise', mat, 'og du må derfor kjøpe:', ', '.join(gryterett))

elif mat == 'Tomatsuppe':
    print('Du skal spise', mat, 'og du må derfor kjøpe:', ', '.join(tomatsuppe))

elif mat == 'Pizza':
    print('Du skal spise', mat, 'og du må derfor kjøpe:', ', '.join(pizza))

elif mat == 'Hamburger':
    print('Du skal spise', mat, 'og du må derfor kjøpe:', ', '.join(hamburger))

elif mat == 'Taco':
    print('Du skal spise', mat, 'som hver fredag og du må derfor kjøpe:', ', '.join(taco))








