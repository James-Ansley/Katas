import re
from datetime import datetime
from typing import Final

from audit_everything.file_system import FileSystem
from audit_everything.file_utils import FileWrapper


class AuditManager:
    audit_regex: Final[re.Pattern] = re.compile(r".*audit_(\d+)\.txt")
    audit_format: Final[str] = "audit_{}.txt"
    record_fmt: Final[str] = "{};{:%Y-%m-%d %H:%M:%S}"

    def __init__(
          self,
          max_entries_per_file: int,
          directory_name: str,
          file_system: FileSystem,
    ):
        self._max_entries_per_file: Final[int] = max_entries_per_file
        self._files = FileWrapper(file_system, directory_name)

    def add_record(self, visitor_name: str, time_of_visit: datetime) -> None:
        record = self.record_fmt.format(visitor_name, time_of_visit)
        audit_path = self._next_available_path()
        self._files.append_to(audit_path, record)

    def _next_available_path(self) -> str:
        result = self._last_audit_path()
        if result is None:
            return self._format_audit_path(1)
        elif self._can_append_to(result):
            return result
        else:
            next_audit_number = self._audit_number_from_path(result) + 1
            return self._format_audit_path(next_audit_number)

    def _last_audit_path(self) -> str | None:
        files = self._files.list_matching(self.audit_regex)
        if files:
            return max(files, key=self._audit_number_from_path)
        else:
            return None

    def _can_append_to(self, audit_path) -> bool:
        return self._files.file_length(audit_path) < self._max_entries_per_file

    def _format_audit_path(self, number):
        return self.audit_format.format(number)

    @classmethod
    def _audit_number_from_path(cls, path):
        return int(cls.audit_regex.match(path).group(1))
