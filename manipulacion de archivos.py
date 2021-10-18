def escritura ():
    from io import open
    texto = "una línea de texto/n0tra línea con texto"
    fichero = open("fichero.txt","w")
    fichero.write(texto)
    fichero.close()
def lectura ():
    from io import open
    fichero = open("fichero.txt","r")
    fichero.read()
    fichero.close()
    print(texto)
def extension ():
    from io import open
    fichero = open("fichero.txt","a")
    fichero.write("\n0tra línea mas abajo del todo")
    fichero.close()

escritura ()
lectura ()
extension ()
