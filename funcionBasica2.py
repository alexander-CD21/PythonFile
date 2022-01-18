#1Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def countdown(num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append(i)
    return arr

valor=countdown(5)
print(valor)

#2 Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imprimirYDevolver(arr):
    print(arr[0])
    return arr[1]

imprimirYDevolver([4,5])
valor=imprimirYDevolver([5,4])
print(valor)

#3Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

def PrimeroMasLongitud(arr):
    suma=arr[0]+len(arr)
    return suma

variable=PrimeroMasLongitud([5,4,3,2,1,0])
print(variable)

#4Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def valoresMayoresQueElSegundo(arr):
    arr1=[]
    count=0
    if (len(arr)<=2):
        return False
    else:    
        for i in range(0,len(arr)):
            if( arr[i] > arr[1] ):
                count+=1
                arr1.append(arr[i])
        print(count)
        return arr1

resultado=valoresMayoresQueElSegundo([5,2,3,2,1,4])
print(resultado)

#5Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

def EstaLongitudEseValor(long,val):
    arr3=[]
    for i in range(0,long):
        arr3.append(val)
    return arr3

resultado=EstaLongitudEseValor(6,2)
print(resultado)
