from pathlib import Path

ANNO = "2026"


def crea_laboratorio():

    root = Path.cwd()

    cartelle = [

        # ARCHIVIO
        root / "archive",

        # DATI GREZZI
        root / "data" / "raw" / ANNO / "terna",
        root / "data" / "raw" / ANNO / "arera",
        root / "data" / "raw" / ANNO / "gse",
        root / "data" / "raw" / ANNO / "gme",
        root / "data" / "raw" / ANNO / "istat",
        root / "data" / "raw" / ANNO / "eurostat",

        # DATI ELABORATI
        root / "data" / "processed" / ANNO,

        # DATI DI RIFERIMENTO
        root / "data" / "reference",

        # PROGETTI
        root / "projects",

        # NOTEBOOK
        root / "notebooks",

        # CODICE
        root / "src",

        # MODELLI
        root / "models",

        # OUTPUT
        root / "outputs" / "figures",
        root / "outputs" / "reports",
        root / "outputs" / "tables",
        root / "outputs" / "presentations",

        # DOCUMENTAZIONE
        root / "docs" / "papers",
        root / "docs" / "methodologies",
        root / "docs" / "notes",

    ]

    for cartella in cartelle:
        cartella.mkdir(parents=True, exist_ok=True)

    print("Laboratorio creato correttamente.")


def crea_readme():

    testo = """# Energy Research Lab

Repository per ricerca e analisi dei sistemi energetici.

## Fonti dati

- Terna
- ARERA
- GSE
- GME
- ISTAT
- Eurostat

## Workflow

1. Acquisizione dati
2. Pulizia dati
3. Analisi
4. Modellazione
5. Visualizzazione
6. Reportistica

## Struttura

data/raw       -> dati originali
data/processed -> dati elaborati
projects       -> progetti di ricerca
outputs        -> risultati
models         -> modelli
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(testo)

    print("README creato correttamente.")


if __name__ == "__main__":
    crea_laboratorio()
    crea_readme()

    from pathlib import Path

def crea_progetto(nome_progetto):
    
    root = Path.cwd()
    progetto = root / "projects" / nome_progetto
    
    sottocartelle = [
        progetto / "data",
        progetto / "notebooks",
        progetto / "outputs",
    ]
    
    for cartella in sottocartelle:
        cartella.mkdir(parents=True, exist_ok=True)
    
    readme = progetto / "README.md"
    readme.write_text(f"# {nome_progetto}\n\nDescrizione del progetto.\n", encoding="utf-8")
    
    print(f"Progetto '{nome_progetto}' creato correttamente.")

if __name__ == "__main__":
    crea_progetto("2026_06_Teleriscaldamento_Torino_EC")
    