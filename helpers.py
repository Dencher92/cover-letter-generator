import yaml
from openai import OpenAI

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_completion(prompt, model_params):
    client = OpenAI()
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        messages=messages,
        **model_params
    )
    return response.choices[0].message.content
