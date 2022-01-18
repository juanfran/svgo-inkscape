# SVGO-inkscape

This is an extension to save and optimize SVG files with [SVGO](https://github.com/svg/svgo) at Inkscape, it is an alternative to the already [implemented](https://commons.wikimedia.org/wiki/Help:Inkscape#Inkscape_SVG_vs._Plain_SVG) optimization Tool: [scour](https://github.com/scour-project/scour)

The default Inkscape SVG files produces a lot of inkscape metadata for edition purposes since SVG is the default file extension at inkscape. Using SVGO we can remove a lot of redundant and useless information such as editor metadata, comments, hidden elements, default or unknown values and other stuff that can be removed or converted often without affecting SVG rendering result.

## Warning for using optimizers

optimizing svg can lead to server damage
- it often breaks svgs (e.g. svgo has [200 open bugs-reports](https://github.com/svg/svgo/issues))
- svgo is in all fair benchmarks the worst in breaking svgs, see e.g. [benchmark by svgcleaner](https://github.com/RazrFalcon/svgcleaner/#correctness)
- removing editor metadata can be a copyright violation if resharing others work
- removing comments, can make manual editing of the file more difficult
- removing hidden elements, removes deactivated layers
- removing unknown and invalid values, removes helpfull editor-data, such as grids or removes the ability to [edit arcs](https://commons.wikimedia.org/wiki/File:Sodipodi-type%3D%22arc%22.svg) in inkscape, other unknown inkscape-attributes will [break](https://gitlab.com/inkscape/inbox/-/issues/427) the inkscape behavior (see e.g. [invalid elements that should be kept](https://commons.wikimedia.org/wiki/User:JoKalliauer/Optimization#invalid_elements_that_should_be_kept))

## Download

SVGO inkscape for Linux 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v1.0.0/svgo-inkscape-linux64.zip)

SVGO inkscape for Windows 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v1.0.0/svgo-inkscape-windows64.zip)

SVGO inkscape for Mac 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v1.0.0/svgo-inkscape-mac64.zip)


## Install

Download and uncompress, copy the content inside the uncompresed folder (svgo-inkscape-windows64, svgo-inkscape-linux64 or svgo-inkscape-mac64) to your Inkscape extension folder.

For Linux
```
~/.config/inkscape/extensions
```

For Windows
```
C:\Program Files\Inkscape\share\inkscape\extensions\
```

Then, you will be able to save your files as 'Optimized with SVGO'
```
Save as -> Optimized with svgo (*.svg)
```
