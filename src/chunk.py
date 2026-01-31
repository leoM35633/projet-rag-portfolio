from langchain_text_splitters import MarkdownHeaderTextSplitter
import os


def construir_chunk(markdown_text) -> list :
    """_summary_
    Découpe un fichier markdown en plusieurs chunks. On a pour chaque chunk
    ses métadonnées (les tritres ratachés) et le texte avec les titres
    Args:
        markdown_text (_type_): le texte du fichier markdown

    Returns:
        list: renvoie une liste de tuple, premier élèment les métadonnées (les titres : h1,h2, ...), deuxième le texte
    """
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "h1"),
            ("##", "h2"),
            ("###", "h3"),
        ],
    )
    chunks = splitter.split_text(markdown_text)
    return[(c.metadata, 
            c.page_content.replace("\n"," ") + " " + " | ".join([titre for titre in c.metadata.keys()])) 
                for c in chunks]


def avoir_les_chunk(chemin_fichiers_md : str) -> list :
    """_summary_
    Découpe l'ensemble des fichiers markdonwn et les divises en plusieurs chunks.

    Args:
        chemin_fichiers_md (str): le chemin du dossier qui contier les fichiers markdonwns

    Returns:
        list: list avec l'ensemble des chunck.
    """
    les_nom_fichiers = os.listdir(chemin_fichiers_md)
    les_chunk = []

    for nom_fichier in les_nom_fichiers :
        with open(os.path.join(chemin_fichiers_md, nom_fichier), encoding="utf-8") as fichier_markdown :
            les_chunk = les_chunk + construir_chunk(fichier_markdown.read())

    return les_chunk

    