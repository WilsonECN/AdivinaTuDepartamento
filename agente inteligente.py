import random
import dataset

print(len(dataset.ListaRegiones))

def PreguntasRegion():
    listaRandomRegion = [""]
    for i in range(4):
        RANDOM = random.randrange(len(ListaDepartamentos))
        listo=True
        while listo:
            if ListaDepartamentos[RANDOM].Region in listaRandomRegion:
                # print("el objeto ya"" esta en la lista")
                RANDOM =random.randrange(len(ListaDepartamentos))
            else:
                listaRandomRegion.append(ListaDepartamentos[RANDOM].Region)
                # print("El objeto no esta en la lista")
                listo=False
        print(dataset.PREGUNTA.Region + ListaDepartamentos[RANDOM].Region)
        print("1) Sí  2) No")
        Respuesta = int(input("Respuesta: "))
        if Respuesta == 1:
            for a in range(len(ListaDepartamentos)):
                if ListaDepartamentos[RANDOM].Region == ListaDepartamentos[a].Region:
                    ListaDepartamentos[a].Probabilidad+=1
            break
        else:
            for a in range(len(ListaDepartamentos)):
                if ListaDepartamentos[RANDOM].Region != ListaDepartamentos[a].Region:
                    ListaDepartamentos[a].Probabilidad+=1   

# def PreguntasRegion():
#     listaRandom = []
#     for i in range(4):
#         RANDOM = RANDOMNUMERONUEVO(listaRandom)
#         print(dataset.PREGUNTA.Region + ListaDepartamentos[RANDOM].Region)
#         print("1) Sí  2) No")
#         Respuesta = int(input("Respuesta: "))
#         if Respuesta == 1:
#             for a in range(len(ListaDepartamentos)):
#                 if ListaDepartamentos[RANDOM].Region == ListaDepartamentos[a].Region:
#                     ListaDepartamentos[a].Probabilidad+=1
#         else:
#             for a in range(len(ListaDepartamentos)):
#                 if ListaDepartamentos[RANDOM].Region != ListaDepartamentos[a].Region:
#                     ListaDepartamentos[a].Probabilidad+=1   


def PreguntasLengua():
    listaRandomLenguas = [""]
    for x in range(4):
        RANDOM = random.randrange(len(ListaDepartamentos))
        RANDOMLENGUA = random.randrange(len(ListaDepartamentos[RANDOM].Lenguas))
        contador=0
        listo=True
        while listo:
            contador+=1
            if contador>+20:
                listo = False
                break
            # print(listaRandomLenguas)
            if ListaDepartamentos[RANDOM].Lenguas[RANDOMLENGUA] in listaRandomLenguas:
                # print("el objeto ya"" esta en la lista")
                RANDOM =random.randrange(len(ListaDepartamentos))
                RANDOMLENGUA = random.randrange(len(ListaDepartamentos[RANDOM].Lenguas))
            else:
                listaRandomLenguas.append(ListaDepartamentos[RANDOM].Lenguas[RANDOMLENGUA])
                # print("El objeto no esta en la lista")
                listo=False
        print(dataset.PREGUNTA.Lengua + ListaDepartamentos[RANDOM].Lenguas[RANDOMLENGUA])
        print("1) Sí  2) No")
        Respuesta = int(input("Respuesta: "))
        if Respuesta == 1:
            for a in range(len(ListaDepartamentos)):
                resultado = False
                for e in range(len(ListaDepartamentos[a].Lenguas)):
                    if ListaDepartamentos[a].Lenguas[e] == ListaDepartamentos[RANDOM].Lenguas[RANDOMLENGUA]:
                        resultado = True
                        # print("En "+ListaDepartamentos[a].Nombre + " esta "+ ListaDepartamentos[RANDOM].Lenguas[RANDOMLENGUA])
                        break
                if resultado:
                    ListaDepartamentos[a].Probabilidad+=1
                    # print("En "+ListaDepartamentos[a].Nombre + " se sumo 1 por "+ ListaDepartamentos[a].Lenguas[e])

def PregutnasComidas():
    listaRandomComidas = [""]
    for x in range(3):
        # print(listaRandomComidas)
        RANDOM = random.randrange(len(ListaDepartamentos))
        contador = 0
        listo=True
        while listo:
            contador+=1
            if contador>20:
                listo = False
                break
            if ListaDepartamentos[RANDOM].Comidas in listaRandomComidas:
                # print("el objeto ya"" esta en la lista")
                RANDOM =random.randrange(len(ListaDepartamentos))
            else:
                listaRandomComidas.append(ListaDepartamentos[RANDOM].Comidas)
                # print("El objeto no esta en la lista")
                listo=False
        print(dataset.PREGUNTA.Comida + ListaDepartamentos[RANDOM].Comidas)
        print("1) Sí  2) No")
        Respuesta = int(input("Respuesta: "))
        if Respuesta == 1:
            ListaDepartamentos[RANDOM].Probabilidad+=3
        else:
            for a in range(len(ListaDepartamentos)):
                if ListaDepartamentos[a].Comidas != ListaDepartamentos[RANDOM].Comidas:
                    ListaDepartamentos[a].Probabilidad+=1

def PreguntasLugares():
    listaRandomLugares = [""]
    for x in range(len(ListaDepartamentos)):
        RANDOM = random.randrange(len(ListaDepartamentos))
        RANDOMLUGAR = random.randrange(len(ListaDepartamentos[RANDOM].Lugares))
        listo=True
        while listo:
            # print(listaRandomLugares)
            if ListaDepartamentos[RANDOM].Lugares[RANDOMLUGAR] in listaRandomLugares:
                # print("el objeto ya"" esta en la lista")
                RANDOM =random.randrange(len(ListaDepartamentos))
                RANDOMLUGAR = random.randrange(len(ListaDepartamentos[RANDOM].Lugares))
            else:
                listaRandomLugares.append(ListaDepartamentos[RANDOM].Lugares[RANDOMLUGAR])
                # print("El objeto no esta en la lista")
                listo=False
        print(dataset.PREGUNTA.Lugar + ListaDepartamentos[RANDOM].Lugares[RANDOMLUGAR])
        print("1) Sí  2) No")
        Respuesta = int(input("Respuesta: "))
        if Respuesta == 1:
            # print("5 mas para "+ListaDepartamentos[RANDOM].Nombre+" Por: "+ListaDepartamentos[RANDOM].Lugares[RANDOMLUGAR])
            ListaDepartamentos[RANDOM].Probabilidad+=10
        else:
            for z in range(len(ListaDepartamentos)):
                # print("1 mas para "+ListaDepartamentos[z].Nombre+" Por no tener: "+ListaDepartamentos[RANDOM].Lugares[RANDOMLUGAR])
                if ListaDepartamentos[RANDOM].Nombre != ListaDepartamentos[z].Nombre:
                    ListaDepartamentos[z].Probabilidad+=1
# def PreguntasRegion():
#     for i in range(4):
#         RegionRandom = random.randrange(len(dataset.ListaRegiones))
#         print(dataset.PREGUNTA.Region + dataset.ListaRegiones[RegionRandom].Nombre)
#         print("1) Sí  2) No")
#         Respuesta = int(input("Respuesta: "))
#         if Respuesta == 1:
#             #print("Departamentos en esta region: "+str(len(ListaRegiones[RegionRandom].Departamentos)))
#             for i in range(len(dataset.ListaRegiones[RegionRandom].Departamentos)):
#                 dataset.ListaDepartamentos[dataset.ListaRegiones[RegionRandom].DepOnID[i]].Probabilidad+=1
#                 #print("+1 a "+ ListaDepartamentos[ListaRegiones[RegionRandom].DepOnID[i]].Nombre)
#         else:
#             for e in range(len(dataset.ListaRegiones)): 
#                 #print("ciclo : "+str(e) +" "+ ListaRegiones[e].Nombre)
#                 if e != RegionRandom:
#                     for a in range(len(dataset.ListaRegiones[e].Departamentos)):
#                         dataset.ListaDepartamentos[dataset.ListaRegiones[e].DepOnID[a]].Probabilidad+=1
#                         #print("     ciclo interno: "+str(a))
#                         #print("     deptOnID : "+str(ListaRegiones[e].DepOnID[a]))
#                         #print("+1 a "+ ListaDepartamentos[ListaRegiones[e].DepOnID[a]].Nombre)

def PROMEDIO():
    Promedio = 0
    for p in range(len(ListaDepartamentos)):
        Promedio+=ListaDepartamentos[p].Probabilidad
        # print(ListaDepartamentos[p].Nombre + " prob "+str(ListaDepartamentos[p].Probabilidad))

    Promedio = Promedio/len(ListaDepartamentos)
    # print(str(Promedio))

    LISTA = [y for y in range(len(ListaDepartamentos)) if ListaDepartamentos[y].Probabilidad < Promedio]
    # print (LISTA)

    #PURGA
    x=0
    while x<len(ListaDepartamentos):
        if ListaDepartamentos[x].Probabilidad < Promedio:
            # print(ListaDepartamentos[x].Nombre +" ELIMINADO " + str(ListaDepartamentos[x].Probabilidad))
            del ListaDepartamentos[x]
        else:
            x+=1
            # print(str(x)+" no eliminado")

# for i in range(0,10):
#     NumRandom = random.randrange(len(dataset.ListaLenguas))
#     print(str(NumRandom) +" "+dataset.PREGUNTA.Lengua + dataset.ListaLenguas[NumRandom].Nombre)
#     print("1) Sí  2) No")
#     Respuesta = int(input("Respuesta: "))
#     if Respuesta == 1:
#         #Si
#         for a in range(len(dataset.ListaLenguas[NumRandom].Departamentos)):
#             dataset.ListaDepartamentos[dataset.ListaLenguas[NumRandom].DepOnID[a]].Probabilidad+=1
#     else:
#         # for e in range(len(dataset.ListaLenguas[NumRandom].Departamentos)):
#         #     for i in range(dataset.ListaDepartamentos):
#         #         if dataset.ListaLenguas[NumRandom].Departamentos[i] == dataset.ListaLenguas[NumRandom].Departamentos[]
#         print("else")
#         #No
 
#PROMEDIO
ListaDepartamentos = dataset.ListaDepartamentos

PreguntasRegion()
PROMEDIO()
PreguntasLengua()
PROMEDIO()
PregutnasComidas()
PROMEDIO
PreguntasLugares()
PROMEDIO()

# for x in range(len(ListaDepartamentos)):
#     print(str(x) + ":  "+ListaDepartamentos[x].Nombre + " pr: "+str(ListaDepartamentos[x].Probabilidad))
# print("Tu departamento es: "+ListaDepartamentos[0].Nombre)

maxnum = 0
maxDep = 0
for a in range(len(ListaDepartamentos)):
    if ListaDepartamentos[a].Probabilidad>=maxDep:
        max = a
        maxDep = ListaDepartamentos[a].Probabilidad

print("Tu departamento es: "+ListaDepartamentos[max].Nombre)

# for x in range (len(dataset.ListaDepartamentos)):
#     print(dataset.ListaDepartamentos[x].Nombre + " " + str(dataset.ListaDepartamentos[x].Probabilidad))

# # del ListaLocal[0]
# # del ListaLocal[1]
# PROMEDIO()         


# for x in range (len(dataset.ListaDepartamentos)):
#     print(dataset.ListaDepartamentos[x].Nombre + " " + str(dataset.ListaDepartamentos[x].Probabilidad))

#PREGUNTA CON 

# listaRandom.append(3)
# listaRandom.append(10)
# print(listaRandom)