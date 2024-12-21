# research-llama

This project implements a research agent using a large language model. The agent uses a state machine to manage the research process.

## How to run

To run the project, execute the `researcher.py` file using streamlit:

```bash
streamlit run researcher.py
```

## Project Structure

The project has the following structure:

```
research-llama/
├── config.ini          # Configuration settings for the research agent
├── prompts.py          # Prompts used by the research agent
├── README.md           # This file
├── researcher.py       # Main logic for the research agent
├── state.py            # Defines the SummaryState class
└── utils.py            # Utility functions for searching and formatting sources
```

## Code Description

This project implements a research agent that can perform web searches, summarize the results, and reflect on the summaries to generate follow-up queries. The agent uses a state machine to manage the research process. Here's a breakdown of each file:

- `researcher.py`: This file contains the main logic for the research agent. It uses a state machine to manage the research process, and it uses several functions to generate queries, perform web research, summarize sources, reflect on summaries, and finalize summaries. It also uses `streamlit` to create a simple UI.
- `prompts.py`: This file contains the prompts used by the research agent. These prompts are used to generate queries, summarize sources, and reflect on summaries.
- `state.py`: This file defines the `SummaryState` class, which is used to manage the state of the research process. It includes fields for the research topic, search query, web research results, sources gathered, research loop count, and running summary.
- `utils.py`: This file contains utility functions for searching and formatting sources. It includes functions for deduplicating and formatting sources, formatting search results, and performing Tavily searches.
- `config.ini`: This file contains configuration settings for the research agent, such as the local LLM to use and the maximum number of web research loops.

This project is designed to be easy to use and understand, even for those who are new to large language models and research agents.
