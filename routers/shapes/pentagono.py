import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_pentagon(req: GenerateRequest) -> bytes:
    # Para un pentágono regular, solemos usar el 'lado' o el 'radio'
    # Asumiremos que 'length' actúa como el radio si no se especifica otra cosa
    if req.radio is None:
        raise ValueError("Para shape='pentagon' debes enviar 'radio' (como radio del centro al vértice).")

    R = req.radio
    label_side = req.label_length or f"Radio = {R}"

    fig, ax = plt.subplots()

    # RegularPolygon: (centro_x, centro_y), num_lados, radio, orientación (radianes)
    # Ponemos la punta hacia arriba con orientation=0
    pentagon = RegularPolygon((R, R), 5, radius=R, orientation=0, fill=False, edgecolor='black')
    ax.add_patch(pentagon)

    # Cálculo opcional para etiqueta en la base o centro
    ax.text(R, 0.1 * R, label_side, ha="center", va="top")

    ax.set_title(req.title or "Pentágono Regular")

    # Ajustar límites para que no se corte la figura
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(0, 2 * R)
    ax.set_ylim(0, 2 * R)
    ax.axis("off")

    return fig_to_png_bytes(fig)