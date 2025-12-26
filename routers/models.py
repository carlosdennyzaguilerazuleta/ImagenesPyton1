# routers/models.py

from pydantic import BaseModel, Field
from typing import Optional, Literal, List, Dict, Any

# =========================================================
# Modelos de parámetros para estándar 3D y nuevas figuras
# =========================================================
class RectangularPrismParams(BaseModel):
    length: float
    width: float
    height: float

    label_length: Optional[str] = None
    label_width: Optional[str] = None
    label_height: Optional[str] = None


class TriangularPrismParams(BaseModel):
    # Base triangular rectángula (simple y clara para problemas escolares)
    base: float
    height: float
    length: float  # profundidad del prisma

    label_base: Optional[str] = None
    label_height: Optional[str] = None
    label_length: Optional[str] = None


class CylinderParams(BaseModel):
    radius: float
    height: float

    label_radius: Optional[str] = None
    label_height: Optional[str] = None


class SphereParams(BaseModel):
    radius: float
    label_radius: Optional[str] = None

class ConeParams(BaseModel):
    radius: float
    height: float
    label_radius: Optional[str] = None
    label_height: Optional[str] = None

class CubeParams(BaseModel):
    side: float
    label_side: Optional[str] = None

class PyramidParams(BaseModel):
    base: float # lado de la base cuadrada
    height: float
    label_base: Optional[str] = None
    label_height: Optional[str] = None


class SolidEnvelope(BaseModel):
    shape: Literal["solid"]
    type: Literal["rectangular_prism", "triangular_prism", "cylinder", "sphere", "spher", "cone", "cube", "pyramid"]
    title: Optional[str] = None
    params: Dict[str, Any]


# =========================================================
# Modelos para diagrama de ángulos (paralelas + transversal)
# =========================================================
class AngleLine(BaseModel):
    id: str
    type: Literal["parallel", "transversal"]


class AngleItem(BaseModel):
    id: str
    measure: Optional[float] = None
    label: Optional[str] = None
    formed_by: List[str]


class AnglesDiagramRequest(BaseModel):
    shape: Literal["angles"]
    title: Optional[str] = None
    lines: List[AngleLine]
    angles: List[AngleItem]


# =========================================================
# Modelo legacy + 2D
# =========================================================
class GenerateRequest(BaseModel):
    shape: Literal[
        "triangle",
        "circle",
        "line",
        "function",
        "cartesian",
        "rectangle",
        "circle_in_square",
        "square_in_circle",
        "triangle_in_circle",

        # legacy 3D directos
        "rectangle_prism",
        "triangular_prism",
        "cylinder",
        "sphere",
        "spher",
    ]
    title: Optional[str] = None

    # -------------------------
    # 2D - Triángulo
    # -------------------------
    # Legacy - para triángulos rectángulos
    base: Optional[float] = None
    height: Optional[float] = None
    label_base: Optional[str] = None
    label_height: Optional[str] = None
    label_hypotenuse: Optional[str] = None

    # Nuevos modos de construcción
    mode: Optional[Literal["sss", "sas", "asa", "aas"]] = None

    # Lados (usados por sss, sas, asa, aas)
    side_ab: Optional[float] = None
    side_bc: Optional[float] = None
    side_ac: Optional[float] = None
    
    # Ángulos en grados (usados por sas, asa, aas)
    angle_A: Optional[float] = None
    angle_B: Optional[float] = None
    angle_C: Optional[float] = None
    
    # Etiquetas de lados
    label_side_ab: Optional[str] = None
    label_side_bc: Optional[str] = None
    label_side_ac: Optional[str] = None

    # -------------------------
    # 2D - Círculo
    # -------------------------
    radius: Optional[float] = None
    center_x: float = 0.0
    center_y: float = 0.0

    # -------------------------
    # 2D - Línea
    # -------------------------
    m: Optional[float] = None
    b: Optional[float] = None
    x1: Optional[float] = None
    y1: Optional[float] = None
    x2: Optional[float] = None
    y2: Optional[float] = None

    # -------------------------
    # 2D - Función
    # -------------------------
    expression: Optional[str] = None
    x_min: float = -10
    x_max: float = 10

    # -------------------------
    # 2D - Plano cartesiano
    # -------------------------
    show_grid: bool = True
    points: Optional[List[List[float]]] = None

    # -------------------------
    # 2D - Figuras inscritas
    # -------------------------
    side: Optional[float] = None # Para circle_in_square (y cuadrado general si se quisiera)
    label_side: Optional[str] = None # Etiqueta lado
    label_radius: Optional[str] = None # Etiqueta radio (reutilizada)

    # -------------------------
    # 3D legacy - Prisma rectangular
    # acepta JSON con "height"
    # -------------------------
    length: Optional[float] = None
    width: Optional[float] = None
    height3d: Optional[float] = Field(default=None, alias="height")

    label_length: Optional[str] = None
    label_width: Optional[str] = None
    label_height: Optional[str] = None

    # -------------------------
    # 3D legacy - Prisma triangular
    # -------------------------
    tri_base: Optional[float] = None
    tri_height: Optional[float] = None
    tri_length: Optional[float] = None

    label_tri_base: Optional[str] = None
    label_tri_height: Optional[str] = None
    label_tri_length: Optional[str] = None

    # -------------------------
    # 3D legacy - Cilindro
    # -------------------------
    cyl_radius: Optional[float] = None
    cyl_height: Optional[float] = None
    label_radius_3d: Optional[str] = None
    label_cyl_height: Optional[str] = None

    # -------------------------
    # 3D legacy - Esfera
    # -------------------------
    sphere_radius: Optional[float] = None
    label_sphere_radius: Optional[str] = None

    class Config:
        # permite que el alias "height" pueble height3d
        populate_by_name = True
        allow_population_by_field_name = True
