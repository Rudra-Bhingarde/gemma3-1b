from langchain_ollama import OllamaLLM

model = OllamaLLM(model='gemma3:1b')

result = model.invoke(input="what is your name?")
print(result)