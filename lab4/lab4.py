import matplotlib.pyplot as plt
from additive import additive_pareto
from discrim import discriminant_pareto
from successive import successive_pareto

# Вариант 1. Параметры взяты из примера методички.
# fi(x1, x2) = ai*(x1 - bi)^2 + ci*(x2 - di)^2
# f1: a=2, b=6,  c=3, d=6   → безусловный min в точке (6, 6)
# f2: a=3, b=-4, c=1, d=-6  → безусловный min в точке (-4, -6)
# f3: a=1, b=-7, c=2, d=8   → безусловный min в точке (-7, 8)

def f1(x): return 2 * (x[0] - 6)**2  + 3 * (x[1] - 6)**2
def f2(x): return 3 * (x[0] + 4)**2  + 1 * (x[1] + 6)**2
def f3(x): return 1 * (x[0] + 7)**2  + 2 * (x[1] - 8)**2

funcs = (f1, f2, f3)

pts_add  = additive_pareto(funcs)
pts_disc = discriminant_pareto(funcs)
pts_succ = successive_pareto(funcs)

# ── График ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 7))

xs, ys = zip(*pts_add)
ax.scatter(xs, ys, marker='o', s=80, label='Аддитивная свертка')

xs, ys = zip(*pts_disc)
ax.scatter(xs, ys, marker='s', s=80, label='Дискриминационный')

xs, ys = zip(*pts_succ)
ax.scatter(xs, ys, marker='^', s=80, label='Посл. уступок')

# Отмечаем безусловные минимумы каждого критерия
ax.scatter([6,  -4, -7], [6,  -6,  8],
           marker='*', s=200, c='black', zorder=5, label='Минимумы fi')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Множество Парето — вариант 1')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig('pareto.png', dpi=120)
plt.show()
print("\nГрафик сохранён в pareto.png")
