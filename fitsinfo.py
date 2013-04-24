#!/usr/bin/python

import sys
import pyfits

fitsfile = sys.argv[1]

hdulist = pyfits.open(fitsfile)
if len(sys.argv) > 2:
    for header_num in sys.argv[2:]:
        print "Header no. %s:" % header_num
        for card in hdulist[int(header_num)].header.cards:
            print card
else:
    for hdu_num, hdu in enumerate(hdulist):
        print "Header no. %d:" % hdu_num
        for card in hdu.header.cards:
            print card
