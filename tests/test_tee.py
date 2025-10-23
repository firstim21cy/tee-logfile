import shutil
from pathlib import Path

from tee_logfile.tee import Tee

ROOT_PATH = Path(__file__).resolve().parent.parent


def test_tee_str():
    temp_dir = ROOT_PATH / 'tests' / 'temp'
    log_file = temp_dir / 'test.log'
    with Tee.context(str(log_file)):
        print('This is a test message.')
        print('Another line of output.')

    assert True


def test_tee():
    temp_dir = ROOT_PATH / 'tests' / 'temp'
    log_file = temp_dir / 'test.log'
    with Tee.context(log_file.resolve()):
        print('This is a test message.')
        print('Another line of output.')

    assert True


def test_tee_rm():
    temp_dir = ROOT_PATH / 'tests' / 'temp'
    log_file = temp_dir / 'test.log'

    if temp_dir.exists():
        shutil.rmtree(temp_dir)

    with Tee.context(log_file):
        print('This is a test message.')
        print('Another line of output.')

    assert True
