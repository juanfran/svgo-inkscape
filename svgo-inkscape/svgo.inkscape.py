#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys, inkex, os

options = {
    "cleanupAttrs": True,
    "removeDoctype": True,
    "removeXMLProcInst": True,
    "removeComments": True,
    "removeMetadata": True,
    "removeTitle": False,
    "removeDesc": True,
    "removeUselessDefs": True,
    "removeEditorsNSData": True,
    "removeEmptyAttrs": True,
    "removeHiddenElems": True,
    "removeEmptyText": True,
    "removeEmptyContainers": True,
    "removeViewBox": True,
    "cleanupEnableBackground": True,
    "convertStyleToAttrs": True,
    "convertColors": True,
    "convertPathData": True,
    "convertTransform": True,
    "removeUnknownsAndDefaults": True,
    "removeNonInheritableGroupAttrs": True,
    "removeUselessStrokeAndFill": True,
    "removeUnusedNS": True,
    "cleanupIDs": True,
    "cleanupNumericValues": True,
    "moveElemsAttrsToGroup": True,
    "moveGroupAttrsToElems": True,
    "collapseGroups": True,
    "removeRasterImages": False,
    "mergePaths": True,
    "convertShapeToPath": True,
    "sortAttrs": False,
    "transformsWithOnePath": False,
    "removeDimensions": False,
    "removeAttrs": False,
    "addClassesToSVGElement": False
}

class SvgoInkscape (inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)

        self.arg_parser.add_argument("--tabs",
            type=str,
            dest="tab")

        for key in options:
            self.arg_parser.add_argument("--" + key, type=inkex.Boolean,
                                      dest=key, default=options[key])

    def getCommand(self, name, option):
        return " --"+ name + " " + str(option).lower()

    def effect(self):
        command = "./node/bin/node svgo.js --file=" + self.options.input_file

        optionsDict = self.options.__dict__

        for key in options:
            command += self.getCommand(key, optionsDict[key])

        p = os.popen(command)
        result = p.read()
        p.close()

        sys.stdout.write(result)
        sys.stdout.close()

if __name__ == '__main__':
    e = SvgoInkscape()
    e.run()
