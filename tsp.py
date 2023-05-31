import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

def encontrar_camino_mas_corto(puntos, distancias):
    num_ciudades = len(puntos)
    mejores_rutas = []
    mejores_distancias = []

    for ruta in permutations(range(num_ciudades)):
        distancia = sum(distancias[ruta[i], ruta[i+1]] for i in range(num_ciudades - 1))
        distancia_ultima_primera = distancias[ruta[-1], ruta[0]]
        distancia += distancia_ultima_primera
        mejores_rutas.append(ruta)
        mejores_distancias.append(distancia)

    indice_camino_mas_corto = np.argmin(mejores_distancias)
    camino_mas_corto = mejores_rutas[indice_camino_mas_corto]
    camino_mas_corto = np.append(camino_mas_corto, camino_mas_corto[0])  # Agregar la primera ciudad al final del camino

    distancia_camino_mas_corto = mejores_distancias[indice_camino_mas_corto]

    return camino_mas_corto, distancia_camino_mas_corto

# Ejemplo de uso
# Coordenadas de las ciudades
# puntos = [
#     0,1,2,3,4,5    # Ciudad 5
# ]

puntos = np.array([
    [0, 0],   # Ciudad 0
    [1, 5],   # Ciudad 1
    [2, 3],   # Ciudad 2
    [5, 1],   # Ciudad 3
    [6, 4],   # Ciudad 4
    [3, 8],    # Ciudad 5
])

# # Ciudades conectadas entre si , todas
# distancias = np.array([
#     [0, 8, 5, 11, 15, 20],   # Distancias desde la Ciudad 0 a las demás ciudades
#     [8, 0, 3, 12, 10, 8],   # Distancias desde la Ciudad 1 a las demás ciudades
#     [5, 3, 0, 5, 8, 11],   # Distancias desde la Ciudad 2 a las demás ciudades
#     [11, 12, 5, 0, 4, 15],    # Distancias desde la Ciudad 3 a las demás ciudades
#     [15, 10, 8, 4, 0, 9],    # Distancias desde la Ciudad 4 a las demás ciudades
#     [20, 8, 11, 15, 9, 0]    # Distancias desde la Ciudad 5 a las demás ciudades
# ])


# # Ciudades del problema viajante de comercio
distancias = np.array([
    [0, 4, 3, 21, np.inf, 35],   # Distancias desde la Ciudad 0 a las demás ciudades
    [4, 0, 3, np.inf, 8,np.inf],   # Distancias desde la Ciudad 1 a las demás ciudades
    [3, 3, 0, 7, 5, np.inf],   # Distancias desde la Ciudad 2 a las demás ciudades
    [21, np.inf, 7, 0, 1, 2],    # Distancias desde la Ciudad 3 a las demás ciudades
    [np.inf, 8, 5, 1, 0, 9],    # Distancias desde la Ciudad 4 a las demás ciudades
    [35, np.inf, np.inf, 2, 9, 0]    # Distancias desde la Ciudad 5 a las demás ciudades
])


# Ciudades que no esten conectadas entre si
# distancias = np.array([
#     [0, 10, np.inf, 9, 7, np.inf],   # Distancias desde la Ciudad 0 a las demás ciudades
#     [10, 0, 7, 6, np.inf, 5],        # Distancias desde la Ciudad 1 a las demás ciudades
#     [np.inf, 7, 0, np.inf, 6, 11],   # Distancias desde la Ciudad 2 a las demás ciudades
#     [9, 6, np.inf, 0, 3, 8],         # Distancias desde la Ciudad 3 a las demás ciudades
#     [7, np.inf, 6, 3, 0, np.inf],    # Distancias desde la Ciudad 4 a las demás ciudades
#     [np.inf, 5, 11, 8, np.inf, 0]    # Distancias desde la Ciudad 5 a las demás ciudades
# ])

# Encuentra el camino más corto y la distancia
camino_mas_corto, distancia_camino_mas_corto = encontrar_camino_mas_corto(puntos, distancias)

# Imprime el resultado
print("Camino más corto:", camino_mas_corto)
print("Distancia del camino más corto:", distancia_camino_mas_corto)


# Visualización gráfica
plt.figure()
plt.scatter(puntos[:, 0], puntos[:, 1], color='red', label='Ciudades')
plt.plot(puntos[camino_mas_corto, 0], puntos[camino_mas_corto, 1], color='blue', linestyle='-', linewidth=1.5, label='Camino más corto')
plt.plot([puntos[camino_mas_corto[-1], 0], puntos[camino_mas_corto[0], 0]], [puntos[camino_mas_corto[-1], 1], puntos[camino_mas_corto[0], 1]], color='blue', linestyle='-', linewidth=1.5)
plt.scatter(puntos[camino_mas_corto[0], 0], puntos[camino_mas_corto[0], 1], color='green', label='Inicio')
plt.legend()
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Viajero de Comercio: Camino más corto')
plt.show()