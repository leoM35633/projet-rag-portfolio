from upstash_vector import Index, Vector
from dotenv import load_dotenv

from src.chunk import avoir_les_chunk

if __name__ == "__main__" :
    load_dotenv(override=True) #Chargement des variables d'environement
    les_chunks = avoir_les_chunk("data/fichiers_md/")
    index = Index.from_env()
    les_vecteur =  [Vector(id="id-"+str(i-1) ,data=c[1], metadata=c[0]) for i,c in enumerate(les_chunks)]

    index.upsert(les_vecteur)
