import openai
import sys
# this is really ugly and i don't know why we need it
# importing from adjacent directories has worked fine in other 
# projects I've worked on
sys.path.insert(1, "../")
from dailyplate.utilities import read_file, construct_prompt

# https://platform.openai.com/docs/api-reference/chat/create
# https://gist.github.com/pszemraj/c643cfe422d3769fd13b97729cf517c5#file-inference_openai-py-L93
# TODO: is 256 enough tokens for a recipe??
def gpt_query(prompt: str,
              system_prompt: str,
              api_key: str,
              model: str = "gpt-3.5-turbo",
              temperature: float = 0.3, 
              max_tokens: int = 256, 
              n: int = 1, 
              presence_penalty: float = 0, 
              frequency_penalty: float = 0.1) -> list[str]:

  openai.api_key = api_key

  messages = [
    {"role": "system", "content": f"{system_prompt}"},
    {"role": "user", "content": prompt},
  ]

  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=temperature,
    max_tokens=max_tokens,
    n=n,
    presence_penalty=presence_penalty,
    frequency_penalty=frequency_penalty,
  )

  generated_texts = [choice.message["content"].strip() for choice in response["choices"]]

  return generated_texts

if __name__ == "__main__":
  # test code for development
  api_key = read_file("../newopenaikey")
  prompt = construct_prompt("../dailyplate/prompts/GOOD_PROMPT_FOR_SINGLE_RECIPE.txt", [])
  system_prompt = "You are a helpful assistant"
  result = gpt_query(prompt, system_prompt, api_key)
  print(result)