# Avalanche dynamics : Bak-Tang-Wiesenfeld model

This project was carried out during my 2nd year of "classe préparatoire" (two-year undergraduate intensive course in mathematics and/or physics).
The problem was to determine the dynamic characteristics of a dense avalanche in order to determine the constructible areas in the mountains.
As part of the modelisation, I chose to use the Bak-Tang-Wiesenfeld sandpile model, also known as Abelian sandpile model. 

## Modelization 1D

For a first visualization, I implemented a 1D version of the model.

The mountain consists of 5 "columns" of snow, each column having its own height (which can range from 0 to 6 at initialization). It is considered that the peak of the mountain is the column on the left, and that the valley is on the right of the mountain. The principle is to calculate the difference in snow between two columns. If this difference is strictly greater than 2, the leftmost column collapses on its right neighbor with 2 piles of snow.\
To add a little realism, the "it's snowing" event is added and takes place before each mountain relaxation. 


## Modelization 2D

The modelization 2D works on the same principle, i.e. calculate the differences of height between columns. This time, the mountain consists of a square area of 50 columns per side, so it looks more like a sandpile : the difference of height is calculated between a column and its neighbors all around. Therefore, the avalanche can spread on different directions and in different proportions. 


In _modelisation2D.py_, we perform the relaxations of the mountain and get a file gathering the height of every column of snow of the mountain. _slopes.py_ gives us a vizualization of the state of the mountain : the heights are gathered by color which can give an idea of the distribution of snow on the mountain.

Finally, _plot.py_ gives us plots of the total slope stability on the maximum slope, the probability density of occurrence of an avalanche according to its size
and a log-log diagram of the size distribution of avalanches.



