from setuptools import setup, find_packages

setup(
    name="amocarray",
    version="0.1.1",  # Deprecation release (fixed RST formatting)
    author="Eleanor Frajka-Williams",
    author_email="eleanorrajka@gmail.com",
    description="[DEPRECATED] Please use AMOCatlas instead",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    url="https://github.com/eleanorfrajka/amocarray",
    packages=find_packages(),
    install_requires=[
        "AMOCatlas",  # This ensures the new package gets installed
    ],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",  # Match your license
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
    keywords="deprecated amoc atlas oceanography",
)