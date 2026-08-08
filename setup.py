from setuptools import setup, find_packages

setup(
    name="mszx",
    version="1.0.0",
    author="mt.co",
    author_email="txz.file@gmail.com",
    description="7-битный архиватор текста",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://szx.pythonanywhere.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

