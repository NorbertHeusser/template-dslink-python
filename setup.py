from setuptools import setup

setup(
    name="dslink-python-template",
    version="0.2.1",
    description="Python DSLink Template",
    url="http://github.com/NorbertHeusser/template-dslink-python.git",
    author="Logan Gorence",
    author_email="Logan.Gorence@AcuityBrands.com",
    license="Apache 2.0",
    install_requires=[
        "dslink == 0.7.3.1"
    ],
    dependency_links=[
        "https://github.com/NorbertHeusser/sdk-dslink-python/archive/v0.7.3.1.tar.gz#egg=dslink-0.7.3.1"
    ]
)
