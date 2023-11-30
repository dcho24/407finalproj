(b) By putting sufficiently many independent uniform points on the surface of the Earth (not literally but using a computer model, of course), estimate the areas of Antarctica and Africa, compare your results with the actual values [about 5.5 million square miles/15 million square kilometers for Antarctica and about 12 million square miles/30 million square kilometers for Africa], and make a few comments (e.g. are the relative errors similar? would you expect them to be similar? if not, which one should be bigger? how does accuracy improve if you use more points? etc.)


Implementation Descriptions: 

1b. There are added functions and logic to handle the estimation logic and visualizations of Antarcitca and Africa on the sphere. For one, there is an added region_check function that identifies whether each point within predefined regions on the sphere.

When identifying the regions of Antarctica and Africa on the sphere, it is important to note that the estimation is based on the radius of the sphere being 1. As Antarctica is part of the South Pole, the estimation will be on the southern hemisphere, hence the z <= 0.5. As for Africa, the region was a little difficult to estimate but I was able to estimate it compared to a real 3D map image. The estimation I came up with was (x > 0.35) & (y < 0.5) & (z < 0.5). This is an extremely rough estimation to replicate the locations of Antarctica and Africa on our sphere.

