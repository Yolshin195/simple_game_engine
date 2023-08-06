from setuptools import setup, find_namespace_packages

setup(
    name="ygsge",
    version="0.1",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    namespace_packages=["ygsge"],
)
