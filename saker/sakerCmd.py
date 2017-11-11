#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from saker.data.banner import banner
from saker.classes.sakerClass import Saker

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='CTF Web fuzz framework',
        usage='%(prog)s [options]',
        epilog='CTF Web fuzz framework')
    parser.add_argument('-s', '--scan', action="store_true",
                        help='run with list model')
    parser.add_argument('-f', '--file', metavar='file',
                        default='',
                        help='scan specific file')
    parser.add_argument('-e', '--ext', metavar='ext',
                        default='php',
                        help='scan specific ext')
    parser.add_argument('-i', '--interactive', action="store_true",
                        help='run with interactive model')
    parser.add_argument("-u", '--url',
                        dest="url", help="define specific url")
    parser.add_argument("-t", '--timeinterval', type=int,
                        dest="interval", help="set time interval", default=0)

    opts = parser.parse_args()

    url = opts.url

    if not url:
        sys.stderr.write('Url is required!')
        sys.exit(1)

    print banner

    c = Saker(url)

    if opts.scan:
        c.scan(filename=opts.file,
               interval=opts.interval,
               ext=opts.ext)

    if opts.interactive:
        c.interactive()
