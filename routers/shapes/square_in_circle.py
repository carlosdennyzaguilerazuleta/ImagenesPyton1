# routers/shapes/square_in_circle.py

import matplotlib.pyplot as plt
import numpy as np
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_square_in_circle(req: GenerateRequest) -> bytes:
    if req.radius is None:
        raise ValueError("Para shape='square_in_circle' debes enviar 'radius'.")

    radius = req.radius
    side = radius * np.sqrt(2)

    fig, ax = plt.subplots()

    # Círculo
    circle = plt.Circle((0, 0), radius, fill=False, color='blue', linestyle='--')
    ax.add_patch(circle)

    # Cuadrado
    half_side = side / 2
    square_coords = [
        (-half_side, -half_side),
        (half_side, -half_side),
        (half_side, half_side),
        (-half_side, half_side),
        (-half_side, -half_side) # para cerrar el polígono
    ]
    xs, ys = zip(*square_coords)
    ax.plot(xs, ys, color='red')

    # Etiquetas y líneas de referencia
    if req.label_radius:
        ax.plot([0, radius], [0, 0], color='gray', linestyle=':')
        ax.text(radius/2, 0.1, req.label_radius, ha='center')

    if req.label_side:
        ax.text(0, -half_side - 0.1*radius, req.label_side, ha='center', va='top')

    ax.set_title(req.title or "Cuadrado inscrito en un Círculo")
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    lim = radius * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    return fig_to_png_bytes(fig)
