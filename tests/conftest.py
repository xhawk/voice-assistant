"""Pytest configuration for Home Assistant Voice Client."""

import sys
from pathlib import Path

# Add src to path so imports work during testing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
