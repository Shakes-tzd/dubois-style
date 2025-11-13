"""Du Bois–style Georgia map example using marimo."""

import marimo

__generated_with = "0.8.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    from dubois_style import apply_dubois_style, dubois_legend, DUBOIS_FAMILIES, DUBOIS_LIGHT_CYCLE

    return (
        DUBOIS_FAMILIES,
        DUBOIS_LIGHT_CYCLE,
        Rectangle,
        dubois_legend,
        np,
        plt,
        apply_dubois_style,
    )


@app.cell
def _(apply_dubois_style):
    # Apply Du Bois style
    apply_dubois_style(
        cycle="light",
        use_contrast_colors=True,
        show_x_axis=False,
        show_y_axis=False,
    )
    return


@app.cell
def _(DUBOIS_LIGHT_CYCLE, Rectangle, dubois_legend, np, plt):
    # Example: Simplified Georgia map visualization
    # Inspired by Du Bois' "Georgia Negro" map from the 1900 Paris Exposition
    # This is a simplified representation using rectangles

    fig, ax = plt.subplots(figsize=(10, 12))

    # Simulated counties/regions (represented as rectangles)
    # In a real implementation, you would use actual geographic data
    regions = [
        {"name": "Region 1", "x": 0.1, "y": 0.7, "width": 0.15, "height": 0.2, "value": 45},
        {"name": "Region 2", "x": 0.3, "y": 0.7, "width": 0.15, "height": 0.2, "value": 78},
        {"name": "Region 3", "x": 0.5, "y": 0.7, "width": 0.15, "height": 0.2, "value": 32},
        {"name": "Region 4", "x": 0.7, "y": 0.7, "width": 0.15, "height": 0.2, "value": 91},
        {"name": "Region 5", "x": 0.1, "y": 0.4, "width": 0.15, "height": 0.2, "value": 56},
        {"name": "Region 6", "x": 0.3, "y": 0.4, "width": 0.15, "height": 0.2, "value": 67},
        {"name": "Region 7", "x": 0.5, "y": 0.4, "width": 0.15, "height": 0.2, "value": 43},
        {"name": "Region 8", "x": 0.7, "y": 0.4, "width": 0.15, "height": 0.2, "value": 89},
        {"name": "Region 9", "x": 0.1, "y": 0.1, "width": 0.15, "height": 0.2, "value": 34},
        {"name": "Region 10", "x": 0.3, "y": 0.1, "width": 0.15, "height": 0.2, "value": 72},
        {"name": "Region 11", "x": 0.5, "y": 0.1, "width": 0.15, "height": 0.2, "value": 58},
        {"name": "Region 12", "x": 0.7, "y": 0.1, "width": 0.15, "height": 0.2, "value": 95},
    ]

    # Normalize values for color mapping
    values = [r["value"] for r in regions]
    min_val, max_val = min(values), max(values)

    # Use Du Bois light color cycle
    colors = DUBOIS_LIGHT_CYCLE
    
    for i, region in enumerate(regions):
        # Map value to color
        normalized = (region["value"] - min_val) / (max_val - min_val) if max_val > min_val else 0
        color_idx = int(normalized * (len(colors) - 1))
        color = colors[color_idx]
        
        rect = Rectangle(
            (region["x"], region["y"]),
            region["width"],
            region["height"],
            facecolor=color,
            edgecolor="#111111",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        
        # Add value label
        ax.text(
            region["x"] + region["width"] / 2,
            region["y"] + region["height"] / 2,
            str(region["value"]),
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="white" if normalized > 0.5 else "#111111",
        )
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(
        "Du Bois–Style Regional Map\n(Inspired by 'Georgia Negro' 1900)",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )
    ax.axis("off")
    
    plt.tight_layout()
    fig
    return ax, color, color_idx, colors, fig, max_val, min_val, normalized, rect, region, regions, values


