#SVGO-inkscape

This is an extension to save and optimize SVG files with [SVGO](https://github.com/svg/svgo) at Inkscape.

The default Inkscape SVG files require a lot of inkscape metadata for edition purposes since SVG is the default file extension at inkscape. Using SVGO we can remove a lot of redundant and useless information such as editor metadata, comments, hidden elements, default or non-optimal values and other stuff that can be safely removed or converted without affecting SVG rendering result.

[SVGO](https://github.com/svg/svgo) is a very active plugin in continuous development.

## Download

SVGO inkscape for Linux 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.0/svgo-inkscape-linux-64.tar.gz)

SVGO inkscape for Linux 32bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.0/svgo-inkscape-linux-32.tar.gz)

SVGO inkscape for Windows 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.0/svgo-inkscape-windows-64.zip)

SVGO inkscape for Windows 32bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.0/svgo-inkscape-windows-32.zip)

SVGO inkscape for Mac 64bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.0/svgo-inkscape-mac-64.tar.gz)

SVGO inkscape for Mac 32bits [Download](https://github.com/juanfran/svgo-inkscape/releases/download/v0.1.0/svgo-inkscape-mac-32.tar.gz)


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
