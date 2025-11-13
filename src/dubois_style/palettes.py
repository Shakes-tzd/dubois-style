"""Du Bois–inspired color palettes for matplotlib."""

# --------------------------------------------------------------------
# 1. Full DuBois palette: light + dark variants
# --------------------------------------------------------------------
DUBOIS_FAMILIES = {
    "Warm Tan": {
        "light": "#d6c1ab",
        "dark":  "#b69c7e",
    },
    "Dusty Pink": {
        "light": "#e8b7b0",
        "dark":  "#cc8f88",
    },
    "Ochre": {
        "light": "#e9c057",
        "dark":  "#c89c33",
    },
    "Red": {
        "light": "#c83737",
        "dark":  "#9e2424",
    },
    "Deep Green": {
        "light": "#58705c",
        "dark":  "#35473b",
    },
    "Dark Brown": {
        "light": "#6f5740",
        "dark":  "#4b3928",
    },
    "Deep Navy": {
        "light": "#3d4b74",
        "dark":  "#2a3556",
    },
}

DUBOIS_COLORS_LIGHT = {
    "warm_tan":   DUBOIS_FAMILIES["Warm Tan"]["light"],
    "dusty_pink": DUBOIS_FAMILIES["Dusty Pink"]["light"],
    "ochre":      DUBOIS_FAMILIES["Ochre"]["light"],
    "red":        DUBOIS_FAMILIES["Red"]["light"],
    "deep_green": DUBOIS_FAMILIES["Deep Green"]["light"],
    "dark_brown": DUBOIS_FAMILIES["Dark Brown"]["light"],
    "deep_navy":  DUBOIS_FAMILIES["Deep Navy"]["light"],
}

DUBOIS_COLORS_DARK = {
    "warm_tan":   DUBOIS_FAMILIES["Warm Tan"]["dark"],
    "dusty_pink": DUBOIS_FAMILIES["Dusty Pink"]["dark"],
    "ochre":      DUBOIS_FAMILIES["Ochre"]["dark"],
    "red":        DUBOIS_FAMILIES["Red"]["dark"],
    "deep_green": DUBOIS_FAMILIES["Deep Green"]["dark"],
    "dark_brown": DUBOIS_FAMILIES["Dark Brown"]["dark"],
    "deep_navy":  DUBOIS_FAMILIES["Deep Navy"]["dark"],
}

# ordered by your intensity preference
DUBOIS_LIGHT_CYCLE = [
    DUBOIS_COLORS_LIGHT["warm_tan"],
    DUBOIS_COLORS_LIGHT["dusty_pink"],
    DUBOIS_COLORS_LIGHT["ochre"],
    DUBOIS_COLORS_LIGHT["red"],
    DUBOIS_COLORS_LIGHT["deep_green"],
    DUBOIS_COLORS_LIGHT["dark_brown"],
    DUBOIS_COLORS_LIGHT["deep_navy"],
]

DUBOIS_DARK_CYCLE = [
    DUBOIS_COLORS_DARK["warm_tan"],
    DUBOIS_COLORS_DARK["dusty_pink"],
    DUBOIS_COLORS_DARK["ochre"],
    DUBOIS_COLORS_DARK["red"],
    DUBOIS_COLORS_DARK["deep_green"],
    DUBOIS_COLORS_DARK["dark_brown"],
    DUBOIS_COLORS_DARK["deep_navy"],
]

# High-contrast categorical palette:
# ordered so the first few colors are easy to distinguish
DUBOIS_CATEGORICAL_CYCLE = [
    DUBOIS_COLORS_LIGHT["deep_navy"],   # strong cool
    DUBOIS_COLORS_LIGHT["ochre"],       # bright warm
    DUBOIS_COLORS_LIGHT["deep_green"],  # mid cool
    DUBOIS_COLORS_LIGHT["red"],         # mid warm
    DUBOIS_COLORS_LIGHT["warm_tan"],    # neutral light
    DUBOIS_COLORS_LIGHT["dusty_pink"],  # muted warm
    DUBOIS_COLORS_LIGHT["dark_brown"],  # dark neutral
]
