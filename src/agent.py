from dotenv import load_dotenv
from upstash_vector import Index
from agents import Agent, ModelSettings, function_tool, Runner
load_dotenv(override=True)


@function_tool
def recherche_upstach(chaine_caract : str) -> str:
   """Recherche dans l'index Upstash les chunks les plus pertinents.

   Description:
       Interroge l'index vectoriel Upstash en utilisant la chaîne fournie
       et récupère les `top_k` chunks (par défaut 5). Construit une
       représentation textuelle contenant les métadonnées (titres)
       et le contenu de chaque chunk, prête à être utilisée par l'agent.

   Args:
       chaine_caract (str): Requête ou texte de recherche à envoyer à l'index.

   Returns:
       str: Chaîne formatée contenant pour chaque chunk les métadonnées
            (titres) et le contenu, séparés par des en-têtes `TITRE`/`CONTENU`.
   """
   index = Index.from_env()
   chunks = index.query(data=chaine_caract, top_k=5, include_metadata=True, include_data=True)

   resultat = ""
   for c in chunks :
       #On récupère les titres stockées en métadata
       titre = "TITRE : "
       for key, value in c.metadata.items() :
           titre += f"{key} : {value}, "
        
       resultat += titre+"\nCONTENU :" + c.data + "\n\n"

   return resultat
    

def interoger_agent(prompt:str) -> str :
    """Envoie un prompt à l'agent conversationnel et retourne sa réponse.

    Description:
        Construit un agent configuré pour utiliser `recherche_upstach` comme outil
        de récupération de contexte. Exécute le `prompt` de manière synchrone
        et renvoie la sortie finale (trimée).

    Args:
        prompt (str): Texte de la question ou instruction à fournir à l'agent.

    Returns:
        str: Réponse générée par l'agent, sans espaces en début/fin.

    Exemple:
        >>> interoger_agent("Parle-moi de mon projet universitaire en info")
        'Le projet universitaire en info porte sur...'
    """
    agent = Agent(
        name="Agent-upstach",
        instructions=""" 
                Tu es un assistant.
                Réponds de façon professionnelle.
                """,
        model="gpt-4.1-nano",
        model_settings=ModelSettings(temperature=0), #Pas de hasard, se basse exclusivement sur le résultat de recherche_upstach
        tools=[recherche_upstach]
    )

    resultat = Runner.run_sync(agent, prompt).final_output.strip()
    return resultat


        

   