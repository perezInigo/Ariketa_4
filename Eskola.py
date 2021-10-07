from Nota import Nota
from Ikaslea import Ikaslea

class Eskola:
    ikasleak = []

    def __init__(self,i_ikasleak):
        self.ikasleak = i_ikasleak

    def menua(self):
        opcion = 0
        while opcion != 3:
            print("-------------Menú-------------")
            print("1.- Ikasleak gehitu ")
            print("2.- Ikasleak ikusi ")
            print("3.- Itxi")
            print("------------------------------")
            print("Escribe el numero a ejecutar:")
            opcion = int(input())

            if opcion == 1:
                self.gehitu()
            if opcion == 2:
                self.zerrenda()

    def gehitu(self):
        ikaslearen_notak = []
        fin = 1
        print("-----------Ikaslea sortzen-----------")
        print("Idatzi ikaslearen IZENA:")
        izen_berria = input()
        print("Sortu "+izen_berria+"-ren notak.")
        while fin != 0:
            print("Ikasgaiaren izena: (bukatzeko exit idatzi izenean)")
            ikasgai_izena_berria = input()
            if ikasgai_izena_berria != "exit":
                print("Zein nota du "+izen_berria+" "+ikasgai_izena_berria+" ikasgaian?")
                ikasgai_nota_berria = int(input())
                nota_berria = Nota(ikasgai_izena_berria,ikasgai_nota_berria)
                ikaslearen_notak.append(nota_berria)
            else:
                fin = 0
        ikasle_berria = Ikaslea(izen_berria,ikaslearen_notak)
        self.ikasleak.append(ikasle_berria)


    def zerrenda(self):
        for ikaslea in self.ikasleak:
            print("-------------")
            print(ikaslea.izena)
            print("-------------")
            for nota in ikaslea.notak:
                print("- "+nota.izena+": "+str(nota.notak))
