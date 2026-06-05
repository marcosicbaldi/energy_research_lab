# plot.py
from zipfile import Path

import matplotlib.pyplot as plt

def salva_grafico(fig, nome: str):
    output = Path(__file__).parent / "outputs" / nome
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)
    