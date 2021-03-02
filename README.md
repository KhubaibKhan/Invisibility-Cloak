# Invisibility-Cloak

This project has two parts.

1. color_selection.py which is used to find the mask for the specific color that you want to detect.
2. main.py where you can use the mask found in color_selection.py and that color will be used as an invisibility cloak.

### How does it work
The algorithm that is used here is quite simple. You take a picture of the background then replace the specific color(In my case i ued white(kinda white)) from the foreground with the background.

### How can you use it?
It's simple 

* Clone the repository
* Install the dependencies 

    > Numpy
    
    >OpenCv

    >Time
* Use color_selection.py to detect the color you want by tuning the nobs and get the mask.
* Use the mask obtained in the main file and run it.

### Demo

