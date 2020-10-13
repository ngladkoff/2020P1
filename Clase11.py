#Recursividad
def cuenta_regresiva(nro):
    for i in range(0,nro + 1):
        print(nro - i)

# cuenta_regresiva(5)

def cuenta_regresiva_rec(nro):
    print(nro)
    if nro == 0:
        print("Fin")
    else:
        cuenta_regresiva_rec(nro-1)

#cuenta_regresiva_rec(5)

def fact(n):
    cuenta = 1
    for i in range(1,n+1):
        cuenta = cuenta * i
    return cuenta


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

#print(factorial(5))
#print(fact(5))



def mover_torre(discos, origen, aux, destino):
    if discos == 0:
        pass
    else:
        mover_torre(discos-1, origen, destino, aux)
        mover_disco(origen,destino)
        mover_torre(discos-1, aux, origen, destino)


def mover_disco(desde,hasta):
    print("mover disco de {0} a {1}".format(desde, hasta))

# mover_disco("A","B")

mover_torre(4, "A", "B", "C")
