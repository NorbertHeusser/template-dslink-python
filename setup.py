from setuptools import setup

setup(
    name="dslink-python-template",
    version="0.2.1",
    description="Python DSLink Template",
    url="http://github.com/IOT-DSA/template-dslink-python",
    author="Logan Gorence",
    author_email="Logan.Gorence@AcuityBrands.com",
    license="Apache 2.0",
    install_requires=[
        "dslink == 0.7.2"
    ],
    dependency_links=[
        "https://github.com/IOT-DSA/sdk-dslink-python/archive/v0.7.1.tar.gz#egg=dslink-0.7.2"
    ]
)
