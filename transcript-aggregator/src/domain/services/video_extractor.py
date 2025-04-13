from typing import List, Optional
import re
import yt_dlp
import logging

from ..entities.video import Video
from ..entities.channel import Channel

class VideoExtractorService:
    """Service for extracting video information from YouTube channels."""
    
    CHANNEL_URL_PATTERNS = {
        'handle': r'@[\w-]+',
        'channel_id': r'UC[\w-]{22}',
        'custom_url': r'c/[\w-]+',
        'user': r'user/[\w-]+'
    }
    
    def __init__(self):
        self.ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': True,
            'ignoreerrors': True
        }
        
    def _get_channel_url(self, channel: Channel) -> str:
        """Construct proper YouTube channel URL based on identifier format."""
        if re.match(self.CHANNEL_URL_PATTERNS['handle'], channel.id):
            return f"https://www.youtube.com/{channel.id}/videos"
        elif re.match(self.CHANNEL_URL_PATTERNS['channel_id'], channel.id):
            return f"https://www.youtube.com/channel/{channel.id}/videos"
        elif re.match(self.CHANNEL_URL_PATTERNS['custom_url'], channel.id):
            return f"https://www.youtube.com/{channel.id}/videos"
        elif re.match(self.CHANNEL_URL_PATTERNS['user'], channel.id):
            return f"https://www.youtube.com/{channel.id}/videos"
        else:
            # Try as direct URL
            return channel.id if 'youtube.com' in channel.id else f"https://www.youtube.com/{channel.id}/videos"

    def get_channel_videos(self, channel: Channel, limit: Optional[int] = None) -> List[Video]:
        """
        Extract videos from a YouTube channel.
        
        Args:
            channel: Channel entity
            limit: Maximum number of videos to extract
            
        Returns:
            List of Video entities
        """
        videos = []
        channel_url = self._get_channel_url(channel)
        
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            try:
                logging.info(f"Fetching videos from: {channel_url}")
                playlist = ydl.extract_info(channel_url, download=False)
                
                if not playlist or 'entries' not in playlist:
                    logging.error(f"No videos found for channel: {channel_url}")
                    return []

                entries = playlist['entries']
                if limit:
                    entries = entries[:limit]
                
                for entry in entries:
                    if entry is None:
                        continue
                        
                    video = Video(
                        id=entry['id'],
                        title=entry.get('title'),
                        url=entry.get('webpage_url'),
                        channel_id=channel.id,
                        duration=entry.get('duration')
                    )
                    videos.append(video)
                    
            except Exception as e:
                logging.error(f"Error extracting videos: {str(e)}")
                return []
                
        return videos

    def extract_channel_id(self, url: str) -> Optional[str]:
        """
        Extract channel ID from various YouTube URL formats.
        
        Args:
            url: YouTube channel URL
            
        Returns:
            Channel ID if found, None otherwise
        """
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            try:
                result = ydl.extract_info(url, download=False)
                return result.get('channel_id') or result.get('uploader_id')
            except Exception as e:
                logging.error(f"Error extracting channel ID: {str(e)}")
                return None