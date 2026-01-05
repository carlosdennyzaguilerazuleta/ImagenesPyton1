import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_pentagon(req: GenerateRequest) -> bytes:
    # Verificamos que los datos necesarios existan (puedes ajustar según tu GenerateRequest)
    if req.lado is None or req.apotema is None or req.radio is None:
        raise ValueError("Se requiere 'lado', 'apotema' y 'radio' para el pentágono.")

    S = req.lado
    A = req.apotema
    R = req.radio

    fig, ax = plt.subplots(figsize=(6, 6))

    # Creamos el pentágono
    # Usamos el radio (R) para el tamaño
    # orientation=0 deja un vértice arriba y la base plana abajo
    pentagon = RegularPolygon((0, 0), 5, radius=R, orientation=0, fill=False, edgecolor='black', lw=2)
    ax.add_patch(pentagon)

    # --- Dibujo de líneas técnicas ---
    
    # 1. Línea del Apotema (del centro al punto medio de la base)
    ax.plot([0, 0], [0, -A], color="red", linestyle="--", label="Apotema")
    
    # 2. Línea del Radio (del centro a un vértice superior)
    # Calculamos el vértice superior derecho por trigonometría o simplemente hacia arriba
    ax.plot([0, 0], [0, R], color="blue", linestyle="--", label="Radio")

    # --- Etiquetas ---

    # Etiqueta del Lado (en la base)
    label_side =  f"Lado = {S}"
    ax.text(0, -A - (0.1 * R), label_side, ha="center", va="top", fontweight='bold')

    # Etiqueta del Apotema
    label_apo =  f"Ap = {A}"
    ax.text(0.05 * R, -A/2, label_apo, color="red", va="center")

    # Etiqueta del Radio
    label_rad =  f"R = {R}"
    ax.text(0.05 * R, R/2, label_rad, color="blue", va="center")

    # Título
    ax.set_title(req.title or "Pentágono Regular")

    # Configuración de los ejes
    ax.set_aspect("equal")
    # Margen dinámico basado en el radio
    lim = R * 1.3
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.axis("off")

    return fig_to_png_bytes(fig)