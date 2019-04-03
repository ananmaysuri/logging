from setuptools import setup, find_packages

setup(
    name="asv_python_configure",
    version=version,
    description="Logger",
    long_description=readme,
    long_description_type="text/markdown",
    author="Ananmay Suri",
    author_email="ananmaysuri2000@gmail.com",
    url="",
    packages=["logging"],
    include_package_data=True,
    install_requires=requirements,
    license="BSD-3-Clause",
    zip_safe=True,
    keywords="asv_mq"
)
