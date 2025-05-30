# -*- coding: utf-8 -*-
"""
This script extracts a ZIP file containing world administrative boundaries,
loads the shapefile, and plots a map of major aquifer regions with their depletion rates. It also generates a dual-axis
bar chart showing the depletion rates in mm/year and km³/year for each aquifer region. The map is saved as a
high-resolution PNG file, and the dual-axis chart is also saved as a high-resolution image.

The depletion rates (depth depletion in mm/year and volume depletion in km³/year) are based on
Famiglietti, J. S. (2014). The global groundwater crisis. Nature Climate Change, 4(11), 945–948. https://doi.org/10.1038/nclimate2425

Author: Mr. Santanu Banerjee (bane7352@vandals.uidaho.edu)
Modified by: Dr. Sayantan Majumdar (sayantan.majumdar@dri.edu)
"""

import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import zipfile
import os

# ── Extract ZIP ──
zip_path = "Data/world-administrative-boundaries.zip"
extract_root = "Data/wb_countries_extracted"
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_root)

# ── Locate .shp file ──
shapefile_path = ""
for root, dirs, files in os.walk(extract_root):
    for file in files:
        if file.endswith(".shp"):
            shapefile_path = os.path.join(root, file)

# ── Load shapefile ──
gdf = gpd.read_file(shapefile_path)

# ── Final Aquifer Coordinates ──
regions = {
    "Northwest Sahara": {"coord": (10, 26), "label": (-20, 22)},
    "California Central Valley": {"coord": (-120, 37), "label": (-140, 27)},
    "High Plains (Ogallala)": {"coord": (-100, 39), "label": (-90, 52)},
    "Guarani": {"coord": (-55, -25), "label": (-35, -35)},
    "Northern Middle East": {"coord": (44, 34), "label": (44, 47)},
    "Arabian": {"coord": (50, 20), "label": (65, 10)},
    "Northwestern India": {"coord": (73, 28), "label": (83, 20)},
    "North China Plain": {"coord": (116, 36), "label": (135, 42)},
    "Canning Basin": {"coord": (122, -22), "label": (140, -32)},
}

region_colors = {
    "Northwest Sahara": "#1f78b4",
    "California Central Valley": "#33a02c",
    "High Plains (Ogallala)": "#e31a1c",
    "Guarani": "#ff7f00",
    "Northern Middle East": "#6a3d9a",
    "Arabian": "#b15928",
    "Northwestern India": "#a6cee3",
    "North China Plain": "#fb9a99",
    "Canning Basin": "#fdbf6f"
}

# ── Plot Settings ──
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 14
plt.rcParams["font.weight"] = "bold"

fig, ax = plt.subplots(figsize=(20, 10))  # Don't set dpi here

# Plot base world map
gdf.plot(ax=ax, facecolor='white', edgecolor='black', linewidth=0.8)

# Add aquifer markers and arrows
for region, data in regions.items():
    x, y = data["coord"]
    lx, ly = data["label"]
    ax.plot(x, y, 'o', color=region_colors[region], markersize=30, zorder=5)
    ax.annotate(region, xy=(x, y), xytext=(lx, ly),
                fontsize=14, fontweight='bold', color='black',
                ha='center',
                arrowprops=dict(arrowstyle="->", color='black', lw=1.5,
                                connectionstyle="arc3,rad=0.2"))

# Add legend
legend_elements = [Patch(facecolor=color, edgecolor='black', label=region)
                   for region, color in region_colors.items()]
ax.legend(handles=legend_elements, loc='lower left', fontsize=12,
          title="Major Aquifer Regions", title_fontsize=14, frameon=True)

# Final layout
ax.axis('off')
plt.tight_layout()

# Save BEFORE plt.show()
save_path = "Data/global_aquifers_map_900dpi.png"
fig.savefig(save_path, dpi=900, bbox_inches='tight', facecolor='white')

# Show the map
plt.show()

print(f"Map saved successfully at: {save_path}")

import matplotlib.pyplot as plt
import numpy as np

# Aquifer names and time period
regions = [
    "Northwest Sahara\n(2003–2013)", "California Central Valley\n(2003–2010)",
    "High Plains (Ogallala)\n(2003–2013)", "Guarani\n(2003–2009)",
    "Northern Middle East\n(2003–2009)", "Arabian\n(2003–2013)",
    "Northwestern India\n(2002–2008)", "North China Plain\n(2003–2010)",
    "Canning Basin\n(2003–2013)"
]

# Accurate depletion rates from Table 1
mm_per_year = [2.8, 20.4, 27.6, 0.6, 17.3, 9.1, 40.0, 22.0, 9.4]
km3_per_year = [2.7, 3.1, 12.5, 1.0, 13.0, 15.5, 17.7, 8.3, 3.6]

x = np.arange(len(regions))
width = 0.35

# Create high-resolution figure
fig, ax1 = plt.subplots(figsize=(14, 6), dpi=600)

# Left Y-axis: mm/year
bar1 = ax1.bar(x - width/2, mm_per_year, width, label='mm/year', color='royalblue')
ax1.set_ylabel('Depletion Rate (mm/year)', fontsize=14, fontweight='bold')
ax1.tick_params(axis='y', labelsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(regions, rotation=45, ha='right', fontsize=12, fontweight='bold')

# Right Y-axis: km³/year
ax2 = ax1.twinx()
bar2 = ax2.bar(x + width/2, km3_per_year, width, label='km³/year', color='indianred')
ax2.set_ylabel('Depletion Rate (km³/year)', fontsize=14, fontweight='bold', color='brown')
ax2.tick_params(axis='y', labelsize=12, colors='brown')

# Add legends
ax1.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.grid(False)

# Save 900 DPI image
plt.savefig("Data/aquifer_depletion_dual_axis_corrected.png", dpi=900, bbox_inches='tight')
plt.show()


