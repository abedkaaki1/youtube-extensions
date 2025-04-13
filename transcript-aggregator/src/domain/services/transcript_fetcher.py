import logging
from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi
from ..entities.transcript import Transcript, TranscriptSegment

class TranscriptFetcherService:
    """Service for fetching transcripts from YouTube videos."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def fetch_transcript(self, video_id: str, language: str = "en") -> Optional[Transcript]:
        """
        Fetch transcript for a specific video.
        
        Args:
            video_id: YouTube video ID
            language: Preferred language code (default: "en")
            
        Returns:
            Transcript object if available, None otherwise
        """
        try:
            self.logger.debug(f"Fetching transcript for video ID: {video_id}")
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
            
            segments = [
                TranscriptSegment(
                    text=item['text'],
                    start=item['start'],
                    duration=item['duration']
                ) for item in transcript_list
            ]
            
            transcript = Transcript(
                video_id=video_id,
                language=language,
                segments=segments,
                is_generated='auto-generated' in transcript_list[0].get('asr_type', '')
            )
            
            self.logger.debug("Transcript fetched successfully")
            return transcript
            
        except Exception as e:
            self.logger.error(f"Error fetching transcript: {e}")
            return None