# Web Scraping News App README

## Overview
The Web Scraping News App is a Python-based tool for fetching and formatting recent news articles related to specific topics or categories. It leverages the Groq API, DuckDuckGo, and GoogleSearch tools to perform efficient web searches, followed by structured formatting for easy readability.

## Features
- Search for top 10 articles on a given topic using DuckDuckGo or GoogleSearch.
- Extract the 5 most recent and relevant results with descriptions and URLs.
- Format results into a structured JSON format for further processing.
- Output results in a clean, readable format.

## Prerequisites
1. **Python**: Ensure Python 3.7 or later is installed.
2. **Dependencies**: Install the required Python libraries:
   - `dotenv`
   - `phi`
   - `pydantic`
3. **API Key**: Set up a `.env` file with the following key:
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Groq API key to a `.env` file in the project root directory.

## Usage

### Single Topic Search
To search for news articles about a single topic:
1. Replace the placeholder `query` with your topic:
   ```python
   query = "Sharks"
   response = quick_web_search.run(query)
   ```
2. Run the script to see formatted results.

### Multiple Topics Search
To search for multiple topics:
1. Update the `podcaster_interest` list with your topics of interest:
   ```python
   podcaster_interest = ["Great White Sharks", "Plastic in Oceans", "Biodiversity in Sharks"]
   ```
2. The script will process each topic and display formatted results.

### Output Example
For the topic **"Great White Sharks"**, the output will be:
```
### Results for: Great White Sharks
1. 9-million-year-old fossil of colossal Great White Shark ancestor discovered, The fossilized remains belong to Cosmopolitodus hastalis - an extinct mackerel shark closely related to the modern great white shark.
   URL: https://www.msn.com/en-us/news/world/9-million-year-old-fossil-of-colossal-great-white-shark-ancestor-discovered/ar-AA1xALCE

2. Unearthing History: Discovery of a Shark Ancestor in Peru, Paleontologists in Peru have uncovered a remarkable 9-million-year-old fossil, which belonged to an ancestor of the great white shark.
   URL: https://www.devdiscourse.com/article/science-environment/3236207-unearthing-history-discovery-of-a-shark-ancestor-in-peru
```

## File Structure
- `main.py`: The main script for executing web searches and formatting results.
- `.env`: Contains the Groq API key (not included in the repository for security).
- `requirements.txt`: Lists all Python dependencies.

## Key Components
1. **Agents**:
   - `quick_web_search`: Searches using DuckDuckGo.
   - `quick_google_search`: Searches using GoogleSearch.
   - `quick_web_search_format`: Formats the search results into a JSON structure.
2. **Formatted Models**:
   - `FormattedResult`: Schema for a single search result.
   - `FormattedResponse`: Schema for a collection of results.
3. **Formatting Function**:
   - `format_results`: Converts JSON-structured results into a readable string format.

## Customization
1. **Search Engine**: Replace `DuckDuckGo` or `GoogleSearch` with other supported tools if needed.
2. **Formatting**: Adjust `format_results` for custom output formats.

## Future Enhancements
- Add support for additional search engines.
- Enable error handling for failed API calls.
- Implement a GUI for easier use.

## License
This project is licensed under the [MIT License](LICENSE).

---

Feel free to reach out for further assistance or contribute to the project!
