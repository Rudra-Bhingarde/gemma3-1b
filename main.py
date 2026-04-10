from langchain_ollama import OllamaLLM

model = OllamaLLM(model='gemma3:1b')

result = model.invoke(input="what food do you eat?")
print(result)