"""Comprehensive test of dubois-style package."""

import matplotlib.pyplot as plt
import numpy as np
from dubois_style import (
    apply_dubois_style,
    dubois_legend,
    DUBOIS_LIGHT_CYCLE,
    DUBOIS_DARK_CYCLE,
    DUBOIS_CATEGORICAL_CYCLE,
    DUBOIS_FAMILIES,
)

print("Testing dubois-style package...")
print("=" * 50)

# Test 1: Import all components
print("\n1. Testing imports...")
assert len(DUBOIS_LIGHT_CYCLE) > 0
assert len(DUBOIS_DARK_CYCLE) > 0
assert len(DUBOIS_CATEGORICAL_CYCLE) > 0
assert "blue" in DUBOIS_FAMILIES
print("   ✓ All imports successful")

# Test 2: Apply light style
print("\n2. Testing apply_dubois_style (light cycle)...")
apply_dubois_style(cycle="light", show_x_axis=True, show_y_axis=True)
assert plt.rcParams["figure.facecolor"] == "none"
assert plt.rcParams["axes.facecolor"] == "none"
print("   ✓ Light style applied correctly")

# Test 3: Apply dark style
print("\n3. Testing apply_dubois_style (dark cycle)...")
apply_dubois_style(cycle="dark", use_contrast_colors=False)
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
assert len(colors) > 0
print(f"   ✓ Dark style applied with {len(colors)} colors")

# Test 4: Test categorical colors
print("\n4. Testing categorical colors...")
apply_dubois_style(cycle="light", use_contrast_colors=True)
categorical_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
assert len(categorical_colors) >= len(DUBOIS_LIGHT_CYCLE)
print(f"   ✓ Categorical colors applied ({len(categorical_colors)} colors)")

# Test 5: Create a plot with legend
print("\n5. Testing plot creation and legend...")
fig, ax = plt.subplots(figsize=(6, 4))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label="Sine")
ax.plot(x, np.cos(x), label="Cosine")
legend = dubois_legend(ax, outside=True)
assert legend is not None
print("   ✓ Plot and legend created successfully")
plt.close(fig)

# Test 6: Test color families
print("\n6. Testing color families...")
assert DUBOIS_FAMILIES["blue"] == "#2E86AB"
assert DUBOIS_FAMILIES["red"] == "#A23B72"
print("   ✓ Color families accessible")

# Test 7: Test font fallback (no custom fonts)
print("\n7. Testing font fallback...")
apply_dubois_style(base_font="DejaVu Sans", title_font="DejaVu Sans")
# matplotlib stores font.family as a list
font_family = plt.rcParams["font.family"]
assert "DejaVu Sans" in (font_family if isinstance(font_family, list) else [font_family])
print("   ✓ Font fallback works correctly")

print("\n" + "=" * 50)
print("✓ All tests passed!")
print("=" * 50)

