

"""

from turtle import *
from freegames import line

turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}

def grid():
    "Draw Connect Four grid."
    bgcolor('light blue')

    for x in range(-150, 200, 50):
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()

def tap(x, y):
    "Draw red or yellow circle in tapped row."
    player = state['player']
    rows = state['rows']

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    rows[row] = count + 1
    state['player'] = turns[player]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(tap) # clique souris tekhou lcordonnees x y taa souris f blaset l click
done()
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


class Personne():
    def __init__(self,nom='',prenom=''):
        self.nom=nom
        self.prenom=prenom
class Etudiant (Personne):
    def __init__(self,nom='',prenom='',matricue='',note={}):
        Personne.__init__(self,nom,prenom)
        self.matricule=matricue
        self.note=note
    def ajouter_note_cours(self,id_cours,note):
        self.note[id_cours]=note
class Cours ():
    def __init__(self,id_cours='',liste_etudiants=[]):
        self.id_cours=id_cours
        self.liste_etudiant=liste_etudiants
    def ajouter_etudiant(self,etudiant):
        self.liste_etudiant.append(etudiant)
    def retourner_moy(self):
        x=0
        h=0
        for i in self.liste_etudiant :

             x+=i.note[self.id_cours]
             h+=1
        return x/h
c1=Cours("Paradigme")
et1=Etudiant('mahmoud','ali','122')
et1.ajouter_note_cours("Paradigme",15.5)
c1.ajouter_etudiant(et1)
et2=Etudiant('salah','fatma','123')
et2.ajouter_note_cours("Paradigme",12.0)
c1.ajouter_etudiant(et2)
print(c1.retourner_moy())



"""
def f(x):
    if (x > 50):
        return x - 5
    return f(f(x+10))
print(f(20))


