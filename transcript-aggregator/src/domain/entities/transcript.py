from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TranscriptSegment:
    """A single segment/line in a transcript."""
    text: str
    start: float
    duration: float
    
@dataclass
class Transcript:
    """Represents a YouTube video transcript."""
    video_id: str
    language: str
    segments: List[TranscriptSegment]
    is_generated: bool = False
    
    @property
    def full_text(self) -> str:
        """Get the complete transcript text."""
        return " ".join(segment.text for segment in self.segments)