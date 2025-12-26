# routers/shapes/cube.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from ..models import CubeParams
from .utils import fig_to_png_bytes
from typing import Optional

def draw_cube(p: CubeParams, title: Optional[str]) -> bytes:
    side = p.side

    label_side = p.label_side or f"Lado = {side}"

    vertices = np.array([
        [0, 0, 0],
        [side, 0, 0],
        [side, side, 0],
        [0, side, 0],
        [0, 0, side],
        [side, 0, side],
        [side, side, side],
        [0, side, side],
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

    ax.text(side/2, 0, 0, label_side, ha="center", va="top")

    if title:
        ax.set_title(title)

    ax.set_xlim(0, side * 1.1)
    ax.set_ylim(0, side * 1.1)
    ax.set_zlim(0, side * 1.1)

    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()

    return fig_to_png_bytes(fig)
