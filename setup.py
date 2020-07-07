import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="py3snowflake",
    version="0.1.0",
    author="Linghui Zeng",
    author_email="lh.zeng@hotmail.com",
    description="Python Snowflake Kit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathsyouth/py3snowflake",
    packages=setuptools.find_packages(),
    install_requires=["thriftpy2", "gunicorn_thrift"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="snowflake server client thrift",
    include_package_data=True,
    zip_safe=False,
)
