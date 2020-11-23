import timeit
import random
a = []


def listafeltoltes(a):
    a.clear()
    for i in range(0, 1000):
        b = random.randint(0, 10000)
        while b in a:
            b = random.randint(0, 10000)
        a.append(b)


print('Megmutatja milyen gyorsaságal lehet lefutatni a kölönbözö elrendezéseket,így elenőrizhetjűk a teljesitményt.\n'
      'Létrehoztumk egy listát amit feltöltötünk 1000 random elemel.A lehetséges elemek 0-10000 bármely szám.\n'
      )


def beilleszteses_rendez1(x, n): #x(tomb), n(tomb hossz)
    print('\nEredeti tömb:')
    print(x)
    start = timeit.default_timer()
    for i in range(0, n):
        j = i-1
        y = x[i]
        while j >= 0 and x[j] > y:
            x[j+1] = x[j]
            j = j - 1
        x[j+1] = y
    stop = timeit.default_timer()
    futasi_ido = stop-start
    print('A rendezet tömb:')
    print(x)
    print('A program futási ideje:'+ str(futasi_ido))

def beilleszteses_rendez2(x, n): #x(tomb), n(tomb hossz)
    print('\nEredeti tömb:')
    print(x)
    start = timeit.default_timer()
    for i in range(0, n):
        j = i-1
        y = x[i]
        while j >= 0 and x[j] > y:
            x[j+1] = x[j]
            j = j - 1
        x[j+1] = y
    stop = timeit.default_timer()
    futasi_ido = stop-start
    print('A program futási ideje:'+ str(futasi_ido))
    return (x)



def rendminkivel1(tomb):
    print("\nEredeti lista: ",tomb)
    start = timeit.default_timer()
    for i in range(0,len(tomb)):
        mini=i
        for j in range(i+1,len(tomb)):
            if tomb[j]<tomb[mini]:
                mini=j
        tomb[i],tomb[mini]=tomb[mini],tomb[i]
    stop = timeit.default_timer()
    futasi_ido = stop - start
    print('A program futási ideje:' + str(futasi_ido))
    print("Rendezett: ",tomb)



def rendminkivel2(tomb):
    print("\nEredeti lista: ", tomb)
    start = timeit.default_timer()
    for i in range(0,len(tomb)):
        mini=i
        for j in range(i+1,len(tomb)):
            if tomb[j]<tomb[mini]:
                mini=j
        tomb[i],tomb[mini]=tomb[mini],tomb[i]
    stop = timeit.default_timer()
    futasi_ido = stop - start
    print('A program futási ideje:' + str(futasi_ido))
    return(tomb)

print('Javított beillesztés')
listafeltoltes(a)
beilleszteses_rendez1(a, len(a))
listafeltoltes(a)
print('\nRendezett lista', beilleszteses_rendez2(a, len(a)))
print('\nJavított beillesztés vége')
print('\nMinimum kiválasztás')
listafeltoltes(a)
rendminkivel1(a)
listafeltoltes(a)

print("Rendezett 2.0 ", rendminkivel2(a))
print('Minimum kiválasztás vége')

def javbub1(tomb):
    print('Javított buborek')
    i = len(tomb)
    print('Rendezés elött: ')
    print(tomb)
    start = timeit.default_timer()
    while i >= 2:
        cs = 0
        for j in range(0, i-1):
            if tomb[j] > tomb[j+1]:
                tomb[j], tomb[j+1] = tomb[j+1], tomb[j]
                cs = j
        i = cs
    stop = timeit.default_timer()
    print("A rendezés futási ideje: ", stop-start)
    print('Rendezés után: ')
    print(tomb)

def javbub2(tomb):
    print('Javított buborek')
    print(tomb)
    i = len(tomb)
    start = timeit.default_timer()
    while i >= 2:
        cs = 0
        for j in range(0, i-1):
            if tomb[j] > tomb[j+1]:
                tomb[j], tomb[j+1] = tomb[j+1], tomb[j]
                cs = j
        i = cs
    stop = timeit.default_timer()
    print("A rendezés futási ideje: ", stop-start)
    return tomb

print('\nBuborék rendezés')
listafeltoltes(a)
javbub1(a)
listafeltoltes(a)

print("Rendezett 2.0 ", javbub2(a))
print('Buborék rendezés vége')

def shellSort1(arr):
    n = len(arr)
    gap = n/2
    print('\nEredeti tömb:')
    print(arr)
    i = len(arr)
    start = timeit.default_timer()
    while gap > 0:
        gap = int(gap)
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
                arr[j] = temp
        gap /= 2
    stop = timeit.default_timer()
    print("A rendezés futási ideje: ", stop - start)
    print('rendezet')
    print(arr)


def shellSort2(arr):

    n = len(arr)
    gap = n/2
    print('\nEredeti tömb:')
    print(arr)
    i = len(arr)
    start = timeit.default_timer()
    while gap > 0:
        gap = int(gap)
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
                arr[j] = temp
        gap /= 2
    stop = timeit.default_timer()
    print("A rendezés futási ideje: ", stop - start)
    return(arr)
print('\nShell rendezés')
listafeltoltes(a)
shellSort1(a)
listafeltoltes(a)

print("Rendezett 2.0 ", shellSort2(a))
print('Shell rendezés vége')


def rendezes1(x):
    print("Eredeti tömb: ")
    print (x)
    start = timeit.default_timer()
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    stop = timeit.default_timer()
    print("A rendezés futási ideje: ", stop - start)
    print("A rendezett tömb: ")
    print(x)


print('Cserés rendezés')
listafeltoltes(a)
rendezes1(a)


def rendezes2(x):
    print("Eredeti tömb: ")
    print (x)
    start = timeit.default_timer()
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    stop = timeit.default_timer()
    print("A rendezés futási ideje: ", stop - start)
    return(x)


listafeltoltes(a)
print('Rendezés 2.0: ', rendezes2(a))
print('Cserés rendezés vége')
