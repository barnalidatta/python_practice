# my_lib/text_utils.py
from __future__ import annotations # For forward references in type hints

class TextProcessor:
    """A stateful utility class that tracks and modifies text."""

    def __init__(self, raw_text: str):
        self.text = raw_text  # Internal state tracking

    def remove_whitespace(self) -> TextProcessor:
        """Strips leading/trailing gaps. Returns self for chainability."""
        self.text = self.text.strip()
        return self

    def uppercase(self) -> TextProcessor:
        """Converts internal text to uppercase."""
        self.text = self.text.upper()
        return self

    def get_result(self) -> str:
        """Returns the final manipulated string."""
        return self.text