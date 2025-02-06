import rasterio

# Open the TIFF file
with rasterio.open('your_satellite_image.tif') as src:
    # Print some basic metadata about the image
    print("Image Metadata:")
    print(f"Driver: {src.driver}")
    print(f"Width: {src.width} pixels")
    print(f"Height: {src.height} pixels")
    print(f"Number of Bands: {src.count}")
    print(f"Coordinate Reference System: {src.crs}")
    print(f"Bounds: {src.bounds}")
    
    # Read data from each band
    for i in range(1, src.count + 1):
        band = src.read(i)  # Read band i (bands are 1-indexed)
        print(f"\nBand {i} data:")
        print(f"Shape: {band.shape}")  # Shape of the band (height x width)
        print(f"Min value: {band.min()}")  # Minimum pixel value in the band
        print(f"Max value: {band.max()}")  # Maximum pixel value in the band
        print(f"Mean value: {band.mean()}")  # Mean pixel value in the band
