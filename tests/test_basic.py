"""Basic tests for airportfyi."""

from airportfyi import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"
