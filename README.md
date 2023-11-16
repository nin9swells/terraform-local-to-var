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

### Options

- `--dir`: Terraform directory (default: current working directory).
- `--local-file`: Use a single Terraform file instead of searching for all .tf files.
- `--sort`: Sort output (default: unsorted).

### Examples

Assuming you have the following locals block in your Terraform files:

```
locals {
  tg_healthcheck_healthy_threshold   = "3"
  tg_healthcheck_unhealthy_threshold = "3"
  tg_healthcheck_interval            = "30"
}
```

Running the command:

```
terraform-local-to-var --dir /path/to/terraform/directory
```

will produce the following output:

```
variable "tg_healthcheck_healthy_threshold" {}
variable "tg_healthcheck_unhealthy_threshold" {}
variable "tg_healthcheck_interval" {}

tg_healthcheck_healthy_threshold   = var.tg_healthcheck_healthy_threshold
tg_healthcheck_unhealthy_threshold = var.tg_healthcheck_unhealthy_threshold
tg_healthcheck_interval            = var.tg_healthcheck_interval
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
