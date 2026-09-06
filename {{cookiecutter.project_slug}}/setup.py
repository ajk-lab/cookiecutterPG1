from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.project_description }}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">={{ cookiecutter.python_version }}",
)
