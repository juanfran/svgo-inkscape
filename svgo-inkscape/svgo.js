var fs = require('fs');
var execSync = require('child_process').execSync;

var argv = require('minimist')(process.argv.slice(2), {boolean: true});

var SVGOptimize = require('svgo');

var file = fs.readFileSync(argv.file, 'utf8');

var options = {};
var optionsKeys = Object.keys(argv).filter(function(key) {
    return key !== 'file' && key !== '_';
});

options.plugins = optionsKeys.map(function(key) {
    var obj = {};

    obj[key] = argv[key];

    return obj;
});


var svgo = new SVGOptimize(options);

svgo.optimize(file, function (result) {
    process.stdout.write(result.data);
});
