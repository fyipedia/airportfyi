"""MCP server for airportfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from airportfyi.api import AirportFYI

mcp = FastMCP("airportfyi")


@mcp.tool()
def search_airportfyi(query: str) -> dict[str, Any]:
    """Search airportfyi.com for content matching the query."""
    with AirportFYI() as api:
        return api.search(query)
