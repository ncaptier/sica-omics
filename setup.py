import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sica-omics",
    version="0.0.1",
    author="Nicolas Captier",
    author_email="nicolas.captier@curie.fr",
    description="Toolbox for omics analysis with stabilized-ica package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ncaptier/sica-omics",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "anndata>=0.8.0",
        "pandas>=1.4.2",
        "mygene>=3.2.2",
        "reactome2py>=1.0.0",
        "requests>=2.27.1",
        "stabilized-ica==2.0.0",
    ],
    extras_require={
        "dev": ["pytest"],
        "doc": [
            "sphinx == 5.0.2",
            "sphinx-gallery == 0.10.0",
            "numpydoc == 1.2",
            "nbsphinx == 0.8.9",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
