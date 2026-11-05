"""Drawing helpers for the ME F211 study guide (Crandall sign conventions)."""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle, FancyArrowPatch, Arc

OUT = "/tmp/claude-0/-home-user-mech-sol-/5e236ef2-e171-5cb2-82aa-007544f55ba5/scratchpad/docx/img"
TC = "#1f6fb2"   # tension / positive
CC = "#c0392b"   # compression / negative
LD = "#222222"   # loads
GR = "#888888"
plt.rcParams.update({"font.size": 9.5, "font.family": "DejaVu Sans", "axes.linewidth": 0.8,
                     "mathtext.fontset": "dejavusans"})


def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def fmt(v, nd=3):
    if abs(v) < 5e-4:
        return "0"
    a = abs(v)
    if a >= 1000:
        return f"{v:.0f}"
    if a >= 100:
        s = f"{v:.1f}"
        return s[:-2] if s.endswith(".0") else s
    s = f"{v:.{nd}g}"
    return s


def arrow(ax, x0, y0, x1, y1, color=LD, lw=1.6, ms=12, z=5):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=ms,
                                 color=color, lw=lw, zorder=z, shrinkA=0, shrinkB=0))


def curved_arrow(ax, x, y, r, ccw=True, color=LD, label=None, lw=1.5):
    a0, a1 = (200, 520) if ccw else (520, 200)
    th = np.radians(np.linspace(a0, a1 - (40 if ccw else -40), 40))
    ax.plot(x + r * np.cos(th), y + r * np.sin(th), color=color, lw=lw, zorder=6)
    t = th[-1]
    d = 1 if ccw else -1
    tip = (x + r * np.cos(t + d * 0.35), y + r * np.sin(t + d * 0.35))
    arrow(ax, x + r * np.cos(t), y + r * np.sin(t), *tip, color=color, lw=lw, ms=10)
    if label:
        ax.text(x, y + r * 1.45, label, ha="center", va="bottom", fontsize=9, color=color)


# ---------------------------------------------------------------- supports
def support(ax, x, y, kind, s, side="bottom"):
    if kind in ("pin", "roller"):
        tri = Polygon([[x, y], [x - 0.6 * s, y - s], [x + 0.6 * s, y - s]], closed=True,
                      fc="white", ec=LD, lw=1.2, zorder=4)
        ax.add_patch(tri)
        if kind == "roller":
            for dx in (-0.3 * s, 0.3 * s):
                ax.add_patch(Circle((x + dx, y - 1.18 * s), 0.17 * s, fc="white", ec=LD, lw=1, zorder=4))
            yb = y - 1.38 * s
        else:
            yb = y - s
        ax.plot([x - 0.9 * s, x + 0.9 * s], [yb, yb], color=LD, lw=1.2)
        for k in range(6):
            xx = x - 0.9 * s + k * 0.36 * s
            ax.plot([xx, xx - 0.25 * s], [yb, yb - 0.3 * s], color=LD, lw=0.8)
    elif kind in ("fixedL", "fixedR"):
        d = -1 if kind == "fixedL" else 1
        ax.plot([x, x], [y - 1.6 * s, y + 1.6 * s], color=LD, lw=2)
        for k in range(9):
            yy = y - 1.6 * s + k * 0.4 * s
            ax.plot([x, x + d * 0.4 * s], [yy, yy - 0.3 * s], color=LD, lw=0.8)


# ---------------------------------------------------------------- beams
def beam(name, L, sup, P=(), C=(), W=(), labels=None, title=None, unit_F="kN", unit_L="m",
         extra_x=(), show_reactions=True, figw=7.2, crandall=True):
    """sup: dict x -> 'pin'|'roller'|'fixedL'|'fixedR'.  P: (x, F) F up +.  C: (x, C) ccw +.
    W: (x1, x2, w1, w2) intensity up +.  Returns reactions and (x, V, M) arrays."""
    labels = labels or {}
    xs_sup = sorted(sup)

    def wres(x1, x2, w1, w2):
        R = 0.5 * (w1 + w2) * (x2 - x1)
        if abs(w1 + w2) < 1e-12:
            return 0.0, 0.5 * (x1 + x2), (w2 - w1) * (x2 - x1) ** 2 / 6.0
        xc = x1 + (x2 - x1) * (w1 + 2 * w2) / (3 * (w1 + w2))
        return R, xc, None

    Fy = sum(f for _, f in P) + sum(wres(*w)[0] for w in W)
    fixed = [x for x in xs_sup if sup[x].startswith("fixed")]
    reac = {}
    if fixed:
        a = fixed[0]
        Ma = sum(f * (x - a) for x, f in P) + sum(c for _, c in C) + sum(wres(*w)[0] * (wres(*w)[1] - a) for w in W)
        reac[a] = (-Fy, -Ma)
        pts = list(P) + [(a, -Fy)]
        cps = list(C) + [(a, -Ma)]
    else:
        a, b = xs_sup
        Ma = sum(f * (x - a) for x, f in P) + sum(c for _, c in C) + sum(wres(*w)[0] * (wres(*w)[1] - a) for w in W)
        Rb = -Ma / (b - a)
        Ra = -Fy - Rb
        reac[a] = (Ra, 0)
        reac[b] = (Rb, 0)
        pts = list(P) + [(a, Ra), (b, Rb)]
        cps = list(C)

    def VM(x):
        v = sum(f for xi, f in pts if xi < x)
        m = sum(f * (x - xi) for xi, f in pts if xi < x) - sum(c for xi, c in cps if xi < x)
        for x1, x2, w1, w2 in W:
            if x > x1:
                xe = min(x, x2)
                we = w1 + (w2 - w1) * (xe - x1) / (x2 - x1)
                R = 0.5 * (w1 + we) * (xe - x1)
                v += R
                if R != 0:
                    xc = x1 + (xe - x1) * (w1 + 2 * we) / (3 * (w1 + we)) if abs(w1 + we) > 1e-12 else 0.5 * (x1 + xe)
                    m += R * (x - xc)
        return v, m

    xg = np.linspace(0, L, 4001)
    eps = L * 1e-6
    keys = sorted(set([0, L] + [x for x, _ in P] + [x for x, _ in C] + [w[0] for w in W] + [w[1] for w in W] + xs_sup + list(extra_x)))
    xx, VV, MM = [], [], []
    for x in xg:
        v, m = VM(x)
        xx.append(x); VV.append(v); MM.append(m)
    xx = np.array(xx); VV = np.array(VV); MM = np.array(MM)
    # insert exact jumps
    xp, Vp, Mp = [], [], []
    for x in keys:
        for xe in (x - eps, x + eps):
            if 0 <= xe <= L:
                v, m = VM(xe)
                xp.append(xe); Vp.append(v); Mp.append(m)
    xa = np.concatenate([xx, xp]); order = np.argsort(xa)
    xa = xa[order]; Va = np.concatenate([VV, Vp])[order]; Ma_ = np.concatenate([MM, Mp])[order]
    Vc = -Va if crandall else Va

    fig, axs = plt.subplots(3, 1, figsize=(figw, 6.3), sharex=True,
                            gridspec_kw={"height_ratios": [1.15, 1, 1], "hspace": 0.12})
    ax = axs[0]
    s = 0.035 * L
    ax.add_patch(Rectangle((0, -0.25 * s), L, 0.5 * s, fc="#dddddd", ec=LD, lw=1, zorder=3))
    for x, k in sup.items():
        support(ax, x, -0.25 * s, k, s * 1.1)
    Fmax = max([abs(f) for _, f in P] + [abs(w[2]) for w in W] + [abs(w[3]) for w in W] + [1e-9])
    for x, f in P:
        h = 3.2 * s
        if f < 0:
            arrow(ax, x, 0.25 * s + h, x, 0.25 * s)
            ax.text(x, 0.25 * s + h * 1.05, f"{fmt(abs(f))} {unit_F}", ha="center", va="bottom", fontsize=8.5)
        else:
            arrow(ax, x, -0.25 * s - h, x, -0.25 * s)
            ax.text(x, -0.25 * s - h * 1.1, f"{fmt(abs(f))} {unit_F}", ha="center", va="top", fontsize=8.5)
    for x, c in C:
        curved_arrow(ax, x, 0, 1.2 * s, ccw=c > 0, label=f"{fmt(abs(c))} {unit_F}·{unit_L}")
    for x1, x2, w1, w2 in W:
        n = max(4, int(12 * (x2 - x1) / L) + 2)
        top = []
        for t in np.linspace(x1, x2, n):
            w = w1 + (w2 - w1) * (t - x1) / (x2 - x1)
            h = 2.6 * s * abs(w) / Fmax if Fmax else 0
            h = max(h, 0.0)
            top.append((t, 0.25 * s + h))
            if h > 0.15 * s:
                arrow(ax, t, 0.25 * s + h, t, 0.25 * s, lw=1.0, ms=7)
        ax.plot([p[0] for p in top], [p[1] for p in top], color=LD, lw=1)
        wl = f"{fmt(abs(w1))}" if abs(w1 - w2) < 1e-9 else f"{fmt(abs(w1))}→{fmt(abs(w2))}"
        ax.text(0.5 * (x1 + x2), max(p[1] for p in top) + 0.3 * s, f"{wl} {unit_F}/{unit_L}", ha="center", va="bottom", fontsize=8.5)
    for x, lab in labels.items():
        ax.text(x, -0.25 * s - 0.4 * s, lab, ha="center", va="top", fontsize=9, fontweight="bold",
                bbox=dict(fc="white", ec="none", pad=0.3))
    if show_reactions:
        rt = []
        for x, (R, M) in reac.items():
            nm = labels.get(x, f"x={fmt(x)}")
            t = f"R$_{{{nm}}}$ = {fmt(R)} {unit_F}"
            if M:
                t += f",  M$_{{{nm}}}$ = {fmt(M)} {unit_F}·{unit_L} ({'ccw' if M > 0 else 'cw'})"
            rt.append(t)
        ax.text(0.01, 0.97, "Reactions (+ up): " + ";  ".join(rt), transform=ax.transAxes, va="top", fontsize=8.3,
                bbox=dict(fc="#f6f6f6", ec="#cccccc", pad=2.5))
    ax.set_ylim(-5.8 * s if any(f > 0 for _, f in P) else -2.6 * s, 5.4 * s)
    ax.set_aspect("auto"); ax.axis("off")
    if title:
        ax.set_title(title, fontsize=10.5, fontweight="bold", loc="left")

    def panel(ax, y, lab, col):
        ax.fill_between(xa, 0, y, where=y >= 0, color=TC, alpha=0.25, lw=0)
        ax.fill_between(xa, 0, y, where=y < 0, color=CC, alpha=0.25, lw=0)
        ax.plot(xa, y, color=LD, lw=1.3)
        ax.axhline(0, color=LD, lw=0.8)
        ax.set_ylabel(lab, fontsize=9)
        ax.grid(alpha=0.25)
        rng = (y.max() - y.min()) or 1
        ax.set_ylim(y.min() - 0.22 * rng, y.max() + 0.22 * rng)

    panel(axs[1], Vc, f"V ({unit_F})\n{'Crandall sign' if crandall else ''}", TC)
    panel(axs[2], Ma_, f"M$_b$ ({unit_F}·{unit_L})\nsagging +", TC)
    # annotate key values
    vs = np.abs(Vc).max() + 1e-12; ms_ = np.abs(Ma_).max() + 1e-12
    def ann(ax, x, y, above=True):
        sc_ = vs if ax is axs[1] else ms_
        if abs(y) < 1e-3 * sc_:
            y = 0.0
        rng = ax.get_ylim()[1] - ax.get_ylim()[0]
        ax.annotate(fmt(y), (x, y), xytext=(0, 7 if y >= 0 else -9), textcoords="offset points",
                    ha="center", va="bottom" if y >= 0 else "top", fontsize=8, color="#111")
    for x in keys:
        vl = -VM(x - eps)[0] if crandall else VM(x - eps)[0]
        vr = -VM(x + eps)[0] if crandall else VM(x + eps)[0]
        jump = abs(vr - vl) > 1e-3 * vs
        if 0 < x < L and jump:
            axs[1].plot([x, x], [vl, vr], "o", ms=2.5, color=LD)
            ann(axs[1], x - 0.02 * L, vl); ann(axs[1], x + 0.02 * L, vr)
        elif x == 0:
            ann(axs[1], x + 0.02 * L, vr)
        elif x == L:
            ann(axs[1], x - 0.02 * L, vl)
        else:
            axs[1].plot([x], [vl], "o", ms=2.5, color=LD); ann(axs[1], x, vl)
        ml = VM(x - eps)[1]; mr = VM(x + eps)[1]
        m0 = mr if x == 0 else ml
        axs[2].plot([x], [m0], "o", ms=2.5, color=LD)
        if abs(mr - ml) > 1e-3 * ms_ and 0 < x < L:
            axs[2].plot([x], [mr], "o", ms=2.5, color=LD)
            ann(axs[2], x - 0.02 * L, ml); ann(axs[2], x + 0.02 * L, mr)
        elif abs(m0) > 1e-3 * ms_ or 0 < x < L:
            ann(axs[2], x, m0)
    # interior extremes of M (V = 0)
    for i in range(1, len(xx) - 1):
        if (MM[i] - MM[i - 1]) * (MM[i + 1] - MM[i]) < 0 and min(abs(xx[i] - k) for k in keys) > 0.01 * L:
            axs[2].plot([xx[i]], [MM[i]], "o", ms=3, color=CC)
            axs[2].annotate(f"{fmt(MM[i])} at x={fmt(xx[i])}", (xx[i], MM[i]), xytext=(0, 8 if MM[i] >= 0 else -10),
                            textcoords="offset points", ha="center", va="bottom" if MM[i] >= 0 else "top", fontsize=8, color=CC)
    # contraflexure
    for i in range(1, len(xx)):
        if MM[i - 1] * MM[i] < 0 and abs(MM[i - 1] - MM[i]) < 0.2 * (abs(MM).max() + 1e-9) and 0.01 * L < xx[i] < 0.99 * L \
                and abs(MM[i - 1]) > 1e-4 * ms_:
            axs[2].plot([xx[i]], [0], "s", ms=4, color="#8e44ad")
            axs[2].annotate(f"contraflexure\nx={fmt(xx[i])}", (xx[i], 0), xytext=(4, 10), textcoords="offset points",
                            fontsize=7.5, color="#8e44ad")
    axs[2].set_xlabel(f"x ({unit_L})")
    axs[2].set_xlim(-0.04 * L, 1.04 * L)
    save(fig, name)
    return reac


# ---------------------------------------------------------------- trusses
def truss(name, nodes, members, forces, loads=(), sups=(), title=None, unit="kN", figw=6.6, scale=None, label_off=None):
    """forces: dict (a,b)->value (+T, -C). loads: (node, fx, fy). sups: (node, kind)."""
    xs = [p[0] for p in nodes.values()]; ys = [p[1] for p in nodes.values()]
    span = max(max(xs) - min(xs), max(ys) - min(ys))
    s = scale or 0.06 * span
    fig, ax = plt.subplots(figsize=(figw, figw * 0.62))
    label_off = label_off or {}
    for (a, b) in members:
        f = forces.get((a, b), forces.get((b, a), 0))
        col = TC if f > 1e-9 else (CC if f < -1e-9 else GR)
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        ax.plot([x1, x2], [y1, y2], color=col, lw=3.2 if abs(f) > 1e-9 else 1.6,
                ls="-" if abs(f) > 1e-9 else "--", solid_capstyle="round", zorder=2)
        mx, my = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
        dx, dy = label_off.get((a, b), (0, 0))
        t = f"{fmt(abs(f))} {'T' if f > 1e-9 else ('C' if f < -1e-9 else '(zero)')}"
        ax.text(mx + dx, my + dy, t, ha="center", va="center", fontsize=8.2, color=col,
                bbox=dict(fc="white", ec=col, lw=0.6, pad=1.5, boxstyle="round,pad=0.25"), zorder=6)
    for n, (x, y) in nodes.items():
        ax.add_patch(Circle((x, y), 0.12 * s, fc="white", ec=LD, lw=1.2, zorder=5))
        ax.text(x - 0.35 * s, y + 0.35 * s, n, fontsize=10, fontweight="bold", ha="right", va="bottom", zorder=7)
    for n, fx, fy in loads:
        x, y = nodes[n]
        L = 2.2 * s
        mag = math.hypot(fx, fy)
        ux, uy = fx / mag, fy / mag
        arrow(ax, x - ux * L, y - uy * L, x - ux * 0.15 * s, y - uy * 0.15 * s, ms=13)
        ax.text(x - ux * L * 1.12, y - uy * L * 1.12, f"{fmt(mag)} {unit}", ha="center",
                va="bottom" if uy < 0 else "top", fontsize=9)
    for n, k in sups:
        x, y = nodes[n]
        if k in ("pin", "roller"):
            support(ax, x, y - 0.12 * s, k, 0.8 * s)
        else:
            support(ax, x - 0.12 * s, y, k, 0.6 * s)
    ax.set_aspect("equal"); ax.axis("off")
    ax.margins(0.12)
    ax.plot([], [], color=TC, lw=3, label="tension (T)")
    ax.plot([], [], color=CC, lw=3, label="compression (C)")
    ax.plot([], [], color=GR, lw=1.6, ls="--", label="zero-force")
    ax.legend(loc="lower right", fontsize=8, frameon=True, bbox_to_anchor=(1.0, -0.12), ncol=3)
    if title:
        ax.set_title(title, fontsize=10.5, fontweight="bold", loc="left")
    save(fig, name)


# ---------------------------------------------------------------- Mohr's circle
def mohr(name, sx, sy, txy, title=None, unit="MPa", strain=False, rot=None, sigma3=None, figw=6.4, note=None):
    """Crandall convention: +txy plotted DOWNWARD at X, upward at Y.
    For strain pass ex, ey, gamma_xy/2 and strain=True."""
    c = 0.5 * (sx + sy); R = math.hypot(0.5 * (sx - sy), txy)
    s1, s2 = c + R, c - R
    fig, ax = plt.subplots(figsize=(figw, figw * 0.78))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(c + R * np.cos(th), R * np.sin(th), color=TC, lw=1.8)
    if sigma3 is not None:
        for a, b in ((s1, sigma3), (s2, sigma3)):
            cc, rr = 0.5 * (a + b), 0.5 * abs(a - b)
            ax.plot(cc + rr * np.cos(th), rr * np.sin(th), color=GR, lw=1, ls="--")
    X = (sx, -txy); Y = (sy, txy)
    ax.plot([X[0], Y[0]], [X[1], Y[1]], color=LD, lw=1.3)
    ax.plot(*X, "o", color=CC, ms=6, zorder=5); ax.plot(*Y, "o", color=CC, ms=6, zorder=5)
    sym = "ε" if strain else "σ"
    tsym = "γ/2" if strain else "τ"
    xs = "x"; ys = "y"
    for P_, nm, v in (((X, "X", sx), (Y, "Y", sy)) if abs(txy) > 1e-9 else ()):
        left = P_[0] < c - 1e-9
        ax.annotate(f"{nm} ({fmt(v)}, {fmt(txy)})", P_, xytext=(-8 if left else 8, 6 if P_[1] >= 0 else -12),
                    textcoords="offset points", fontsize=8.5, color=CC, ha="right" if left else "left")
    ax.plot([c], [0], "k+", ms=9)
    ax.annotate(f"C = {fmt(c)}", (c, 0), xytext=(-4, -14), textcoords="offset points", fontsize=8.5, ha="right")
    for v, lab in ((s1, f"{sym}$_1$ = {fmt(s1)}"), (s2, f"{sym}$_2$ = {fmt(s2)}")):
        ax.plot([v], [0], "s", color="#27ae60", ms=6, zorder=5)
        ax.annotate(lab, (v, 0), xytext=(4 if v == s1 else -4, 6), textcoords="offset points",
                    ha="left" if v == s1 else "right", fontsize=9, color="#1e8449", fontweight="bold")
    ax.plot([c, c], [-R, R], ":", color=GR)
    ax.annotate(f"{tsym}$_{{max}}$ = R = {fmt(R)}", (c, -R), xytext=(0, -9), textcoords="offset points", fontsize=8.5, color="#7d3c98", ha="center", va="top")
    ax.plot([c], [R], "^", color="#7d3c98", ms=5); ax.plot([c], [-R], "v", color="#7d3c98", ms=5)
    # 2 theta_p arc from CX to the sigma1 axis
    a_x = math.degrees(math.atan2(X[1], X[0] - c))
    if R > 1e-12:
        ang = -a_x  # rotate from X to s1 (angle 0)
        r_arc = 0.35 * R
        ax.add_patch(Arc((c, 0), 2 * r_arc, 2 * r_arc, theta1=min(a_x, 0), theta2=max(a_x, 0), color="#e67e22", lw=1.4))
        mid = math.radians(0.5 * a_x)
        ax.text(c + 1.25 * r_arc * math.cos(mid), 1.25 * r_arc * math.sin(mid),
                f"2θ$_p$ = {abs(a_x):.1f}°\n({'ccw' if a_x < 0 else 'cw'} X→{sym}$_1$)", fontsize=8, color="#e67e22",
                ha="center", va="center")
    if rot is not None:
        phi = math.radians(rot * 2)
        def rotp(p):
            dx, dy = p[0] - c, p[1]
            # ccw rotation on circle (plot coordinates) = ccw rotation of element in Crandall convention
            return (c + dx * math.cos(phi) - dy * math.sin(phi), dx * math.sin(phi) + dy * math.cos(phi))
        Xp, Yp = rotp(X), rotp(Y)
        ax.plot([Xp[0], Yp[0]], [Xp[1], Yp[1]], color="#16a085", lw=1.3, ls="--")
        ax.plot(*Xp, "D", color="#16a085", ms=5); ax.plot(*Yp, "D", color="#16a085", ms=5)
        ax.annotate(f"X′ ({fmt(Xp[0])}, {fmt(-Xp[1])})", Xp, xytext=(6, 6), textcoords="offset points", fontsize=8.5, color="#16a085")
        ax.annotate(f"Y′ ({fmt(Yp[0])})", Yp, xytext=(6, -12), textcoords="offset points", fontsize=8.5, color="#16a085")
    ax.axhline(0, color=LD, lw=0.8); ax.axvline(0, color=LD, lw=0.8)
    ax.set_aspect("equal")
    lim = max(abs(s1), abs(s2), R) * 1.15 + 1e-9
    xmin = min(0, s2, sigma3 if sigma3 is not None else 0) - 0.15 * lim
    xmax = max(0, s1) + 0.15 * lim
    ax.set_xlim(xmin, xmax); ax.set_ylim(-1.32 * R - 0.1 * lim, 1.25 * R + 0.08 * lim)
    ax.set_xlabel(f"{sym} ({unit})")
    ax.set_ylabel(f"{tsym} ({unit})\n(+{tsym}$_{{xy}}$ plotted DOWN at X)")
    ax.grid(alpha=0.25)
    if title:
        ax.set_title(title, fontsize=10.5, fontweight="bold", loc="left")
    if note:
        ax.text(0.01, 0.01, note, transform=ax.transAxes, fontsize=8, va="bottom",
                bbox=dict(fc="#fffbe6", ec="#e0c060", pad=2))
    save(fig, name)
    return s1, s2, R


# ---------------------------------------------------------------- stress element
def _elem(ax, cx, cy, a, sx, sy, txy, ang=0, unit="MPa", labs=None, col=LD):
    """Square element of half-size a rotated by ang (deg, ccw); draws sx, sy, txy (Crandall signs)."""
    t = math.radians(ang)
    ex = np.array([math.cos(t), math.sin(t)]); ey = np.array([-math.sin(t), math.cos(t)])
    C0 = np.array([cx, cy])
    corners = [C0 + a * (sx_ * ex + sy_ * ey) for sx_, sy_ in ((1, 1), (-1, 1), (-1, -1), (1, -1))]
    ax.add_patch(Polygon(corners, closed=True, fc="#eaeaea", ec=LD, lw=1.2, zorder=2))
    labs = labs or {}
    L = 1.1 * a
    for n, sgn in ((ex, 1), (ex, -1), (ey, 1), (ey, -1)):
        s = sx if n is ex else sy
        if abs(s) > 1e-9:
            p0 = C0 + sgn * n * a * 1.05
            d = sgn * n * (1 if s > 0 else -1)
            start = p0 if s > 0 else p0 - d * L
            end = p0 + d * L if s > 0 else p0
            arrow(ax, *(start if s > 0 else start), *(end if s > 0 else end), color=TC if s > 0 else CC, ms=11)
    # normal stress labels
    if abs(sx) > 1e-9:
        p = C0 + ex * (a * 1.05 + L * 1.25)
        ax.text(*p, labs.get("sx", f"{fmt(abs(sx))}"), ha="center", va="center", fontsize=8.5, color=TC if sx > 0 else CC)
    if abs(sy) > 1e-9:
        p = C0 + ey * (a * 1.05 + L * 1.25)
        ax.text(*p, labs.get("sy", f"{fmt(abs(sy))}"), ha="center", va="center", fontsize=8.5, color=TC if sy > 0 else CC)
    if abs(txy) > 1e-9:
        sg = 1 if txy > 0 else -1
        off = 0.22 * a
        for face, along in ((ex, ey), (-ex, -ey), (ey, ex), (-ey, -ex)):
            base = C0 + face * (a + off)
            arrow(ax, *(base - along * sg * 0.7 * a), *(base + along * sg * 0.7 * a), color="#7d3c98", ms=9, lw=1.3)
        p = C0 + ex * (a + off) + ey * (0.95 * a) + ex * 0.25 * a
        ax.text(*p, labs.get("t", f"{fmt(abs(txy))}"), fontsize=8.5, color="#7d3c98", ha="left", va="bottom")


def element(name, sx, sy, txy, title=None, unit="MPa", principal=True, extra=None, figw=6.4, labs=None):
    c = 0.5 * (sx + sy); R = math.hypot(0.5 * (sx - sy), txy)
    tp = 0.5 * math.degrees(math.atan2(2 * txy, sx - sy))
    n = 3 if principal else 1
    fig, axs = plt.subplots(1, n, figsize=(figw if n == 1 else 7.6, (figw * 0.8) if n == 1 else 3.2))
    axs = np.atleast_1d(axs)
    _elem(axs[0], 0, 0, 1, sx, sy, txy, 0, labs=labs)
    if principal: axs[0].set_title(f"given (x–y)\nσx={fmt(sx)}, σy={fmt(sy)}, τxy={fmt(txy)} {unit}", fontsize=8)
    if principal:
        _elem(axs[1], 0, 0, 1, c + R, c - R, 0, tp)
        axs[1].set_title(f"principal, θp = {tp:.1f}° ({'ccw' if tp >= 0 else 'cw'})\nσ1={fmt(c+R)}, σ2={fmt(c-R)}", fontsize=8)
        _elem(axs[2], 0, 0, 1, c, c, R, tp - 45)
        axs[2].set_title(f"max in-plane shear, θs = {tp-45:.1f}°\nτmax={fmt(R)}, σ′={fmt(c)}", fontsize=8)
    for a in axs:
        a.set_xlim(-3.6, 3.6); a.set_ylim(-3.6, 3.6); a.set_aspect("equal"); a.axis("off")
        arrow(a, -3.3, -3.3, -2.3, -3.3, color=GR, lw=1, ms=8); arrow(a, -3.3, -3.3, -3.3, -2.3, color=GR, lw=1, ms=8)
        a.text(-2.2, -3.35, "x", fontsize=8, color=GR, va="center"); a.text(-3.35, -2.2, "y", fontsize=8, color=GR, ha="center")
    if title:
        fig.suptitle(title, fontsize=10.5, fontweight="bold", x=0.02, ha="left", y=1.02)
    save(fig, name)


# ---------------------------------------------------------------- step diagrams (axial / torque)
def step_diagram(name, xs, vals, labels, title, ylab, unit, bar_widths=None, arrows=None, figw=6.6, kind="axial"):
    """xs: segment boundaries (n+1), vals: internal value per segment (n)."""
    fig, axs = plt.subplots(2, 1, figsize=(figw, 3.9), sharex=True, gridspec_kw={"height_ratios": [0.9, 1], "hspace": 0.1})
    ax = axs[0]
    bw = bar_widths or [1] * len(vals)
    mw = max(bw)
    for i in range(len(vals)):
        h = 0.5 * bw[i] / mw
        ax.add_patch(Rectangle((xs[i], -h / 2), xs[i + 1] - xs[i], h, fc="#dddddd", ec=LD, lw=1))
    for x, lab in zip(xs, labels):
        ax.text(x, -0.5, lab, ha="center", va="top", fontweight="bold")
    L = xs[-1] - xs[0]
    if arrows:
        for x, v, txt in arrows:
            if kind == "axial":
                d = 0.08 * L * (1 if v > 0 else -1)
                arrow(ax, x, 0.42, x + d, 0.42, ms=11)
                ax.text(x + d / 2, 0.5, txt, ha="center", va="bottom", fontsize=8.5)
            else:
                curved_arrow(ax, x, 0.0, 0.18, ccw=v > 0, label=txt)
    ax.set_ylim(-0.75, 0.95); ax.set_xlim(xs[0] - 0.08 * L, xs[-1] + 0.08 * L); ax.axis("off")
    ax.set_title(title, fontsize=10.5, fontweight="bold", loc="left")
    ax2 = axs[1]
    for i, v in enumerate(vals):
        col = TC if v > 0 else CC
        ax2.add_patch(Rectangle((xs[i], 0), xs[i + 1] - xs[i], v, fc=col, alpha=0.3, ec=col))
        ax2.text(0.5 * (xs[i] + xs[i + 1]), v, f"{fmt(v)} {unit}", ha="center", va="bottom" if v >= 0 else "top", fontsize=8.5)
    m = max(abs(v) for v in vals)
    ax2.set_ylim(min(0, min(vals)) - 0.3 * m, max(0, max(vals)) + 0.3 * m)
    ax2.axhline(0, color=LD, lw=0.8); ax2.set_ylabel(ylab); ax2.grid(alpha=0.25)
    save(fig, name)
