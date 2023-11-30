Problem 1. Find a procedure for sampling uniformly on the surface of the sphere.
(a) Use computer to generate a thousand points that are random, independent, and uniform on the unit sphere, and print the resulting picture.
(b) By putting sufficiently many independent uniform points on the surface of the Earth (not literally but using a computer model, of course), estimate the areas of Antarctica and Africa, compare your results with the actual values [about 5.5 million square miles/15 million square kilometers for Antarctica and about 12 million square miles/30 million square kilometers for Africa], and make a few comments (e.g. are the relative errors similar? would you expect them to be similar? if not, which one should be bigger? how does accuracy improve if you use more points? etc.)


Installation Pre-Requisites:

Matplotlib: 
python -m pip install -U matplotlib
Numpy:
pip install numpy

Matplotlib and Numpy are necessary Python libraries that will be used to create the 3 dimensional visual of the sphere and the uniform, independent points. 


Implementation Descriptions: 
1a. There are two functions: sphere and generate_points. The sphere function is used to create a 3D representation of a sphere using Numpy to generate the points and then Motplotlib to plot the generated points. The sphere is currently hard coded to have a radius of 1 but can be changed. 

Based on the user input of points (must be at least 1000), there will be 


1b. 

