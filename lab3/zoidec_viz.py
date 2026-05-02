import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def func(x, y): return x**2 + y**2
def phi(x, y):  return 2*x - y - 2

delta = 1e-6

def grad_f(x, y):
    return ((func(x+delta,y)-func(x,y))/delta,
            (func(x,y+delta)-func(x,y))/delta)

def tangent(x, y):
    dpx = (phi(x+delta,y)-phi(x,y))/delta
    dpy = (phi(x,y+delta)-phi(x,y))/delta
    return -dpy, dpx

# ── путь Зойтендейка ─────────────────────────────────────────────────────────
def zoidec_path(eps=0.01):
    x, y = 1.0, 0.0
    step = 0.1
    path = [(x, y)]
    arrows = []  # (точка, направление шага)

    for _ in range(101):
        gx, gy = grad_f(x, y)
        tx, ty = tangent(x, y)
        sx, sy = tx, ty

        # выбираем знак: идём туда где f убывает
        if gx*sx + gy*sy > 0:
            sx, sy = -sx, -sy

        nx, ny = x + step*sx, y + step*sy

        if func(nx, ny) > func(x, y):
            step /= 2
            if step < eps: break
            continue

        norm_s = math.sqrt(sx**2 + sy**2)
        arrows.append((x, y, sx/norm_s, sy/norm_s, step))

        if math.sqrt((nx-x)**2 + (ny-y)**2) < eps: break
        x, y = nx, ny
        path.append((x, y))

    return path, arrows

path, arrows = zoidec_path()

# ── сетка ────────────────────────────────────────────────────────────────────
xs = np.linspace(-1, 3, 400)
ys = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(xs, ys)
Z = X**2 + Y**2

fig, ax = plt.subplots(figsize=(9, 7))

levels = [0.2, 0.5, 0.8, 1.0, 1.5, 2.5, 4.0, 6.0]
cs = ax.contour(X, Y, Z, levels=levels, colors='steelblue', linewidths=0.9, alpha=0.6)
ax.clabel(cs, fmt='f=%.1f', fontsize=8, inline_spacing=4)

x_line = np.linspace(-1, 3, 300)
ax.plot(x_line, 2*x_line - 2, 'k-', lw=2, label='φ(x,y)=0  (ограничение)')

px, py = zip(*path)
ax.plot(px, py, 'o-', color='mediumorchid', lw=1.5, ms=5, label='путь Зойтендейка', zorder=5)
ax.plot(px[0], py[0], 's', color='mediumorchid', ms=10, label=f'старт ({px[0]:.1f}, {py[0]:.1f})')
ax.plot(px[-1], py[-1], '*', color='green', ms=14, zorder=6,
        label=f'минимум ({px[-1]:.2f}, {py[-1]:.2f})')

# ── стрелки в нескольких точках ──────────────────────────────────────────────
show_at = [0, len(arrows)//2] if len(arrows) >= 2 else [0]
sc = 0.20

for idx in show_at:
    x0, y0, sx, sy, step = arrows[idx]
    gx, gy = grad_f(x0, y0)
    gnorm = math.sqrt(gx**2 + gy**2)
    tx, ty = tangent(x0, y0)
    tnorm = math.sqrt(tx**2 + ty**2)

    # градиент f (синий)
    ax.annotate('', xy=(x0+gx/gnorm*sc, y0+gy/gnorm*sc), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color='steelblue', lw=1.8))

    # касательная (серый, оба направления обозначаем одним)
    ax.annotate('', xy=(x0+tx/tnorm*sc, y0+ty/tnorm*sc), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.4, linestyle='dashed'))

    # направление шага Зойтендейка (оранжевый)
    ax.annotate('', xy=(x0+sx*sc, y0+sy*sc), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color='darkorange', lw=2.2))

arrows_legend = [
    mpatches.Patch(color='steelblue',  label='∇f  — градиент функции'),
    mpatches.Patch(color='gray',       label='t   — касательная к φ=0'),
    mpatches.Patch(color='darkorange', label='s   — выбранное направление шага'),
]

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles+arrows_legend, fontsize=9, loc='upper right')

ax.set_xlim(-1, 3)
ax.set_ylim(-2, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Метод Зойтендейка: движение вдоль касательной к ограничению')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('zoidec_viz.png', dpi=130)
plt.show()
print("Сохранено в zoidec_viz.png")
