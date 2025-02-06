# Deep-Learning-with-Satellite-Images
Deep Learning with Satellite Images


## Understanding NVID:
### Overview
The **Normalized Difference Vegetation Index (NDVI)** is a widely used metric in remote sensing to assess vegetation health and density. This project provides a simple implementation of the NDVI calculation using satellite imagery data.
NDVI is calculated using reflectance measurements in the near-infrared (NIR) and red spectral bands. It is particularly effective for monitoring vegetation health and can be applied in various fields such as agriculture, forestry, and ecology.

$$
NDVI = \frac{NIR - RED}{NIR + RED}
$$

Where:
- **NIR**: Reflectance in the near-infrared spectrum.
- **RED**: Reflectance in the red spectrum.
- This formula yields values ranging from -1 to 1:
- Values close to 1 indicate dense, healthy vegetation.
- Values around 0 suggest barren areas or sparse vegetation.
- Negative values (approaching -1) typically correspond to water bodies.
## Applications
NDVI can be applied in various fields, including:
- **Agriculture**: Monitoring crop health and estimating yields.
- **Forestry**: Assessing forest cover and health.
- **Ecology**: Studying vegetation dynamics and ecosystem changes.

Source : - [Wikipedia: Normalized Difference Vegetation Index](https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index)

## Satellite Image Source
- https://earthexplorer.usgs.gov/
- https://www.sentinel-hub.com/

## Reading Tiff Iamges
TIFF files can store metadata along with the image data. This metadata can include vital information such as:
- Georeferencing data: Latitude and longitude of each pixel, the projection used, and the spatial resolution of the image.
- Sensor information: The type of sensor, the time the image was taken, satellite information, and more.
- Calibration data: Information to help convert raw sensor data into usable imagery (such as reflectance values).
- rasterio lib can be used to read and process the information in TIFF image.
  
```bash
pip install rasterio
```

## Processing and export

## Analysis
