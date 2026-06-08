from pathlib import Path
from datetime import datetime
import argparse
import json
import shutil


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
        root / "01_workspace",
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

        # 02_data/<anno>/<fonte>
        for fonte in FONTI_DATI:
            cartelle.append(
                root / "02_data" / anno / fonte
            )

        # 01_workspace/<anno>
        cartelle.append(
            root / "01_workspace" / anno
        )

        crea_cartelle(cartelle)

        print(f"✓ Anno creato: {anno}")


# --------------------------------------------------
# Verifica coerenza
# --------------------------------------------------
def verifica_coerenza_anno(anno):
    root = Path.cwd()

    data_path = root / "02_data" / anno
    workspace_path = root / "01_workspace" / anno

    if not data_path.exists():
        print(f"⚠ Creazione automatica: 02_data/{anno}")

        crea_cartelle(
            [
                data_path / fonte
                for fonte in FONTI_DATI
            ]
        )

    if not workspace_path.exists():
        print(f"⚠ Creazione automatica: 01_workspace/{anno}")

        workspace_path.mkdir(
            parents=True,
            exist_ok=True
        )

    print(f"✓ Coerenza verificata per {anno}")


# --------------------------------------------------
# Creazione progetto
# --------------------------------------------------
def crea_progetto(anno, nome, data_sources=None):

    root = Path.cwd()

    verifica_coerenza_anno(anno)

    nome = formatta_nome(nome)

    progetto = (
        root
        / "01_workspace"
        / anno
        / nome
    )

    cartelle = [
        progetto / "notebooks",
        progetto / "notebooks" / "docs",
        progetto / "notebooks" / "reports",
        progetto / "models",
        progetto / "outputs",
        progetto / "src",
    ]

    crea_cartelle(cartelle)

    readme = progetto / "README.md"

    readme.write_text(
        f"""# {nome}

## Anno
{anno}

## Obiettivo
Da definire.
""",
        encoding="utf-8",
    )

    metadata = {
        "nome": nome,
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
        f"✓ Progetto creato: {anno}/{nome}"
    )


# --------------------------------------------------
# Migrazione
# --------------------------------------------------
def migra_projects_to_workspace():

    root = Path.cwd()

    old = root / "projects"
    new = root / "01_workspace"

    if not old.exists():
        print(
            "✓ Nessuna cartella projects da migrare"
        )
        return

    if new.exists():
        print(
            "⚠ 01_workspace esiste già. Migrazione annullata."
        )
        return

    shutil.move(str(old), str(new))

    print(
        "✓ Migrazione completata: projects → 01_workspace"
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

    parser.add_argument(
        "--migrate",
        action="store_true"
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

    if args.migrate:
        migra_projects_to_workspace()


if __name__ == "__main__":
    main()