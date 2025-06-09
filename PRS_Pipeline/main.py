#!/usr/bin/env python3
#main.py

import argparse
from steps import step1_preprocess, step2_run_pgsc_calc, step3_validate
import yaml

#----Load Config----
def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

#----Argument Parsing----
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run PRS pipeline steps")
    parser.add_argument("--step", required=True, help="Step to run (preprocess, run_pgsc_calc, validate)")
    args = parser.parse_args()

    config = load_config()

    if args.step == "preprocess":
        step1_preprocess.run(config)
    elif args.step == "run_pgsc_calc":
        step2_run_pgsc_calc.run(config)
    elif args.step == "validate":
        step3_validate.run(config)
    else:
        print("[ERROR] Unknown step. Use one of these steps: preprocess \n run_pgsc_calc \n validate")
