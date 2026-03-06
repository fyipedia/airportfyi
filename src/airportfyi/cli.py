"""Command-line interface for airportfyi."""

from __future__ import annotations

import json

import typer

from airportfyi.api import AirportFYI

app = typer.Typer(help="AirportFYI — Airport codes, routes and aviation data API client.")


@app.command()
def search(query: str) -> None:
    """Search airportfyi.com."""
    with AirportFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
