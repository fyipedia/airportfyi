# airportfyi

Airport codes, routes and aviation data API client — [airportfyi.com](https://airportfyi.com)

## Install

```bash
pip install airportfyi
```

## Quick Start

```python
from airportfyi.api import AirportFYI

with AirportFYI() as api:
    results = api.search("JFK")
    print(results)
```

## License

MIT
