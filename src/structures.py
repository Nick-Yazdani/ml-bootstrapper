"""
This file holds all constants, initially created to house the lists of
directories, sub-directories and boilerplate filenames.
"""
DIRECTORY_STRUCTURE = [
    {"data": ["external", "interim", "processed", "raw"]},
    "models",
    "notebooks",
    "references",
    {"reports": ["figures"]},
    {"src": ["data", "features", "models", "visualisation"]},
]

FILE_STRUCTURE = [
    "LICENSE",
    "Makefile",
    "README.md",
    "requirements.txt",
    "setup.py",
    "src/__init__.py",
    "src/data/make_dataset.py",
    "src/features/build_features.py",
    "src/models/predict_model.py",
    "src/models/train_model.py",
    "src/models/predict_model.py",
    "src/visualisation/visualisation.py"
]
