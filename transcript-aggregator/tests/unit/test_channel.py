import pytest
from src.domain.entities.channel import Channel

def test_channel_creation():
    channel = Channel(id="UCxxx")
    assert channel.id == "UCxxx"
    assert channel.video_ids is None

def test_channel_from_url():
    url = "https://www.youtube.com/@example"
    channel = Channel.from_url(url)
    assert channel.id == url  # TODO: Should extract proper ID