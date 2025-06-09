#!/usr/bin/env python3

#step2_run_pgsc_calc.py

import os
import subprocess

def run(config):
        print("Step 2: Running pgsc_calc...")

        #inputs from user
        pgs_id = input("Enter PGS Catalog ID (PGSxxxxxx): ").strip()
        samplesheet = input("Enter the absolute path to samplesheet.csv: ").strip()
        target_build = input("Enter the required target build (GRCh37 or GRCh38 only. Perform liftover for consistency otherwise): ").strip()
        profile = input("Enter profile to use (conda/docker/singularity): ").strip()
        op_dir = input("Enter the absolute path to output directory: ").strip()

        # Optional flags
        additional_flags = {}
        print("\n[Optional] Enter additional pgsc_calc flags. Leave blank to skip each.\n")
        additional_flags['min_overlap'] = input("--min_overlap: ").strip()
        additional_flags['ref'] = input("--ref (Ancestry reference RDS file): ").strip()
        additional_flags['liftover_chain'] = input("--liftover_chain: ").strip()
        additional_flags['ancestry_method'] = input("--ancestry_method (e.g., gmm, pca, etc.): ").strip()
        additional_flags['variant_filter'] = input("--variant_filter (e.g., common, rare, etc.): ").strip()
        additional_flags['score_file'] = input("--score_file (custom scoring file): ").strip()
        additional_flags['target_format'] = input("--target_format (vcf/bfile/pfile): ").strip()
        additional_flags['clump'] = input("--clump (true/false): ").strip()

        if not os.path.exists(samplesheet):
                print("Error: Samplesheet not found")
                return

        os.makedirs(op_dir, exist_ok = True)

        # Nextflow command
        command = [ "nextflow", "run", "pgscatalog/pgsc_calc",
                "-profile", profile,
                "--input", samplesheet,
                "--pgs_id", pgs_id,
                "--target_build", target_build,
                "--outdir", op_dir
        ]


        for flag,value in additional_flags.items():
                if value:
                        command.extend([f"--{flag}", value])

        print("Running command: ")
        print("".join(command))

        try:
                subprocess.run(command, check = True)
                print("pgsc_calc ran successfully")
        except subprocess.CalledProcessError as e:
                print("Running pgsc_calc failed. Please check inputs")
                print(e)
