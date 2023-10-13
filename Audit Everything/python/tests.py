import unittest
from collections import defaultdict
from datetime import datetime
from pathlib import PurePath

from audit_everything import AuditManager, FileSystem


class MockFileSystem(FileSystem):
    def __init__(self, files):
        self.files = defaultdict(str, files)

    def get_files(self, dir_name: PurePath | str) -> list[str]:
        return list(self.files)

    def write_all_text(self, path: PurePath | str, content: str) -> None:
        self.files[str(path)] = content

    def read_all_lines(self, path: PurePath | str) -> list[str]:
        return self.files[str(path)].splitlines()


class Tests(unittest.TestCase):
    def test_a_new_audit_file_is_created_when_the_current_file_overflows(self):
        # Arrange
        original_files = {
            "audits/audit_2.txt": (
                "Alex;2019-04-06 16:30:00\n"
                "Bryn;2019-04-06 16:40:00\n"
                "Chris;2019-04-06 17:00:00\n"
            ),
            "audits/audit_1.txt": (
                "Peter;2019-04-06 16:30:00\n"
                "Jane;2019-04-06 16:40:00\n"
                "Jack;2019-04-06 17:00:00\n"
            ),
        }
        file_system = MockFileSystem(dict(original_files))
        audits = AuditManager(3, 'audits', file_system)

        # Act
        audits.add_record(
            'Alice', datetime.fromisoformat('2019-04-06T18:00:00')
        )

        # Assert
        self.assertEqual(
            file_system.files,
            original_files | {"audits/audit_3.txt": "Alice;2019-04-06 18:00:00"}
        )

    def test_a_new_audit_file_is_created_in_an_empty_directory(self):
        # Arrange
        file_system = MockFileSystem({})
        audits = AuditManager(3, 'audits', file_system)

        # Act
        audits.add_record(
            'Alice', datetime.fromisoformat('2019-04-06T18:00:00')
        )

        # Assert
        self.assertEqual(
            file_system.files,
            {"audits/audit_1.txt": "Alice;2019-04-06 18:00:00"}
        )

    def test_files_that_do_not_match_the_audit_format_are_ignored(self):
        # Arrange
        original_files = {
            "audits/audit_2.txt": (
                "Alex;2019-04-06 16:30:00\n"
                "Bryn;2019-04-06 16:40:00\n"
                "Chris;2019-04-06 17:00:00\n"
            ),
            "audits/audit_1.txt": (
                "Peter;2019-04-06 16:30:00\n"
                "Jane;2019-04-06 16:40:00\n"
                "Jack;2019-04-06 17:00:00\n"
            ),
            "audits/audit_3OLD.txt": "",
        }
        file_system = MockFileSystem(dict(original_files))
        audits = AuditManager(3, 'audits', file_system)

        # Act
        audits.add_record(
            'Alice', datetime.fromisoformat('2019-04-06T18:00:00')
        )

        # Assert
        self.assertEqual(
            file_system.files,
            original_files | {"audits/audit_3.txt": "Alice;2019-04-06 18:00:00"}
        )


if __name__ == '__main__':
    unittest.main()
