import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="kpr",
    version="0.0.1",
    description="ETL om KPR data over te zetten vanuit Oracle naar Aspect Database",
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-clarity",
            'mock;python_version<"3.11"']
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["PyYAML", "other_packages"],
    url="https://git.dev.cloud.kadaster.nl/gima/gima-kpr/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)