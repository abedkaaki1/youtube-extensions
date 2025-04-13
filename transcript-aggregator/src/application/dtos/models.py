from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TranscriptDTO:
    video_id: str
    title: Optional[str]
    text: str
    language: str
    segments: List[dict]
    url: str

@dataclass
class ChannelDTO:
    id: str
    name: Optional[str]
    url: str
    video_count: int