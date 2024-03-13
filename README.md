# News-Generator

This Python script generates Top 10 News Headlines using data from NewsAPI.org.

- Fetches JSON data from **NewsAPI.org** and arranges Top 10 News Headlines from it, storing them in a text file.
- Converts the text into MP3 format using **GTTS (Google Translate's text-to-speech) API**.
- Uses the provided image (`eng.png`) as a thumbnail for the MP3 audio when converting it into MP4 format.
- Converts the MP3 into MP4 using the **Moviepy** library.

## Usage

1. Add your **API KEY** at **Line 7** in [eng.py](https://github.com/rishabhraj1572/News-Generator/blob/main/eng.py). Get it from [NewsAPI.org](https://newsapi.org).
2. Install required libraries using:

3. Run `eng.py`:
```bash
py eng.py

## Features
- ✅ Fetches Top 10 News Headlines.
- ✅ Stores fetched News Data in a text file.
- ✅ Converts it to MP3 Format.
- ✅ Converts it to MP4 Format using an Image.
- ✅ Uploads generated video to YouTube.
- ✅ Automation: Uploads Videos at regular intervals automatically.

**FEEL FREE TO CONTRIBUTE TO THIS PROJECT 😉😉**

**Note:** This project was originally made in 2020. Due to privacy reasons, the previous repository is now deleted, and this is a reupload.

