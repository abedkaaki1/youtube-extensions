from typing import List, Optional
from rich.progress import Progress

from ...domain.entities.channel import Channel
from ...domain.services.video_extractor import VideoExtractorService
from ...domain.services.transcript_fetcher import TranscriptFetcherService
from ..dtos.models import TranscriptDTO

class GetTranscriptsUseCase:
    def __init__(
        self,
        video_extractor: VideoExtractorService,
        transcript_fetcher: TranscriptFetcherService
    ):
        self.video_extractor = video_extractor
        self.transcript_fetcher = transcript_fetcher

    def execute(
        self,
        channel_url: str,
        limit: Optional[int] = None,
        progress: Optional[Progress] = None
    ) -> List[TranscriptDTO]:
        channel = Channel.from_url(channel_url)
        videos = self.video_extractor.get_channel_videos(channel, limit)
        
        transcripts = []
        task = progress.add_task("[cyan]Fetching transcripts...", total=len(videos))
        
        for video in videos:
            transcript = self.transcript_fetcher.fetch_transcript(video.id)
            if transcript:
                dto = TranscriptDTO(
                    video_id=video.id,
                    title=video.title,
                    text=transcript.full_text,
                    language=transcript.language,
                    segments=[{
                        "text": s.text,
                        "start": s.start,
                        "duration": s.duration
                    } for s in transcript.segments],
                    url=video.full_url
                )
                transcripts.append(dto)
            
            progress.advance(task)
            
        return transcripts