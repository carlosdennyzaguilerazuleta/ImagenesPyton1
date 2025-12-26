# routers/shapes/angles.py

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from ..models import AnglesDiagramRequest
from .utils import fig_to_png_bytes

def draw_angles(req: AnglesDiagramRequest) -> bytes:
    """
    Dibuja 2 rectas paralelas (r y s) cortadas por una transversal (t).
    Como el JSON no incluye coordenadas, se usa un layout por defecto.
    """

    # Layout por defecto
    r_y = 2.0
    s_y = 0.0
    x_min, x_max = -1.0, 5.0

    # Definimos transversal t por dos puntos que crucen ambas paralelas
    t_p1 = (1.0, r_y)
    t_p2 = (3.2, s_y)

    fig, ax = plt.subplots()

    # Paralelas
    ax.plot([x_min, x_max], [r_y, r_y], linewidth=2)
    ax.plot([x_min, x_max], [s_y, s_y], linewidth=2)

    # Transversal extendida
    (x1, y1), (x2, y2) = t_p1, t_p2
    if x2 == x1:
        ax.axvline(x1, linewidth=2)
        m = None
        t_is_vertical = True
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        xs = np.array([x_min, x_max])
        ys = m * xs + b
        ax.plot(xs, ys, linewidth=2)
        t_is_vertical = False

    # Etiquetas de rectas según ids
    line_ids = {ln.id: ln.type for ln in req.lines}
    if "r" in line_ids:
        ax.text(x_max - 0.25, r_y + 0.12, "r", fontsize=12)
    if "s" in line_ids:
        ax.text(x_max - 0.25, s_y + 0.12, "s", fontsize=12)
    if "t" in line_ids:
        ax.text(x_min + 0.2, r_y + 0.25, "t", fontsize=12)

    # Intersección principal r ∩ t
    ix, iy = t_p1

    # Recuperar ángulos por ID
    angle1 = next((a for a in req.angles if a.id == "1"), None)
    angle2 = next((a for a in req.angles if a.id == "2"), None)

    # Dibujar arco para ∠1 si hay medida
    if angle1 and angle1.measure is not None:
        measure = float(angle1.measure)

        # Ángulo de la transversal respecto al eje x
        if t_is_vertical:
            theta_t = 90.0
        else:
            theta_t = math.degrees(math.atan(m))

        # r horizontal -> 0°
        theta_r = 0.0

        # Dibujamos un arco pequeño en la intersección
        start = min(theta_r, theta_t)
        end = start + abs(measure)

        radius = 0.55
        arc = Arc(
            (ix, iy),
            width=radius,
            height=radius,
            angle=0,
            theta1=start,
            theta2=end,
            linewidth=1.5
        )
        ax.add_patch(arc)

        label_text = angle1.label or f"∠{angle1.id} = {int(measure)}°"
        ax.text(ix + 0.25, iy + 0.18, label_text, fontsize=10)

    # Etiqueta ∠2 (opuesto por el vértice) si viene
    if angle2:
        label_text = angle2.label or f"∠{angle2.id}"
        ax.text(ix - 1.0, iy - 0.45, label_text, fontsize=10)

    ax.set_title(req.title or "Rectas paralelas y transversal")
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    return fig_to_png_bytes(fig)
