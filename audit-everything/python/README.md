# Audit Everything (Python)

Kata from: <https://sammancoaching.org/kata_descriptions/audit.html>

Starting Code from: <https://github.com/katalogs/audit-kata/tree/main/python>

## Comments

For this kata, I started by writing some approval tests with an in-memory file
system implementation. This kata originally started with a test case that used a
mock object to test the file system, but I felt it would be easiest to use a
simple in-memory file system and approval tests. These tests revealed a bug in
the way the `AuditManager` sorts files (i.e. using alphabetical sorting rather
than sorting the audit files by their number).

Once I had some tests in place, I started to refactor the `AuditManager`. I
found this quite awkward as the `AuditManager` was really handling two
intertwined responsibilities in one class—writing audits to the correct file,
and checking and setting file contents. After refactoring a few methods, I felt
I had separated these two responsibilities enough to be able to create a
new `FileWrapper` class that extends the simple `FileManager` functionality.
This meant the `Audit` manager class could just focus on managing audits.

In this refactoring exercise, I also decided to fix the previously mentioned
bug. If this were a real legacy system, I probably wouldn't do this—but since
this is an exercise, I took the liber to change the functionality. Other than
this, all public interfaces and functionality have stayed the same.

### Pain Points

Since this is a simple exercise, I haven't focused too much on "real-world"
issues. One glaring issue with the project as it is, is that it assumes the file
system will always be in a correct state (i.e. no files will be manually
added, deleted, or changed) and that reads and writes will always pass.
It's not clear what the `AuditManager` should do if the file system is in some
kind of error state.

Another smaller issue is that currently the `Record` logic is tied up in
the `AuditManager` class. I am not sure if it is worth it to refactor this into
a separate `Record` class or data class.

The tests for this project are also quite simple in that the approvals merely
dump the file system to be verified. I did toy with the idea of adding a
given-when-then helper class to help format the approval test cases, but decided
the added verbosity of the test cases was not worth it for this project.
