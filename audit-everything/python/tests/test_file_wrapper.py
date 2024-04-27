import re
from pprint import pformat

from approvaltests import verify

from audit_everything.file_utils import FileWrapper
from utils import InMemoryFileSystem, test


@test
def a_file_wrapper_returns_empty_defaults_for_non_existent_files():
    file_system = InMemoryFileSystem({})

    sut = FileWrapper(file_system, "root_dir")

    assert sut.list_matching(re.compile(r".*")) == []
    assert sut.file_length("a_file.txt") == 0
    assert sut.file_lines("a_file.txt") == []


@test
def a_file_wrapper_returns_the_content_of_files():
    file_system = InMemoryFileSystem({"root_dir/a_file.txt": "line 1\nline 2"})

    sut = FileWrapper(file_system, "root_dir")

    assert sut.list_matching(re.compile(r".*\.txt")) == ["a_file.txt"]
    assert sut.file_length("a_file.txt") == 2
    assert sut.file_lines("a_file.txt") == ["line 1", "line 2"]


@test
def a_file_wrapper_creates_a_new_file_when_appending_to_a_nonexistent_file():
    file_system = InMemoryFileSystem({})
    sut = FileWrapper(file_system, "root_dir")
    sut.append_to("a_file.txt", "some new text")
    verify(pformat(file_system.files))


@test
def a_file_wrapper_appends_to_existing_files():
    file_system = InMemoryFileSystem({"root_dir/a_file.txt": "line 1"})
    sut = FileWrapper(file_system, "root_dir")
    sut.append_to("a_file.txt", "some new text")
    verify(pformat(file_system.files))
