import pytest
from src.domain.services.transcript_fetcher import TranscriptFetcherService
from src.domain.entities.transcript import Transcript

def test_fetch_real_transcript():
    """Test fetching a transcript from a known video."""
    service = TranscriptFetcherService()
    # Use a video ID that's known to have transcripts
    video_id = "5MWT_doo68k"  # "Me at the zoo" - First YouTube video
    
    transcript = service.fetch_transcript(video_id)
    
    assert isinstance(transcript, Transcript)
    assert transcript.video_id == video_id
    assert len(transcript.segments) > 0
    assert transcript.language == "en"