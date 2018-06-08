## Installation
Download python script and set it as executable:
'''
chmod +x sra-download.py
'''
Ensure that the environment python version is >= 3.4.

## Setup
Install the SRA toolkit at https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit\_doc&f=std

Move the sratoolkit folder to /usr/bin, and add it to your environment using by appending '''export PATH=$PATH:/usr/bin/sratoolkit/bin''' to ~/.bash\_profile

Install bwa (https://github.com/lh3/bwa) and ensure it is in your environment

Index the reference genome you intend to use with '''bwa index hg18.fa'''

## Usage
sra-download.py [-h] [--pileup] reference acclist

reference: Reference genome file, must be indexed already
acclist: List of SRA sequences to be downloaded
--pileup: Combines bam output into pileup file. Requires samtools

Output will be in the sra-download-out folder
