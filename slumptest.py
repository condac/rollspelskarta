import random


def T(antal):
    return random.randint(1, antal)

def T66():
    out = (T(6)*10) + T(6) 
    return out

def stats4T6():
    # 4T6 ta bort sämsta
    res = []
    res.append(T(6))
    res.append(T(6))
    res.append(T(6))
    res.append(T(6))
    sortedres = sorted(res)
    #print(res)
    #print(sortedres)
    total = sortedres[1] +sortedres[2] +sortedres[3]
    #print(total)
    return total

def stats3T6():
    # 4T6 ta bort sämsta
    
    return T(6) + T(6) + T(6)

    
antal = 100000
resultat = {}
for i in range(antal):
    tal = stats4T6() +stats4T6() +stats4T6() +stats4T6() +stats4T6() +stats4T6() 
    if str(tal) not in resultat:
        resultat[str(tal)] = 0
    resultat[str(tal)] = resultat[str(tal)] + 1
    
    
for x in sorted(resultat):
    print(x, resultat[x]/antal*100)


stats4T6()
