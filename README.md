# terraform-local-to-var

A script for converting Terraform `locals` blocks to variable declarations.

## Installation

```bash
pip install git+https://github.com/nin9swells/terraform-local-to-var.git
```

## Usage

```
terraform-local-to-var --dir /path/to/terraform/directory
```

For more options, use:

```
terraform-local-to-var --help
```

## Options

- `--dir`: Terraform directory (default: current working directory).
- `--local-file`: Use a single Terraform file instead of searching for all .tf files.
- `--sort`: Sort output (default: unsorted).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
