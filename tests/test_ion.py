"""Tests for the ion package."""

from __future__ import annotations

from ion import dummy


def test_dummy() -> None:
    """Test the dummy() function."""
    assert dummy(1, 2) == 3
