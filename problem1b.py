#!/usr/bin/env python3
from mpl_toolkits import mplot3d
import numpy
import matplotlib.pyplot as plt

#Problem 1a:

#create sphere, we will add points onto the points on the sphere 
def sphere(axis, radius=1):
    u = numpy.linspace(0, 2 * numpy.pi, 100)
    v = numpy.linspace(0, numpy.pi, 100)
    x = radius * numpy.outer(numpy.cos(u), numpy.sin(v))
    y = radius * numpy.outer(numpy.sin(u), numpy.sin(v))
    z = radius * numpy.outer(numpy.ones(numpy.size(u)), numpy.cos(v))
    axis.plot_surface(x, y, z, color='blue', alpha=0.5)

def generate_points(points):
    theta = 2 * numpy.pi * numpy.random.rand(points)
    phi = numpy.arccos(1- 2*numpy.random.rand(points))
    x = numpy.sin(phi) * numpy.cos(theta)
    y = numpy.sin(phi) * numpy.sin(theta)
    z = numpy.cos(phi)
    return x, y, z


def region_check(x,y,z,region): 
    if region == "Antarctica":
        return z <= 0.5
    elif region == "Africa":
        return (x > 0.35) & (y < 0.5) & (z < 0.5) #very rough estimate of africa's region on radius 1 sphere
    return numpy.full(x.shape, False)

def main():
    enter_points = int(input("Enter at least 1000 points to generate on sphere"))
    print("Entered points:", enter_points)  # Added print statement
    # Check if the entered value is less than 1000
    if enter_points < 1000:
        print("Invalid number of points. Please enter at least 200 points.")
        return
    
    x, y, z = generate_points(enter_points)

    in_antarctica = region_check(x,y,z, "Antarctica")
    in_africa = region_check(x,y,z, "Africa")
    antarctica_estimate = numpy.sum(in_antarctica) / enter_points
    africa_estimate = numpy.sum(in_africa) / enter_points

    #creating the matplotlib figure
    fig = plt.figure()

    #creates 3d axies
    axis = fig.add_subplot(111, projection = '3d')

    #plotting the sphere
    sphere(axis)

    #plotting points
    axis.scatter(x,y,z, color = 'blue')
    axis.scatter(x[in_antarctica], y[in_antarctica], z[in_antarctica], color = 'red')
    axis.scatter(x[in_africa], y[in_africa], z[in_africa], color = 'white')

    #show plot with title
    axis.set_title('Uniform Independent Points on the Sphere w/ Africa and Antarctica')
    print(f"Estimated size for Antarctica in 1 radius sphere: {antarctica_estimate}")
    print(f"Estimated size for Africa in 1 radius sphere: {africa_estimate}")

    plt.show()

if __name__ == "__main__":
    main()
#Problem 1b: