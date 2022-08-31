"""
Module which houses all path related functions.
"""
import os


def construct_path(
    project_path: str, directory_paths: list[str], filename: str = ""
) -> str:
    """
    Function which constructs path from the root project directory
    path with arbitrary directory nesting
    """
    return (
        os.path.join(project_path, *directory_paths)
        if filename == ""
        else f"{os.path.join(project_path, *directory_paths)}/{filename}"
    )


def create_path(
    project_path: str, paths: list[str], directory_mode: bool = True
) -> None:
    """
    Creates files and folders from constructed paths
    """
    for refs in paths:
        if isinstance(refs, dict):
            top_level_dir = list(refs.keys())[0]
            for subref in list(refs.values())[0]:
                os.makedirs(construct_path(project_path, [top_level_dir, subref]))

        else:
            if directory_mode:
                os.makedirs(construct_path(project_path, [refs]))
            else:
                with open(
                    construct_path(project_path, [refs]),
                    "w",
                    encoding="utf-8",
                ):
                    pass
