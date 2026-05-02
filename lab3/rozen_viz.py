import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── функции из варианта 1 ────────────────────────────────────────────────────
def func(x, y): return x**2 + y**2
def phi(x, y):  return 2*x - y - 2

delta = 1e-6

def grad_f(x, y):
    return ((func(x+delta,y)-func(x,y))/delta,
            (func(x,y+delta)-func(x,y))/delta)

def tangent(x, y):
    dpx = (phi(x+delta,y)-phi(x,y))/delta
    dpy = (phi(x,y+delta)-phi(x,y))/delta
    return -dpy, dpx   # касательная к phi=0

def proj(x, y):
    gx, gy = grad_f(x, y)
    tx, ty = tangent(x, y)
    norm_t = tx**2 + ty**2
    s = (gx*tx + gy*ty) / norm_t
    return s*tx, s*ty  # проекция градиента на касательную

# ── путь метода Розена ───────────────────────────────────────────────────────
def rozen_path(eps=0.01):
    x, y = 1.0, 0.0
    step = 0.1
    path = [(x, y)]
    for _ in range(200):
        sx, sy = proj(x, y)
        if math.sqrt(sx**2 + sy**2) < eps:
            break
        nx, ny = x - step*sx, y - step*sy
        if func(nx, ny) >= func(x, y):
            step /= 2
            if step < eps*0.01:
                break
            continue
        x, y = nx, ny
        path.append((x, y))
    return path

path = rozen_path()

# ── координатная сетка ───────────────────────────────────────────────────────
xs = np.linspace(-1, 3, 400)
ys = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(xs, ys)
Z = X**2 + Y**2

fig, ax = plt.subplots(figsize=(9, 7))

# линии уровня f
levels = [0.2, 0.5, 0.8, 1.0, 1.5, 2.5, 4.0, 6.0]
cs = ax.contour(X, Y, Z, levels=levels, colors='steelblue', linewidths=0.9, alpha=0.6)
ax.clabel(cs, fmt='f=%.1f', fontsize=8, inline_spacing=4)

# кривая ограничения phi=0
x_line = np.linspace(-1, 3, 300)
y_line = 2*x_line - 2
ax.plot(x_line, y_line, 'k-', lw=2, label='φ(x,y)=0  (ограничение)')

# путь метода
px, py = zip(*path)
ax.plot(px, py, 'o-', color='tomato', lw=1.5, ms=5, label='путь Розена', zorder=5)
ax.plot(px[0], py[0], 's', color='tomato', ms=10, label=f'старт ({px[0]:.1f}, {py[0]:.1f})')
ax.plot(px[-1], py[-1], '*', color='green', ms=14, zorder=6,
        label=f'минимум ({px[-1]:.2f}, {py[-1]:.2f})')

# ── стрелки в нескольких точках на пути ─────────────────────────────────────
show_at = [0, len(path)//3, 2*len(path)//3]
sc = 0.18  # масштаб стрелок

for idx in show_at:
    x0, y0 = path[idx]
    gx, gy = grad_f(x0, y0)
    tx, ty = tangent(x0, y0)
    norm_t = math.sqrt(tx**2 + ty**2)
    tx_n, ty_n = tx/norm_t, ty/norm_t
    sx, sy = proj(x0, y0)
    norm_s = math.sqrt(sx**2 + sy**2)

    # градиент f (синий)
    ax.annotate('', xy=(x0+gx*sc, y0+gy*sc), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color='steelblue', lw=1.8))

    # касательная к phi=0 (серый, оба направления)
    ax.annotate('', xy=(x0+tx_n*sc*1.1, y0+ty_n*sc*1.1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.4, linestyle='dashed'))

    # проекция = то куда реально идём (оранжевый, антипроекция)
    if norm_s > 1e-6:
        sx_n, sy_n = sx/norm_s, sy/norm_s
        ax.annotate('', xy=(x0-sx_n*sc*0.9, y0-sy_n*sc*0.9), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle='->', color='darkorange', lw=2.2))

# легенда стрелок
arrows = [
    mpatches.Patch(color='steelblue',   label='∇f  — градиент функции'),
    mpatches.Patch(color='gray',        label='t   — касательная к φ=0'),
    mpatches.Patch(color='darkorange',  label='−s  — антипроекция (шаг Розена)'),
]

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles+arrows, fontsize=9, loc='upper right')

ax.set_xlim(-1, 3)
ax.set_ylim(-2, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Метод Розена: проекция антиградиента на ограничение')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('rozen_viz.png', dpi=130)
plt.show()
print("Сохранено в rozen_viz.png")
