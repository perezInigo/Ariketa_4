from Eskola import Eskola
from Ikaslea import Ikaslea
from Nota import Nota

alumnos_prueba = []
notas_prueba = []

nota = Nota("Programación",9)
notas_prueba.append(nota)
nota1 = Nota("Hacking etico",7)
notas_prueba.append(nota1)

ikaslea = Ikaslea("Iñigo",notas_prueba)
alumnos_prueba.append(ikaslea)

eskola = Eskola(alumnos_prueba)
eskola.menua()