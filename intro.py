#includes that we are using (two are used in part 6)
from astropy.io import fits
import matplotlib.pyplot as plt
from photutils.aperture import CircularAperture
import numpy as np 

#open the fits file
hdul = fits.open('12410-PS-DATA copy/PSDataFile.001.fits')

#display file info
hdul.info()

#save image data from opened file
image_data = hdul[0].data

#set title and figure size, and show the image data
plt.figure(figsize=(8, 8))
plt.imshow(image_data)
plt.title('2022-09-06T18:25:42 | 60 Second Exposure | PS Data File 001')

#including the axes labels from the header, found with SAOImageViewer
plt.xlabel('Length of Data Axis 1')
plt.ylabel('Length of Data Axis 2')

#include color bar, show plot
plt.colorbar()
plt.show()

#make list of sizes  to calculate mean and std of. loops through each one and saves the mean and std in a list. 
size_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
std_list = []
mean_list = []
count_list = []
#loop through each size to add in the mean and std
for i in size_list:
    aper = CircularAperture([1, 3], i)
    mask = aper.to_mask()
    std_list.append(np.std(mask))
    mean_list.append(np.mean(mask))
    count_list.append(np.sum(mask))

#plot for the standard deviations
plt.title('Aperture Size vs Standard Deviation of Pixels')
plt.xlabel("Aperture Size")
plt.ylabel('Standard Deviation of Pixels')
plt.plot(size_list, std_list, "bo")

plt.show()

#plot for the means
plt.title('Aperture Size vs Mean of Pixels')
plt.xlabel("Aperture Size")
plt.ylabel('Mean of Pixels')
plt.plot(size_list, mean_list, "bo")
plt.show()

#plot for the aperture size 
plt.title('Aperture Size vs Sum of Enclosed Count Intensities')
plt.xlabel("Aperture Size")
plt.ylabel('Sum of Enclosed Count Intensities')
plt.plot(size_list, count_list, "bo")
plt.show()

#close file
hdul.close()

