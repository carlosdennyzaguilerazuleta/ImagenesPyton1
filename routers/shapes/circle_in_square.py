# routers/shapes/circle_in_square.py

import matplotlib.pyplot as plt
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_circle_in_square(req: GenerateRequest) -> bytes:
    if req.side is None:
        raise ValueError("Para shape='circle_in_square' debes enviar 'side'.")

    side = req.side
    radius = side / 2

    fig, ax = plt.subplots()

    # Cuadrado
    half_side = side / 2
    square_coords = [
        (-half_side, -half_side),
        (half_side, -half_side),
        (half_side, half_side),
        (-half_side, half_side),
        (-half_side, -half_side)
    ]
    xs, ys = zip(*square_coords)
    ax.plot(xs, ys, color='red')

    # Círculo
    circle = plt.Circle((0, 0), radius, fill=False, color='blue', linestyle='--')
    ax.add_patch(circle)

    # Etiquetas y líneas de referencia
    if req.label_side:
        ax.text(0, -half_side - 0.1*radius, req.label_side, ha='center', va='top')

    if req.label_radius:
        ax.plot([0, radius], [0, 0], color='gray', linestyle=':')
        ax.text(radius/2, 0.1, req.label_radius, ha='center')


    ax.set_title(req.title or "Círculo inscrito en un Cuadrado")
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    lim = half_side * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    return fig_to_png_bytes(fig)
