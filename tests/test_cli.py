import pytest

from pgbackup import cli

url = "postgres://bogdan:password@example.com:5432/db_one"

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    # what follows is a docstring
    """
    the parser will exit if a driver is not specified
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):
    """
    the parser will exit if it receives a driver withouth a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

# happy path test
def test_parser_with_driver_and_destination(parser):
    """
    the parser will not exit if it receives a driver and a destination
    """
    args = parser.parse_args([url, "--driver", "local", "/some/path"])
    assert args.driver == "local"
    assert args.destination == "/some/path"

def test_parser_with_unknown_driver(parser):
    """
    the parser will exit if the driver name is unknown
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", "destination"])

def test_parser_with_known_driver(parser):
    """
    the parser will not exit if the driver is known
    """
    for driver in ["local", "s3"]:
        assert parser.parse_args([url, "--driver", driver, "destination"])

