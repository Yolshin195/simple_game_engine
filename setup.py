from setuptools import setup, find_packages

setup(
    name="name_my_lib",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
