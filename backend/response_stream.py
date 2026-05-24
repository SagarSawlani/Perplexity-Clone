# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# import asyncio

# app = FastAPI()


# async def stream_resp():
#     for item in [1, 2, 3,4,5,6,7,8,9]:
#         yield f"{item}\n"
#         # await asyncio.sleep(0.5)


# @app.get("/")
# async def stream():
#     return StreamingResponse(
#         stream_resp(),
#         media_type="text/event-stream"
    # )

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

async def llm_call():

  stream = client.chat.completions.create(
      #
      # Required parameters
      #
      messages=[
          # Set an optional system message. This sets the behavior of the
          # assistant and can be used to provide specific instructions for
          # how it should behave throughout the conversation.
          {
              "role": "system",
              "content": "You are a helpful assistant."
          },
          # Set a user message for the assistant to respond to.
          {
              "role": "user",
              "content": "Explain the importance of fast language models",
          }
      ],

      # The language model which will generate the completion.
      model="llama-3.3-70b-versatile",

      #
      # Optional parameters
      #

      # Controls randomness: lowering results in less random completions.
      # As the temperature approaches zero, the model will become deterministic
      # and repetitive.
      temperature=0.5,

      # The maximum number of tokens to generate. Requests can use up to
      # 2048 tokens shared between prompt and completion.
      max_completion_tokens=1024,

      # Controls diversity via nucleus sampling: 0.5 means half of all
      # likelihood-weighted options are considered.
      top_p=1,

      # A stop sequence is a predefined or user-specified text string that
      # signals an AI to stop generating content, ensuring its responses
      # remain focused and concise. Examples include punctuation marks and
      # markers like "[end]".
      stop=None,

      # If set, partial message deltas will be sent.
      stream=True,
  )

  # Print the incremental deltas returned by the LLM.
  for chunk in stream:
    yield(chunk.choices[0].delta.content)  

app = FastAPI()

@app.get('/')
async def llm_resp():
  return StreamingResponse(
  llm_call(),
  media_type="text/event-stream"
)