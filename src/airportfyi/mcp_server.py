"""MCP server for airportfyi — AI assistant tools for airportfyi.com.

Run: uvx --from "airportfyi[mcp]" python -m airportfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AirportFYI")


@mcp.tool()
def list_airports(limit: int = 20, offset: int = 0) -> str:
    """List airports from airportfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from airportfyi.api import AirportFYI

    with AirportFYI() as api:
        data = api.list_airports(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No airports found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_airport(slug: str) -> str:
    """Get detailed information about a specific airport.

    Args:
        slug: URL slug identifier for the airport.
    """
    from airportfyi.api import AirportFYI

    with AirportFYI() as api:
        data = api.get_airport(slug)
        return str(data)


@mcp.tool()
def list_airlines(limit: int = 20, offset: int = 0) -> str:
    """List airlines from airportfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from airportfyi.api import AirportFYI

    with AirportFYI() as api:
        data = api.list_airlines(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No airlines found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_airport(query: str) -> str:
    """Search airportfyi.com for airports, airlines, IATA/ICAO codes, and routes.

    Args:
        query: Search query string.
    """
    from airportfyi.api import AirportFYI

    with AirportFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
