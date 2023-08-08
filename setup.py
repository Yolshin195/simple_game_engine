# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding="utf-8") as f:
        return f.read()


setup(
    name="ygame",
    version="1.0.3",
    description="Your Game (ygame) is simple game engine, using cells to draw the playing field",
    long_description=readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/Yolshin195/ygame",
    packages=['ygame'],
    author_email="elshin195@gmail.com",
    keywords='simple cell game python',
    zip_safe=False,
    project_urls={
        'Documentation': 'https://github.com/Yolshin195/ygame/tree/main/docs'
    },
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    license='MIT',
    python_requires='>=3.11',
)
