__author__ = 'Ola'
#polecenia wpisane w konsoli pythona w arcgisie
import arcpy
import numpy
#zdefiniowanie zmiennych
X=arcpy.da.FeatureClassToNumPyArray("powiaty","POP")
Y=arcpy.da.FeatureClassToNumPyArray("powiaty","POLE_KM2")
#obliczenie wartoœci korelacji
numpy.corrcoef(X,Y)
