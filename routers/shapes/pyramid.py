# routers/shapes/pyramid.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# Import PyramidParams from the new models file
from ..models import PyramidParams
from .utils import fig_to_png_bytes
from typing import Optional

def draw_pyramid(p: PyramidParams, title: Optional[str]) -> bytes:
    base, height = p.base, p.height

    label_base = p.label_base or f"Base = {base}"
    label_height = p.label_height or f"Altura = {height}"

    # Vértices de la base cuadrada
    v0 = np.array([-base/2, -base/2, 0])
    v1 = np.array([base/2, -base/2, 0])
    v2 = np.array([base/2, base/2, 0])
    v3 = np.array([-base/2, base/2, 0])
    # Vértice superior (ápice)
    v4 = np.array([0, 0, height])

    vertices = [v0, v1, v2, v3, v4]

    # Caras de la pirámide
    faces = [
        [v0, v1, v2, v3], # Base
        [v0, v1, v4],     # Cara 1
        [v1, v2, v4],     # Cara 2
        [v2, v3, v4],     # Cara 3
        [v3, v0, v4]      # Cara 4
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Colección de polígonos 3D
    poly = Poly3DCollection(faces, alpha=0.6, facecolors='cyan', linewidths=1, edgecolors='r')
    ax.add_collection3d(poly)

    # Etiquetas
    ax.text(0, -base/2 - 0.1, 0, label_base, ha='center')
    ax.text(0, 0, height/2, label_height, ha='center')
    ax.plot([0,0], [0,0], [0, height], linestyle='--', color='black') # Eje altura

    if title:
        ax.set_title(title)

    ax.set_xlim(-base, base)
    ax.set_ylim(-base, base)
    ax.set_zlim(0, height * 1.1)
    ax.set_box_aspect([2*base, 2*base, height])

    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()

    return fig_to_png_bytes(fig)
