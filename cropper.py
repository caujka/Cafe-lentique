#!/usr/bin/python

import Image
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option("-p", dest="prefix",
                  help="resulting images file name prefix", metavar="PREFIX")
parser.add_option("-s", dest="shift", type='int',
                  help="total shift between first and last image in pixels",
                  metavar="SHIFT")

(options, args) = parser.parse_args()

files = args.sort()
total_shift = options.shift

print "Cropping files:"

for i in xrange(len(files)):
    print files[i]

    offset = total_shift * i / len(files)

    src_img = Image.open(files[i])

    (width, height) = src_img.size

    dest_img = src_img.crop((offset, 0, width - total_offset + offset, height))

    dest_img.save(options.prefix + files[i], src_img.format)
