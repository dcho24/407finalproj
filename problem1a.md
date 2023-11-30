Problem 1. Find a procedure for sampling uniformly on the surface of the sphere.
(a) Use computer to generate a thousand points that are random, independent, and uniform on the unit sphere, and print the resulting picture.

Installation Pre-Requisites:

Matplotlib: 
python -m pip install -U matplotlib
Numpy:
pip install numpy

Running the script:
python3 problem1a.py
or on the VS Code header-> run -> start debugging

Matplotlib and Numpy are necessary Python libraries that will be used to create the 3 dimensional visual of the sphere and the uniform, independent points. 


Implementation Descriptions: 
1a. There are two functions: sphere and generate_points. The sphere function is used to create a 3D representation of a sphere using Numpy to generate the points and then Motplotlib to plot the generated points. The sphere is currently hard coded to have a radius of 1 but can be changed. 

The generate_points function generates the points based on the user input of points (must be at least 1000), there will be the same number of uniform, independent points entered by the user onto the hard-coded sphere's surface. Notice also how the points are correctly being placed over the sphere. The points are also being randomly being placed on the sphere so sphere image will look the same.

The main function creates the actual visualization combining the sphere and randomly generated points. The logic to show and display the figure was helped by another source (Refer to sources.md)

Couple visualization examples below:

1000 Randomly Generated Uniform, Independent Points:
<img width="619" alt="Screenshot 2023-11-30 at 10 32 08 AM" src="https://github.com/dcho24/407finalproj/assets/89420699/d236b1f5-9104-449f-8c44-eb6fefed15b5">


1000 Randomly Generated Uniform, Independent Points #2 (To show random location and same number of points)
<img width="471" alt="Screenshot 2023-11-30 at 10 32 55 AM" src="https://github.com/dcho24/407finalproj/assets/89420699/fe4b43ef-11b7-4370-9c75-e95e62c75a45">

2000 Randomly Generated Uniform, Independent Points:
<img width="438" alt="Screenshot 2023-11-30 at 10 33 50 AM" src="https://github.com/dcho24/407finalproj/assets/89420699/0fbfa983-8fee-44e2-97ac-7214572627f5">

3000 Randomly Generated Uniform, Independent Points:
<img width="499" alt="Screenshot 2023-11-30 at 10 34 17 AM" src="https://github.com/dcho24/407finalproj/assets/89420699/84794f70-a567-44a2-81b7-3405247cffea">


1b.     