#!/usr/bin/env python
from argparse import ArgumentParser
import subprocess

# Parse inputs
parser = ArgumentParser()
parser.add_argument("reference")
parser.add_argument("acclist")
parser.add_argument("--pileup", help="combines bam output into pileup. requires samtools",
                    action="store_true")

args = parser.parse_args()

# print("Arguments: ", args)

# Parse acclist
acclist_file = open(args.acclist, "r")
acclist = acclist_file.read().strip().split()
acclist.sort()

print("Acclist: ", acclist)

# Download fasta files
try:
    subprocess.run(["mkdir", "sra-download-out"])
except subprocess.CalledProcessError:
    print("Directory already created.")

for seq in acclist:
    subprocess.check_output(["fastq-dump", seq, "--outdir", "sra-download-out"])

    with open("sra-download-out/" + seq +".sam", "w") as outfile:
        subprocess.call(["bwa", "mem", args.reference, "sra-download-out/" + seq + ".fastq"], stdout=outfile)
    print("Saved as " + seq + ".sam")

# Cleanup
for seq in acclist:
    subprocess.run(["rm", "sra-download-out/" + seq + ".fastq"])

# Optional, compilation into bamfile
if args.pileup:
    with open("sra-download-out/samfiles.txt", "w") as samfiles:
        for seq in acclist:
            samfiles.write("sra-download-out/" + seq + ".sam\n")

    subprocess.check_output(["samtools", "mpileup", "-BQ0", "-d10000", "-f", args.reference, "-q", "40", "-b", "sra-download-out/samfiles.txt"])

    # Cleanup