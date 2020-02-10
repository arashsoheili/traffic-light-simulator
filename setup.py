from setuptools import setup

setup(
    name="TrafficLight",
    version="0.1",
    description="Traffic Light Simulator",
    url="https://github.com/arashsoheili/traffic-light-simulator",
    author="Arash Soheili",
    author_email="me@arashsoheili.com",
    packages=["app"],
    include_package_data=False,
    license="MIT",
    install_requires=["colorama"],
    extras_require={"test": ["pytest", "pytest-pep8",]},
    entry_points={"console_scripts": ["trafficlight=app.__main__:main"]},
    python_requires=">3.6.0",
)
