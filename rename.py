import os
from pathlib import Path


def prefix_files(directory, prefix):
    """
    Objective : Prefix files splitted manually between music and voice with target name
    Input : Directory path, prefix (string)
    Output : Files prefixed in target directory
    """
    for filepath in list(Path(directory).glob("*")):
        Path.rename(filepath, filepath.parent / (prefix + filepath.name))
    return True


directory = Path("raw_data/Dataset/Voix/")
directory2 = Path("raw_data/Dataset/Musique")
directory2
prefix = "voice"
prefix2 = "music"

# prefix_files(directory2, prefix2)
