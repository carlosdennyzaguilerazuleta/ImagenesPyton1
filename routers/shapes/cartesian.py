# routers/shapes/cartesian.py

import matplotlib.pyplot as plt
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_cartesian(req: GenerateRequest) -> bytes:
    fig, ax = plt.subplots()

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    if req.show_grid:
        ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    if req.points:
        xs = [p[0] for p in req.points]
        ys = [p[1] for p in req.points]
        ax.scatter(xs, ys)
        for x_val, y_val in zip(xs, ys):
            ax.text(x_val, y_val, f"({x_val}, {y_val})",
                    fontsize=8, ha="left", va="bottom")

    ax.set_title(req.title or "Plano cartesiano")
    ax.set_aspect("equal", adjustable="box")

    return fig_to_png_bytes(fig)
