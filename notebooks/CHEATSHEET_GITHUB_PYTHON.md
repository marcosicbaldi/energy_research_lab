# Energy Research Lab - Cheatsheet

## Aprire il progetto

Aprire VS Code nella cartella:

```powershell
cd C:\Users\marco\Desktop\energy_research_lab
code .
```

---

## Verificare lo stato del repository

```powershell
git status
```

Controlla:
- file modificati
- file nuovi
- branch attivo

---

## Aggiungere modifiche

Tutti i file:

```powershell
git add .
```

Singolo file:

```powershell
git add nomefile.py
```

---

## Salvare una versione del lavoro

```powershell
git commit -m "Descrizione modifica"
```

Esempi:

```powershell
git commit -m "Added CER data structure"
git commit -m "Updated README"
git commit -m "First photovoltaic analysis"
```

---

## Pubblicare su GitHub

```powershell
git push
```

---

## Aggiornare il repository locale

```powershell
git pull
```

---

## Verificare il collegamento GitHub

```powershell
git remote -v
```

---

## Verificare configurazione Git

```powershell
git config --global user.name
git config --global user.email
```

---

# Python

## Eseguire uno script

```powershell
python nome_script.py
```

Esempio:

```powershell
python setup_lab.py
```

---

## Installare una libreria

```powershell
pip install nome_libreria
```

Esempio:

```powershell
pip install pandas
```

---

## Verificare versione Python

```powershell
python --version
```

---

# Workflow standard

1. Aprire VS Code
2. Modificare codice
3. Salvare
4. Testare script
5. git status
6. git add .
7. git commit -m "descrizione"
8. git push

---

# Struttura del laboratorio

data/
    raw/
    processed/
    reference/

projects/

models/

notebooks/

outputs/
    figures/
    reports/
    tables/

docs/

archive/

src/

---

# Regola personale

Prima:

    Domanda di ricerca

Poi:

    Dati

Poi:

    Metodo

Poi:

    Python

Mai il contrario.
