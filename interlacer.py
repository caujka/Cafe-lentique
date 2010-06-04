#!/usr/bin/env python

# Lenticular interlacer
# Author: Alexander Sheremet <asheremet@gmail.com>
# License: public domain

import Image
from math import *

def interlace(nlens, images, height=0, width=0):
    if height==0:
        height = images[0].size[1]

    if width==0:
        width = nlens * images[0].size[0]

    img_dest = Image.new(images[0].mode, (width, height))

    img1 = images[0]
    xx1 = 0
    for x_dest in xrange(width):
        lens_pos = float(x_dest) * float(nlens)/float(width)

        # 1e-5 is a dirty hack to overcome irrational nature
        # of numbers binary presentation.
        img_selector = modf(lens_pos)[0] * (len(images)) + 1e-5
        img2 = images[trunc(img_selector)]
        xx2 = img2.size[0] * x_dest / width

        proportion = int(modf(img_selector)[0]*255)

        for y_dest in xrange(height):
            yy1 = img1.size[1] * y_dest / height
            yy2 = img2.size[1] * y_dest / height

            pix1 = img1.getpixel((xx1, yy1))
            pix2 = img2.getpixel((xx2, yy2))

            pix = tuple(map(lambda a,b: (b*proportion + a*(255-proportion))/255,
                                pix1, pix2 ))

            img_dest.putpixel((x_dest, y_dest), pix)

        print "%d / %d" % (x_dest, width)
        img1 = img2
        xx1 = xx2

    return img_dest


if __name__ == '__main__':
    import optparse

    parser = optparse.OptionParser()
    parser.add_option("-o", dest="ofile",
                      help="write resulting image to FILE", metavar="FILE")
    parser.add_option("-t", dest="height", type='int',
                      help="height of result in pixels", metavar="HEIGHT")
    parser.add_option("-w", dest="width", type='int',
                      help="width of result in pixels", metavar="FILE")
    parser.add_option("-n", dest="nlens", type='int',
                      help="number of lenses on top of image", metavar="LENS_NUMBER")
    parser.add_option("-r", "--dpi", dest="dpi",
                      help="x and y print resolutions (dpi)", metavar="(x_res,y_res)")

    (options, args) = parser.parse_args()

    ims = map(lambda x: Image.open(x), args)

    dest = interlace(options.nlens, ims, height=options.height, width=options.width)

    dest.save(options.ofile, dpi=eval(options.dpi))

