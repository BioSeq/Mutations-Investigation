# Mutations Investigation
### BioSeq Group, Tufts University
##### BioSeq Program Administrator: Matt Fierman (bioseq@tufts.edu)
##### Author: Mark Hartman (markrhartman@gmail.com)

### Introduction
This analysis pipeline analyses the VCF results from the Mutations Investigation Experiment from the Illumina MiSeq.
Currently consists of a single tiny script.

### Setup
Put all of the VCF files generated by the MiSeq in the same directory as the script. The script uses all files in this folder that have the ".vcf" file extension, so make sure there are no other files of this type in the same folder.

### Use
`./combineVCFs.py`  (very simple)

### Output
For each run, the `combineVCFs.py` script creates tab-separated text file "combinedVCFs.txt" in the following format.
Example:
AB2_S9
CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	AB2
pUC19	3	.	G	C	177.01	PASS	AC=1;AF=0.5;AN=2;DP=41;QD=4.32	GT:AD:DP:GQ:PL:VF:GQX	0/1:25,16:41:99:207,0,480:0.390:99
pUC19	16	.	A	C	77.01	PASS	AC=1;AF=0.5;AN=2;DP=229;QD=0.34	GT:AD:DP:GQ:PL:VF:GQX	0/1:182,47:238:99:107,0,4243:0.205:77
pUC19	1631	.	A	G	112964.01	PASS	AC=2;AF=1.0;AN=2;DP=3260;QD=34.65	GT:AD:DP:GQ:PL:VF:GQX	1/1:4,3256:3264:99:112964,8378,0:0.999:99
pUC19	2680	.	C	G	25.02	PASS	AC=1;AF=0.5;AN=2;DP=207;QD=0.12	GT:AD:DP:GQ:PL:VF:GQX	0/1:162,45:209:54.85:55,0,2384:0.217:25


### Further Analysis
Once the VCF files are combined into a single file, this file can be formatted into a summary sheet for exploring the various mutations identified in the run.

Questions? Comments? Suggestions? Don't hesitate to contact us!
