import os
import argparse
from dotenv import find_dotenv, load_dotenv
import openai

from helpers import get_completion, load_config, read_file

# Load Environment Variables
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']
SUPPORTED_MODELS = ['gpt-4', 'gpt-3.5-turbo']


def construct_prompt(config, resume, job_posting):
    # Read the main template
    main_template = read_file('prompt/main.txt')
    
    # Read the parts specified in the config and construct the letter_parts content
    letter_parts_content = []
    for part in config['prompt_parts']:
        part_file_name = f"{part}.txt"
        part_content = read_file(os.path.join('prompt/parts', part_file_name))
        letter_parts_content.append(part_content)
    
    # Join all parts into a single string
    letter_parts_joined = '\n\n'.join(letter_parts_content)
    
    # Replace placeholders in the main template with actual content
    final_prompt = main_template.format(
        resume=resume,
        job_posting=job_posting,
        letter_parts=letter_parts_joined,
        **config['prompt_params']
    )
    
    return final_prompt


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate a cover letter from a job posting and a resume.')
    parser.add_argument('--job', '-j', type=str, default='job_posting.txt', help='Path to the job posting file.')
    parser.add_argument('--resume', '-r', type=str, default='resume.txt', help='Path to the resume file.')
    parser.add_argument('--output', '-o', type=str, default='cover_letter.txt', help='Path to save the generated cover letter.')
    
    return parser.parse_args()


def main():
    # Set up configuration
    args = parse_arguments()
    config = load_config()
    assert config['model_params']['model'] in SUPPORTED_MODELS

    # Read data and construct the prompt
    job_posting = read_file(args.job)
    resume = read_file(args.resume)
    prompt = construct_prompt(config, resume, job_posting)
    
    # Generate the cover letter
    print("Generating cover letter...")
    cover_letter = get_completion(prompt, config['model_params'])
    
    # Save the generated cover letter to the specified output path
    with open(args.output, 'w') as file:
        file.write(cover_letter)
    print(f"Cover letter saved to {args.output}")

    # Save the prompt to a file as well (for debugging purposes)
    with open('prompt.txt', 'w') as file:
        file.write(prompt)
    print("Prompt saved to prompt.txt")

if __name__ == "__main__":
    main()
