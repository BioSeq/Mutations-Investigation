#!/usr/bin/env python
#
# combineVCFs.py
# Author: Mark Hartman
# Copyright (c) 2016 BioSeq
#
# Collects information from all VCF files in the current directory and writes them to a 
# single text file
#

import os

# CONSTANTS
OUTPUT_FILENAME = "combinedVCFs.txt"
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def main():
	#tries to delete and re-make the output file each time the script is run
	try: 
		os.remove(OUTPUT_FILENAME)
		print "previous output file deleted"
	except: 
		print "no previous output file detected"
	writeCombinedVcfData()
	print "done"

#opens the output file and adds the info from each VCF file in the current directory
def writeCombinedVcfData():
	with open(OUTPUT_FILENAME, 'a') as filea:
		for f in os.listdir(CURRENT_PATH):
			if f.endswith(".vcf"):
				filea.write(f.strip('.vcf') + '\n')			
				vcfData=getVcfData(f)
				for item in vcfData:
					item='\t'.join(item)
					filea.write(item + '\n')
				filea.write('\n')

#given the handle to a VCF file, return the relevant info (any line that is not a ##comment)
def getVcfData(f):
	with open(f, 'r') as filer:
		toReturn = []
		for line in filer:
			if not line.startswith("##"):
				toReturn.append(line.strip('#').strip().split('\t'))
		return toReturn

if __name__ == '__main__':
		main()
