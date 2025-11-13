# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "cycler",
# ]
# ///

"""Gallery of Du Bois–style visualizations using marimo."""

import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    from cycler import cycler
    return cycler, font_manager, np, plt


@app.cell
def _():
    # ============================================================================
    # DU BOIS STYLE - INLINED FOR WASM COMPATIBILITY
    # ============================================================================

    # Du Bois Color Palettes
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

    DUBOIS_CATEGORICAL_CYCLE = [
        DUBOIS_COLORS_LIGHT["deep_navy"],
        DUBOIS_COLORS_LIGHT["ochre"],
        DUBOIS_COLORS_LIGHT["deep_green"],
        DUBOIS_COLORS_LIGHT["red"],
        DUBOIS_COLORS_LIGHT["warm_tan"],
        DUBOIS_COLORS_LIGHT["dusty_pink"],
        DUBOIS_COLORS_LIGHT["dark_brown"],
    ]

    return (
        DUBOIS_CATEGORICAL_CYCLE,
        DUBOIS_COLORS_DARK,
        DUBOIS_COLORS_LIGHT,
        DUBOIS_DARK_CYCLE,
        DUBOIS_FAMILIES,
        DUBOIS_LIGHT_CYCLE,
    )


@app.cell
def _(cycler, font_manager, plt):
    # Du Bois Style Functions

    def apply_dubois_style(
        *,
        cycle: str = "light",
        show_x_axis: bool = False,
        show_y_axis: bool = False,
        use_contrast_colors: bool = False,
        base_font: str | list[str] = "DejaVu Sans",
        custom_font_paths: list[str] | None = None,
    ):
        """Apply a DuBois-inspired Matplotlib style globally."""
        # Import color cycles
        from __main__ import (
            DUBOIS_CATEGORICAL_CYCLE,
            DUBOIS_DARK_CYCLE,
            DUBOIS_LIGHT_CYCLE,
        )

        # Register custom font files if provided
        if custom_font_paths is not None:
            for font_path in custom_font_paths:
                font_manager.fontManager.addfont(font_path)

        if use_contrast_colors:
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

            # Color cycle
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
        """Convenience wrapper for ax.legend() with DuBois-friendly defaults."""
        if outside:
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
            kwargs.setdefault("loc", "best")
            kwargs.setdefault("frameon", False)
            return ax.legend(*args, **kwargs)

    return apply_dubois_style, dubois_legend


@app.cell
def _(mo):
    mo.md(r"""
    # Du Bois Style Visualization Gallery

    A comprehensive gallery of data visualizations inspired by W.E.B. Du Bois' groundbreaking 1900 Paris Exposition visualizations.

    This package provides authentic Du Bois color palettes (warm tans, dusty pinks, ochres, deep greens) and styling options for creating historically-inspired, beautiful data visualizations.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## About the Color Palette

    The Du Bois palette features **seven earthy, muted tones** characteristic of early 20th-century hand-colored visualizations:

    - **Warm Tan** (#d6c1ab) - Neutral, warm base tone
    - **Dusty Pink** (#e8b7b0) - Soft, muted rose
    - **Ochre** (#e9c057) - Rich golden yellow
    - **Red** (#c83737) - Deep crimson accent
    - **Deep Green** (#58705c) - Muted forest green
    - **Dark Brown** (#6f5740) - Earthy chocolate
    - **Deep Navy** (#3d4b74) - Sophisticated dark blue

    Each color has both **light** and **dark** variants for different backgrounds.
    """)
    return


@app.cell
def _(apply_dubois_style):
    # Apply Du Bois style globally for all visualizations
    apply_dubois_style(
        cycle="light",
        use_contrast_colors=True,
        show_x_axis=True,
        show_y_axis=True,
    )
    return


@app.cell
def _(mo):
    mo.callout(
        "The style has been applied globally. All plots below use the Du Bois aesthetic with open-source fonts (DejaVu Sans).",
        kind="success",
    )
    return


@app.cell
def _(DUBOIS_FAMILIES, DUBOIS_LIGHT_CYCLE, dubois_legend, np, plt):
    # Create all example visualizations

    # ========== BASIC EXAMPLES ==========


    def create_bar_chart():
        fig, ax = plt.subplots(figsize=(8, 6))

        categories = ["Category A", "Category B", "Category C", "Category D"]
        values = [45, 78, 32, 91]

        # Get colors from the current color cycle
        colors = [prop["color"] for prop in plt.rcParams["axes.prop_cycle"]][
            : len(categories)
        ]

        ax.bar(categories, values, color=colors)
        ax.set_title("Du Bois–Style Bar Chart", fontsize=14, fontweight="bold")
        ax.set_ylabel("Values")

        plt.tight_layout()
        return fig


    def create_line_plot():
        fig, ax = plt.subplots(figsize=(8, 6))

        x = np.linspace(0, 10, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)
        y3 = np.sin(x) * np.cos(x)

        ax.plot(x, y1, label="Series 1")
        ax.plot(x, y2, label="Series 2")
        ax.plot(x, y3, label="Series 3")

        ax.set_title("Du Bois–Style Line Plot", fontsize=14, fontweight="bold")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")

        dubois_legend(ax, outside=True)
        plt.tight_layout()
        return fig


    def create_area_chart():
        fig, ax = plt.subplots(figsize=(8, 6))

        x = np.arange(0, 10)
        y1 = np.array([2, 3, 4, 3, 5, 6, 7, 8, 9, 10])
        y2 = np.array([1, 2, 3, 4, 5, 4, 3, 4, 5, 6])
        y3 = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

        ax.fill_between(x, 0, y1, label="Group 1", alpha=0.7)
        ax.fill_between(x, y1, y1 + y2, label="Group 2", alpha=0.7)
        ax.fill_between(x, y1 + y2, y1 + y2 + y3, label="Group 3", alpha=0.7)

        ax.set_title(
            "Du Bois–Style Stacked Area Chart", fontsize=14, fontweight="bold"
        )
        ax.set_xlabel("Time")
        ax.set_ylabel("Cumulative Value")

        dubois_legend(ax, outside=True)
        plt.tight_layout()
        return fig


    def create_scatter():
        fig, ax = plt.subplots(figsize=(8, 6))

        np.random.seed(42)
        x1 = np.random.normal(5, 1, 50)
        y1 = np.random.normal(5, 1, 50)
        x2 = np.random.normal(7, 1, 50)
        y2 = np.random.normal(7, 1, 50)

        ax.scatter(x1, y1, label="Group 1", alpha=0.7, s=60)
        ax.scatter(x2, y2, label="Group 2", alpha=0.7, s=60)

        ax.set_title("Du Bois–Style Scatter Plot", fontsize=14, fontweight="bold")
        ax.set_xlabel("X Variable")
        ax.set_ylabel("Y Variable")

        dubois_legend(ax, outside=True)
        plt.tight_layout()
        return fig


    def create_horizontal_bar():
        fig, ax = plt.subplots(figsize=(8, 6))

        categories = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        values = [85, 72, 68, 91, 55]

        # Get colors from the current color cycle
        colors = [prop["color"] for prop in plt.rcParams["axes.prop_cycle"]][
            : len(categories)
        ]

        ax.barh(categories, values, color=colors)
        ax.set_title(
            "Du Bois–Style Horizontal Bar Chart", fontsize=14, fontweight="bold"
        )
        ax.set_xlabel("Values")

        plt.tight_layout()
        return fig


    # ========== COMPREHENSIVE MULTI-PLOT ==========


    def create_comprehensive():
        # Sample data
        x = np.arange(1, 6)
        y1 = np.array([3, 4, 2, 5, 4])
        y2 = np.array([2, 3, 3, 2, 1])
        y3 = np.array([1, 2, 1, 3, 2])

        # Create figure with subplots
        fig, axs = plt.subplots(2, 3, figsize=(14, 8))
        (ax_line, ax_bar, ax_stacked), (ax_pie, ax_scatter, ax_box) = axs

        # Line plot
        ax_line.plot(x, y1, marker="o", label="Series A", linewidth=2)
        ax_line.plot(x, y2, marker="o", label="Series B", linewidth=2)
        ax_line.set_title("Line Plot", fontsize=12, fontweight="bold")
        ax_line.set_xlabel("X", fontsize=10)
        ax_line.set_ylabel("Y", fontsize=10)
        dubois_legend(ax_line)

        # Bar chart
        bar_width = 0.35
        ax_bar.bar(x - bar_width / 2, y1, width=bar_width, label="Group A")
        ax_bar.bar(x + bar_width / 2, y2, width=bar_width, label="Group B")
        ax_bar.set_title("Bar Chart", fontsize=12, fontweight="bold")
        ax_bar.set_xlabel("Category", fontsize=10)
        ax_bar.set_ylabel("Value", fontsize=10)
        dubois_legend(ax_bar)

        # Stacked bar chart
        ax_stacked.bar(x, y1, label="Bottom")
        ax_stacked.bar(x, y2, bottom=y1, label="Middle")
        ax_stacked.bar(x, y3, bottom=y1 + y2, label="Top")
        ax_stacked.set_title("Stacked Bar Chart", fontsize=12, fontweight="bold")
        ax_stacked.set_xlabel("Category", fontsize=10)
        ax_stacked.set_ylabel("Total", fontsize=10)
        dubois_legend(ax_stacked)

        # Pie chart
        pie_values = np.array([y1.sum(), y2.sum(), y3.sum()])
        pie_labels = ["A", "B", "C"]
        ax_pie.pie(
            pie_values,
            labels=pie_labels,
            colors=DUBOIS_LIGHT_CYCLE[:3],
            autopct="%1.0f%%",
            textprops={"color": "#111111", "fontsize": 10},
        )
        ax_pie.set_title("Pie Chart", fontsize=12, fontweight="bold")

        # Scatter plot
        rng = np.random.default_rng(0)
        xs = rng.normal(0, 1, 50)
        ys = rng.normal(0, 1, 50)
        ax_scatter.scatter(xs, ys, alpha=0.8, s=60)
        ax_scatter.set_title("Scatter Plot", fontsize=12, fontweight="bold")
        ax_scatter.set_xlabel("X", fontsize=10)
        ax_scatter.set_ylabel("Y", fontsize=10)

        # Box plot
        data = [
            rng.normal(0, 1, 100),
            rng.normal(1.5, 0.5, 100),
            rng.normal(-1, 0.7, 100),
        ]
        bp = ax_box.boxplot(
            data,
            patch_artist=True,
            labels=["Set 1", "Set 2", "Set 3"],
        )

        for patch, color in zip(bp["boxes"], DUBOIS_LIGHT_CYCLE):
            patch.set_facecolor(color)

        ax_box.set_title("Box Plot", fontsize=12, fontweight="bold")

        # Overall title and layout
        fig.suptitle(
            "Comprehensive Du Bois Style Examples",
            fontsize=16,
            fontweight="bold",
            y=0.98,
        )
        fig.tight_layout(rect=[0, 0, 1, 0.96])
        fig.patch.set_alpha(0.0)

        return fig


    # ========== COLOR PALETTE SHOWCASE ==========


    def create_palette_showcase():
        # Prepare data using all seven color families
        labels = list(DUBOIS_FAMILIES.keys())
        colors = [DUBOIS_FAMILIES[name]["light"] for name in labels]
        x = np.arange(len(labels))
        values = np.linspace(1, 7, len(labels))

        # Create figure with three visualization types
        fig, (ax_bar, ax_pie, ax_line) = plt.subplots(1, 3, figsize=(15, 5))

        # Horizontal bar chart showing all 7 colors
        ax_bar.barh(x, values, color=colors)
        ax_bar.set_yticks(x)
        ax_bar.set_yticklabels(labels, fontsize=9)
        ax_bar.set_xlabel("Value", fontsize=10)
        ax_bar.set_title("All 7 Colors (Bar)", fontsize=12, fontweight="bold")

        # Pie chart showing all 7 colors
        ax_pie.pie(
            values,
            labels=None,
            colors=colors,
            autopct="%1.0f%%",
            textprops={"color": "#111111", "fontsize": 9},
        )
        ax_pie.set_title("All 7 Colors (Pie)", fontsize=12, fontweight="bold")

        # Legend mapping colors to labels
        legend_handles = [
            plt.Line2D(
                [],
                [],
                marker="o",
                linestyle="None",
                color=c,
                label=lab,
                markersize=10,
            )
            for lab, c in zip(labels, colors)
        ]
        ax_pie.legend(
            handles=legend_handles,
            loc="center left",
            bbox_to_anchor=(1.05, 0.5),
            frameon=False,
            fontsize=9,
        )

        # Line plot with 7 colored points
        for i, (lab, c) in enumerate(zip(labels, colors)):
            ax_line.plot(
                i + 1,
                values[i],
                marker="o",
                markersize=10,
                linestyle="None",
                color=c,
                label=lab,
            )

        ax_line.set_xlim(0.5, len(labels) + 0.5)
        ax_line.set_xticks(range(1, len(labels) + 1))
        ax_line.set_xlabel("Category Index", fontsize=10)
        ax_line.set_ylabel("Value", fontsize=10)
        ax_line.set_title("All 7 Colors (Points)", fontsize=12, fontweight="bold")

        # Overall title and layout
        fig.suptitle(
            "Du Bois Palette – All Seven Colors",
            fontsize=16,
            fontweight="bold",
            y=0.98,
        )
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        fig.patch.set_alpha(0.0)

        return fig


    # Return all functions for use in other cells
    return (
        create_area_chart,
        create_bar_chart,
        create_comprehensive,
        create_horizontal_bar,
        create_line_plot,
        create_palette_showcase,
        create_scatter,
    )


@app.cell
def _(
    create_area_chart,
    create_bar_chart,
    create_horizontal_bar,
    create_line_plot,
    create_scatter,
    mo,
):
    basic_examples = mo.vstack(
        [
            mo.hstack(
                [create_bar_chart(), create_line_plot()], widths="equal", gap=1.0
            ),
            mo.hstack(
                [create_area_chart(), create_scatter()], widths="equal", gap=1.0
            ),
            create_horizontal_bar(),
        ],
        gap=1.5,
    )
    return (basic_examples,)


@app.cell
def _(mo):
    mo.md(r"""
    ---

    ## Gallery Sections

    Explore different aspects of the Du Bois style through the tabs below.
    """)
    return


@app.cell
def _(
    apply_dubois_style,
    basic_examples,
    create_comprehensive,
    create_palette_showcase,
    mo,
    np,
    plt,
):
    # Create style configuration examples


    def style_light_sequential():
        apply_dubois_style(
            cycle="light",
            use_contrast_colors=False,
            show_x_axis=False,
            show_y_axis=False,
        )

        fig, ax = plt.subplots(figsize=(8, 5))

        categories = ["A", "B", "C", "D", "E"]
        values = [45, 67, 32, 78, 54]

        colors = [prop["color"] for prop in plt.rcParams["axes.prop_cycle"]][
            : len(categories)
        ]

        ax.bar(categories, values, color=colors)
        ax.set_title(
            "Light Cycle, Sequential Colors, No Axes",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )

        plt.tight_layout()
        return fig


    def style_light_contrast():
        apply_dubois_style(
            cycle="light",
            use_contrast_colors=True,
            show_x_axis=True,
            show_y_axis=True,
        )

        fig, ax = plt.subplots(figsize=(8, 5))

        x = np.linspace(0, 10, 100)
        for i in range(4):
            ax.plot(
                x, np.sin(x + i * np.pi / 4), label=f"Series {i + 1}", linewidth=2
            )

        ax.set_title(
            "Light Cycle, High Contrast, Axes Visible",
            fontsize=14,
            fontweight="bold",
        )
        ax.set_xlabel("X Axis", fontsize=11)
        ax.set_ylabel("Y Axis", fontsize=11)
        ax.legend(loc="upper right", frameon=False)

        plt.tight_layout()
        return fig


    def style_dark_contrast():
        apply_dubois_style(
            cycle="dark",
            use_contrast_colors=True,
            show_x_axis=True,
            show_y_axis=True,
        )

        fig, ax = plt.subplots(figsize=(8, 5))

        categories = ["Q1", "Q2", "Q3", "Q4"]
        revenue = [120, 145, 178, 165]
        expenses = [80, 95, 110, 105]

        x = np.arange(len(categories))
        width = 0.35

        ax.bar(x - width / 2, revenue, width, label="Revenue")
        ax.bar(x + width / 2, expenses, width, label="Expenses")

        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.set_title(
            "Dark Cycle, High Contrast, Axes Visible",
            fontsize=14,
            fontweight="bold",
        )
        ax.set_xlabel("Quarter", fontsize=11)
        ax.set_ylabel("Amount ($K)", fontsize=11)
        ax.legend(loc="upper left", frameon=False)

        plt.tight_layout()
        return fig


    def style_dark_sequential():
        apply_dubois_style(
            cycle="dark",
            use_contrast_colors=False,
            show_x_axis=False,
            show_y_axis=False,
        )

        fig, ax = plt.subplots(figsize=(8, 5))

        x = np.arange(0, 10, 0.5)
        y1 = np.sin(x) + 3
        y2 = np.cos(x) + 2
        y3 = np.sin(x * 0.5) + 1

        ax.fill_between(x, 0, y1, alpha=0.7, label="Layer 1")
        ax.fill_between(x, y1, y1 + y2, alpha=0.7, label="Layer 2")
        ax.fill_between(x, y1 + y2, y1 + y2 + y3, alpha=0.7, label="Layer 3")

        ax.set_title(
            "Dark Cycle, Sequential Colors, No Axes",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        ax.legend(loc="upper right", frameon=False)

        plt.tight_layout()
        return fig


    # Create tabs to organize all examples
    gallery_tabs = mo.ui.tabs(
        {
            "📊 Basic Examples": mo.vstack(
                [
                    mo.md("""
            ### Basic Chart Types

            These examples demonstrate the Du Bois style applied to common chart types. Each uses authentic historical colors and minimal styling.

            **Features:**
            - Authentic Du Bois color palette (earthy tones)
            - Clean, minimal axes
            - Outside legends for clarity
            - Transparent backgrounds
            """),
                    basic_examples,
                ],
                gap=1.0,
            ),
            "🎨 Comprehensive": mo.vstack(
                [
                    mo.md("""
            ### Multi-Plot Showcase

            A comprehensive example showing **six different visualization types** in a single figure:
            - Line plot, bar chart, stacked bar chart
            - Pie chart, scatter plot, box plot

            This demonstrates the versatility of the Du Bois palette across diverse chart types.
            """),
                    create_comprehensive(),
                ],
                gap=1.0,
            ),
            "🌈 Color Palette": mo.vstack(
                [
                    mo.md("""
            ### Complete Color Palette

            All **seven Du Bois color families** displayed in three different chart types:

            1. **Horizontal Bar** - Shows each color with its family name
            2. **Pie Chart** - Displays color proportions with legend
            3. **Point Plot** - Individual colored markers

            The palette includes: Warm Tan, Dusty Pink, Ochre, Red, Deep Green, Dark Brown, and Deep Navy.
            """),
                    create_palette_showcase(),
                ],
                gap=1.0,
            ),
            "⚙️ Style Configurations": mo.vstack(
                [
                    mo.md("""
            ### Style Toggle Options

            The `apply_dubois_style()` function offers several configuration options:

            - **`cycle`**: `"light"` or `"dark"` - Choose color palette variant
            - **`use_contrast_colors`**: `True` = categorical/distinct, `False` = sequential
            - **`show_x_axis`** / **`show_y_axis`**: Control axis visibility

            Below are four different configurations demonstrating the flexibility of the style.
            """),
                    mo.accordion(
                        {
                            "Light Cycle, Sequential, No Axes": mo.vstack(
                                [
                                    mo.md(
                                        "**Configuration:** `cycle='light'`, `use_contrast_colors=False`, axes hidden"
                                    ),
                                    style_light_sequential(),
                                ]
                            ),
                            "Light Cycle, High Contrast, Axes Visible": mo.vstack(
                                [
                                    mo.md(
                                        "**Configuration:** `cycle='light'`, `use_contrast_colors=True`, axes visible"
                                    ),
                                    style_light_contrast(),
                                ]
                            ),
                            "Dark Cycle, High Contrast, Axes Visible": mo.vstack(
                                [
                                    mo.md(
                                        "**Configuration:** `cycle='dark'`, `use_contrast_colors=True`, axes visible"
                                    ),
                                    style_dark_contrast(),
                                ]
                            ),
                            "Dark Cycle, Sequential, No Axes": mo.vstack(
                                [
                                    mo.md(
                                        "**Configuration:** `cycle='dark'`, `use_contrast_colors=False`, axes hidden"
                                    ),
                                    style_dark_sequential(),
                                ]
                            ),
                        }
                    ),
                ],
                gap=1.0,
            ),
            "ℹ️ About": mo.md("""
        ### About This Gallery

        This gallery showcases the **dubois-style** package for creating data visualizations inspired by W.E.B. Du Bois' groundbreaking work at the 1900 Paris Exposition.

        #### Historical Context

        W.E.B. Du Bois was a pioneering Black scholar and civil-rights intellectual whose innovative data visualizations combined rigorous social science with artistic excellence. His hand-colored charts used carefully chosen earthy tones to communicate complex demographic data about African Americans in the post-Reconstruction era.

        #### Package Features

        - **Authentic color palettes** - Muted, earthy tones faithful to the original visualizations
        - **Open-source fonts** - Uses DejaVu Sans (no proprietary fonts required)
        - **Flexible styling** - Light/dark cycles, categorical/sequential colors, axis control
        - **Modern Python** - Built on matplotlib with marimo for interactive notebooks

        #### Color Philosophy

        The seven-color palette captures the aesthetic of early 20th-century hand-colored visualizations:
        - Warm, inviting tones (Warm Tan, Dusty Pink, Ochre)
        - Deep, sophisticated accents (Red, Deep Green, Dark Brown, Deep Navy)
        - Both light and dark variants for different backgrounds

        #### Installation

        ```bash
        pip install "git+https://github.com/Shakes-tzd/dubois-style.git"
        ```

        #### Basic Usage

        ```python
        from dubois_style import apply_dubois_style
        import matplotlib.pyplot as plt

        # Apply the style
        apply_dubois_style(cycle="light", use_contrast_colors=True)

        # Create your plots
        fig, ax = plt.subplots()
        ax.bar(['A', 'B', 'C'], [10, 20, 15])
        plt.show()
        ```

        #### Resources

        - [Du Bois Challenge](https://duboischallenge.com/)
        - [W.E.B. Du Bois' Data Portraits](https://www.princeton.edu/news/2018/11/13/we-b-du-boiss-data-portraits-visualizing-black-america)
        - [GitHub Repository](https://github.com/Shakes-tzd/dubois-style)
        """),
        },
        value="📊 Basic Examples",
    )
    return (gallery_tabs,)


@app.cell
def _(gallery_tabs):
    gallery_tabs


@app.cell
def _(mo):
    mo.md(r"""
    ---

    ## Next Steps

    - **Try it yourself**: Modify the style parameters and see the results
    - **Explore the code**: Each example is defined as a Python function above
    - **Read the docs**: Check out the GitHub repository for full documentation
    - **Create your own**: Use the Du Bois style in your own matplotlib visualizations

    ---

    _Gallery created with [marimo](https://marimo.io) - A reactive Python notebook_
    """)
    return


if __name__ == "__main__":
    app.run()
