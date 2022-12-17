import os
import openai
def getFileContents(filename, output):
    with open(filename, 'r') as f:
        output = f.read()
    return output
log = open("Output.txt", "r")
lines = ""
liney = ""
my_secret = getFileContents("key.txt", liney)
openai.api_key = (my_secret)
response_output = ("")
response = openai.Completion.create(
  model="text-davinci-002",
  prompt=input("Please Enter Your Chemistry Doubt: "),
  temperature=1,
  max_tokens=4000,
  top_p=1,
  frequency_penalty=0.43,
  presence_penalty=0.66
)
(response_output) = str(response)
text = response['choices'][0]['text']
with open("Output.txt", "r") as file1:
  line = file1.readlines()
  file1.close
with open("Output.txt", 'w') as file:
  file.write(str(text))
  for number, line in enumerate(lines):
      if number not in [4, 7]:
       file.write(line)
  file.close()
with open('Output.txt', 'r') as f:
    print(f.read())