# routers/shapes/function.py

import numpy as np
import matplotlib.pyplot as plt
from ..models import GenerateRequest
from .utils import fig_to_png_bytes

def draw_function(req: GenerateRequest) -> bytes:
    if not req.expression:
        raise ValueError("Para shape='function' debes enviar 'expression'.")

    x = np.linspace(req.x_min, req.x_max, 800)

    allowed_names = {
        "x": x,
        "np": np,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "exp": np.exp,
        "sqrt": np.sqrt,
        "log": np.log,
        "pi": np.pi,
        "e": np.e,
    }

    try:
        y = eval(req.expression, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {e}")

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlim(req.x_min, req.x_max)

    ax.set_title(req.title or f"y = {req.expression}")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    return fig_to_png_bytes(fig)
