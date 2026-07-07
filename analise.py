import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["font.size"] = 11
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.25

def wilson_ci(x, n, z=1.96):
    if n == 0:
        return (np.nan, np.nan, np.nan)
    phat = x / n
    denom = 1 + z**2 / n
    center = (phat + z**2 / (2 * n)) / denom
    margin = (z * np.sqrt((phat * (1 - phat) / n) + (z**2 / (4 * n**2)))) / denom
    return phat, max(0, center - margin), min(1, center + margin)

# ---------- dados de CARREIRA TODA (clube + selecao), Transfermarkt + pesquisa ----------
# Bruno Guimaraes corrigido p/ 3/4 (Transfermarkt ainda nao processou o miss vs Noruega 05/07/26)
carreira = {
    "Rayan":              (2, 2),
    "Igor Thiago":        (2, 2),
    "Gabriel Martinelli": (1, 1),
    "Raphinha":           (19, 20),
    "Neymar":             (93, 115),
    "Matheus Cunha":      (4, 5),
    "Bruno Guimaraes":    (3, 4),
    "Vini Jr":            (13, 18),
    "Danilo":             (2, 3),
}

resumo = pd.DataFrame(
    [(j, g, n) for j, (g, n) in carreira.items()], columns=["jogador", "gols", "n"]
)
resumo["pct"], resumo["ci_low"], resumo["ci_high"] = zip(
    *resumo.apply(lambda r: wilson_ci(r["gols"], r["n"]), axis=1)
)
resumo = resumo.sort_values("pct", ascending=False).reset_index(drop=True)

highlight = ["Vini Jr", "Bruno Guimaraes"]

# ================= FIG 1 (carreira) — aproveitamento com IC 95% =================
fig, ax = plt.subplots(figsize=(9, 6))
y = np.arange(len(resumo))
pct = resumo["pct"].values * 100
err_low = (resumo["pct"].values - resumo["ci_low"].values) * 100
err_high = (resumo["ci_high"].values - resumo["pct"].values) * 100
colors = ["#c0392b" if p in highlight else "#2980b9" for p in resumo["jogador"]]

ax.barh(y, pct, xerr=[err_low, err_high], color=colors, alpha=0.85,
        capsize=5, error_kw={"elinewidth": 1.5, "ecolor": "#333"})
for i in range(len(resumo)):
    g, n = int(resumo.loc[i, "gols"]), int(resumo.loc[i, "n"])
    ax.text(pct[i] + err_high[i] + 2, i, f"{g}/{n}", va="center", fontsize=10, fontweight="bold")

ax.set_yticks(y)
ax.set_yticklabels(resumo["jogador"])
ax.set_xlabel("Aproveitamento em pênaltis — carreira toda, clube+seleção (%)")
ax.set_xlim(0, 118)
ax.set_title("Pênaltis na CARREIRA TODA (clube + seleção)\naproveitamento com intervalo de confiança de 95% (Wilson)",
             fontsize=12, fontweight="bold")
ax.invert_yaxis()
legend_elems = [mpatches.Patch(color="#c0392b", label="Envolvidos na decisão Bruno G x Vini Jr"),
                mpatches.Patch(color="#2980b9", label="Outros cobradores")]
ax.legend(handles=legend_elems, loc="lower right", fontsize=9)
plt.tight_layout()
plt.savefig("", dpi=160)
plt.close()

# ================= FIG 2 (carreira) — amostra x aproveitamento =================
fig, ax = plt.subplots(figsize=(8, 6.5))
for i in range(len(resumo)):
    p = resumo.loc[i, "jogador"]
    n = resumo.loc[i, "n"]
    pct_i = resumo.loc[i, "pct"] * 100
    color = "#c0392b" if p in highlight else "#2980b9"
    ax.scatter(n, pct_i, s=260, color=color, alpha=0.85, edgecolor="black", linewidth=0.8, zorder=3)
    ax.annotate(p, (n, pct_i), textcoords="offset points", xytext=(9, 4), fontsize=10)

ax.set_xlabel("Tamanho da amostra (nº de pênaltis batidos na carreira)")
ax.set_ylabel("Aproveitamento (%)")
ax.set_title("Quanto menor a amostra, mais instável é a estatística\n(carreira toda: clube + seleção)",
              fontsize=12, fontweight="bold")
ax.set_xlim(0, resumo["n"].max() + 8)
ax.set_ylim(-5, 110)
plt.tight_layout()
plt.savefig("", dpi=160)
plt.close()

# ================= FIG 3 (carreira) — índice ponderado mata-mata 2x =================
# OBS / limitação importante: só temos a QUEBRA por fase (mata-mata x normal) confirmada
# jogo-a-jogo para uma parte das cobrancas de Neymar, Bruno G. e Vini Jr (fonte: reportagens
# especificas). Para os demais jogadores e para o restante das cobrancas de carreira desses
# tres, nao ha quebra publica disponivel -> tratamos como peso 1x ("normal") por padrao.
# Isso deve SUBESTIMAR o indice clutch real de quem tiver mais mata-mata nao documentado.
mata_mata_confirmado = {
    # jogador: (gols_mata_mata, tentativas_mata_mata)  -> extraido das reportagens usadas antes
    "Neymar": (2, 2),            # Coreia do Sul 2022 (WC) + Noruega 2026 (WC) - ambos convertidos
    "Bruno Guimaraes": (0, 1),   # miss vs Noruega 2026 (oitavas WC)
    "Vini Jr": (1, 3),           # CL: Atletico (miss) + City ida (miss) + City volta (gol)
}

linhas = []
for _, row in resumo.iterrows():
    jogador, gols_tot, n_tot = row["jogador"], int(row["gols"]), int(row["n"])
    gols_mm, n_mm = mata_mata_confirmado.get(jogador, (0, 0))
    n_normal = n_tot - n_mm
    gols_normal = gols_tot - gols_mm
    gols_pond = gols_normal * 1 + gols_mm * 2
    tent_pond = n_normal * 1 + n_mm * 2
    linhas.append([jogador, n_tot, n_mm, gols_pond / tent_pond * 100])

pond = pd.DataFrame(linhas, columns=["jogador", "n_bruto", "n_mata_mata_conf", "indice_clutch"])
pond = pond.sort_values("indice_clutch", ascending=False).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(9.5, 6))
y = np.arange(len(pond))
colors = ["#c0392b" if p in highlight else "#27ae60" for p in pond["jogador"]]
ax.barh(y, pond["indice_clutch"], color=colors, alpha=0.85)
for i in range(len(pond)):
    nb = int(pond.loc[i, "n_bruto"])
    nmm = int(pond.loc[i, "n_mata_mata_conf"])
    tag = f"n={nb}" + (f" ({nmm} mata-mata conf.)" if nmm > 0 else "")
    ax.text(pond.loc[i, "indice_clutch"] + 1.5, i, tag, va="center", fontsize=8.5,
            style="italic", color="#555")

ax.set_yticks(y)
ax.set_yticklabels(pond["jogador"])
ax.invert_yaxis()
ax.set_xlim(0, 118)
ax.set_xlabel("Índice clutch (%) — mata-mata confirmado conta 2x, resto conta 1x")
ax.set_title("Índice ponderado — CARREIRA TODA (clube + seleção)\nmata-mata só pesa 2x onde há confirmação jogo-a-jogo (ver nota)",
              fontsize=11.5, fontweight="bold")
plt.tight_layout()
plt.savefig("", dpi=160)
plt.close()

print(resumo[["jogador", "gols", "n", "pct", "ci_low", "ci_high"]].round(3).to_string(index=False))
print()
print(pond.round(3).to_string(index=False))
