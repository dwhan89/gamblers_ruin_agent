"""Python setup.py for gamblers_ruin_agent package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("gamblers_ruin_agent", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="gamblers_ruin_agent",
    version=read("gamblers_ruin_agent", "VERSION"),
    description="Awesome gamblers_ruin_agent created by dwhan89",
    url="https://github.com/dwhan89/gamblers_ruin_agent/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="dwhan89",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["gamblers_ruin_agent = gamblers_ruin_agent.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
