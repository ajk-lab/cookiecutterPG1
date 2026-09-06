# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Metadata
- Author: {{ cookiecutter.author_name }}
- Email: {{ cookiecutter.author_email }}
- Version: {{ cookiecutter.version }}
- Python: {{ cookiecutter.python_version }}
- Spark App Name: {{ cookiecutter.spark_app_name }}

## Project Structure

- conf/
- notebooks/
- src/{{ cookiecutter.package_name }}/
- tests/
- data/
- logs/
- spark-warehouse/
- spark-local/
- scripts/
- docs/

## Getting Started

1. Create a virtual environment
2. Install dependencies
3. Open notebooks or run jobs from src/{{ cookiecutter.package_name }}/jobs

## Main Package

src/{{ cookiecutter.package_name }}/
