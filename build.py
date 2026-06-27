"""Build the GUI app with Nuitka.

Run:
    D:\\miniconda3\\envs\\SUEP\\python.exe build.py
"""
import sys


def main():
    sys.argv = [
        "nuitka",
        "--standalone",
        "--include-data-dir=frontend=frontend",
        "--jobs=4",
        "--lto=no",
        "--include-package=backend",
        "--include-package=ids",
        "--include-package=_jsonnet",
        "--include-package=lxml",
        "--include-package=uvicorn",
        "--enable-plugin=anti-bloat",
        "--nofollow-import-to=tkinter",
        "--nofollow-import-to=PIL",
        "--nofollow-import-to=matplotlib",
        "--windows-console-mode=force",
        "--output-dir=dist",
        "--windows-product-name=Course Elect Terminal",
        "--windows-file-version=0.2.0",
        "--windows-product-version=0.2.0",
        "app.py",
    ]
    import nuitka.__main__

    nuitka.__main__.main()


if __name__ == "__main__":
    main()
