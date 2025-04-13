# 📺 YouTube Channel Transcript Aggregator

Fetch all available transcripts from a public YouTube channel — no API key required.

---

## ✨ Features

- ✅ No need for YouTube Data API
- ✅ Retrieve transcripts for all videos in a channel
- ✅ Export to JSON, CSV, or plain text
- ✅ Command-line interface
- ✅ Modular and domain-driven architecture

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `youtube-transcript-api` for fetching transcripts
- `yt-dlp` for channel video extraction
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-transcript-aggregator.git
cd youtube-transcript-aggregator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Basic usage with a YouTube channel URL:

```bash
python main.py --channel https://www.youtube.com/@exampleChannel
```

Options:
```bash
python main.py --channel https://www.youtube.com/@exampleChannel \
               --format json \  # Output format (json, csv, txt)
               --limit 10 \     # Maximum number of videos to process
               --output transcripts.json  # Output file path
```

---

## ⚙️ CLI Options

| Option         | Description                        |
|----------------|------------------------------------|
| `--channel`    | (Required) Channel URL or ID       |
| `--format`     | Output format: `json`, `csv`, `txt`|
| `--limit`      | Max number of videos to process    |
| `--output`     | Output file path or folder         |

---

## 🧠 Architecture Overview

This project follows **Domain-Driven Design (DDD)** principles.

- `domain/` – Core business logic (entities, services, aggregates)
- `application/` – Use cases and orchestration
- `infrastructure/` – Integrations like transcript API and file writers
- `interfaces/` – CLI layer (main entry point)

See [Architecture Docs](docs/architecture.md) for a full breakdown.

---

## 🧪 Testing

```bash
pytest tests/
```

Includes unit and integration tests. Mocks are used for YouTube responses.

---

## 📁 Project Structure

```
transcript-aggregator/
│
├── domain/                  # Core entities and services
├── application/             # Use cases and orchestration
├── infrastructure/          # Adapters for YouTube and file writing
├── interfaces/              # CLI entry point
├── tests/                   # Test cases
├── main.py                  # CLI runner
├── requirements.txt
└── README.md
```

---

## 🙌 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📝 License

MIT License. See [LICENSE](LICENSE) for details.