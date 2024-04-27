from datetime import datetime
from pprint import pformat

from approvaltests import verify

from audit_everything.audit import AuditManager
from utils import InMemoryFileSystem, test


@test
def audit_will_create_an_initial_audit_file_in_an_empty_directory():
    file_system = InMemoryFileSystem({})
    sut = AuditManager(3, "audits", file_system)
    sut.add_record("Alice", datetime.fromisoformat("2019-04-06T18:00:00"))
    verify(pformat(file_system.files))


@test
def audit_will_append_to_the_latest_file_when_it_has_not_overflowed():
    file_system = InMemoryFileSystem({
        "audits/audit_1.txt": (
            "Peter;2019-04-06 16:30:00\n"
            "Jane;2019-04-06 16:40:00\n"
            "Jack;2019-04-06 17:00:00"
        ),
        "audits/audit_2.txt": (
            "Peter;2019-04-06 16:30:00\n"
            "Jane;2019-04-06 16:40:00"
        ),
    })

    sut = AuditManager(3, "audits", file_system)
    sut.add_record("Alice", datetime.fromisoformat("2019-04-06T18:00:00"))
    verify(pformat(file_system.files))


@test
def audit_will_overflow_to_a_new_file_when_max_number_is_reached():
    file_system = InMemoryFileSystem({
        "audits/audit_1.txt": (
            "Peter;2019-04-06 16:30:00\n"
            "Jane;2019-04-06 16:40:00\n"
            "Jack;2019-04-06 17:00:00"
        ),
        "audits/audit_2.txt": (
            "Peter;2019-04-06 16:30:00\n"
            "Jane;2019-04-06 16:40:00\n"
            "Jack;2019-04-06 17:00:00"
        ),
    })

    sut = AuditManager(3, "audits", file_system)
    sut.add_record("Alice", datetime.fromisoformat("2019-04-06T18:00:00"))
    verify(pformat(file_system.files))


@test
def audit_does_not_rely_on_file_ordering_when_selecting_the_latest_file():
    file_system = InMemoryFileSystem({
        "audits/audit_2.txt": (
            "Peter;2019-04-06 16:30:00\n"
            "Jane;2019-04-06 16:40:00"
        ),
        "audits/audit_1.txt": (
            "Peter;2019-04-06 16:30:00\n"
            "Jane;2019-04-06 16:40:00\n"
            "Jack;2019-04-06 17:00:00"
        ),
    })

    sut = AuditManager(3, "audits", file_system)
    sut.add_record("Alice", datetime.fromisoformat("2019-04-06T18:00:00"))
    verify(pformat(file_system.files))


@test
def audit_can_create_multiple_files_after_repeated_additions():
    file_system = InMemoryFileSystem({
        "audits/audit_1.txt": (
            "Jane;2019-04-06 16:40:00\n"
            "Jack;2019-04-06 17:00:00"
        ),
        "audits/audit_2.txt": (
            "Peter;2019-04-06 16:30:00\n"
        ),
    })

    sut = AuditManager(2, "audits", file_system)

    sut.add_record("Alex", datetime.fromisoformat("2019-04-06T18:00:00"))
    sut.add_record("Bryn", datetime.fromisoformat("2019-04-06T18:01:00"))
    sut.add_record("Chris", datetime.fromisoformat("2019-04-06T18:02:00"))
    sut.add_record("Dana", datetime.fromisoformat("2019-04-06T18:03:00"))

    verify(pformat(file_system.files))


@test
def audit_sorts_files_by_their_number():
    file_system = InMemoryFileSystem({
        "audits/audit_1.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_2.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_3.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_4.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_5.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_6.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_7.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_8.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_9.txt": "A;2019-04-06 16:40:00\nB;2019-04-06 17:00:00",
        "audits/audit_10.txt": "A;2019-04-06 16:40:00",
    })

    sut = AuditManager(2, "audits", file_system)

    sut.add_record("Alex", datetime.fromisoformat("2019-04-06T18:00:00"))
    sut.add_record("Bryn", datetime.fromisoformat("2019-04-06T18:01:00"))
    sut.add_record("Chris", datetime.fromisoformat("2019-04-06T18:02:00"))

    verify(pformat(file_system.files))
