# routers/shapes/utils.py
import io
import matplotlib.pyplot as plt

def fig_to_png_bytes(fig) -> bytes:
    """Converts a matplotlib figure to PNG bytes."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return buf.read()
