#!/usr/bin/python

import Image
import os.path
import optparse

parser = optparse.OptionParser()
parser.add_option("-p", dest="prefix",
                  help="resulting images file name prefix", metavar="PREFIX")
parser.add_option("-s", dest="shift", type='int',
                  help="total shift between first and last image in pixels",
                  metavar="SHIFT")

(options, args) = parser.parse_args()

files = sorted(args)
total_shift = options.shift

print "Cropping files:"

for i in xrange(len(files)):
    print files[i]

    offset = total_shift * i / len(files)

    src_img = Image.open(files[i])

    (width, height) = src_img.size

    dest_img = src_img.crop((offset, 0, width - total_shift + offset, height))

    path,name = os.path.split(files[i])

    dest_img.save(os.path.join(path, options.prefix + name), src_img.format)
