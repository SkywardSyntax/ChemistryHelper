import os
import openai
import openai

def getFileContents(filename, output):
    with open(filename, 'r') as f:
        output = f.read()
    return output

# Check the size of the file
size = os.path.getsize('key.txt')
prompty = input("Enter your Chemistry Question: ")
# Check if the file is blank
if size == 0:
  exit("You require an API Key to use this program. Please go to https://openai.com/ and create an account.\nAfter, you've created your, or you already have one, go to https://beta.openai.com/account/api-keys to get your API Key.\nOnce you have your API Key, paste it into the key.txt file and rerun the program\nThank You!.")
else:
    # Open the file
    openai.api_key = open("key.txt", "r").read()
# Get the completion response from the OpenAI API
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=str(prompty),
  temperature=1,
  max_tokens=4000,
  top_p=1,
  frequency_penalty=0.43,
  presence_penalty=0.66
)

# Get the text from the response
text = response['choices'][0]['text']

# Split the text into words
words = text.split()

# Initialize an empty list to store the lines
lines = []

# Iterate over the words in the text
i = 0
while i < len(words):
  # Initialize an empty list to store the words in the current line
  line = []
  # Add up to 10 words to the current line
  while len(line) < 15 and i < len(words):
    line.append(words[i])
    i += 1
  # Join the words in the current line into a string
  line_str = ' '.join(line)
  # Add the current line to the list of lines
  lines.append(line_str)

# Open the Output.txt file in write mode
with open("Output.txt", 'w') as f:
  # Write the lines to the file
  f.write('\n'.join(lines))

# Open the Output.txt file in read mode
with open('Output.txt', 'r') as f:
    # Print the contents of the file
    print(f.read())