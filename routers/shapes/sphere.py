# routers/shapes/sphere.py

import numpy as np
import matplotlib.pyplot as plt
from ..models import SphereParams
from .utils import fig_to_png_bytes
from typing import Optional

def draw_sphere_params(p: SphereParams, title: Optional[str]) -> bytes:
    r = p.radius
    label_r = p.label_radius or f"Radio = {r}"

    u = np.linspace(0, np.pi, 40)
    v = np.linspace(0, 2*np.pi, 60)
    U, V = np.meshgrid(u, v)

    X = r * np.sin(U) * np.cos(V)
    Y = r * np.sin(U) * np.sin(V)
    Z = r * np.cos(U)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, alpha=0.2)

    ax.text(r, 0, 0, label_r, ha="left", va="center")

    if title:
        ax.set_title(title)

    lim = r * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()

    return fig_to_png_bytes(fig)
