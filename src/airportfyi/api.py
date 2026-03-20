"""HTTP API client for airportfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install airportfyi[api]``

Usage::

    from airportfyi.api import AirportFYI

    with AirportFYI() as api:
        items = api.list_airlines()
        detail = api.get_airline("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class AirportFYI:
    """API client for the airportfyi.com REST API.

    Provides typed access to all airportfyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://airportfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://airportfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_airlines(self, **params: Any) -> dict[str, Any]:
        """List all airlines."""
        return self._get("/api/v1/airlines/", **params)

    def get_airline(self, slug: str) -> dict[str, Any]:
        """Get airline by slug."""
        return self._get(f"/api/v1/airlines/" + slug + "/")

    def list_airports(self, **params: Any) -> dict[str, Any]:
        """List all airports."""
        return self._get("/api/v1/airports/", **params)

    def get_airport(self, slug: str) -> dict[str, Any]:
        """Get airport by slug."""
        return self._get(f"/api/v1/airports/" + slug + "/")

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_glossary_terms(self, **params: Any) -> dict[str, Any]:
        """List all glossary terms."""
        return self._get("/api/v1/glossary-terms/", **params)

    def get_glossary_term(self, slug: str) -> dict[str, Any]:
        """Get glossary term by slug."""
        return self._get(f"/api/v1/glossary-terms/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_route_pairs(self, **params: Any) -> dict[str, Any]:
        """List all route pairs."""
        return self._get("/api/v1/route-pairs/", **params)

    def get_route_pair(self, slug: str) -> dict[str, Any]:
        """Get route pair by slug."""
        return self._get(f"/api/v1/route-pairs/" + slug + "/")

    def list_runways(self, **params: Any) -> dict[str, Any]:
        """List all runways."""
        return self._get("/api/v1/runways/", **params)

    def get_runway(self, slug: str) -> dict[str, Any]:
        """Get runway by slug."""
        return self._get(f"/api/v1/runways/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> AirportFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
