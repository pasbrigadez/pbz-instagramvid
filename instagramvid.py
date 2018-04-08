#!/usr/bin/env python
#Made by PasoendanBrigadeZ
#Respect our Works
import os
import re
import urllib2
import argparse

outdir = 'Downloaded'

def Download(url,output):
    os.makedirs(outdir) if not os.path.isdir(outdir) else 0
    filenya = "{}/{}".format(outdir, output if '.mp4' in output else output + '.mp4')
    try:
        rtek = urllib2.urlopen(url).read()
    except:
        print "Pastikan link yang dipaste benar"
    link = re.search(r'og:video" content="(.*)"', rtek).group(0).replace('og:video" content="', '').replace('"','')
    load = urllib2.urlopen(link).read()
    with open(filenya, 'wb') as f:
        f.write(load)
    print "Downloaded into {}/{}".format(os.path.abspath('.'), filenya)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="|-PBZ Instagram Video Downloader-|")
    parser.add_argument(
        '-u',
        '--url',
        required = True,
        help = "URL of Video (Example: https://www.instagram.com/p/BhI2DWNFe14)")
    parser.add_argument(
        '-o',
        '--output',
        required = True,
        help = "Output Name (Example: video.mp4)")
    args = parser.parse_args()
    Download(args.url,args.output)
