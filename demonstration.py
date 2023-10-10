import json
from Moteur_du_tool import ChatCompletion_openai_with_function, web_explorer
from dotenv import load_dotenv
import os
load_dotenv()

input_user = os.getenv("input_user")
MEMOIRE = ""
prompt = """
Repond en français , essaie de faire une reponse complete:
D'apres le document suivant """+input_user+"""\nSi tu ne trouve pas la reponse essaie de quand meme donner des informations sur le sujet et demande de reformuler la question."""

# execution du choix determiné par le llm
data = ChatCompletion_openai_with_function(input_user,MEMOIRE)

# filtrage
if "choices" in data and len(data["choices"]) > 0 and "message" in data["choices"][0] and "function_call" in data["choices"][0]["message"] and "arguments" in data["choices"][0]["message"]["function_call"]:
    arguments = data["choices"][0]["message"]["function_call"]["arguments"]
    title = json.loads(arguments)["title"]

    reponse = web_explorer(input_user,title)
    print(reponse)
else:
    print("reponse basique sans web explorer")
    reponse = (str(data["choices"][0]["message"]["content"]))
    print(reponse)
    