# routers/shapes/circle.py

import matplotlib.pyplot as plt
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_circle(req: GenerateRequest) -> bytes:
    if req.radius is None:
        raise ValueError("Para shape='circle' debes enviar 'radius'.")

    fig, ax = plt.subplots()
    circle = plt.Circle((req.center_x, req.center_y), req.radius, fill=False)
    ax.add_patch(circle)

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)

    lim = req.radius * 1.5
    ax.set_xlim(req.center_x - lim, req.center_x + lim)
    ax.set_ylim(req.center_y - lim, req.center_y + lim)

    if req.title:
        ax.set_title(req.title)

    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    return fig_to_png_bytes(fig)
