from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plotter
import numpy as np



def Producto_Cruz(vector_a, vector_b):

    comp_i = vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1]
    comp_j = vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2]
    comp_k = vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]

    prod_cruz = np.array([comp_i, comp_j, comp_k])

    return prod_cruz


def Graficar_Suma_Vectorial(vectores):

    fig = plotter.figure()
    ax = fig.gca(projection='3d')

    result_suma = np.array([0,0,0])

    for vector in vectores:

        tail_x = result_suma[0]
        tail_y = result_suma[1]
        tail_z = result_suma[2]

        head_x = tail_x + vector[0]
        head_y = tail_y + vector[1]
        head_z = tail_z + vector[2]



        ax.quiver(tail_x, tail_y, tail_z, vector[0], vector[1], vector[2], length=1,colors='g', arrow_length_ratio=0.1, normalize=False)
        result_suma = result_suma + vector

    ax.text2D(0.4, 1, r'$Visualización Suma Vectorial$', transform=ax.transAxes)
    ax.quiver(0, 0, 0, head_x, head_y, head_z, colors='k', arrow_length_ratio=0.1, normalize=False)


    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.set_zlim(0,10)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plotter.show()


def Graficar_Componentes_Cartesianas(punto_a, punto_b):

    fig = plotter.figure()
    ax = fig.gca(projection='3d')

    a_x = punto_a[0]
    a_y = punto_a[1]
    a_z = punto_a[2]

    b_x = punto_b[0]
    b_y = punto_b[1]
    b_z = punto_b[2]

    a_text = "[" + str(a_x) + "," + str(a_y) + "," + str(a_z) + "]"
    b_text = "[" + str(b_x) + "," + str(b_y) + "," + str(b_z) + "]"

    ax.quiver(a_x, a_y, a_z, b_x - a_x, b_y - a_y, b_z - a_z, length=1,colors='g', arrow_length_ratio=0.1, normalize=False)
    ax.text(a_x, a_y, a_z, a_text, color='red')
    ax.text(b_x, b_y, b_z, b_text, color='red')
    ax.text2D(0.4, 1, r'$Visualización Componentes Cartesianas$', transform=ax.transAxes)

    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.set_zlim(0,10)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plotter.show()


def Graficar_Producto_Cruz(vector_a, vector_b):

    fig = plotter.figure()
    ax = fig.gca(projection='3d')

    a_x = vector_a[0]
    a_y = vector_a[1]
    a_z = vector_a[2]

    b_x = vector_b[0]
    b_y = vector_b[1]
    b_z = vector_b[2]

    prod_cruz = Producto_Cruz(vector_a, vector_b)

    pc_x = prod_cruz[0]
    pc_y = prod_cruz[1]
    pc_z = prod_cruz[2]

    a_text = "[" + str(a_x) + "," + str(a_y) + "," + str(a_z) + "]"
    b_text = "[" + str(b_x) + "," + str(b_y) + "," + str(b_z) + "]"
    prod_cruz_txt = "[" + str(pc_x) + "," + str(pc_y) + "," + str(pc_z) + "]"

    ax.quiver(0, 0, 0, a_x, a_y, a_z, length=1,colors='k', arrow_length_ratio=0.1, normalize=False)
    ax.quiver(0, 0, 0, b_x, b_y, b_z, length=1,colors='k', arrow_length_ratio=0.1, normalize=False)
    ax.quiver(0, 0, 0, pc_x, pc_y, pc_z, length=1,colors='r', arrow_length_ratio=0.1, normalize=False)
    ax.text(a_x, a_y, a_z, a_text, color='red')
    ax.text(b_x, b_y, b_z, b_text, color='red')
    ax.text(pc_x, pc_y, pc_z, prod_cruz_txt, color='red')
    ax.text2D(0.4, 1, r'$Visualización Producto Cruz$', transform=ax.transAxes)

    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.set_zlim(0,10)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    x = [0, a_x, b_x]
    y = [0, a_y, b_y]
    z = [0, a_z, b_z]
    verts = [list(zip(x,y,z))]
    ax.add_collection3d(Poly3DCollection(verts))


    plotter.show()
