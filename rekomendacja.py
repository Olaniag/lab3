#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt
import numpy

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    korelacja=0
    udaloSiePorownac=False
    n= 0
    sxy=0
    sx=0
    sy=0
    sx2=0
    sy2=0
    for i in rating1.keys():
        if i in rating2.keys():
            udaloSiePorownac=True
            sxy=sxy+rating1[i]*rating2[i]
            sx=sx+rating1[i]
            sy=sy+rating2[i]
            sx2=sx2+pow(rating1[i],2)
            sy2=sy2+pow(rating2[i],2)
            n=n+1
    korelacja=(sxy-(sx*sy)/n)/(sqrt(sx2-pow(sx,2)/n)*sqrt(sy2-pow(sy,2)/n))
    if (udaloSiePorownac==True):
        return korelacja
    else:
        return -1

def pearsonNumpy(rating1, rating2):
    
    korelacja=0
    udaloSiePorownac=False
    X=[]
    Y=[]

    for i in rating1.keys():
        if i in rating2.keys():
            X.append(rating1[i])
            Y.append(rating2[i])
    korelacja=numpy.corrcoef(X,Y)

    return korelacja

print "Wartość odległości manhattan dla preferncji Boni i Ani wynosi: " + str(manhattan(users["Bonia"],users["Ania"]))
print "Wartość korelacji między preferencjami Boni i Ani, obliczona z przybliżonego wzoru na współczynnik koleracji Pearsona wynosi: "+ str(pearson(users["Bonia"],users["Ania"]))
print "Korelacja obliczona dla preferencji Boni i Ani z numpy - funkcja corrcoef wynosi: " + str(pearsonNumpy(users["Bonia"],users["Ania"])[0][1])
