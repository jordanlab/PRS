#!/usr/bin/env python3

#step1_preprocess.py

import glob
import os

def run(config):
	print("Step 1: Starting check...")
	
	prefix = config.get("genotype_prefix")

	if not prefix:
		print("Error: 'prefix' not found in config.yaml")
		return
	
	if not os.path.isabs(prefix):
		print("Error: Path prefix should be absolute")

	matched_prefixes = glob.glob(prefix + "*")
	if not matched_prefixes:
		print("Error: No matching files found.")
		return
	
	prefixes = set()
	for path in matched_prefixes:
		base = path
		for ext in [".vcf", ".vcf.gz", ".bed", ".bim", ".fam", ".pgen", ".pvar", ".psam"]:
			if path.endswith(ext):
				base = path.replace(ext, "")
				break
		prefixes.add(base)

	for prefix in sorted(prefixes):
		vcf = prefix + ".vcf"
		vcfgz = prefix + ".vcf.gz"
		bim = prefix + ".bim"
		bed = prefix + ".bed"
		fam = prefix + ".fam"
		pgen = prefix + ".pgen"
		pvar = prefix + ".pvar"
		psam = prefix + ".psam"

		print("Input files are:\n")
		if os.path.exists(vcf) or os.path.exists(vcfgz):
			format = vcf if os.path.exists(vcf) else vcfgz
			print(f" - VCF File: {format}")
			print("Perform QC. Merge into a single multi-vcf file or split by chromosomes.")
		elif os.path.exists(bed) and os.path.exists(bim) and os.path.exists(fam):
			print(f" - PLINK bfile: Make sure the filenames are consistent. format field in samplesheet is 'bfile', proceed with running pgsc_calc")
		elif os.path.exists(pgen) and os.path.exists(pvar) and os.path.exists(psam):
			print(f" - PLINK pfile: Make sure filenames are consistent. format field in samplesheet is 'pfile', proceed with running pgsc_calc")
		else:
			print("File format not supported. Expected (vcf/vcf.gz) or (bed,bim,fam) or (pgen,pvar,psam).")
	
	print("Preprocess check complete")
