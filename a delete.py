def compteRebours(nombre, limite) :
    print(nombre)
    nombre_suivant = nombre - 1
    if nombre_suivant >= limite:
        compteRebours(nombre_suivant, limite)


#compteRebours(5, -10)



def recherche ( x , deb , fin , L) :
    if deb>fin :
        return "Fini."
    t =(deb+fin)//2
    if x==L[t] :
        return t
    if x<L[t] :
        return recherche ( x , deb , t-1,L)
    else :
        return recherche ( x , t +1 , fin , L)
L = [2 ,3 ,4 ,7 ,11 ,15 ,17]
#print (recherche (2 ,0 , len(L)-1,L))



def ed(L ,M=[ ] ) :
 #L est une liste
 if not (L) : return M
 a=L.pop(0)
 if a not in M : M.append(a)
 return ed(L ,M)
L = [2 ,3 ,2 ,6 ,8 ,9 ,9 ,10 ,9 ,3 ,6 ,7 ,8 ,8 ,9]
#M=ed(L)
#print (M)

def pp(L) :
 if len(L)==1 : return L[0]
 if L[0] < L[1] : L.pop(1)
 else : L.pop(0)
 return pp(L)
L=[24 ,45 ,2 ,3 ,2 ,6 ,8 ,9 ,9 ,10 ,9 ,3 ,6 ,7 ,8 ,8 ,9]
#print (pp(L))



def nbChiffres(n):
    if n/10==n//10:
        return n/10
    else:
       return nbChiffres(n-1)
#print(nbChiffres(7471))




def pgcd(a, b):
    if a<b:
        if b/a==a:
            return a
        return pgcd(a, b-1)
    else:
        if a==b:
            return 1
        return pgcd(b, a)
print(pgcd(10, 1230))    

def nfactoriel(n, x):
    if n==1:
        return x
    else:
       x=x*n
    nfactoriel(n-1, x)

#nfactoriel(5, 1)