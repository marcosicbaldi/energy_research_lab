from pathlib import Path
from datetime import datetime
import argparse
import json


FONTI_DATI = [
    "terna",
    "arera",
    "gse",
    "gme",
    "istat",
    "eurostat",
    "reference",
]


# --------------------------------------------------
# Utility
# --------------------------------------------------
def crea_cartelle(cartelle):
    for cartella in cartelle:
        cartella.mkdir(parents=True, exist_ok=True)


def formatta_nome(nome):
    return nome.strip().lower().replace(" ", "_")


# --------------------------------------------------
# Inizializzazione laboratorio
# --------------------------------------------------
def crea_laboratorio():

    root = Path.cwd()

    cartelle = [
        root / "01_Progetti",
        root / "02_data",
        root / "03_archive",
        root / "src",
    ]

    crea_cartelle(cartelle)

    print("✓ Laboratorio inizializzato")


# --------------------------------------------------
# Creazione anni
# --------------------------------------------------
def crea_anni(lista_anni):

    root = Path.cwd()

    for anno in lista_anni:

        cartelle = []

        # dati
        for fonte in FONTI_DATI:
            cartelle.append(
                root / "02_data" / anno / fonte
            )

        # progetti
        cartelle.append(
            root / "01_Progetti" / anno
        )

        crea_cartelle(cartelle)

        print(f"✓ Anno creato: {anno}")


# --------------------------------------------------
# Verifica coerenza
# --------------------------------------------------
def verifica_coerenza_anno(anno):

    root = Path.cwd()

    data_path = root / "02_data" / anno
    projects_path = root / "01_Progetti" / anno

    if not data_path.exists():

        crea_cartelle(
            [
                data_path / fonte
                for fonte in FONTI_DATI
            ]
        )

        print(
            f"⚠ Creata struttura dati per {anno}"
        )

    if not projects_path.exists():

        projects_path.mkdir(
            parents=True,
            exist_ok=True
        )

        print(
            f"⚠ Creata struttura progetti per {anno}"
        )

    print(f"✓ Coerenza verificata: {anno}")


# --------------------------------------------------
# Creazione progetto
# --------------------------------------------------
def crea_progetto(
    anno,
    nome_progetto,
    data_sources=None
):

    root = Path.cwd()

    verifica_coerenza_anno(anno)

    nome_progetto = formatta_nome(
        nome_progetto
    )

    progetto = (
        root
        / "01_Progetti"
        / anno
        / nome_progetto
    )

    cartelle = [
        progetto / "notebooks",
        progetto / "notebooks" / "docs",
        progetto / "notebooks" / "reports",
        progetto / "notebooks" / "outputs",
        progetto / "models",
        progetto / "src",
    ]

    crea_cartelle(cartelle)

    readme = progetto / "README.md"

    readme.write_text(
        f"""# {nome_progetto}

## Anno
{anno}

## Obiettivo
Da definire.

## Dataset utilizzati
Da definire.
""",
        encoding="utf-8",
    )

    metadata = {
        "nome": nome_progetto,
        "anno": anno,
        "creato_il": datetime.now().isoformat(),
        "status": "active",
        "data_sources": data_sources or [],
    }

    with open(
        progetto / "project.json",
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            metadata,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print(
        f"✓ Progetto creato: {anno}/{nome_progetto}"
    )


# --------------------------------------------------
# CLI
# --------------------------------------------------
def main():

    parser = argparse.ArgumentParser(
        description="Energy Research Lab Manager"
    )

    parser.add_argument(
        "--init",
        action="store_true"
    )

    parser.add_argument(
        "--years",
        nargs="*"
    )

    parser.add_argument(
        "--project",
        nargs=2,
        metavar=("ANNO", "NOME")
    )

    parser.add_argument(
        "--sources",
        nargs="*"
    )

    parser.add_argument(
        "--check"
    )

    args = parser.parse_args()

    if args.init:
        crea_laboratorio()

    if args.years:
        crea_anni(args.years)

    if args.project:

        anno, nome = args.project

        crea_progetto(
            anno,
            nome,
            args.sources
        )

    if args.check:
        verifica_coerenza_anno(
            args.check
        )


if __name__ == "__main__":
    main()