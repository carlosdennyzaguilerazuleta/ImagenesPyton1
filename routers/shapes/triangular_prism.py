# routers/shapes/triangular_prism.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from ..models import TriangularPrismParams
from .utils import fig_to_png_bytes
from typing import Optional

def draw_triangular_prism_params(p: TriangularPrismParams, title: Optional[str]) -> bytes:
    B, H, L = p.base, p.height, p.length

    label_base   = p.label_base or f"Base = {B}"
    label_height = p.label_height or f"Altura = {H}"
    label_length = p.label_length or f"Largo = {L}"

    v0 = np.array([0, 0, 0])
    v1 = np.array([B, 0, 0])
    v2 = np.array([0, H, 0])

    v3 = np.array([0, 0, L])
    v4 = np.array([B, 0, L])
    v5 = np.array([0, H, L])

    faces = [
        [v0, v1, v2],
        [v3, v4, v5],
        [v0, v1, v4, v3],
        [v1, v2, v5, v4],
        [v2, v0, v3, v5],
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    poly = Poly3DCollection(faces, alpha=0.2)
    ax.add_collection3d(poly)

    # aristas base
    ax.plot([0, B], [0, 0], [0, 0])
    ax.plot([0, 0], [0, H], [0, 0])
    ax.plot([B, 0], [0, H], [0, 0])

    # aristas tapa
    ax.plot([0, B], [0, 0], [L, L])
    ax.plot([0, 0], [0, H], [L, L])
    ax.plot([B, 0], [0, H], [L, L])

    # aristas verticales
    ax.plot([0, 0], [0, 0], [0, L])
    ax.plot([B, B], [0, 0], [0, L])
    ax.plot([0, 0], [H, H], [0, L])

    ax.text(B/2, 0, 0, label_base, ha="center", va="top")
    ax.text(0, H/2, 0, label_height, ha="left", va="center")
    ax.text(0, 0, L/2, label_length, ha="left", va="center")

    if title:
        ax.set_title(title)

    ax.set_xlim(0, B * 1.1)
    ax.set_ylim(0, H * 1.1)
    ax.set_zlim(0, L * 1.1)

    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()

    return fig_to_png_bytes(fig)
