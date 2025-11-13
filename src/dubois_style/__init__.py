"""A W.E.B. Du Bois–inspired Matplotlib style and color palette."""

from .palettes import (
    DUBOIS_FAMILIES,
    DUBOIS_COLORS_LIGHT,
    DUBOIS_COLORS_DARK,
    DUBOIS_LIGHT_CYCLE,
    DUBOIS_DARK_CYCLE,
    DUBOIS_CATEGORICAL_CYCLE,
)
from .style import (
    apply_dubois_style,
    dubois_legend,
)

__all__ = [
    "DUBOIS_FAMILIES",
    "DUBOIS_COLORS_LIGHT",
    "DUBOIS_COLORS_DARK",
    "DUBOIS_LIGHT_CYCLE",
    "DUBOIS_DARK_CYCLE",
    "DUBOIS_CATEGORICAL_CYCLE",
    "apply_dubois_style",
    "dubois_legend",
]

__version__ = "0.1.0"


