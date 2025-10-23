import shutil
from pathlib import Path

from tee_logfile.tee import Tee

ROOT_PATH = Path(__file__).resolve().parent.parent

import pytest
from pathlib import Path
import shutil

@pytest.fixture
def temp_dir():
    path = ROOT_PATH / 'tests' / 'temp'
    # path.mkdir(exist_ok=True)
    yield path
    if path.exists():
        shutil.rmtree(path)

@pytest.fixture
def log_file(temp_dir):
    file_path = temp_dir / "test.log"
    yield file_path
    if file_path.exists():
        file_path.unlink()

def test_tee_str(log_file):

    with Tee.context(str(log_file)):
        print('This is a test message.')
        print('Another line of output.')

    content = log_file.read_text()
    assert "Another line of output." in content


def test_tee(log_file):

    with Tee.context(log_file.resolve()):
        print('This is a test message.')
        print('Another line of output.')

    content = log_file.read_text()
    assert "Another line of output." in content


def test_tee_rm(temp_dir):
    log_file = temp_dir / 'test.log'

    if temp_dir.exists():
        shutil.rmtree(temp_dir)

    with Tee.context(log_file):
        print('This is a test message.')
        print('Another line of output.')

    content = log_file.read_text()
    assert "Another line of output." in content
