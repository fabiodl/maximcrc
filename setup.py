
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='maximcrc',
    version='0.1',
    scripts=[],
    author="Fabio Dalla Linera",
    author_email="fabiodl@gmail.com",
    description="Maxim CRC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javatechy/dokr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GPL",
         "Operating System :: OS Independent",
    ],
)
