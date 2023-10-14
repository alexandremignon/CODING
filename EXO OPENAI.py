import os
import openai
openai.api_key = os.getenv("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")

def developper(text) -> Any:
    return openai.Completion.create(
        model="text-davinci-003"
        prompt = "Developper le texte: " + text,
        temperature = 0.25,
        max_tokens = 2000
    ).choices[0].text.strip()

input_text = "Le jeune informaticien aime coder"
response = resumer(input_text)

print(response)

    