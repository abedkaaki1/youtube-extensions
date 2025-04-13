**📄 Product Requirements Document**

**Project Title:**  
YouTube Channel Transcript Aggregator

### **1. Background / Problem Statement**

Accessing YouTube video transcripts typically requires using the YouTube Data API, which introduces complexity such as quota limits, API key management, and added setup for developers. 

To streamline access and avoid reliance on external APIs, we aim to develop a tool that can extract video transcripts from a YouTube channel without requiring an API key.

> **Engineering Perspective:**  
> This presents an opportunity to build a lightweight, dependency-minimal solution using open-source tools and web scraping techniques. However, it also means we must consider YouTube's rate limits, structural changes to HTML, and long-term maintainability of the scraping approach.

---

### **2. Goals**

- Extract all video URLs from a public YouTube channel.
- Retrieve and aggregate the transcripts of those videos.
- Avoid all use of API keys and official YouTube APIs.
- Provide an output that can be used in analytics, content generation, or archival purposes.

---

### **3. Requirements**

#### **3.1 Functional Requirements**

- **FR1:** Accept a YouTube channel ID or full channel URL as input.
- **FR2:** Collect all video URLs from the specified channel.
- **FR3:** Fetch the transcript for each video, if available.
- **FR4:** Store the transcripts in a structured format (e.g., JSON, CSV, TXT).
- **FR5:** Log and skip videos without transcripts (no retries).
- **FR6:** Provide progress indication and error handling throughout the process.

> **Engineering Perspective:**  
> - For video collection (FR2), we'll use `yt-dlp` or direct web scraping if needed.  
> - For transcript fetching (FR3), the `youtube-transcript-api` package offers a lightweight and API-free solution that supports multiple languages and auto-generated captions.  
> - We’ll need to handle videos with disabled captions or those restricted by region/privacy. Graceful fallback and logging are key.  
> - Optionally, transcripts could be stored with timestamps or speaker segmentation if available.

#### **3.2 Non-Functional Requirements**

- **NFR1:** No YouTube Data API or authentication should be required.
- **NFR2:** Handle channels with up to 1000 videos in under 15 minutes (target runtime).
- **NFR3:** CLI-based MVP; optional web UI if time allows.
- **NFR4:** Robust error handling and retry logic for transient network failures.
- **NFR5:** Modular codebase with unit-test coverage for core modules.

> **Engineering Perspective:**  
> - We must respect YouTube’s Terms of Service. The solution should not scrape excessively or appear as bot-like behavior.  
> - We’ll build in pacing/throttling (e.g., 1–2 requests per second) to reduce likelihood of IP blocks.  
> - Transcripts will be cached locally to avoid re-downloading.

---

### **4. Constraints**

- No official YouTube API usage.
- No user authentication or private video support.
- Must work cross-platform (macOS, Linux, Windows) with Python 3.8+.
- Limited project scope — delivery within 2–3 sprints.

> **Engineering Perspective:**  
> - If YouTube page structures change, scraping logic may break; we should encapsulate those components for easier patching.
> - Consider using Docker for environment consistency across machines.

---

### **5. Assumptions**

- The YouTube channel is public and has accessible transcripts.
- Video count remains within reasonable limits (< 1000).
- End users can install dependencies (e.g., Python, pip, yt-dlp).

---

### **6. Tools & Technologies**

| Component         | Tool                         | Notes |
|------------------|------------------------------|-------|
| Video Listing     | `yt-dlp`                      | Robust support for playlist and channel extraction |
| Transcript Fetching | `youtube-transcript-api`     | API-free transcript retrieval |
| Language          | Python 3.8+                  | For speed, community packages, and scriptability |
| Optional UI       | Streamlit or Flask            | Only if UI is prioritized |
| Packaging         | Docker (optional)             | For environment consistency |

---

### **7. Success Metrics**

- ✅ Tool successfully gathers >95% of available transcripts from test channels.
- ✅ CLI can process 100+ videos in under 5 minutes.
- ✅ Output files (JSON/CSV/TXT) are readable and accurate.
- ✅ No API key or authentication prompts during the process.
- ✅ Engineering effort remains under 3 weeks (core functionality).

---

Would you like me to help turn this into sprint tasks, create an architecture outline, or generate a GitHub README structure for the repo?