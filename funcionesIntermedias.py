#-----------------------------------------------------------------
#1
#Cambiar al 10 por el 15
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
#cambiar el apellido de jordan a bryant
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]["last_name"]="bryant"
print(estudiantes)
#Cambiar a messi por andres
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes["fútbol"]=['Andres','Ronaldo','Rooney']
print(directorio_deportes)
#cambia 20 a 30 
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)
#-----------------------------------------------------
#2
estudiantes1= [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(estudiantes1):
    for i in range(0,len(estudiantes1)):
        print(estudiantes1[i])

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#-------------------------------------------------------------------------
#3
#Obtener valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(keyName,someList):
    for i in range(0,len(someList)):
        print(someList[i][keyName])
iterateDictionary2('first_name',estudiantes1)
iterateDictionary2('last_name',estudiantes1)
#------------------------------------------------------------------------------------
#4

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(someList_dict):
    for i in someList_dict.keys():
        print(f'{len(someList_dict[i])} {i.upper()}')
        for y in someList_dict[i]:
            print(y)
            
printInfo(dojo)




