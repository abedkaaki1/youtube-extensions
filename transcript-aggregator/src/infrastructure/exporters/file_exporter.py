import json
import csv
from pathlib import Path
from typing import List

from ...application.dtos.models import TranscriptDTO

class FileExporter:
    def export(
        self,
        transcripts: List[TranscriptDTO],
        output_path: Path,
        format: str
    ) -> Path:
        if format == "json":
            return self._export_json(transcripts, output_path)
        elif format == "csv":
            return self._export_csv(transcripts, output_path)
        elif format == "txt":
            return self._export_txt(transcripts, output_path)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def _export_json(self, transcripts: List[TranscriptDTO], path: Path) -> Path:
        data = [vars(t) for t in transcripts]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path

    def _export_csv(self, transcripts: List[TranscriptDTO], path: Path) -> Path:
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["video_id", "title", "url", "text"])
            for t in transcripts:
                writer.writerow([t.video_id, t.title, t.url, t.text])
        return path

    def _export_txt(self, transcripts: List[TranscriptDTO], path: Path) -> Path:
        with open(path, "w", encoding="utf-8") as f:
            for t in transcripts:
                f.write(f"Video: {t.title}\n")
                f.write(f"URL: {t.url}\n\n")
                f.write(t.text)
                f.write("\n\n---\n\n")
        return path