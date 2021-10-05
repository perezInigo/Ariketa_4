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

    def zerrenda(self):
