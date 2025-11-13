"""Apply Du Bois–inspired styling to matplotlib plots."""

from cycler import cycler
from matplotlib import pyplot as plt
from matplotlib import font_manager

from .palettes import (
    DUBOIS_CATEGORICAL_CYCLE,
    DUBOIS_DARK_CYCLE,
    DUBOIS_FAMILIES,
    DUBOIS_LIGHT_CYCLE,
)

# Re-export palettes for convenience
__all__ = [
    "DUBOIS_FAMILIES",
    "DUBOIS_LIGHT_CYCLE",
    "DUBOIS_DARK_CYCLE",
    "DUBOIS_CATEGORICAL_CYCLE",
    "apply_dubois_style",
    "dubois_legend",
]


def apply_dubois_style(
    *,
    cycle: str = "light",
    show_x_axis: bool = False,
    show_y_axis: bool = False,
    use_contrast_colors: bool = False,
    base_font: str | list[str] = "DejaVu Sans",
    custom_font_paths: list[str] | None = None,
):
    """
    Apply a DuBois-inspired Matplotlib style globally.

    Parameters
    ----------
    cycle : str, default "light"
        Base palette family. "light" or "dark" for sequential ramps.
    show_x_axis : bool, default False
        Whether to show the x-axis spine and ticks.
    show_y_axis : bool, default False
        Whether to show the y-axis spine and ticks.
    use_contrast_colors : bool, default False
        If True, use a high-contrast categorical palette instead of the
        sequential ramp for the axes color cycle. Great for multi-series
        line/bar plots.
    base_font : str | list[str], default "DejaVu Sans"
        Font family to use. Can be a single font name or a list of fallbacks.
        Default uses DejaVu Sans (bundled with matplotlib).

        Recommended alternatives:
        - "DejaVu Sans" (default, always available)
        - "Liberation Sans" (often pre-installed)
        - ["Libre Franklin", "DejaVu Sans"] (if Libre Franklin installed)
        - ["Public Sans", "DejaVu Sans"] (if Public Sans installed)
    custom_font_paths : list[str] | None, default None
        Optional paths to custom font files (.ttf, .otf) to register.
        Fonts will be registered with matplotlib's font manager.

    Notes
    -----
    This package uses open-source fonts by default:
    - **DejaVu Sans**: Pre-installed with matplotlib, excellent readability
    - **Liberation Sans**: Often pre-installed, Arial/Helvetica alternative

    Optional fonts for enhanced styling (require separate installation):
    - **Libre Franklin**: Open-source Franklin Gothic alternative (Google Fonts)
    - **Public Sans**: U.S. government's open-source sans-serif (Google Fonts)

    The original Du Bois visualizations likely used hand-lettering and
    early 20th century typefaces. These modern sans-serifs capture the
    clean, legible aesthetic while remaining freely available.

    Examples
    --------
    >>> # Default usage with DejaVu Sans
    >>> apply_dubois_style(cycle="light", show_x_axis=True, show_y_axis=True)

    >>> # Use Liberation Sans (commonly pre-installed)
    >>> apply_dubois_style(base_font="Liberation Sans", use_contrast_colors=True)

    >>> # Use Libre Franklin with fallback to DejaVu Sans
    >>> apply_dubois_style(base_font=["Libre Franklin", "DejaVu Sans"])

    >>> # Register and use custom fonts
    >>> apply_dubois_style(
    ...     base_font="Custom Font",
    ...     custom_font_paths=["/path/to/font.ttf"],
    ...     cycle="dark"
    ... )
    """
    # Register custom font files if provided
    if custom_font_paths is not None:
        for font_path in custom_font_paths:
            font_manager.fontManager.addfont(font_path)

    if use_contrast_colors:
        # same categorical palette regardless of base light/dark choice
        color_cycle = DUBOIS_CATEGORICAL_CYCLE
    else:
        if cycle == "light":
            color_cycle = DUBOIS_LIGHT_CYCLE
        elif cycle == "dark":
            color_cycle = DUBOIS_DARK_CYCLE
        else:
            raise ValueError("cycle must be 'light' or 'dark'")

    plt.rcParams.update({
        # Transparency & backgrounds
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.facecolor": "none",

        "axes.unicode_minus": False,

        # >>> color cycle we just chose <<<
        "axes.prop_cycle": cycler(color=color_cycle),

        # Axes & spines
        "axes.edgecolor": "#333333",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": show_y_axis,
        "axes.spines.bottom": show_x_axis,
        "axes.grid": False,

        # Ticks
        "xtick.bottom": show_x_axis,
        "ytick.left": show_y_axis,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,

        # Text & legend
        "font.family": [base_font] if isinstance(base_font, str) else base_font,
        "text.color": "#111111",
        "axes.labelcolor": "#111111",
        "xtick.color": "#666666",
        "ytick.color": "#666666",
        "legend.frameon": False,
        "legend.labelcolor": "#666666",

        # Lines & patches
        "lines.linewidth": 2.0,
        "patch.edgecolor": "#111111",
    })


def dubois_legend(
    ax,
    *args,
    outside: bool = True,
    outside_pad: float = 0.02,
    **kwargs,
):
    """
    Convenience wrapper for ax.legend() that uses DuBois-friendly defaults
    and (optionally) places the legend outside the axes to the right.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to attach the legend to.
    outside : bool, default True
        If True, place legend to the right of the axes (centered vertically).
        If False, fall back to an inside location (default 'best' or kwargs["loc"]).
    outside_pad : float, default 0.02
        Horizontal padding beyond the axes when outside=True.
    *args, **kwargs :
        Passed through to ax.legend().

    Returns
    -------
    matplotlib.legend.Legend
        The created legend object.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], label="Series 1")
    >>> dubois_legend(ax, outside=True)
    """
    if outside:
        # Get the current loc/bbox if provided, otherwise use defaults
        loc = kwargs.pop("loc", "center left")
        bbox = kwargs.pop("bbox_to_anchor", (1.0 + outside_pad, 0.5))
        return ax.legend(
            *args,
            loc=loc,
            bbox_to_anchor=bbox,
            borderaxespad=0.0,
            frameon=False,
            **kwargs,
        )
    else:
        # inside-axes legend with DuBois defaults
        kwargs.setdefault("loc", "best")
        kwargs.setdefault("frameon", False)
        return ax.legend(*args, **kwargs)
