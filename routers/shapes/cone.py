# routers/shapes/cone.py

import numpy as np
import matplotlib.pyplot as plt
from ..models import ConeParams
from .utils import fig_to_png_bytes
from typing import Optional

def draw_cone(p: ConeParams, title: Optional[str]) -> bytes:
    r, h = p.radius, p.height

    label_r = p.label_radius or f"Radio = {r}"
    label_h = p.label_height or f"Altura = {h}"

    # Malla para la base circular
    theta = np.linspace(0, 2 * np.pi, 100)
    xb = r * np.cos(theta)
    yb = r * np.sin(theta)
    zb = np.zeros_like(xb)

    # Malla para la superficie cónica
    z_cone = np.linspace(0, h, 100)
    # El radio linealmente disminuye con la altura desde r hasta 0
    # r(z) = r * (1 - z/h)
    
    # Creamos un meshgrid para theta y z
    theta_grid, z_grid = np.meshgrid(theta, z_cone)
    r_grid = r * (1 - z_grid / h)
    
    x_grid = r_grid * np.cos(theta_grid)
    y_grid = r_grid * np.sin(theta_grid)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Dibujar superficie
    ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.2, color='b')
    # Dibujar borde base
    ax.plot(xb, yb, zb, color='b') 

    # Etiquetas
    ax.text(r / 2, 0, 0, label_r, color='black', ha='center', va='top')
    ax.plot([0, r], [0, 0], [0, 0], color='black') # Línea del radio
    ax.text(0, 0, h / 2, label_h, color='black', ha='left', va='center')
    ax.plot([0, 0], [0, 0], [0, h], color='black', linestyle='--') # Línea de la altura

    if title:
        ax.set_title(title)

    lim = max(r, h/2) * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(0, h * 1.1)

    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()

    return fig_to_png_bytes(fig)
