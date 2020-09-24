from setuptools import setup, find_packages

with open("README.rst", "r") as f:
    readme_file = f.read()

# setup function
setup(
    name="pgbackup",
    version="0.1.0",
    description="postgresql database backup utility",
    long_description=readme_file,
    author="Bogdan Dancu",
    author_email="bogdan@arrakis.spice",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requirements=["boto3"],
    entry_points={
        "console_scripts": [
            "pgbackup=pgbackup.cli:main",
        ]
    }
)

