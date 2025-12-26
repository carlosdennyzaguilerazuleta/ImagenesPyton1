# routers/shapes/line.py

import numpy as np
import matplotlib.pyplot as plt
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_line(req: GenerateRequest) -> bytes:
    fig, ax = plt.subplots()

    if req.m is not None and req.b is not None:
        x = np.linspace(-10, 10, 400)
        y = req.m * x + req.b
        ax.plot(x, y)
    elif None not in (req.x1, req.y1, req.x2, req.y2):
        x = np.linspace(req.x1, req.x2, 400)
        if req.x2 != req.x1:
            m = (req.y2 - req.y1) / (req.x2 - req.x1)
            b = req.y1 - m * req.x1
            y = m * x + b
            ax.plot(x, y)
        else:
            ax.axvline(req.x1)
    else:
        raise ValueError("Para shape='line' envía 'm' y 'b' o 'x1,y1,x2,y2'.")

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    if req.title:
        ax.set_title(req.title)

    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)
    ax.set_aspect("equal", adjustable="box")

    return fig_to_png_bytes(fig)
