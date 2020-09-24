import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://bogdan:password@example.com:5432/db_one"

def test_dump_call_pg_dump(mocker):
    """
    use pg_dump to interact with the database
    """
    proc = mocker.Mock()
    mocker.patch("subprocess.Popen", return_value=proc)
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(["pg_dump", url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump is not installed
    """
    mocker.patch("subprocess.Popen", side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

