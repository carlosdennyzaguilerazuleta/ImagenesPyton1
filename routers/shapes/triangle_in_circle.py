# routers/shapes/triangle_in_circle.py

import matplotlib.pyplot as plt
import numpy as np
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_triangle_in_circle(req: GenerateRequest) -> bytes:
    if req.radius is None:
        raise ValueError("Para shape='triangle_in_circle' debes enviar 'radius'.")

    radius = req.radius

    fig, ax = plt.subplots(figsize=(6, 6))

    # Círculo
    circle = plt.Circle((0, 0), radius, fill=False, color='blue', linestyle='--')
    ax.add_patch(circle)

    # Vértices del triángulo equilátero inscrito
    # Colocamos un vértice en la parte superior (0, radius) para que la base sea horizontal
    p1 = (0, radius)
    p2 = (radius * np.cos(7 * np.pi / 6), radius * np.sin(7 * np.pi / 6))
    p3 = (radius * np.cos(11 * np.pi / 6), radius * np.sin(11 * np.pi / 6))

    triangle_coords = [p1, p2, p3, p1]
    xs, ys = zip(*triangle_coords)
    ax.plot(xs, ys, color='red')
# Etiquetas y líneas de referencia
    if req.label_radius:
        ax.plot([0, 0], [0, radius], color='gray', linestyle=':')
        ax.text(0.05 * radius, radius / 2, req.label_radius, va='center')

    if req.label_side:
        # Etiquetar la base del triángulo
        mid_point_x = (p2[0] + p3[0]) / 2
        mid_point_y = (p2[1] + p3[1]) / 2
        ax.text(mid_point_x, mid_point_y - 0.1 * radius, req.label_side, ha='center', va='top')

    ax.set_title(req.title or "Triángulo inscrito en un Círculo")
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    lim = radius * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    return fig_to_png_bytes(fig)