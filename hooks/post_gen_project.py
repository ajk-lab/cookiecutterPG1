import shutil
from pathlib import Path

PROJECT_ROOT = Path.cwd()

def remove_path(relative_path: str):
    path = PROJECT_ROOT / relative_path
    if not path.exists():
        return

    if path.is_dir():
        shutil.rmtree(path)
        print(f"Removed directory: {relative_path}")
    else:
        path.unlink()
        print(f"Removed file: {relative_path}")

def is_no(value: str) -> bool:
    return value.strip().lower() == "no"

if is_no("{{ cookiecutter.use_setup_py }}"):
    remove_path("setup.py")

if is_no("{{ cookiecutter.use_pyproject_toml }}"):
    remove_path("pyproject.toml")

if is_no("{{ cookiecutter.use_notebooks }}"):
    remove_path("notebooks")

if is_no("{{ cookiecutter.use_tests }}"):
    remove_path("tests")

if is_no("{{ cookiecutter.use_docs }}"):
    remove_path("docs")

if is_no("{{ cookiecutter.use_scripts }}"):
    remove_path("scripts")

if is_no("{{ cookiecutter.use_sample_data }}"):
    remove_path("data/sample")

if is_no("{{ cookiecutter.use_sql_folder }}"):
    remove_path("src/{{ cookiecutter.package_name }}/sql")

if is_no("{{ cookiecutter.include_logs_folder }}"):
    remove_path("logs")

if is_no("{{ cookiecutter.include_spark_runtime_dirs }}"):
    remove_path("spark-warehouse")
    remove_path("spark-local")
