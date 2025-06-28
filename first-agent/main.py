from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel


# sabse pehle hame ek client banana parega or bydefault ya open ai ka client hota he.
# Client banate he.

# ya hamara provider(client) ban gaya he 
external_client = AsyncOpenAI(
    api_key= "AIzaSyCey5hUpPsNW3CTXKQZ_3pDHLfcCgVLnhI",
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/" #base url banate he to us se communication kerne  
) #k lya api model use kerte he. yani api ko call kerne k lya ek url get kerte he. jo base url me ati he. jis k through 
# ham api ko get ker sakte he.

external_model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client
)
# SDK MODEL ME 2 API PROVIDE HOTI HE. 
# ! CHAT COMPLETION API
# 2 RESPONSES API

# BYDEFAULT OPEN AI AGENTS SDK RESPONSES API USE KERTA HE.
assistance = Agent (
    name = "Simple Assistant",
    instructions= " You are a helpful assistant the provide information and answers",
)

# run level configration. isme jitne b agent honge wo isi k through chalenge.
config = RunConfig(
    model= external_model,
    model_provider = external_client,
    tracing_disabled = True # tracing ko disable islya kya he k 
)

# agent k behind the scene llm kam ker raha hota he. or us llm ko chalane k lya hame api key ki zarurat hoti he.
# api key ham openai se purchase b ker sakte he or gemenie se free me b le sakte he. 
result = Runner.run_sync(starting_agent=assistance, input= "hi how are you?", run_config=config) # brcket () me ya possitional kehlate he. yani agar ham input or argument nai de to b ya chal jate he.
print(result.final_output) # ya object return kerega
