# Project Report

Here's a quick rundown of the project journey. I started off with big dreams of a finetuned model in Docker but ended up with a cool CLI app using the OpenAI API and some smart prompt-engineering. Let’s walk through what happened.

## Steps and Stumbles

1. **Experimenting with Falcon-7B**: 
- Gave Falcon-7B a go, but it had a wild imagination – lots of made-up stuff!
- Couldn't do much with few-shot learning due to its tiny context size.
- My guess? Models of this size need more tuning to get them right.

2. **Skipping Finetuning**:
- With about 5 hours on the clock, finetuning felt like a stretch, so I decided to pass.

3. **Resource Constraints for Larger Models**:
- Had big plans for larger models, but didn’t have the hardware to back it up.

4. **Middle-Sized Models? Not Quite**:
- Tried LLama-2-13b, but even my RTX-A5000 with 24GB memory couldn’t handle it.

5. **Settling on GPT-4 / GPT-3.5 and Prompt Wizardry**:
- Chose to work with GPT-4 and GPT-3.5 and put my energy into crafting prompts.

## Crafting the Prompts

1. **Gathering Cover Letters**:
- Pulled together a bunch from online and my own collection.

2. **Pattern Recognition**:
- Noticed a common structure in effective cover letters and incorporated that into the prompts.

3. **Adding Style**:
- Used a list of styles from ChatGPT to add some flair.

4. **Refining Prompts**:
- Kept adjusting the prompts. For instance, directing GPT not to fabricate facts helped a bunch.

5. **CLI Development and Debugging**:
- Put everything into a user-friendly CLI and ironed out the kinks.

## Just So You Know

- You’ll need an OpenAI key for this. I’ll provide one for the demo period.
- Had plans for few-shot examples and URL parsing, but time was tight.

## Quick Tip

- GPT-4 tends to outshine GPT-3.5, so I’d lean towards using that.

## Time Breakdown

- Playing with Local Models: 1 hour
- Data Collection: 0.5 hour
- Perfecting the Prompt: 1 hour
- Building the CLI: 0.5 hour
- Writing Docs & Examples: 1 hour

Enjoy :)