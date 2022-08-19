from pathlib import Path
from setuptools.command.build_py import build_py


class BuildPyCommand(build_py):
    def run(self):
        Path('poetry_build_issue/generated/file.py').touch()
        return super().run()


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "cmdclass": {
                "build_py": BuildPyCommand,
            },
        }
    )
