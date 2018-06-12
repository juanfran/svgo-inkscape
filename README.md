# SVGO-inkscape

This is an extension to save and optimize SVG files with [SVGO](https://github.com/svg/svgo) at Inkscape.

The default Inkscape SVG files require a lot of inkscape metadata for edition purposes since SVG is the default file extension at inkscape. Using SVGO we can remove a lot of redundant and useless information such as editor metadata, comments, hidden elements, default or non-optimal values and other stuff that can be safely removed or converted without affecting SVG rendering result.

[SVGO](https://github.com/svg/svgo) is a very active plugin in continuous development.

## Download

SVGO inkscape for Linux 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.1/svgo-inkscape-linux64.zip)

SVGO inkscape for Windows 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.1/svgo-inkscape-windows64.zip)

SVGO inkscape for Mac 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.1/svgo-inkscape-mac64.zip)


## Install

Download and uncompress the content in your Inkscape extension folder.

For Linux
```
~/.config/inkscape/extensions
```

For Windows
```
C:\Program Files\Inkscape\share\extensions
```

Then, you will be able to save your files as 'Optimized with SVGO'
```
Save as -> Optimized with svgo (*.svg)
```
