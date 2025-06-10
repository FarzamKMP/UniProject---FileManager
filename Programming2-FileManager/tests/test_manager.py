import os
import tempfile
import pytest
from file_manager.manager import FileManager, MultiFileManager

def make_file(path: str, content: str):
    with open(path, 'w') as f:
        f.write(content)

def test_path_setter_and_getter(tmp_path):
    bad = tmp_path / "nope.txt"
    with pytest.raises(FileNotFoundError):
        FileManager(str(bad))

def test_lines_and_str_and_file_size(tmp_path):
    f = tmp_path / "a.txt"
    make_file(str(f), "Line1\nLine2\n")
    fm = FileManager(str(f))
    assert list(fm.lines()) == ["Line1\n", "Line2\n"]
    assert "FileManager(" in str(fm)
    assert FileManager.file_size(str(f)) == os.path.getsize(str(f))

def test_from_dir(tmp_path):
    sub = tmp_path / "sub"
    sub.mkdir()
    f = sub / "b.txt"
    make_file(str(f), "X")
    fm = FileManager.from_dir(str(sub), "b.txt")
    assert isinstance(fm, FileManager)
    assert fm.path == str(f)

def test_add_operator(tmp_path):
    f1 = tmp_path / "f1.txt"
    f2 = tmp_path / "f2.txt"
    make_file(str(f1), "A\n")
    make_file(str(f2), "B\n")
    fm1 = FileManager(str(f1))
    fm2 = FileManager(str(f2))
    fm3 = fm1 + fm2
    data = open(fm3.path).read()
    assert data == "A\nB\n"

def test_concat_many(tmp_path):
    f1 = tmp_path / "x1.txt"
    f2 = tmp_path / "x2.txt"
    f3 = tmp_path / "x3.txt"
    make_file(str(f1), "1\n")
    make_file(str(f2), "2\n")
    make_file(str(f3), "3\n")
    mfm = MultiFileManager(str(f1))
    fm_out = mfm.concat_many(str(f2), str(f3))
    assert open(fm_out.path).read() == "1\n2\n3\n"

if __name__ == "__main__":
    pytest.main()
