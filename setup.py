from setuptools import setup, find_packages

setup(
    name='terraform-local-to-var',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'terraform-local-to-var=terraform_local_to_var.convert:main',
        ],
    },
    install_requires=[
        # Add any dependencies here
    ],
)
