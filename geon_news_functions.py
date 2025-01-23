#Webscrapping News App
from dotenv import load_dotenv
import os
from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from phi.tools.newspaper4k import Newspaper4k
from pydantic import BaseModel, Field


#Load .env with api key
load_dotenv()
#Load API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


#Web Search Agent that will search a topic or a category
quick_web_search = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    description="You are a websearchers trying to find the most current articles on a query",
    instructions=[
        "For a given query, search for the top 10 links.",
        "From the top 10 find the 5 most recent results"
        "Return the description of the link with the url",
        "The description should be seperated from the url with a colon",
        "Number the results one through 5"
    ],
    markdown=True,
    show_tool_calls=False,
    add_datetime_to_instructions=True,
    #debug_mode=True,
)
quick_google_search = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[GoogleSearch()],
    description="You are a websearchers trying to find the most current articles on a query",
    instructions=[
        "For a given query, search for the top 10 links.",
        "From the top 10 find the 5 most currnet results"
        "Return the description of the link with the url",
        "The description should be seperated from the url with a colon",
        "Number the results one through 5"
    ],
    markdown=True,
    show_tool_calls=False,
    add_datetime_to_instructions=True,
    #debug_mode=True,
)

class FormattedResult(BaseModel):
    number: int = Field(..., description="The number of the result (1-5).")
    description: str = Field(..., description="Description of the article or webpage.")
    url: str = Field(..., description="URL of the article or webpage.")

class FormattedResponse(BaseModel):
    results: list[FormattedResult] = Field(..., description="List of formatted results with numbers, descriptions, and URLs.")

# Second agent: Formatting agent
quick_web_search_format = Agent(
    model=Groq(id="llama-3.1-8b-instant"),
    description="You are a formatter that organizes web search results into a structured JSON format.",
    instructions=[
        "Take the input from a web search and convert it into a structured JSON format.",
        "The JSON format should include the following fields for each result: number, description, and URL.",
        "The input will consist of numbered lines where each line contains a description and a URL separated by a colon.",
        "Parse the input and output a JSON object."
    ],
    response_model=FormattedResponse,  # Use the structured response model
    markdown=False,
    show_tool_calls=False,
)
# Format the results for readability
def format_results(results):
    output = []
    for result in results:
        description = result.description.strip("**")
        output.append(f"{result.number}. {description}\n   URL: {result.url}")
    return "\n\n".join(output)

llm1="llama-3.1-8b-instant"
llm2="llama-3.3-70b-versatile"
#Solo Test
#query = "Sharks"
#response = quick_web_search.run(query)
#response = quick_google_search.run(query)
#print(response.content)
#formatted_response = quick_web_search_format.run(response.content)
#structured_results = formatted_response.content.results
#print(format_results(structured_results))

#Multiple Interests Test
podcaster_interest = ["Great White Sharks", "Plastic in Oceans", "Biodiversity in Sharks"]
all_responses = {}

for interest in podcaster_interest:
    response = quick_web_search.run(interest)
    formatted_response = quick_web_search_format.run(response.content)
    structured_results = formatted_response.content.results
    formatted_content = format_results(structured_results)  
    all_responses[interest] = formatted_content

for interest, formatted_content in all_responses.items():
    print(f"### Results for: {interest}\n{formatted_content}\n")