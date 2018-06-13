import os

from .core import File
from .ignored import IgnoredFile
from .html import HTMLFile
from .scss import SCSSFile


def file_class_for_path(path):
    _, ext = os.path.splitext(path)

    if os.path.basename(path).startswith('_'):
        return IgnoredFile

    classes = {
        '.html': HTMLFile,
        '.scss': SCSSFile,
    }

    if ext in classes:
        return classes[ext]

    return File
