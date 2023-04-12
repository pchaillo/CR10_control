import HG_C1100_P as ls
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import RubberSensor as rs

import time

# initialiser les capteurs
rubsensor = rs.RubberSerialDuino()
lasensor = ls.SerialDuino()

# créer l'objet figure et axe
fig, ax = plt.subplots()

# initialiser les listes de données
deformations = []
resistances = []

# initialiser la ligne de tracé
line, = ax.plot(deformations, resistances)

# définir les étiquettes de l'axe
plt.xlabel('Déformation')
plt.ylabel('Résistance')
plt.title('Résistance en fonction de la déformation')

# fonction qui lit les données des capteurs
def readSensors():
    rubsensor.UpdateSensors()
    lasensor.UpdateSensors()
    resistance = rubsensor.GetRes()

    deformation= lasensor.Calcul_Strain()
    print(deformation)

    return deformation, resistance


# fonction qui met à jour le tracé
def update(i):
    # lire les données des capteurs
    deformation, resistance = readSensors()

    # ajouter les données à la liste
    deformations.append(deformation)
    resistances.append(resistance)

    # mettre à jour les données du tracé
    line.set_xdata(deformations)
    line.set_ydata(resistances)

    # définir les limites de l'axe
    ax.set_xlim(0, 60)
    ax.set_ylim(1, 3)

    # retourner l'objet de ligne mis à jour
    return line,
def Real_Plot():
 # créer l'objet d'animation
 time.sleep(41)
 ani = animation.FuncAnimation(fig, update, frames=range(1000000))

 # afficher le graphique
 plt.show()
Real_Plot() 


