from pathlib import Path
from datetime import datetime

ANNO = str(datetime.now().year)


def crea_cartelle(cartelle):
    """Crea una lista di cartelle."""
    for cartella in cartelle:
        cartella.mkdir(parents=True, exist_ok=True)


def crea_laboratorio():
    """Crea la struttura principale del laboratorio."""

    root = Path.cwd()

    fonti_dati = [
        "terna",
        "arera",
        "gse",
        "gme",
        "istat",
        "eurostat",
    ]

    cartelle = [
        root / "archive",
        root / "data" / "processed" / ANNO,
        root / "data" / "reference",
        root / "projects",
        root / "notebooks",
        root / "src",
        root / "models",
        root / "outputs" / "figures",
        root / "outputs" / "reports",
        root / "outputs" / "tables",
        root / "outputs" / "presentations",
        root / "docs" / "papers",
        root / "docs" / "methodologies",
        root / "docs" / "notes",
    ]

    cartelle.extend(
        [
            root / "data" / "raw" / ANNO / fonte
            for fonte in fonti_dati
        ]
    )

    crea_cartelle(cartelle)

    print("✓ Struttura laboratorio creata")


if __name__ == "__main__":
    crea_laboratorio()