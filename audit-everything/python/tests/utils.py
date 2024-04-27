from collections.abc import Callable
from dataclasses import dataclass
from inspect import FrameInfo
from pathlib import PurePath
from types import FunctionType

from approvaltests import StackFrameNamer
from approvaltests.pytest.pytest_config import PytestConfig

from audit_everything.file_system import FileSystem


def test[F: Callable](func: F) -> F:
    setattr(func, "__test__", True)
    return func


# Hack to get around approvaltest test discovery
# See: https://github.com/approvals/ApprovalTests.Python/issues/161
def _is_marked_with_test_dunder(maybe_function: FunctionType | None) -> bool:
    return (
          maybe_function is not None
          and hasattr(maybe_function, "__test__")
          and getattr(maybe_function, "__test__")
    )


# noinspection PyProtectedMember
def is_pytest_test(frame: FrameInfo) -> bool:
    method_name = frame[3]
    frame_globals = frame.frame.f_globals
    maybe_function = frame_globals.get(method_name)
    patterns = PytestConfig.test_naming_patterns
    return (
          StackFrameNamer._is_match_for_pytest(method_name, patterns)
          or StackFrameNamer._is_marked_with_test_dunder(maybe_function)
    )


StackFrameNamer._is_marked_with_test_dunder = _is_marked_with_test_dunder
StackFrameNamer.is_pytest_test = is_pytest_test


@dataclass
class InMemoryFileSystem(FileSystem):
    files: dict[str, str]

    def get_files(self, dir_name: str):
        return [
            filename for filename in self.files
            if PurePath(filename).is_relative_to(dir_name)
        ]

    def write_all_text(self, new_file: str, content: str):
        self.files[new_file] = content

    def read_all_lines(self, path: str):
        return self.files[path].splitlines()
