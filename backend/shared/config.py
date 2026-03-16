"""
Configuration values kept deliberately simple.
"""
import os

# Example of magic defaults that frontends might read
SERVICE_NAME = os.getenv("SERVICE_NAME", "polyglot-backend")
DEFAULT_TIMEOUT = int(os.getenv("TIMEOUT", "30"))
ENABLE_EXPERIMENTAL = os.getenv("ENABLE_EXPERIMENTAL", "false").lower() == "true"

# dead constant that is never referenced
LEGACY_FLAG = "legacy-mode"
