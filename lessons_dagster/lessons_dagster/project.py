from pathlib import Path

from dagster_dbt import DbtProject

lessons_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..","lessons").resolve(),
)
lessons_project.prepare_if_dev()