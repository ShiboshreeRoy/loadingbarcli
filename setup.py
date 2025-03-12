from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="loadingbarcli",
    version="0.1.2",
    author="Shiboshree Roy",
    author_email="shiboshreeroy169@gmail.com",
    description="A professional and colorful loading bar for Python applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShiboshreeRoy/loadingbar",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)