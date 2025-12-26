# routers/shapes/rectangle.py

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_rectangle(req: GenerateRequest) -> bytes:
    if req.length is None or req.width is None:
        raise ValueError("Para shape='rectangle' debes enviar 'length' y 'width'.")

    L = req.length
    W = req.width

    label_length = req.label_length or f"Largo = {L}"
    label_width = req.label_width or f"Ancho = {W}"

    fig, ax = plt.subplots()

    rect = Rectangle((0, 0), L, W, fill=False)
    ax.add_patch(rect)

    # Etiquetas
    ax.text(L / 2, -0.08 * W, label_length, ha="center", va="top")
    ax.text(-0.08 * L, W / 2, label_width, ha="right", va="center", rotation=90)

    ax.set_title(req.title or "Rectángulo")

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-0.2 * L, L * 1.2)
    ax.set_ylim(-0.2 * W, W * 1.2)
    ax.axis("off")

    return fig_to_png_bytes(fig)
