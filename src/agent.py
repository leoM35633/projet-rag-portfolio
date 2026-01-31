import os
from dotenv import load_dotenv
from upstash_vector import Index
from agents import Agent, ModelSettings, function_tool, Runner
load_dotenv(override=True)


@function_tool
def recherche_upstach(chaine_caract : str) -> str:
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


        

   