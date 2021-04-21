import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="flames",
    version="1.0.0",
    description="Simple fun module to manipulate the classic game flames",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aadilvarsh/flames",
    author="Aadil Varsh",
    author_email="aadilvarshofficial@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["flames"],
    include_package_data=True,
)
