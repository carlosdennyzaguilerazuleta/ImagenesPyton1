# routers/shapes/cylinder.py

import numpy as np
import matplotlib.pyplot as plt
from ..models import CylinderParams
from .utils import fig_to_png_bytes
from typing import Optional

def draw_cylinder_params(p: CylinderParams, title: Optional[str]) -> bytes:
    r, h = p.radius, p.height

    label_r = p.label_radius or f"Radio = {r}"
    label_h = p.label_height or f"Altura = {h}"

    theta = np.linspace(0, 2*np.pi, 60)
    z = np.linspace(0, h, 30)
    Theta, Z = np.meshgrid(theta, z)

    X = r * np.cos(Theta)
    Y = r * np.sin(Theta)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(X, Y, Z, alpha=0.2)

    ax.text(r, 0, 0, label_r, ha="left", va="center")
    ax.text(0, 0, h/2, label_h, ha="left", va="center")

    if title:
        ax.set_title(title)

    lim = r * 1.3
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(0, h * 1.1)

    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()

    return fig_to_png_bytes(fig)
