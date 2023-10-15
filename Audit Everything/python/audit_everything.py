import abc
import re
from datetime import datetime
from pathlib import PurePath


# I have vaguely assumed this interface is for some reason largely unchangeable
# and is depended on beyond the scope of the audit manager
class FileSystem(abc.ABC):
    @abc.abstractmethod
    def get_files(self, dir_name: PurePath | str) -> list[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def write_all_text(self, new_file: PurePath | str, content: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def read_all_lines(self, path: PurePath | str) -> list[str]:
        raise NotImplementedError

    def append(self, path: PurePath | str, content: str) -> None:
        self.write_all_text(
            path,
            "\n".join((
                *self.read_all_lines(path),
                content,
            ))
        )

    def num_lines_in_file(self, file) -> int:
        return len(self.read_all_lines(file))


class Visit:
    time_fmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self, name: str, time: datetime):
        self.name = name
        self.time = time

    def format(self):
        return f"{self.name};{self.time.strftime(self.time_fmt)}"


class AuditManager:
    _audit_filename_template = "audit_{}.txt"
    _audit_filename_regex = r"audit_\d+.txt"

    def __init__(
          self,
          max_entries_per_file: int,
          directory_name: str,
          file_system: FileSystem,
    ):
        self._max_entries_per_file = max_entries_per_file
        self._directory = PurePath(directory_name)
        self._file_system = file_system

    def add_record(self, visitor_name: str, time_of_visit: datetime) -> None:
        self._file_system.append(
            self._next_available_file(),
            Visit(visitor_name, time_of_visit).format()
        )

    def _audit_files(self) -> list[PurePath]:
        paths = self._file_system.get_files(self._directory)
        paths = [PurePath(file) for file in paths]
        paths = [path for path in paths if path.is_relative_to(self._directory)]
        paths = [path for path in paths
                 if re.match(self._audit_filename_regex, path.name)]
        return sorted(paths)

    def _new_audit_file(self) -> PurePath:
        audit_file_number = len(self._audit_files()) + 1
        new_file = self._audit_filename_template.format(audit_file_number)
        return self._directory / new_file

    def _next_available_file(self) -> PurePath:
        file_paths = self._audit_files()
        has_capacity = (
              file_paths
              and (self._file_system.num_lines_in_file(file_paths[-1])
                   < self._max_entries_per_file)
        )
        if has_capacity:
            return file_paths[-1]
        else:
            return self._new_audit_file()
