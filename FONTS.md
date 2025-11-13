# Font Guide for Du Bois Style

This package uses **open-source fonts** to ensure legal compliance and universal accessibility.

## Default Font: DejaVu Sans

By default, `dubois-style` uses **DejaVu Sans**, which is:
- ✅ **Pre-installed** with matplotlib (no setup required)
- ✅ **Open-source** (redistributable, no licensing issues)
- ✅ **Highly readable** in data visualizations
- ✅ **Comprehensive** character coverage (Latin, Greek, Cyrillic, etc.)

```python
from dubois_style import apply_dubois_style

# Uses DejaVu Sans by default
apply_dubois_style(cycle="light", use_contrast_colors=True)
```

## Why Not Malgun Gothic or Franklin Gothic?

Earlier versions referenced **Malgun Gothic** and **Franklin Gothic**, but these are **proprietary fonts**:
- ❌ Malgun Gothic: Microsoft font (requires Windows license)
- ❌ Franklin Gothic: Commercial font (requires purchase/license)
- ❌ Cannot be redistributed with open-source packages
- ❌ Not available on all systems

## Recommended Open-Source Alternatives

### 1. DejaVu Sans (Default)
**Best for**: Universal compatibility, zero setup
```python
apply_dubois_style(base_font="DejaVu Sans")
```

### 2. Liberation Sans
**Best for**: Arial/Helvetica alternative (metric-compatible)
- Often pre-installed on Linux systems
- Install: `apt install fonts-liberation` (Ubuntu/Debian)

```python
apply_dubois_style(base_font="Liberation Sans")
```

### 3. Libre Franklin (Franklin Gothic Alternative)
**Best for**: Geometric sans-serif, similar to Franklin Gothic
- Download from [Google Fonts](https://fonts.google.com/specimen/Libre+Franklin)
- Install: `apt install fonts-librefranklin` (Ubuntu/Debian)

```python
# Use with fallback to DejaVu Sans
apply_dubois_style(base_font=["Libre Franklin", "DejaVu Sans"])
```

### 4. Public Sans (U.S. Government Font)
**Best for**: Modern, clean sans-serif
- Download from [Google Fonts](https://fonts.google.com/specimen/Public+Sans)
- Developed by the U.S. Web Design System

```python
apply_dubois_style(base_font=["Public Sans", "DejaVu Sans"])
```

## Font Fallback Chain

Matplotlib supports font fallback chains. If the first font isn't available, it tries the next:

```python
apply_dubois_style(
    base_font=[
        "Libre Franklin",    # Preferred (if installed)
        "Liberation Sans",   # Fallback 1
        "DejaVu Sans",       # Fallback 2 (always available)
        "sans-serif"         # System default
    ]
)
```

## Using Custom Fonts

If you have custom fonts (licensed or downloaded), register them:

```python
apply_dubois_style(
    base_font="My Custom Font",
    custom_font_paths=[
        "/path/to/CustomFont-Regular.ttf",
        "/path/to/CustomFont-Bold.ttf",
    ]
)
```

## Historical Context

W.E.B. Du Bois' original 1900 Paris Exposition visualizations likely used:
- **Hand-lettering** (common in the early 1900s)
- **Early American type foundry fonts** (Franklin Gothic was released in 1902)
- **Engraving techniques** for titles and labels

Our modern open-source fonts capture the same aesthetic principles:
- ✓ Clean, legible sans-serif letterforms
- ✓ Strong geometric construction
- ✓ Excellent readability at small sizes
- ✓ Professional appearance suitable for data visualization

## Installation Guide

### Ubuntu/Debian
```bash
# Liberation Sans (often pre-installed)
sudo apt install fonts-liberation

# Libre Franklin
sudo apt install fonts-librefranklin

# Or download from Google Fonts
wget https://fonts.google.com/download?family=Libre%20Franklin
```

### macOS
```bash
# Using Homebrew
brew install font-libre-franklin
brew install font-liberation-sans
```

### Windows
- Download fonts from [Google Fonts](https://fonts.google.com/)
- Right-click → Install for all users
- Restart Python/matplotlib

### Python Package (Alternative)
```bash
# pyfonts package can download Google Fonts
pip install pyfonts
```

```python
from pyfonts import load_google_font
load_google_font('Libre Franklin')
```

## Verifying Installed Fonts

Check which fonts matplotlib can see:

```python
import matplotlib.font_manager as fm

# List all available fonts
fonts = [f.name for f in fm.fontManager.ttflist]
print(sorted(set(fonts)))

# Check if specific font is available
if "Libre Franklin" in fonts:
    print("✓ Libre Franklin is available")
else:
    print("✗ Libre Franklin not found - will use fallback")
```

## Summary

| Font | Type | Availability | Setup Required |
|------|------|--------------|----------------|
| **DejaVu Sans** | Default | ✅ Always (bundled with matplotlib) | None |
| **Liberation Sans** | Alternative | ✅ Usually (pre-installed on Linux) | Minimal |
| **Libre Franklin** | Premium | ⚠️ Requires installation | Download/install |
| **Public Sans** | Premium | ⚠️ Requires installation | Download/install |
| Malgun Gothic | Proprietary | ❌ Microsoft license required | Not supported |
| Franklin Gothic | Proprietary | ❌ Commercial license required | Not supported |

**Recommendation**: Start with the default (DejaVu Sans). If you want enhanced styling, install Libre Franklin and use a fallback chain.
