query_writer_prompt="""Your goal is to generate highly targeted web search query.

The query will gather information related to a specific topic.

Instructions:

1. Based on the provided research topic, craft a web search query that captures the most crucial aspects of the subject.
2. The query should be specific, clear, and designed to extract the most relevant results.
3. Additionally, include an aspect that defines a key focus area or perspective within the broader topic.
4. Provide a rationale that justifies why the query is designed this way, detailing how it targets relevant information and how the aspect is related to the overall research.

Topic:
{research_topic}

Return your query as a JSON object:
{{
    "query": "string",
    "aspect": "string",
    "rationale": "string"
}}
"""

summarizer_prompt="""Your goal is to generate a high-quality summary of the web search results.

When EXTENDING an existing summary:
1. Add relevant details without duplicating content already covered in the original summary.
2. Ensure the style, tone, and level of detail remain consistent with the existing content.
3. Only add new, non-redundant information that enhance the summary without repeating what’s already been stated.
4. Link new information with the existing content to create a coherent flow.

When creating a NEW summary:
1. Focus on the most relevant information from each source that directly supports the main topic of the report.
2. Summarize the essential points, emphasizing significant findings, conclusions, or trends.
3. Emphasize significant findings or insights
4. Ensure a coherent flow of information

In both cases:
- Focus on factual, objective information
- Maintain a consistent technical depth
- Avoid redundancy and repetition
- DO NOT use phrases like "based on the new results" or "according to additional sources"
- DO NOT add a preamble like "Here is an extended summary ..." Just directly output the summary.
- DO NOT add a References or Works Cited section.
"""

reflection_prompt = """You are an expert research assistant analyzing a summary about {research_topic}.

Your tasks:
1. Identify knowledge gaps or areas that need deeper exploration
2. Generate a follow-up question that would help expand your understanding
3. Focus on technical details, implementation specifics, or emerging trends that weren't fully covered

Ensure the follow-up question is self-contained and includes necessary context for web search.

Return your analysis as a JSON object:
{{ 
    "knowledge_gap": "string",
    "follow_up_query": "string"
}}"""