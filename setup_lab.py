from pathlib import Path


def crea_cartelle(cartelle):
    """Crea una lista di cartelle."""
    for cartella in cartelle:
        cartella.mkdir(parents=True, exist_ok=True)


# -------------------------
# LIVELLO 1: LABORATORIO
# -------------------------
def crea_laboratorio():
    """Crea la struttura base del laboratorio (una sola volta)."""

    root = Path.cwd()

    cartelle = [
        root / "data",
        root / "years",
        root / "src",
        root / "models",
        root / "outputs" / "figures",
        root / "outputs" / "tables",
        root / "outputs" / "reports",
        root / "outputs" / "presentations",
        root / "docs" / "methodologies",
        root / "docs" / "papers",
        root / "archive",
    ]

    crea_cartelle(cartelle)

    print("✓ Laboratorio creato")


# -------------------------
# LIVELLO 2: ANNO
# -------------------------
def crea_anno(anno: str):
    """Crea la struttura per un anno specifico."""

    root = Path.cwd()

    fonti_dati = [
        "terna",
        "arera",
        "gse",
        "gme",
        "istat",
        "eurostat",
        "reference",
    ]

    cartelle = [
        root / "data" / anno,
        root / "years" / anno / "projects",
        root / "years" / anno / "notebooks",
        root / "years" / anno / "reports",
        root / "years" / anno / "notes",
    ]

    cartelle.extend(
        [
            root / "data" / anno / fonte
            for fonte in fonti_dati
        ]
    )

    crea_cartelle(cartelle)

    print(f"✓ Anno {anno} creato")


# -------------------------
# LIVELLO 3: PROGETTO
# -------------------------
def crea_progetto(anno: str, nome_progetto: str):
    """Crea un progetto dentro un anno specifico."""

    root = Path.cwd()

    progetto = root / "years" / anno / "projects" / nome_progetto

    cartelle = [
        progetto / "data",
        progetto / "notebooks",
        progetto / "outputs",
        progetto / "docs",
        progetto / "src",
    ]

    crea_cartelle(cartelle)

    readme = progetto / "README.md"

    readme.write_text(
        f"""# {nome_progetto}

## Anno
{anno}

## Obiettivo
Descrizione del progetto.

## Struttura
- data: input del progetto
- notebooks: analisi
- outputs: risultati
- docs: documentazione
- src: codice

## Stato
In sviluppo
""",
        encoding="utf-8",
    )

    print(f"✓ Progetto '{nome_progetto}' creato in {anno}")


# -------------------------
# ESECUZIONE BASE
# -------------------------
if __name__ == "__main__":
    crea_laboratorio()

    # esempio di utilizzo (puoi modificarlo o commentarlo)
    crea_anno("2026")
    crea_progetto("2026", "Teleriscaldamento_Torino_EC")