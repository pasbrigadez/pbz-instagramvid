#!/usr/bin/env python
#Made by PasoendanBrigadeZ
#Respect our Works
import requests
import urllib2
import sys
import argparse
import subprocess
import os

def Download(url,output):
	command1 = "ls"
	process1 = subprocess.Popen(command1.split(), stdout=subprocess.PIPE)
	otput, error = process1.communicate()

	if otput.find('Downloaded') > 0:
		command2 = "mkdir Downloaded"   #specify your cmd command
		process2 = subprocess.Popen(command2.split(), stdout=subprocess.PIPE)
	if output.find('.mp4') > 0:
		filenya = "Downloaded/"+output
	else:
		filenya = "Downloaded/"+output+".mp4"
	try:
		r = requests.get(url)
		rtek = r.text
	except:
		print "Pastikan link yang dipaste benar"
	stringnya = '"og:video:secure_url"'
	videonya = rtek.find(stringnya)
	mp4string = '.mp4" />'
	empefor = rtek.index(mp4string,videonya)
	link1 = rtek[videonya+len(stringnya)+10:empefor+4]
	download = urllib2.urlopen(link1)
	with open(filenya, 'wb') as f:
		f.write(download.read())
	pathname = os.path.dirname(sys.argv[0])
	fullpath = os.path.abspath(pathname)
	print "Downloaded into "+fullpath+"/Downloaded/"+filenya

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="|-PBZ Instagram Video Downloader-|")
	parser.add_argument(
		'-u',
		'--url',
		required = True,
		help = "URL of Video (Example: https://www.instagram.com/p/BhI2DWNFe14/?taken-by=bazitcreativepresent)")
	parser.add_argument(
		'-o',
		'--output',
		required = True,
		help = "Output Name (Example: video.mp4)")
	args = parser.parse_args()
	Download(args.url,args.output)
