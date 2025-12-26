# routers/shapes/triangle.py

import matplotlib.pyplot as plt
import numpy as np
from .utils import fig_to_png_bytes
# Import GenerateRequest from the new models file
from ..models import GenerateRequest

def draw_triangle(req: GenerateRequest) -> bytes:
    # Lógica para dibujar el triángulo
    fig, ax = plt.subplots()

    if req.mode == 'sss':
        # Código para dibujar con SSS
        pass
    elif req.mode == 'sas':
        # Código para dibujar con SAS
        pass
    # ... otros modos ...
    else: # Modo legacy o por defecto
        base, height = req.base or 1, req.height or 1
        label_base = req.label_base or "Base"
        label_height = req.label_height or "Height"
        label_hypotenuse = req.label_hypotenuse or "Hypotenuse"

        # Dibuja un triángulo rectángulo simple
        ax.plot([0, base], [0, 0], 'b-') # base
        ax.plot([0, 0], [0, height], 'b-') # altura
        ax.plot([0, base], [0, height], 'r--') # hipotenusa

        ax.text(base/2, -0.1, label_base, ha='center')
        ax.text(-0.1, height/2, label_height, va='center', rotation='vertical')
        ax.text(base/2, height/2, label_hypotenuse)

    ax.set_aspect('equal', adjustable='box')
    plt.title(req.title or "Triángulo")
    return fig_to_png_bytes(fig)
