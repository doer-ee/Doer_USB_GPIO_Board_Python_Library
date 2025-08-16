from setuptools import setup, find_packages

setup(
    name="DoerGPIO",
    version="1.0",  # Incremented version number
    packages=find_packages(),
    install_requires=[
        "pyserial",  # Required for serial communication
    ],
    author="Pasco Tang",
    author_email="pasco@doer.ee",  # You should add your email here
    description="USB GPIO interface for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://doer.ee",  # You should add your repository URL here
    license="GPL-3.0-or-later",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 
