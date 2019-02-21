# Project Title: miles_2_Km
# Version: 1.0
# Instructions:
# Prerequistes: Paython 3
# Built with: Atom text editor
# Thomas maioli
# coded in Python 3.7
# date 2019-02-20
# Project name: Miles
# Issues and concerns: none
# Problem domain "For loop"

for miles in range(10, 101, 1):
	km = miles * 1.609
	print("%d miles --> %3.2f kilometers" % (miles, km))
