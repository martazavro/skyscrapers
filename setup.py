import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Skyscrapers",
    version="0.0.1",
    author="Marta Nahorniuk",
    author_email="marta.nahorniuk@ucu.edu.ua",
    description="Check skyscrapers game board",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/martazavro/skyscrapers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.5',
)