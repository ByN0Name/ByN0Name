def creación_escritura ():
    from io import open
    texto = "Una línea con texto\n0tra línea con texto"
    fichero = open('fichero.txt','w')
    fichero.write(texto)
    fichero.close()
def lectura ():
    from io import open
    fichero = open('fichero.txt','r')
    texto = fichero.read()
    fichero.close()
    print(texto)
def extension ():
    from io import open
    fichero = open('fichero.txt','a')
    fichero.write('\n0tra línea más abajo del todo')
    fichero.close()
    
creación_escritura ()
lectura ()
extension ()
