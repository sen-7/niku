[English](README.md) | [日本語](README.ja.md)

# niku
* One-dimensional roast beef simulation ;-)

## Requirements
* unix-shell
* python
* numpy
* matplotlib
* imagemagick

## sample
![sample](sample.gif)

## To make a good roast beef
* No cooking methods will achieve boundary conditions (temperature of meat surface) higher than 100 degrees C.
   * If the meat surface is dry, it may exceed 100 degrees but you must scorch it.
* It seems good to keep the boundary condition at 70-80 degrees C.
   * In the case of oven cooking, set it to about 120 degrees C (250 F) and cover the meat with foil. The meat surface will be around 70-80 deg C.
* Initial condition is not an important factor. You don't need to care.
* The cooking time is proportional to the square of the thickness. Say, cook two-cm-meat for 10 minutes.

# Future work
* non-flat meat (consider shape factor)
* model heat conduction and convection outside the meat (air in the oven cabinet)
