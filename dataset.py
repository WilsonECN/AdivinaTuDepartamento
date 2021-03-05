class COMIDAS (object):
    DepOnID = [""]
    Departamentos = [""]
    Nombre = ""
    Peso = 1

class REGIONES (object):
    DepOnID = [""]
    Departamentos = [""]
    Nombre = ""
    Peso = 1

class LUGARES (object):
    DepOnID = [""]
    Departamentos = [""]
    Nombre = ""
    Peso = 1

class LENGUAS (object):
    DepOnID = [""]
    Departamentos = [""]
    Nombre = ""
    Peso = 1

class DEPARTAMENTO (object):
    Nombre = ""
    Probabilidad = 0
    ID = 0
    Comidas = ""
    Region = ""
    Lenguas = [""]
    Lugares = [""]

class PREGUNTA (object):
    Comida = "En tu departamento un platillo comun es: "
    Lengua = "En tu departamento la lengua predominante es: "
    Region = "Tu departamento se encuentra en la region: "
    Lugar  = "En tu departemento se encuentra un lugar llamado: "

#DEPARTAMENTOS
ListaDepartamentos = DEPARTAMENTO()

departamentoC = DEPARTAMENTO()
departamentoC.Nombre = ""
departamentoC.Probabilidad = 0
departamentoC.ID = 0

Guatemala = DEPARTAMENTO()
Guatemala.Nombre = "Guatemala"
Guatemala.Probabilidad = 0
Guatemala.Comidas = "Atol de Elote"
Guatemala.Region = "Metropolitana"
Guatemala.Lenguas = ["Kaqchikel"]
Guatemala.Lugares = ["San Gregorio", "Irtra Petapa", "Santa Teresita"]
Guatemala.ID = 0

Alta_Verapaz = DEPARTAMENTO()
Alta_Verapaz.Nombre = "Alta_Verapaz"
Alta_Verapaz.Probabilidad = 0
Alta_Verapaz.Comidas = "Saquic"
Alta_Verapaz.Region = "Norte"
Alta_Verapaz.Lenguas = ["Q'eqchi'", "Poqomch'i"]
Alta_Verapaz.Lugares = ["Laguna Lachuá", "Candeleria Lodge"]
Alta_Verapaz.ID = 1

Baja_Verapaz = DEPARTAMENTO()
Baja_Verapaz.Nombre = "Baja_Verapaz"
Baja_Verapaz.Probabilidad = 0
Baja_Verapaz.Comidas = "Tupes"
Baja_Verapaz.Region = "Norte"
Baja_Verapaz.Lenguas = ["Kaqchikel", "Poqomch'i", "Achi"]
Baja_Verapaz.Lugares = ["Salto de Chilascó", "Ranchitos del Quetzal"]
Baja_Verapaz.ID = 2

Izabal = DEPARTAMENTO()
Izabal.Nombre = "Izabal"
Izabal.Probabilidad = 0
Izabal.Comidas = "Pan de Camote"
Izabal.Region = "Nororiente"
Izabal.Lenguas = ["Q'eqchi'", "Garifuna"]
Izabal.Lugares = ["Playa Blanca", "Siete Altares"]
Izabal.ID = 3

Chiquimula = DEPARTAMENTO()
Chiquimula.Nombre = "Chiquimula"
Chiquimula.Probabilidad = 0
Chiquimula.Comidas = "Empanadas de loroco con requesón"
Chiquimula.Region = "Nororiente"
Chiquimula.Lenguas = ["Ch'orti'"]
Chiquimula.Lugares = ["Laguna de Ipala", "Parque Cueva de las Minas", "Poza de la Pila"]
Chiquimula.ID = 4

Zacapa = DEPARTAMENTO()
Zacapa.Nombre = "Zacapa"
Zacapa.Probabilidad = 0
Zacapa.Comidas = "Quesadillas"
Zacapa.Region = "Nororiente"
Zacapa.Lenguas = ["Ch'orti'"]
Zacapa.Lugares = ["Montaña del Olvido", "Cascada Santa Rosalia", "Sierra de las Minas"]
Zacapa.ID = 5

El_Progreso = DEPARTAMENTO()
El_Progreso.Nombre = "El_Progreso"
El_Progreso.Probabilidad = 0
El_Progreso.Comidas = "Flor de Izote"
El_Progreso.Region = "Nororiente"
El_Progreso.Lenguas = ["Español"]
El_Progreso.Lugares = ["Parque Agua Caliente", "Tumba de Guaytán", "Paseo del Rancho"]
El_Progreso.ID = 6

Jutiapa = DEPARTAMENTO()
Jutiapa.Nombre = "Jutiapa"
Jutiapa.Probabilidad = 0
Jutiapa.Comidas = "Gallo en chicha"
Jutiapa.Region = "Suroriente"
Jutiapa.Lenguas = ["Xinca"]
Jutiapa.Lugares = ["Cuevas de Andá Mirá", "Lago de Güíja"]
Jutiapa.ID = 7

Jalapa = DEPARTAMENTO()
Jalapa.Nombre = "Jalapa"
Jalapa.Probabilidad = 0
Jalapa.Comidas = "Gallina en crema"
Jalapa.Region = "Suroriente"
Jalapa.Lenguas = ["Xinca", "Poqomam"]
Jalapa.Lugares = ["Parque Pino Dulce", "Catarata de Urianta", "El Hoyo de Monjas"]
Jalapa.ID = 8

Santa_Rosa = DEPARTAMENTO()
Santa_Rosa.Nombre = "Santa_Rosa"
Santa_Rosa.Probabilidad = 0
Santa_Rosa.Comidas = "Carne en amarillo"
Santa_Rosa.Region = "Suroriente"
Santa_Rosa.Lenguas = ["Xinca"]
Santa_Rosa.Lugares =["Cascada de Los Amantes", "Laguna de Ayarza", "Laguna El Pino"]
Santa_Rosa.ID = 9

Chimaltenango = DEPARTAMENTO()
Chimaltenango.Nombre = "Chimaltenango"
Chimaltenango.Probabilidad = 0
Chimaltenango.Comidas = "Chilaquilas de güisquil"
Chimaltenango.Region = "Central"
Chimaltenango.Lenguas = ["Kaqchikel"]
Chimaltenango.Lugares = ["Iximché", "Casa Xara", "Laguna Chichoy"]
Chimaltenango.ID = 10

Sacatepéquez = DEPARTAMENTO()
Sacatepéquez.Nombre = "Sacatepéquez"
Sacatepéquez.Probabilidad = 0
Sacatepéquez.Comidas = "Tamales colorados"
Sacatepéquez.Region = "Central"
Sacatepéquez.Lenguas = ["Kaqchikel"]
Sacatepéquez.Lugares = ["Tenedor del Cerro", "Calle del Arco"]
Sacatepéquez.ID = 11

Escuintla = DEPARTAMENTO()
Escuintla.Nombre = "Escuintla"
Escuintla.Probabilidad = 0
Escuintla.Comidas = "Caldo de mariscos"
Escuintla.Region = "Central"
Escuintla.Lenguas = ["Kaqchikel"]
Escuintla.Lugares = ["Auto Safari Chapín", "Tiquisate"]
Escuintla.ID = 12

San_Marcos = DEPARTAMENTO()
San_Marcos.Nombre = "San_Marcos"
San_Marcos.Probabilidad = 0
San_Marcos.Comidas = "Mole de plátano"
San_Marcos.Region = "Suroccidente"
San_Marcos.Lenguas = ["Mam"]
San_Marcos.Lugares = ["Catarata la Igualdad", "Balneario La Castalia"]
San_Marcos.ID = 13

Quetzaltenango = DEPARTAMENTO()
Quetzaltenango.Nombre = "Quetzaltenango"
Quetzaltenango.Probabilidad = 0
Quetzaltenango.Comidas = "Paches de papa"
Quetzaltenango.Region = "Suroccidente"
Quetzaltenango.Lenguas = ["K'ich'e", "Mam"]
Quetzaltenango.Lugares = ["Fuentes Georginas", "Laguna Chicabal", "Cerro El Baúl"]
Quetzaltenango.ID = 14

Totonicapán = DEPARTAMENTO()
Totonicapán.Nombre = "Totonicapán"
Totonicapán.Probabilidad = 0
Totonicapán.Comidas = "Atol de masa"
Totonicapán.Region = "Suroccidente"
Totonicapán.Lenguas = ["K'ich'e"]
Totonicapán.Lugares = ["Los Riscos Momostenango", "Cuevas de San Miguel", "San Francisco el Alto"]
Totonicapán.ID = 15

Sololá = DEPARTAMENTO()
Sololá.Nombre = "Sololá"
Sololá.Probabilidad = 0
Sololá.Comidas="Patin"
Sololá.Region = "Suroccidente"
Sololá.Lenguas = ["K'ich'e", "Kaqchikel", "Tz'utujil"]
Sololá.Lugares = ["Reserva Natural Atitlán", "Mirador del Rostro Maya", "Cerro Tzankujil"]
Sololá.ID = 16

Retalhuleu = DEPARTAMENTO()
Retalhuleu.Nombre = "Retalhuleu"
Retalhuleu.Probabilidad = 0
Retalhuleu.Comidas = "Carne con miltomate"
Retalhuleu.Region = "Suroccidente"
Retalhuleu.Lenguas = ["K'ich'e"]
Retalhuleu.Lugares = ["Finca el Patrocinio", "Playa Champerico"]
Retalhuleu.ID = 17

Suchitepéquez = DEPARTAMENTO()
Suchitepéquez.Nombre = "Suchitepéquez"
Suchitepéquez.Probabilidad = 0
Suchitepéquez.Comidas = "Chompipe en Arroz"
Suchitepéquez.Region = "Suroccidente"
Suchitepéquez.Lenguas = ["K'ich'e", "Kaqchikel", "Tz'utujil"]
Suchitepéquez.Lugares = ["Iglesia de San Pedro Jocopilas", "Tahuexco"]
Suchitepéquez.ID = 18

Huehuetenango = DEPARTAMENTO()
Huehuetenango.Nombre = "Huehuetenango"
Huehuetenango.Probabilidad = 0
Huehuetenango.Comidas = "Chompipe en Arroz"
Huehuetenango.Region = "Noroccidente"
Huehuetenango.Lenguas = ["Mam", "Q'anob'al"]
Huehuetenango.Lugares = ["Cenote de Candelaria", "Río Azul", "Posada Unicornio Azul"]
Huehuetenango.ID = 19

Quiché = DEPARTAMENTO()
Quiché.Nombre = "Quiché"
Quiché.Probabilidad = 0
Quiché.Comidas = "Ayote en dulce"
Quiché.Region = "Noroccidente"
Quiché.Lenguas = ["K'ich'e", "Q'eqchi'", "Ixil"]
Quiché.Lugares = ["Laguna Lemoa", "Cascada Chichel", "Hacienda Mil Amores"]
Quiché.ID = 20

Peten = DEPARTAMENTO()
Peten.Nombre = "Peten"
Peten.Probabilidad = 0
Peten.Comidas = "Bollitos"
Peten.Region = "Peten"
Peten.Lenguas = ["Q'eqchi'", "Itza'"]
Peten.Lugares = ["Refugio de Vida el Pucté", "El Remate", "Tikal"]
Peten.ID = 21

ListaDepartamentos = [
                        Guatemala,      #0
                        Alta_Verapaz,   #1
                        Baja_Verapaz,   #2
                        Izabal,         #3
                        Chiquimula,     #4
                        Zacapa,         #5
                        El_Progreso,    #6
                        Jutiapa,        #7
                        Jalapa,         #8
                        Santa_Rosa,     #9
                        Chimaltenango,  #10
                        Sacatepéquez,   #11
                        Escuintla,      #12
                        San_Marcos,     #13
                        Quetzaltenango, #14
                        Totonicapán,    #15
                        Sololá,         #16
                        Retalhuleu,     #17
                        Suchitepéquez,  #18
                        Huehuetenango,  #19
                        Quiché,         #20
                        Peten]          #21

#DEPARTEMENTOS FIN

#LENGUAS
Itza = LENGUAS()
Itza.Nombre = "Itza'"
Itza.Departamentos = ["Peten"]
Itza.DepOnID = [21]

Ixil = LENGUAS()
Ixil.Nombre = "Ixil"
Ixil.Departamentos = ["Quiché"]
Ixil.DepOnID = [20]

Qanobal = LENGUAS()
Qanobal.Nombre = "Q'anob'al"
Qanobal.Departamentos = ["Huehuetenango"]
Qanobal.DepOnID = [19]

Achi = LENGUAS()
Achi.Nombre = "Achi"
Achi.Departamentos = ["Baja_Verapaz"]
Achi.DepOnID = [2]

Garifuna = LENGUAS()
Garifuna.Nombre = "Garifuna"
Garifuna.Departamentos = ["Izabal"]
Garifuna.DepOnID = [3]

Xinca = LENGUAS()
Xinca.Nombre = "Xinca"
Xinca.Departamentos = ["Santa_Rosa", "Jutiapa", "Jalapa"]
Xinca.DepOnID = [9, 7, 8]

Poqomam = LENGUAS()
Poqomam.Nombre = "Poqomam"
Poqomam.Departamentos = ["Jalapa", "Escuintla"]
Poqomam.DepOnID = [8, 12]

Tzutujil = LENGUAS()
Tzutujil.Nombre = "Tz'utujil"
Tzutujil.Departamentos = ["Sololá", "Suchitepéquez"]
Tzutujil.DepOnID = [16, 18]

Kiche = LENGUAS()
Kiche.Nombre = "K'ich'e"
Kiche.Departamentos = ["Sololá", "Totonicapán", "Quetzaltenango", "Quiché", "Suchitepéquez", "Retalhuleu"]
Kiche.DepOnID = [16, 15, 14, 20, 18, 17]

Mam = LENGUAS()
Mam.Nombre = "Mam"
Mam.Departamentos = ["Quetzaltenango", "San_Marcos", "Huehuetenango"]
Mam.DepOnID = [14, 13, 19]

Kaqchikel = LENGUAS()
Kaqchikel.Nombre = "Kaqchikel"
Kaqchikel.Departamentos = ["Guatemala", "Sacatepéquez", "Chimaltenango", "Escuintla", "Suchitepequez", "Baja_Verapaz", "Sololá"]
Kaqchikel.DepOnID = [0, 11, 10, 12, 18, 2, 16]

Qeqchi = LENGUAS()
Qeqchi.Nombre = "Q'eqchi'"
Qeqchi.Departamentos = ["Alta_Verapaz", "Peten", "Izabal", "Quiché"]
Qeqchi.DepOnID = [1, 21, 3, 20]

Poqomchi = LENGUAS()
Poqomchi.Nombre = "Poqomch'i"
Poqomchi.Departamentos = ["Baja_Verapaz", "Alta_Verapaz"]
Poqomchi.DepOnID = [1, 2]

ListaLenguas = [
                Itza,       #0
                Ixil,       #1
                Qanobal,    #2
                Achi,       #3
                Garifuna,   #4
                Xinca,      #5
                Poqomam,    #6
                Tzutujil,   #7
                Kiche,      #8
                Mam,        #9
                Kaqchikel,  #10
                Qeqchi,     #11
                Poqomchi]   #12

#LENGUAS FIN


#REGIONES
ListaRegiones = [""]

RegionC = REGIONES()
RegionC.Nombre = "."
RegionC.Departamentos = ["", "", ""]

RegionMetropolitana = REGIONES()
RegionMetropolitana.Nombre = "Metropolitana"
RegionMetropolitana.Departamentos = ["Guatemala"]
RegionMetropolitana.DepOnID = [0]

RegionNorte = REGIONES()
RegionNorte.Nombre = "Norte"
RegionNorte.Departamentos = ["Alta_Verapaz", "Baja_Verapaz"]
RegionNorte.DepOnID = [1,2]

RegionNororiente = REGIONES()
RegionNororiente.Nombre = "Nororiente"
RegionNororiente.Departamentos = ["Izabal", "Chiquimula", "Zacapa", "El_Progreso"]
RegionNororiente.DepOnID = [3,4,5,6]

RegionSuroriente = REGIONES()
RegionSuroriente.Nombre = "Suroriente"
RegionSuroriente.Departamentos = ["Jutiapa", "Jalapa", "Santa_Rosa"]
RegionSuroriente.DepOnID = [7,8,9]

RegionCentral = REGIONES()
RegionCentral.Nombre = "Central"
RegionCentral.Departamentos = ["Chimaltenango", "Sacatepéquez", "Escuintla"]
RegionCentral.DepOnID = [10,11,12]

RegionSuroccidente = REGIONES()
RegionSuroccidente.Nombre = "Suroccidente"
RegionSuroccidente.Departamentos = ["San_Marcos", "Quetzaltenango", "Totonicapán", "Sololá", "Retalhuleu", "Suchitepéquez"]
RegionSuroccidente.DepOnID = [13,14,15,16,17,18]

RegionNoroccidente = REGIONES()
RegionNoroccidente.Nombre = "Noroccidente"
RegionNoroccidente.Departamentos = ["Huehuetenango", "Quiché"]
RegionNoroccidente.DepOnID = [19,20]

RegionPeten = REGIONES()
RegionPeten.Nombre = "Peten"
RegionPeten.Departamentos = ["Peten"]
RegionPeten.DepOnID = [21]

ListaRegiones = [
                    RegionMetropolitana,    #0
                    RegionNorte,            #1
                    RegionNororiente,       #2
                    RegionSuroriente,       #3
                    RegionCentral,          #4
                    RegionSuroccidente,     #5
                    RegionNoroccidente,     #6
                    RegionPeten]            #7

#REGIONES FIN
