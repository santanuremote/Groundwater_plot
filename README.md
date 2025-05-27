# Groundwater Potential Zone Mapping for Sustainable Water Management in India

### Description
Given India's reliance on groundwater and the challenges of depletion and climatic stress, scientifically robust groundwater potential zone (GWPZ) mapping is critical. 
This paper reviews Indian GWPZ research, highlighting a methodological shift from traditional multi-criteria decision-making models towards advanced machine learning techniques, with validation commonly using ROC/AUC metrics. 
Despite these advancements, regional data heterogeneity, aquifer complexity, and climatic variability continue to pose significant challenges. 
The paper advocates for future strategies like high-resolution datasets and 3D subsurface modeling to improve sustainable groundwater management in India.

<center> <img src=https://github.com/user-attachments/assets/e9f7b3aa-8936-4cb4-9133-d6b23a24e2ec height="600"/> </center>


### Citation

Banerjee, S., Majumdar, S., Saha, J., Kukal, M. S., Thakur, P. K., Rathore, V. S., Kaushik, P. R., Talukdar, G., Misra, D., & Ndehedehe, C. (2025). Groundwater Potential Zone Mapping for Sustainable Water Management in India: A Systematic Review of Methods, Validation Techniques, and Future Directions. _Under review in [Cambridge Prisms Drylands](https://www.cambridge.org/core/journals/cambridge-prisms-drylands/information/about-this-journal)_.  


#### Global Aquifer Location Map
This world map highlights the geographic distribution of nine major aquifer systems using color-coded markers. Each aquifer is labeled clearly, and a legend is provided for visual reference. It provides a spatial understanding of where critical groundwater reserves are located globally.

#### Dual-Axis Depletion Rate Chart
This bar chart compares depletion rates of those aquifers in two forms: blue bars indicate the depth lost per year (mm/year), while red bars show the total volume depleted per year (km³/year). It reveals that Northwestern India and the Ogallala Aquifer experience the most severe groundwater loss both in depth and volume.

![42788653-dce9-466b-8659-b1ba5a2e9508](https://github.com/user-attachments/assets/2bf6aa6b-fd86-414e-86c5-eea01f3e519d)
![plot 1](https://github.com/user-attachments/assets/30198833-713b-4e11-98a2-306905554185)



#### Running the Code
To run the code, ensure you have the required libraries installed. You can install them using the terminal commands below.
```
conda create -n gwpz python=3.12
conda activate gwpz
conda install -c conda-forge -y geopandas matplotlib seaborn
python groundwater_plot.py

