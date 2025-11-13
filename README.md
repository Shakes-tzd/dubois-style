# dubois-style

A W.E.B. Du Bois–inspired Matplotlib style and color palette for creating data visualizations that honor the legacy of Du Bois' groundbreaking 1900 Paris Exposition visualizations.

## About

This package provides a Matplotlib style inspired by W.E.B. Du Bois' data visualizations created for the 1900 Paris Exposition. Du Bois was a pioneering Black scholar and civil-rights intellectual whose innovative approach to data visualization continues to influence modern data visualization practice.

**Important:** This package is an independent tribute to Du Bois' work. We are not affiliated with Du Bois' estate or any institution. The package name "dubois-style" is used descriptively to indicate a visualization style inspired by his work, not as an official representation.

## Installation

Install directly from GitHub:

```bash
pip install "git+https://github.com/yourname/dubois-style.git"
```

Or clone the repository and install in development mode:

```bash
git clone https://github.com/yourname/dubois-style.git
cd dubois-style
pip install -e .
```

## Quick Start

```python
import matplotlib.pyplot as plt
from dubois_style import apply_dubois_style

# Apply the Du Bois style globally
apply_dubois_style(
    cycle="light",
    use_contrast_colors=True,
    show_x_axis=True,
    show_y_axis=True,
)

# Create your plots
fig, ax = plt.subplots()
ax.bar(['A', 'B', 'C'], [10, 20, 15])
plt.show()
```

## Features

- **Du Bois–inspired color palettes**: Rich, contrasting colors inspired by the 1900 Paris Exposition visualizations
- **Flexible styling**: Support for light and dark backgrounds, categorical and sequential color schemes
- **Clean aesthetics**: Transparent backgrounds, minimal axes, and elegant typography defaults
- **Font flexibility**: Support for custom fonts while defaulting to open-source alternatives

## Fonts

This package uses **open-source fonts by default** to ensure legal compliance and universal accessibility.

### Default Font: DejaVu Sans

By default, `dubois-style` uses **DejaVu Sans**, which is:
- ✅ Pre-installed with matplotlib (no setup required)
- ✅ Open-source and freely redistributable
- ✅ Excellent readability for data visualizations

```python
# Uses DejaVu Sans by default - works out of the box!
apply_dubois_style(cycle="light", use_contrast_colors=True)
```

### Open-Source Font Alternatives

You can easily switch to other open-source fonts:

```python
# Use Liberation Sans (often pre-installed)
apply_dubois_style(base_font="Liberation Sans")

# Use Libre Franklin with fallback chain
apply_dubois_style(base_font=["Libre Franklin", "DejaVu Sans"])

# Use Public Sans (requires installation)
apply_dubois_style(base_font=["Public Sans", "DejaVu Sans"])
```

### Using Custom Fonts

If you have custom fonts or licensed fonts (like Malgun Gothic or Franklin Gothic), register them:

```python
apply_dubois_style(
    base_font="Franklin Gothic",
    custom_font_paths=["/path/to/FranklinGothic.ttf"],
)
```

**📖 For detailed font information, installation guides, and recommendations, see [FONTS.md](FONTS.md)**

## Usage

### Basic Usage

```python
from dubois_style import apply_dubois_style
import matplotlib.pyplot as plt

apply_dubois_style(cycle="light")
fig, ax = plt.subplots()
# Your plotting code here
```

### Color Cycles

Choose between light and dark color cycles:

```python
# For light backgrounds
apply_dubois_style(cycle="light")

# For dark backgrounds
apply_dubois_style(cycle="dark")
```

### Categorical vs Sequential Colors

```python
# High-contrast categorical colors (for distinct categories)
apply_dubois_style(use_contrast_colors=True)

# Sequential colors (for ordered data)
apply_dubois_style(use_contrast_colors=False)
```

### Axes Configuration

```python
# Show both axes
apply_dubois_style(show_x_axis=True, show_y_axis=True)

# Hide axes (Du Bois style)
apply_dubois_style(show_x_axis=False, show_y_axis=False)
```

### Using Color Palettes Directly

```python
from dubois_style import DUBOIS_LIGHT_CYCLE, DUBOIS_FAMILIES

# Use colors directly in plots
colors = DUBOIS_LIGHT_CYCLE
ax.plot(x, y, color=colors[0])  # Warm Tan
ax.plot(x, y2, color=colors[1])  # Dusty Pink

# Access color families (dict with "light" and "dark" variants)
warm_tan_light = DUBOIS_FAMILIES["Warm Tan"]["light"]  # #d6c1ab
warm_tan_dark = DUBOIS_FAMILIES["Warm Tan"]["dark"]    # #b69c7e
```

### Custom Legends

```python
from dubois_style import dubois_legend

fig, ax = plt.subplots()
ax.plot([1, 2, 3], label="Series 1")
ax.plot([2, 3, 4], label="Series 2")

# Create a legend outside the axes
dubois_legend(ax, outside=True)
```

## Marimo Notebooks

This package includes interactive marimo notebooks demonstrating the style:

- **`notebooks/gallery.py`** — Gallery of different chart types
- **`notebooks/maps.py`** — Example inspired by Du Bois' "Georgia Negro" map

### Running Marimo Notebooks

Install marimo and the docs dependencies:

```bash
pip install -e ".[docs]"
```

Then run the notebooks:

```bash
# Edit mode
marimo edit notebooks/gallery.py

# Run as app
marimo run notebooks/gallery.py
```

### Exporting as HTML

Export notebooks as interactive HTML:

```bash
marimo export html-wasm notebooks/gallery.py -o site --mode run
```

## API Reference

### `apply_dubois_style()`

Apply Du Bois–inspired styling globally to matplotlib.

**Parameters:**
- `cycle` (str): Color cycle to use — `"light"` or `"dark"` (default: `"light"`)
- `use_contrast_colors` (bool): Use high-contrast categorical colors (default: `False`)
- `show_x_axis` (bool): Show x-axis spine and ticks (default: `False`)
- `show_y_axis` (bool): Show y-axis spine and ticks (default: `False`)
- `base_font` (str | list[str]): Font family or fallback chain (default: `"DejaVu Sans"`)
- `custom_font_paths` (list[str] | None): Optional paths to custom font files to register

### `dubois_legend()`

Create a Du Bois–style legend.

**Parameters:**
- `ax`: Matplotlib axes object
- `outside` (bool): Place legend outside axes (default: `True`)
- `outside_pad` (float): Padding when outside (default: `0.02`)
- Additional arguments passed to `ax.legend()`

### Color Palettes

- `DUBOIS_LIGHT_CYCLE`: List of hex colors for light backgrounds (7 colors)
- `DUBOIS_DARK_CYCLE`: List of hex colors for dark backgrounds (7 colors)
- `DUBOIS_CATEGORICAL_CYCLE`: List of high-contrast categorical hex colors (7 colors)
- `DUBOIS_FAMILIES`: Dictionary of color families with "light" and "dark" variants
  - Keys: `"Warm Tan"`, `"Dusty Pink"`, `"Ochre"`, `"Red"`, `"Deep Green"`, `"Dark Brown"`, `"Deep Navy"`
  - Each value is a dict with `"light"` and `"dark"` keys containing hex colors
- `DUBOIS_COLORS_LIGHT`: Dictionary mapping color names to light hex values
- `DUBOIS_COLORS_DARK`: Dictionary mapping color names to dark hex values

## Examples

See the `notebooks/` directory for complete examples, or check out the gallery:

```bash
marimo edit notebooks/gallery.py
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License — see LICENSE file for details.

## Acknowledgments

This package is inspired by W.E.B. Du Bois' groundbreaking data visualizations created for the 1900 Paris Exposition. We acknowledge his contributions to data visualization and social science, and we aim to honor his legacy through this tribute.

For more information about Du Bois' visualizations, see:
- [The Du Bois Challenge](https://duboischallenge.com/)
- [W.E.B. Du Bois' Data Portraits](https://www.princeton.edu/news/2018/11/13/we-b-du-boiss-data-portraits-visualizing-black-america)

## Citation

If you use this package in your work, please consider citing it:

```bibtex
@software{dubois_style,
  title = {dubois-style: A W.E.B. Du Bois–inspired Matplotlib style},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/yourname/dubois-style}
}
```


