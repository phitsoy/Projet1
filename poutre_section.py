# Initialisation des variables
F = 10000  # en N
#E = 210  # en GPa = 10^3 N/mm^2
E = 210*10**3 # en N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

# poutre carrée
a = 15  # en mm

# poutre ronde
d = 5  # en mm

# poutre creuse
D = 15  # en mm
d = 5  # en mm


# Calcul de la section optimale

print("Le type de section minimisant la déformation maximale est " + type + ", avec une déformation de " + str(round(delta_max, 2)) +" mm")