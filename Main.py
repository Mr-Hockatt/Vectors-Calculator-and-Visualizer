import math
import os
import numpy as np
import Graficador

PI = math.pi


def Suma_Vectorial(vectores):

    result_suma = np.array([0,0,0])

    for vector in vectores:
        result_suma = result_suma + vector

    return result_suma

def Producto_Escalar(vector, escalar):

    return vector*escalar

def Magnitud(vector):

    magnitud = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

    return magnitud

def Cosenos_Directores(vector):

    cos_dir = list()
    magnitud = Magnitud(vector)

    for posicion in vector:

        cos_dir.append(posicion/magnitud)

    return cos_dir

def Angulos_Vector(vector):

    angulos = list()
    magnitud = Magnitud(vector)

    for posicion in vector:

        angulos.append(math.acos(posicion/magnitud)*(180/PI))

    return angulos

def Vector_Unitario(vector):

    vector_unitario = list()
    magnitud = Magnitud(vector)

    for posicion in vector:

        vector_unitario.append(posicion/magnitud)

    return vector_unitario

def Componentes_Cartesianas(PuntoA, PuntoB):

    vector_cartesiano = np.array([PuntoB[0]-PuntoA[0], PuntoB[1]-PuntoA[1], PuntoB[2]-PuntoA[2]])

    return vector_cartesiano

def Producto_Punto(vector_a, vector_b):

    prod_punto = 0

    for i in range(0,3):

        prod_punto = prod_punto + vector_a[i]*vector_b[i]

    return prod_punto

def Angulo_Vectores(vector_a, vector_b):

    magnitudes_ab = Magnitud(vector_a)*Magnitud(vector_b)
    prod_punto_ab = Producto_Punto(vector_a, vector_b)
    angulo = math.acos(prod_punto_ab/magnitudes_ab)*(180/PI)

    return angulo

def Producto_Cruz(vector_a, vector_b):

    comp_i = vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1]
    comp_j = vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2]
    comp_k = vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]

    prod_cruz = np.array([comp_i, comp_j, comp_k])

    return prod_cruz


while True:

    os.system("cls")
    print("             CALCULADORA DE VECTORES \n")
    print("             Elija una opcion + ENTER\n\n")
    print("1. Suma n-vectorial")
    print("2. Producto escalar")
    print("3. Magnitud de un vector")
    print("4. Cosenos directores y angulos")
    print("5. Componentes cartesianas. Vector unitario")
    print("6. Componentes cartesianas. vector entre 2 puntos")
    print("7. Producto punto y angulo")
    print("8. Producto cruz y angulo")
    print("9. Respuestas a los ejercicios propuestos")
    print("10. Salir\n\n")


    opcion = int(input("opcion: "))

    if opcion == 1:
        os.system("cls")

        vectores = list()
        print("Ingrese las coordenadas del vector + ENTER\nQUIT + ENTER para finalizar")

        while True:
            txt = input("(Ingrese x, y, z): ")
            if txt == "QUIT":
                break
            else:
                vector_txt = txt.split(",")
                vector = np.array([float(vector_txt[0]), float(vector_txt[1]), float(vector_txt[2])])
                vectores.append(vector)
        print("La suma resultante de vectores es: {}".format(Suma_Vectorial(vectores)))
        input("Presione ENTER para graficar la suma vectorial.")

        Graficador.Graficar_Suma_Vectorial(vectores)

    elif opcion == 2:
        os.system("cls")

        vector = input("(Ingrese x, y, z): ")
        vector_txt = vector.split(",")
        vector = np.array([float(vector_txt[0]), float(vector_txt[1]), float(vector_txt[2])])
        escalar = float(input("Ingrese escalar: "))

        print("El producto escalar es: {}".format(Producto_Escalar(vector, escalar)))
        input("Presione ENTER para continuar")

    elif opcion == 3:
        os.system("cls")

        vector = input("(Ingrese x, y, z): ")
        vector_txt = vector.split(",")
        vector = np.array([float(vector_txt[0]), float(vector_txt[1]), float(vector_txt[2])])

        print("La magnitud del vector es: {}".format(Magnitud(vector)))
        input("Presione ENTER para continuar")

    elif opcion == 4:
        os.system("cls")

        vector = input("(Ingrese x, y, z): ")
        vector_txt = vector.split(",")
        vector = np.array([float(vector_txt[0]), float(vector_txt[1]), float(vector_txt[2])])

        print("Los cosenos directores del vector es: {}".format(Cosenos_Directores(vector)))
        print("Los angulos del vector es: {}".format(Angulos_Vector(vector)))
        input("Presione ENTER para continuar")

    elif opcion == 5:
        os.system("cls")

        vector = input("(Ingrese x, y, z): ")
        vector_txt = vector.split(",")
        vector = np.array([float(vector_txt[0]), float(vector_txt[1]), float(vector_txt[2])])

        print("Las componentes cartesianas del vector unitario son: {}".format(Vector_Unitario(vector)))
        input("Presione ENTER para continuar")

    elif opcion == 6:
        os.system("cls")

        punto_a = input("(Ingrese x, y, z): ")
        punto_b = input("(Ingrese x, y, z): ")
        punto_txt_a = punto_a.split(",")
        punto_a = np.array([int(punto_txt_a[0]), int(punto_txt_a[1]), int(punto_txt_a[2])])
        punto_txt_b = punto_b.split(",")
        punto_b = np.array([int(punto_txt_b[0]), int(punto_txt_b[1]), int(punto_txt_b[2])])

        print("Las componentes cartesianas del vector son: {}".format(Componentes_Cartesianas(punto_a, punto_b)))
        input("Presione ENTER para graficar la suma vectorial.")

        Graficador.Graficar_Componentes_Cartesianas(punto_a, punto_b)

    elif opcion == 7:
        os.system("cls")

        vector_a = input("(Ingrese x, y, z): ")
        vector_b = input("(Ingrese x, y, z): ")
        vector_txt_a = vector_a.split(",")
        vector_a = np.array([int(vector_txt_a[0]), int(vector_txt_a[1]), int(vector_txt_a[2])])
        vector_txt_b = vector_b.split(",")
        vector_b = np.array([int(vector_txt_b[0]), int(vector_txt_b[1]), int(vector_txt_b[2])])

        print("El producto punto entre los vectores es: {}".format(Producto_Punto(vector_a, vector_b)))
        print("El angulo entre los vectores es: {}".format(Angulo_Vectores(vector_a, vector_b)))
        input("Presione ENTER para continuar")

    elif opcion == 8:
        os.system("cls")

        vector_a = input("(Ingrese x, y, z): ")
        vector_b = input("(Ingrese x, y, z): ")
        vector_txt_a = vector_a.split(",")
        vector_a = np.array([int(vector_txt_a[0]), int(vector_txt_a[1]), int(vector_txt_a[2])])
        vector_txt_b = vector_b.split(",")
        vector_b = np.array([int(vector_txt_b[0]), int(vector_txt_b[1]), int(vector_txt_b[2])])

        print("El producto cruz entre los vectores es: {}".format(Producto_Cruz(vector_a, vector_b)))
        print("El angulo entre los vectores es: {}".format(Angulo_Vectores(vector_a, vector_b)))
        input("Presione ENTER para graficar el producto cruz")

        Graficador.Graficar_Producto_Cruz(vector_a, vector_b)

    elif opcion == 9:
        os.system("cls")

        print("         EJERCICIO # 1\n")
        print("punto A: 0,  0, 4")
        print("punto B: 3, -3, 2.5")
        print("punto C: 2,  4, 0\n\n")
        print("Vectores Unitarios:\n")
        print("U_ab = ", Vector_Unitario(Componentes_Cartesianas([0,0,4],[3,-3,2.5])))
        print("U_ac = ", Vector_Unitario(Componentes_Cartesianas([0,0,4],[2,4,0])))
        input()




    elif opcion == 10:
        break

    else:
        input("Ingrese una opcion valida. Oprima ENTER para continuar.")
