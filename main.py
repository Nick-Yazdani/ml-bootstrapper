"""
Main execution script that runs the project creation tool end to end.
"""
import os

from subprocess import Popen
from argparse import ArgumentParser
from itertools import repeat

from src.structures import FILE_STRUCTURE, DIRECTORY_STRUCTURE
from src.pathgen import create_path

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-o",
        "--output-dir",
        dest="output_dir",
        type=str,
        required=True,
        help="Path to root project directory",
    )
    parser.add_argument(
        "-C",
        "--create",
        action="store_true",
        dest="creation",
        default=False,
        required=False,
        help="Creates root project directory if it does not already exist",
    )

    parser.add_argument(
        "-G",
        "--git",
        action="store_true",
        dest="git",
        default=False,
        required=False,
        help="Initialises project directory as a git repository automagically",
    )

    args = parser.parse_args()

    ROOT_DIR_PATH = args.output_dir
    CREATE_PROJECT_DIR = args.creation
    INIT_GIT_REPO = args.git

    # 1. Check if project dir exists or not, handle accordingly based on flags

    if not os.path.exists(ROOT_DIR_PATH) and not CREATE_PROJECT_DIR:
        raise FileNotFoundError(
            """Project directory does not exist,
        please pass the -C or --create flag to force creation of new directory"""
        )

    if os.path.exists(ROOT_DIR_PATH) and CREATE_PROJECT_DIR:
        raise FileExistsError(
            """Project directory exists and -C or --create flag was passed.
        Please manually delete the project if you wish to start fresh and then re-run the tool.
        """
        )

    # 2. Create directories, sub-directories and empty files.

    any(
        map(
            create_path,
            repeat(ROOT_DIR_PATH),
            [DIRECTORY_STRUCTURE, FILE_STRUCTURE],
            [True, False],
        )
    )

    # 3. Check if user wants to initialize git repo automagically and act accordingly

    if INIT_GIT_REPO:
        os.chdir(ROOT_DIR_PATH)

        with Popen(["git", "init"]) as p:
            pass
