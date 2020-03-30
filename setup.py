import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="http_logger",
    version="0.0.0",
    author="Alex Peterson",
    author_email="alexander.peterson89@gmail.com",
    description="Log over http with an auth token",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amp89/http_logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)