import os
import re
from pathlib import PurePath


class FileWrapper:
    def __init__(self, file_system, root):
        self.file_system = file_system
        self.root = root

    def list_matching(self, pattern: re.Pattern) -> list[str]:
        return [
            str(PurePath(path).relative_to(self.root))
            for path in self.file_system.get_files(self.root)
            if pattern.match(path)
        ]

    def file_length(self, path: str) -> int:
        return len(self.file_lines(path))

    def file_lines(self, path: str) -> list[str]:
        path = self.join_relative_to_root(path)
        if path in self.file_system.get_files(self.root):
            return self.file_system.read_all_lines(path)
        else:
            return []

    def append_to(self, path: str, line: str) -> None:
        self.file_system.write_all_text(
            self.join_relative_to_root(path),
            "\n".join((*self.file_lines(path), line)),
        )

    def join_relative_to_root(self, filename: str) -> str:
        return os.path.join(self.root, filename)
