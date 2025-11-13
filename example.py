"""Simple example demonstrating dubois-style usage."""

import matplotlib.pyplot as plt
from dubois_style import apply_dubois_style, dubois_legend

# Apply Du Bois style with default open-source fonts
apply_dubois_style(
    cycle="light",
    use_contrast_colors=True,
    show_x_axis=True,
    show_y_axis=True,
    base_font="DejaVu Sans",  # Default: always available with matplotlib
)

# Create a simple bar chart
fig, ax = plt.subplots(figsize=(8, 6))

categories = ["Category A", "Category B", "Category C", "Category D"]
values = [45, 78, 32, 91]

bars = ax.bar(categories, values)
ax.set_title("Du Bois–Style Bar Chart", fontsize=14, fontweight="bold")
ax.set_ylabel("Values")

plt.tight_layout()
plt.savefig("example_output.png", dpi=150, bbox_inches="tight")
print("Example plot saved as 'example_output.png'")
plt.show()


