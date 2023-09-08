from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models.openai import ChatOpenAI
from langchain.tools import DuckDuckGoSearchResults
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter, CharacterTextSplitter
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os
import re

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupère les variables
FILE_EMBEDING = os.getenv("FILE_EMBEDING")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
VERBOSE=True
QUESTION = "Quel est le vrai prenom de laylow ?"
NUM_LINK = 3
prompt = """
  Repond en français , essaie de faire une reponse complete:
  """+QUESTION

def printdebug(text):
  if VERBOSE:
    print(text)

def get_webpage_text(url):
  text_content = ""
  try :
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'a', 'span']):
      text_content += tag.get_text() + "\n"
    printdebug(url+" est reussie")
  except :
    text_content = ""
    printdebug(url+" est un echec")
  return text_content

def analyze_text(prompt):
    raw_documents = TextLoader(FILE_EMBEDING).load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    pages = text_splitter.split_documents(raw_documents)
    text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(pages)
    index = VectorstoreIndexCreator().from_documents(texts)
    return index.query(prompt, llm=ChatOpenAI(model="gpt-3.5-turbo-16k",temperature=0))

def multi_traitement_ressource(prompt,data):
    printdebug("start embeding")
    with open(FILE_EMBEDING, 'w', encoding='utf-8') as file:
        file.write(str(data))
    result = analyze_text(prompt)
    return result

def clean_url(url):
    if url.endswith('%5D'):
        return url[:-3]
    if url.endswith('],'):
        return url[:-2]
    return url

def web_qa(url_list, query):
  content_ressource = ""
  for i in url_list:
    url = clean_url(i)
    printdebug('loading url : '+str(url))
    content_ressource += get_webpage_text(url)

  reponse = multi_traitement_ressource(query,content_ressource)
  print("\nReponse :")
  print(reponse)

def trouver_urls(texte):
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, texte)[:NUM_LINK]

def main():
  urls = trouver_urls(QUESTION)

  if urls:
    liens = urls
  else:
    search = DuckDuckGoSearchResults()
    liens = str(search.run(QUESTION))
    liens = trouver_urls(liens)

  web_qa(liens,prompt)

main()