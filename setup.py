import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-pypi-template",
    version="1.0.0",
    author="<<< YOUR NAME >>>",
    author_email="<<< YOUR EMAIL >>>",
    description="<<< SHORT DESCRIPTION >>>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<<< URL TO DOC WEBSITE OR GIT PROJECT >>>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
