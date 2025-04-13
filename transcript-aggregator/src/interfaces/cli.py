import click
from rich.console import Console
from rich.progress import Progress
from pathlib import Path

from ..application.use_cases.get_transcripts import GetTranscriptsUseCase
from ..application.use_cases.export_transcripts import ExportTranscriptsUseCase
from ..domain.services.video_extractor import VideoExtractorService
from ..domain.services.transcript_fetcher import TranscriptFetcherService
from ..infrastructure.exporters.file_exporter import FileExporter

console = Console()

@click.command()
@click.option("--channel", required=True, help="YouTube channel URL or ID")
@click.option(
    "--format",
    type=click.Choice(["json", "csv", "txt"]),
    default="json",
    help="Output format"
)
@click.option("--limit", type=int, help="Maximum number of videos to process")
@click.option("--output", type=click.Path(), help="Output file path")
def main(channel: str, format: str, limit: int, output: str):
    """Fetch transcripts from a YouTube channel."""
    try:
        # Initialize services and use cases
        video_extractor = VideoExtractorService()
        transcript_fetcher = TranscriptFetcherService()
        file_exporter = FileExporter()
        
        get_transcripts = GetTranscriptsUseCase(video_extractor, transcript_fetcher)
        export_transcripts = ExportTranscriptsUseCase(file_exporter)
        
        # Execute
        with Progress() as progress:
            transcripts = get_transcripts.execute(channel, limit, progress)
            
            if not transcripts:
                console.print("[bold red]No transcripts found![/]")
                return
                
            output_path = Path(output or f"transcripts.{format}")
            export_transcripts.execute(transcripts, output_path, format)
            
            console.print(f"[bold green]Successfully exported {len(transcripts)} transcripts to {output_path}[/]")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/] {str(e)}")
        raise click.Abort()