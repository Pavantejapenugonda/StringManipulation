import pytest
from main2 import change_the_directory

@pytest.mark.parametrize("current_path, new_path, expected", [
    ("/","abc", "/abc"),
    ("/abc/def", "ghi", "/abc/def/ghi"),
    ("/abc/def", "..","/abc"),
    ("/abc/def", "/abc", "/abc"),
    ("/abc/def", "/abc/klm", "/abc/klm"),
    ("/abc/def", "../..", "/"),
    ("/abc/def", "../../..", "/"),
    ("/abc/def", ".", "/abc/def"),
    ("/abc/def", "..klm", "..klm: No such file or directory"),
    ("/abc/def", "//////", "/"),
    ("/abc/def", "......", "......: No such file or directory"),
    ("/abc/def", "../gh///../klm/.", "/abc/klm"),
    ("/", "......", "......: No such file or directory"),
    ("/", "a/b/c/./d", "/a/b/c/d"),
    ("/", "a/b/c/../d", "/a/b/d"),
    ("/","a/..", "/")
])
def test_change_the_directory(current_path, new_path, expected):
    assert change_the_directory(current_path, new_path) == expected