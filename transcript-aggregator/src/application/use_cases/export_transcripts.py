from pathlib import Path
from typing import List

from ..dtos.models import TranscriptDTO
from ...infrastructure.exporters.file_exporter import FileExporter

class ExportTranscriptsUseCase:
    def __init__(self, exporter: FileExporter):
        self.exporter = exporter

    def execute(
        self,
        transcripts: List[TranscriptDTO],
        output_path: Path,
        format: str = "json"
    ) -> Path:
        return self.exporter.export(transcripts, output_path, format)