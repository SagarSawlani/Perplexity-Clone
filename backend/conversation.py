from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from tavily import TavilyClient
from groq import Groq
from dotenv import load_dotenv
import json

from prompt import SYSTEM_PROMPT, PROMPT_TEMPLATE

load_dotenv()

web_search_client = TavilyClient()
llm_client = Groq()

router = APIRouter()


async def conversation(user_query):
  # Step 1 - get the query from the user
  # make sure the user has access/credits to hit the endpoint
  # check if we have web search indexed for similar query
  # Step 4 - if not, web search to gather sources
  webSearchResponse  = web_search_client.search(
    query = user_query,
    search_depth = "advanced"
  )

  webSearchResult = webSearchResponse["results"]


  # do some context engineering on the prompt + web search responses
  # Step 6 - hit the LLM and stream back the response
  prompt = (
      PROMPT_TEMPLATE
      .replace("{{WEB_SEARCH_RESULTS}}", str(webSearchResult))
      .replace("{{USER_QUERY}}", user_query)
  )
  stream = llm_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
          "role": "system",
          "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    stream=True
  )
  for chunk in stream:
    content  = chunk.choices[0].delta.content

    if content:
      yield(content)  
  
  yield "\n<SOURCES>\n"
  links = []
  for result in webSearchResult:
    links.append(result["url"])
  yield json.dumps(links)
  yield "\n</SOURCES>\n"
  # also stream back the sources and the follow up questions (which we can get from another LLM Call)
  return

async def follow_up_question(user_query):
  # Step 1 - get the existing chat from the db
  # Step 2 - Forward the full history to LLM
  # Step 2.5 - Do Context engineering here
  # Step 3 - Stream the response to the user 
  return

@router.post("/perplexity_ask")
async def chatbot(user_query):
  return StreamingResponse(
    conversation(user_query),
    media_type="text/event-stream"
  )     

@router.post("/perplexity_ask/follow_up")
async def follow_up_query(user_query):
  return StreamingResponse(
    follow_up_question(user_query),
    media_type="text/event-stream"
  )  