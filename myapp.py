import tkinter as tk
import os
import random
import calendar
from datetime import date

height = 700
width = 800

mat = ()
middager = []
dato = date.today()

dagNo = calendar.day_name[dato.weekday()]

sunneMiddager = ['Spagetti', 'Fiskegrateng', 'Kylling', 'Gryterett', 'Suppe']
usunneMiddager = ['Pizza', 'Hamburger', 'Taco']

# Legger begge listene inn i middager listen
middager.extend(sunneMiddager)
middager.extend(usunneMiddager)

# Oppretter lister med ingrediensene som hører til de forskjellige middagene.
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



def middagVelg():
    if dagNo in manTors:
        mat = random.choice(middager[0:5])

    elif dagNo in helg:
        mat = random.choice(middager[5:7])

    elif dagNo == 'Friday':
        mat = (middager[7])



# Printer ut svaret på hva som skal spises, og henter ingrediensene fra listen til de forskjellige middagene.
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




window = tk.Tk()

canvas = tk.Canvas(window, height=height, width=width)
canvas.pack()

frame = tk.Frame(window, bg='#F2B290')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


button = tk.Button(frame, text="Test Button", command= middagVelg)
button.pack()


label = tk.Label(frame, text="Trykk for å få et forsalg til middag og hva du trenger", bg='white')
label.pack()

entry = tk.Entry(frame, text=middagVelg, bg='white')
entry.pack()

window.mainloop()
