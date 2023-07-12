import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vsss_client",
    version="0.0.7",
    author="LLucas de Felippe & Lucas Martins",
    author_email="luscagbr@gmail.com",
    description="A client for VSSS",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fbot-furg/vsss-client.git",
    packages=setuptools.find_packages(),
    install_requires=[
        "configparser",
        "protocolbuffers",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License'
    ],
)   
