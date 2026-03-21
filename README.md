# airportfyi

[![PyPI version](https://agentgif.com/badge/pypi/airportfyi/version.svg)](https://pypi.org/project/airportfyi/)
[![Python](https://img.shields.io/pypi/pyversions/airportfyi)](https://pypi.org/project/airportfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/airportfyi/)

Python API client for global airport data. Look up 4,500+ airports by IATA/ICAO code, query runway specifications, explore terminal configurations, and retrieve geographic coordinates — all from [AirportFYI](https://airportfyi.com/), an airport reference platform with comprehensive data on commercial and regional airports worldwide.

Built on authoritative aviation data sources, AirportFYI covers IATA/ICAO code assignments, airport classifications (international hub, regional, domestic), runway dimensions, elevation, timezone, and country information — used by travel-tech developers, flight tracking apps, and aviation data platforms.

> **Explore airports at [airportfyi.com](https://airportfyi.com/)** — browse by [country](https://airportfyi.com/countries/), search by [IATA code](https://airportfyi.com/airports/), and view airport details.

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/airportfyi/main/demo.gif" alt="airportfyi demo — airport lookup, IATA/ICAO codes, and route data in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [IATA and ICAO Codes](#iata-and-icao-codes)
  - [Airport Classifications](#airport-classifications)
  - [Runway and Elevation Data](#runway-and-elevation-data)
  - [Geographic and Timezone Data](#geographic-and-timezone-data)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Airports](#learn-more-about-airports)
- [Also Available](#also-available)
- [Transport FYI Family](#transport-fyi-family)
- [License](#license)

## Install

```bash
pip install airportfyi                # Core (zero deps)
pip install "airportfyi[cli]"         # + Command-line interface
pip install "airportfyi[mcp]"         # + MCP server for AI assistants
pip install "airportfyi[api]"         # + HTTP client for airportfyi.com API
pip install "airportfyi[all]"         # Everything
```

## Quick Start

```python
from airportfyi.api import AirportFYI

with AirportFYI() as api:
    # Look up airport by IATA code
    icn = api.get_airport("incheon-international")
    print(icn["iata"])           # ICN
    print(icn["icao"])           # RKSI
    print(icn["city"])           # Seoul
    print(icn["country"])        # South Korea

    # List airports by country
    airports = api.list_airports(country="japan")
    for a in airports:
        print(f"{a['iata']} — {a['name']}")

    # Search airports globally
    results = api.search("heathrow")
```

## What You Can Do

### IATA and ICAO Codes

Every commercial airport is assigned two identification codes. The **IATA code** (3 letters) is used on boarding passes and booking systems — familiar codes like LAX, JFK, NRT. The **ICAO code** (4 letters) is used in flight plans and air traffic control — KLAX, KJFK, RJTT. The first letter(s) of ICAO codes indicate the geographic region.

| ICAO Prefix | Region | Examples |
|-------------|--------|---------|
| K | Contiguous United States | KJFK, KLAX, KORD |
| C | Canada | CYYZ, CYVR |
| EG | United Kingdom | EGLL (Heathrow), EGKK (Gatwick) |
| LF | France | LFPG (CDG), LFPO (Orly) |
| RJ | Japan (mainland) | RJTT (Haneda), RJAA (Narita) |
| RK | South Korea | RKSI (Incheon), RKSS (Gimpo) |
| Z | China (mainland) | ZBAA (Beijing), ZSPD (Pudong) |
| WS | Singapore | WSSS (Changi) |

```python
from airportfyi.api import AirportFYI

with AirportFYI() as api:
    # Look up by IATA code
    results = api.search("ICN")
    airport = results[0]
    print(f"{airport['iata']}/{airport['icao']} — {airport['name']}")
    # ICN/RKSI — Incheon International Airport
```

Learn more: [Airport Directory](https://airportfyi.com/airports/) · [Glossary](https://airportfyi.com/glossary/)

### Airport Classifications

Airports are classified by traffic volume, runway capability, and role in the air transport network. Major international hubs handle 40M+ passengers annually and serve as connection points for global airline alliances.

| Classification | Annual Passengers | Characteristics |
|---------------|-------------------|----------------|
| Large Hub | 1% + of total (40M+) | Multiple terminals, long-haul routes |
| Medium Hub | 0.25-1% (10-40M) | Domestic + some international |
| Small Hub | 0.05-0.25% (2-10M) | Regional service |
| Non-Hub Primary | 10K-2M | Essential air service |
| Regional/GA | <10K | General aviation, private |

```python
from airportfyi.api import AirportFYI

with AirportFYI() as api:
    # Browse airports by country
    airports = api.list_airports(country="united-states")
    hubs = [a for a in airports if a.get("classification") == "Large Hub"]
    print(f"{len(hubs)} large hub airports in the US")
```

Learn more: [Countries](https://airportfyi.com/countries/) · [Guides](https://airportfyi.com/guides/)

### Runway and Elevation Data

Runway length determines what aircraft can operate at an airport. Widebody jets (B777, A380) typically require 3,000m+ runways, while regional turboprops can operate from 1,500m. Airport elevation affects takeoff performance — high-altitude airports like La Paz (4,061m) require longer runways due to thinner air.

| Runway Category | Length | Capable Aircraft |
|----------------|--------|-----------------|
| Short (<1,500m) | 4,921 ft | Turboprops, light jets |
| Medium (1,500-2,500m) | 8,202 ft | Narrowbody (A320, B737) |
| Long (2,500-3,500m) | 11,483 ft | Widebody (B777, A350) |
| Ultra-long (>3,500m) | 11,483+ ft | A380, high-altitude ops |

```python
from airportfyi.api import AirportFYI

with AirportFYI() as api:
    # Get runway specifications
    airport = api.get_airport("denver-international")
    print(f"Elevation: {airport['elevation_ft']} ft")   # 5,431 ft
    print(f"Runways: {airport['runway_count']}")
```

Learn more: [Airport Details](https://airportfyi.com/airports/) · [Glossary](https://airportfyi.com/glossary/)

### Geographic and Timezone Data

Every airport entry includes precise latitude/longitude coordinates and IANA timezone identifier, enabling distance calculations, flight time estimation, and local time display in travel applications.

```python
from airportfyi.api import AirportFYI

with AirportFYI() as api:
    airport = api.get_airport("tokyo-haneda")
    print(f"Lat: {airport['latitude']}")       # 35.5533
    print(f"Lon: {airport['longitude']}")      # 139.7811
    print(f"Timezone: {airport['timezone']}")   # Asia/Tokyo
    print(f"UTC Offset: {airport['utc_offset']}")
```

Learn more: [Airport Data](https://airportfyi.com/airports/) · [API Documentation](https://airportfyi.com/developers/)

## Command-Line Interface

```bash
pip install "airportfyi[cli]"

airportfyi airport incheon-international     # Airport details
airportfyi search "LAX"                      # Search by IATA/name
airportfyi country japan                     # All airports in Japan
airportfyi countries                         # List all countries
```

## MCP Server (Claude, Cursor, Windsurf)

```bash
pip install "airportfyi[mcp]"
```

```json
{
    "mcpServers": {
        "airportfyi": {
            "command": "uvx",
            "args": ["--from", "airportfyi[mcp]", "python", "-m", "airportfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```python
from airportfyi.api import AirportFYI

with AirportFYI() as api:
    airport = api.get_airport("incheon-international")  # GET /api/v1/airports/incheon-international/
    airports = api.list_airports(country="japan")        # GET /api/v1/airports/?country=japan
    countries = api.list_countries()                     # GET /api/v1/countries/
    results = api.search("heathrow")                    # GET /api/v1/search/?q=heathrow
```

### Example

```bash
curl -s "https://airportfyi.com/api/v1/airports/incheon-international/"
```

```json
{
    "slug": "incheon-international",
    "name": "Incheon International Airport",
    "iata": "ICN",
    "icao": "RKSI",
    "city": "Seoul",
    "country": "South Korea"
}
```

Full API documentation at [airportfyi.com/developers/](https://airportfyi.com/developers/).

## API Reference

| Function | Description |
|----------|-------------|
| `api.get_airport(slug)` | Airport details (codes, coordinates, runways) |
| `api.list_airports(country)` | List airports, optionally filtered by country |
| `api.list_countries()` | All countries with airport counts |
| `api.get_country(slug)` | Country details with airport list |
| `api.search(query)` | Search by name, IATA, or ICAO code |

## Learn More About Airports

- **Browse**: [Airport Directory](https://airportfyi.com/airports/) · [Countries](https://airportfyi.com/countries/)
- **Guides**: [Aviation Guides](https://airportfyi.com/guides/) · [Glossary](https://airportfyi.com/glossary/)
- **API**: [REST API Docs](https://airportfyi.com/developers/) · [OpenAPI Spec](https://airportfyi.com/api/openapi.json)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install airportfyi` | [npm](https://www.npmjs.com/package/airportfyi) |
| **MCP** | `uvx --from "airportfyi[mcp]" python -m airportfyi.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Transport FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — airports, airlines, aircraft, and railways.

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| **airportfyi** | [PyPI](https://pypi.org/project/airportfyi/) | [npm](https://www.npmjs.com/package/airportfyi) | **4,500+ airports, IATA/ICAO codes, routes — [airportfyi.com](https://airportfyi.com/)** |
| airlinefyi | [PyPI](https://pypi.org/project/airlinefyi/) | [npm](https://www.npmjs.com/package/airlinefyi) | Airlines, fleets, alliances, routes — [airlinefyi.com](https://airlinefyi.com/) |
| planefyi | [PyPI](https://pypi.org/project/planefyi/) | [npm](https://www.npmjs.com/package/planefyi) | Aircraft models, specifications, manufacturers — [planefyi.com](https://planefyi.com/) |
| trainfyi | [PyPI](https://pypi.org/project/trainfyi/) | [npm](https://www.npmjs.com/package/trainfyi) | Railway stations, train routes, rail networks — [trainfyi.com](https://trainfyi.com/) |

## License

MIT
