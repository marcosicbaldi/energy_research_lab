from pathlib import Path
from datetime import datetime
import argparse
import logging


# -------------------------
# LOGGING
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def crea_cartelle(cartelle):
    for cartella in cartelle:
        cartella.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creata cartella: {cartella}")


# -------------------------
# LABORATORIO
# -------------------------
def crea_laboratorio():
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
    logging.info("Laboratorio inizializzato")


# -------------------------
# ANNO
# -------------------------
def crea_anno(anno: str):
    root = Path.cwd()

    fonti = ["terna", "arera", "gse", "gme", "istat", "eurostat", "reference"]

    cartelle = [
        root / "data" / anno,
        root / "years" / anno / "projects",
        root / "years" / anno / "notebooks",
        root / "years" / anno / "reports",
        root / "years" / anno / "notes",
    ]

    cartelle.extend([root / "data" / anno / f for f in fonti])

    crea_cartelle(cartelle)
    logging.info(f"Anno creato: {anno}")


# -------------------------
# PROGETTO
# -------------------------
def formatta_nome_progetto(nome: str) -> str:
    """Naming convention standardizzata."""
    return nome.strip().lower().replace(" ", "_")


def crea_progetto(anno: str, nome_progetto: str):
    root = Path.cwd()

    nome_progetto = formatta_nome_progetto(nome_progetto)

    progetto = root / "years" / anno / "projects" / nome_progetto

    cartelle = [
        progetto / "notebooks",
        progetto / "outputs",
        progetto / "docs",
        progetto / "src",
    ]

    crea_cartelle(cartelle)

    readme = progetto / "README.md"
    readme.write_text(
        f"""# {nome_progetto}

Anno: {anno}

## Obiettivo
Da definire.

## Struttura
- notebooks
- outputs
- docs
- src
""",
        encoding="utf-8"
    )

    logging.info(f"Progetto creato: {nome_progetto} ({anno})")


# -------------------------
# CLI
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="Energy Research Lab Setup")

    parser.add_argument("--init", action="store_true", help="Crea laboratorio base")
    parser.add_argument("--year", type=str, help="Crea struttura anno")
    parser.add_argument("--project", nargs=2, metavar=("ANNO", "NOME"), help="Crea progetto")

    args = parser.parse_args()

    if args.init:
        crea_laboratorio()

    if args.year:
        crea_anno(args.year)

    if args.project:
        crea_progetto(args.project[0], args.project[1])


if __name__ == "__main__":
    main()