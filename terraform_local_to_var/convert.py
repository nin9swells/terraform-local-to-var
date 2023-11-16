import os
import re
import sys
import argparse
from collections import OrderedDict

def extract_locals(tf_content):
    locals_pattern = re.compile(r'locals\s*{([^}]*)}', re.DOTALL)
    locals_block = locals_pattern.search(tf_content)
    
    locals_dict = {}
    if locals_block:
        locals_content = locals_block.group(1)
        lines = locals_content.strip().split('\n')
        
        for line in lines:
            match = re.match(r'\s*([^\s=]+)\s*=\s*"([^"]+)"', line)
            if match:
                key, value = match.groups()
                locals_dict[key.strip()] = value.strip()
    
    return locals_dict

def main():
    parser = argparse.ArgumentParser(description='Process Terraform files.')
    parser.add_argument('--dir', help='Terraform directory (default: current working directory)')
    parser.add_argument('--local-file', help='Use a single Terraform file instead of searching for all .tf files')
    parser.add_argument('--sort', help='Sort output (default: unsorted)', action='store_true')
    args = parser.parse_args()

    terraform_dir = args.dir or os.getcwd()

    if args.local_file:
        tf_files = [args.local_file]
    else:
        tf_files = [filename for filename in os.listdir(terraform_dir) if filename.endswith(".tf")]

    if not tf_files:
        print(f"No Terraform files (.tf) found.")
        sys.exit(1)

    terraform_variables = OrderedDict()

    for filename in sorted(tf_files):
        file_path = os.path.join(terraform_dir, filename)
        
        with open(file_path, 'r') as file:
            tf_content = file.read()
            locals_dict = extract_locals(tf_content)
            
            for var_name in locals_dict:
                terraform_variables[var_name] = None

    # Print sorted or unsorted Terraform variables based on --sort option
    sorted_variables = sorted(terraform_variables) if args.sort else terraform_variables
    for var_name in sorted_variables:
        print(f'variable "{var_name}" {{}}')

    print("\n")

    # Print sorted or unsorted locals assigned by variable values based on --sort option
    for var_name in sorted_variables:
        print(f'{var_name} = var.{var_name}')

if __name__ == "__main__":
    main()
