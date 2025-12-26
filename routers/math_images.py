
# routers/math_images.py

from fastapi import APIRouter, Depends
from typing import Union
import base64

from auth import get_current_client

# Import models from the new models file
from .models import (
    GenerateRequest,
    SolidEnvelope,
    AnglesDiagramRequest,
    RectangularPrismParams,
    TriangularPrismParams,
    CylinderParams,
    SphereParams,
    ConeParams,
    CubeParams,
    PyramidParams
)

# Import drawing functions from the shapes package
from routers.shapes.triangle import draw_triangle
from routers.shapes.circle import draw_circle
from routers.shapes.line import draw_line
from routers.shapes.function import draw_function
from routers.shapes.cartesian import draw_cartesian
from routers.shapes.rectangle import draw_rectangle
from routers.shapes.angles import draw_angles
from routers.shapes.rectangular_prism import draw_rectangular_prism_params
from routers.shapes.triangular_prism import draw_triangular_prism_params
from routers.shapes.cylinder import draw_cylinder_params
from routers.shapes.sphere import draw_sphere_params
from routers.shapes.cone import draw_cone
from routers.shapes.cube import draw_cube
from routers.shapes.pyramid import draw_pyramid
from routers.shapes.circle_in_square import draw_circle_in_square
from routers.shapes.square_in_circle import draw_square_in_circle
from routers.shapes.triangle_in_circle import draw_triangle_in_circle

# =========================================================
# Router protected with JWT
# =========================================================
router = APIRouter(
    tags=["math-images"],
    dependencies=[Depends(get_current_client)],
)


# =========================================================
# Endpoint /generate
# =========================================================
@router.post("/generate")
async def generate(req: Union[GenerateRequest, SolidEnvelope, AnglesDiagramRequest]):
    try:
        print("[generate] Request recibido de tipo", type(req), "con contenido:", req)

        if isinstance(req, AnglesDiagramRequest) and req.shape == "angles":
            img_bytes = draw_angles(req)
            img_b64 = base64.b64encode(img_bytes).decode("utf-8")
            return {"image_base64": img_b64, "shape": "angles"}

        if isinstance(req, SolidEnvelope) and req.shape == "solid":
            t = req.type

            if t == "rectangular_prism":
                p = RectangularPrismParams(**req.params)
                img_bytes = draw_rectangular_prism_params(p, req.title)
            elif t == "triangular_prism":
                p = TriangularPrismParams(**req.params)
                img_bytes = draw_triangular_prism_params(p, req.title)
            elif t == "cylinder":
                p = CylinderParams(**req.params)
                img_bytes = draw_cylinder_params(p, req.title)
            elif t in ("sphere", "spher"):
                p = SphereParams(**req.params)
                img_bytes = draw_sphere_params(p, req.title)
            elif t == "cone":
                p = ConeParams(**req.params)
                img_bytes = draw_cone(p, req.title)
            elif t == "cube":
                p = CubeParams(**req.params)
                img_bytes = draw_cube(p, req.title)
            elif t == "pyramid":
                p = PyramidParams(**req.params)
                img_bytes = draw_pyramid(p, req.title)
            else:
                raise ValueError("Tipo de sólido no soportado.")

            img_b64 = base64.b64encode(img_bytes).decode("utf-8")
            return {"image_base64": img_b64, "shape": "solid", "type": t}
        
        if isinstance(req, GenerateRequest):
            if req.shape == "triangle":
                img_bytes = draw_triangle(req)
            elif req.shape == "circle":
                img_bytes = draw_circle(req)
            elif req.shape == "line":
                img_bytes = draw_line(req)
            elif req.shape == "function":
                img_bytes = draw_function(req)
            elif req.shape == "cartesian":
                img_bytes = draw_cartesian(req)
            elif req.shape == "rectangle":
                img_bytes = draw_rectangle(req)
            elif req.shape == "circle_in_square":
                img_bytes = draw_circle_in_square(req)
            elif req.shape == "square_in_circle":
                img_bytes = draw_square_in_circle(req)
            elif req.shape == "triangle_in_circle":
                img_bytes = draw_triangle_in_circle(req)
            else:
                raise ValueError(f"Shape ''{req.shape}'' no soportado para GenerateRequest.")

            img_b64 = base64.b64encode(img_bytes).decode("utf-8")
            return {"image_base64": img_b64, "shape": req.shape}

        # If none of the above, it's a bad request
        raise ValueError("Tipo de request no soportado o shape incorrecto.")

    except ValueError as e:
        return {"error": str(e)}
