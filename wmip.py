#!/usr/bin/env python

import urllib.request, urllib.parse, urllib.error, re


def getIP():
	base_url = "http://whatsmyip.net/" #you can change this if needed
	
	try:
		webpage = urllib.request.urlopen(base_url).read().decode('utf-8')

	except IOError as e:
		return "Couldn't reach host\n"
	
	classregex = re.compile("class=\"ip\".*?</h1>")#change this for the website you are using
	ipregex = re.compile("\\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b")
	
	ipclass = classregex.search(webpage)
	ipcontainer = ipregex.search(ipclass.group(0))
	
	return ipcontainer.group(0)	
	
	
	
if __name__ == "__main__":
	print(getIP())
	