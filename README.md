# bark-api
Bark-API using FastAPI to connect to https://github.com/suno-ai/bark
JUST FOR TESTING PURPOSE, DO NOT USE IT FOR ANY REAL PROFESSIONAL DEVELOPMENT WORK
  
How to use:
  0. clone this repo
  1. clone the repo https://github.com/suno-ai/bark into the base directory
  2. put the file main.py into the **bark** folder
  3. now run **docker build -t bark-api .** 
  4. now open terminal and run **docker run -d --name bark -p 80:80 bark-api**
  5. open any browser and got to **http://127.0.0.1/docs**
  6. here you can send the request by editing the text and then downloading the generated file
