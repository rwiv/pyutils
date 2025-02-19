import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyutils",
    version="0.1.1",
    description="A collection of utility functions for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rwiv/pyutils",
    packages=setuptools.find_packages(),
)
