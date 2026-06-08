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

    # README
    readme = progetto / "README.md"
    readme.write_text(
        f"""# {nome_progetto}

Anno: {anno}

## Obiettivo
Da definire.
""",
        encoding="utf-8"
    )

    # METADATA (NUOVO PEZZO)
    import json
    from datetime import datetime

    meta = {
        "nome": nome_progetto,
        "anno": anno,
        "creato_il": datetime.now().isoformat(),
        "status": "active"
    }

    config_file = progetto / "project.json"

    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=4, ensure_ascii=False)

    print(f"✓ Progetto creato: {nome_progetto} ({anno})")