from dataclasses import dataclass
from typing import Optional

@dataclass
class Video:
    """Represents a YouTube video."""
    id: str
    title: Optional[str] = None
    url: Optional[str] = None
    channel_id: Optional[str] = None
    duration: Optional[int] = None

    @property
    def full_url(self) -> str:
        """Get the full YouTube URL for this video."""
        return f"https://www.youtube.com/watch?v={self.id}"