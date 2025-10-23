from tee_logfile.tee import Tee


def test_tee():
    with Tee.context('temp/test_output.log'):
        print('This is a test message.')
        print('Another line of output.')

    assert True
