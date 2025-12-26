# routers/shapes/rectangular_prism.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from ..models import RectangularPrismParams
from .utils import fig_to_png_bytes
from typing import Optional

def draw_rectangular_prism_params(p: RectangularPrismParams, title: Optional[str]) -> bytes:
    L, W, H = p.length, p.width, p.height

    label_length = p.label_length or f"Largo = {L}"
    label_width  = p.label_width  or f"Ancho = {W}"
    label_height = p.label_height or f"Altura = {H}"

    vertices = np.array([
        [0, 0, 0],
        [L, 0, 0],
        [L, W, 0],
        [0, W, 0],
        [0, 0, H],
        [L, 0, H],
        [L, W, H],
        [0, W, H],
    ])

    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[3], vertices[0], vertices[4], vertices[7]],
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    poly = Poly3DCollection(faces, alpha=0.2)
    ax.add_collection3d(poly)

    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7),
    ]
    for i, j in edges:
        xs = [vertices[i][0], vertices[j][0]]
        ys = [vertices[i][1], vertices[j][1]]
        zs = [vertices[i][2], vertices[j][2]]
        ax.plot(xs, ys, zs)

    ax.text(L/2, 0, 0, label_length, ha="center", va="top")
    ax.text(0, W/2, 0, label_width, ha="left", va="center")
    ax.text(0, 0, H/2, label_height, ha="left", va="center")

    if title:
        ax.set_title(title)

    ax.set_xlim(0, L * 1.1)
    ax.set_ylim(0, W * 1.1)
    ax.set_zlim(0, H * 1.1)

    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()

    return fig_to_png_bytes(fig)
