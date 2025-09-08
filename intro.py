from astropy.io import fits
import matplotlib.pyplot as plt
from photutils import aperture

hdul = fits.open('12410-PS-DATA copy/PSDataFile.001.fits')

hdul.info()

image_data = hdul[0].data

plt.figure(figsize=(8, 8))
plt.imshow(image_data)
plt.title('PS Data File 001')

plt.xlabel('Length of Data Axis 1')
plt.ylabel('Length of Data Axis 2')

plt.colorbar()
plt.show()

hdul.close()
