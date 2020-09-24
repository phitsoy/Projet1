# Initialisation des variables
import math
F = 10000  # en N
#E = 210  # en GPa = 10^3 N/mm^2
E = 210 * 10**3 # en N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm
I_rectangulaire = (b * h**3) / 12

# poutre carrée
a = 15  # en mm
I_carree = a**4 / 12

# poutre ronde
d = 5  # en mm
I_ronde= (math.pi * d**4) / 64

# poutre creuse
D = 15  # en mm
d = 5  # en mm
I_creuse = (math.pi * (D**4-d**4)) / 64

I=I_rectangulaire
section="rectangulaire"

if I<I_carree:
    I=I_carree
    section="carrée"
if I<I_ronde:
    I=I_ronde
    section="ronde"
if I<I_creuse:
    I=I_creuse
    section="creuse"

# Calcul de la section optimale
delta_max =(F*L**3)/(3*E*I)

print("Le type de section minimisant la déformation maximale est " + section + ", avec une déformation de " + str(round(delta_max, 2)) +" mm")