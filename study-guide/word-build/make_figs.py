import math, sys
import numpy as np
sys.path.insert(0, "/tmp/claude-0/-home-user-mech-sol-/5e236ef2-e171-5cb2-82aa-007544f55ba5/scratchpad/docx")
from figlib import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle, Arc

only = sys.argv[1:]
def want(n):
    return not only or any(n.startswith(o) for o in only)

def solve_truss(nodes, members, sups, loads):
    names = list(nodes); idx = {n: i for i, n in enumerate(names)}
    nu = len(members) + len(sups)
    A = np.zeros((2 * len(names), nu)); b = np.zeros(2 * len(names))
    for j, (p, q) in enumerate(members):
        (x1, y1), (x2, y2) = nodes[p], nodes[q]
        L = math.hypot(x2 - x1, y2 - y1); c, s = (x2 - x1) / L, (y2 - y1) / L
        A[2 * idx[p], j] += c; A[2 * idx[p] + 1, j] += s; A[2 * idx[q], j] -= c; A[2 * idx[q] + 1, j] -= s
    for k, (n, d) in enumerate(sups):
        A[2 * idx[n] + (0 if d == "x" else 1), len(members) + k] = 1
    for n, fx, fy in loads:
        b[2 * idx[n]] -= fx; b[2 * idx[n] + 1] -= fy
    sol = np.linalg.lstsq(A, b, rcond=None)[0]
    return {m: sol[j] for j, m in enumerate(members)}

# =====================================================================  CH 1
if want("c1_cyl"):
    fig, axs = plt.subplots(1, 3, figsize=(7.4, 3.0))
    r = 1.0
    P = (r, r); Q = (r + 2 * r * math.cos(math.pi / 4), r + 2 * r * math.sin(math.pi / 4))
    ax = axs[0]
    ax.plot([0, 0, Q[0] + r, Q[0] + r], [3.6, 0, 0, 3.6], color=LD, lw=2)
    for c, n in ((P, "P"), (Q, "Q")):
        ax.add_patch(Circle(c, r, fc="#e8eef6", ec=LD)); ax.text(*c, n, ha="center", va="center", fontweight="bold")
    ax.plot([P[0], Q[0]], [P[1], Q[1]], ":", color=GR); ax.text(P[0] + 0.55, P[1] + 0.2, "45°", fontsize=8)
    ax.text(-0.1, P[1], "A", ha="right"); ax.text(P[0], -0.15, "B", ha="center", va="top"); ax.text(Q[0] + r + 0.1, Q[1], "C")
    ax.set_title("(a) system", fontsize=9)
    ax = axs[1]
    ax.add_patch(Circle(Q, r, fc="#e8eef6", ec=LD)); ax.text(*Q, "Q", ha="center", va="center", fontweight="bold")
    arrow(ax, Q[0], Q[1], Q[0], Q[1] - 1.8, color=LD); ax.text(Q[0] + 0.1, Q[1] - 1.9, "900 N", fontsize=8)
    arrow(ax, Q[0] + r + 1.2, Q[1], Q[0] + r, Q[1], color=CC); ax.text(Q[0] + r + 0.2, Q[1] + 0.15, "R$_C$ = 900 N", fontsize=8, color=CC)
    d = np.array([math.cos(math.pi / 4), math.sin(math.pi / 4)])
    s0 = np.array(Q) - d * r
    arrow(ax, *(s0 - d * 1.3), *s0, color=TC); ax.text(*(s0 - d * 1.5), "N = 1273 N\n(along line of centres)", fontsize=8, color=TC, ha="center", va="top")
    ax.set_title("(b) FBD of Q", fontsize=9)
    ax = axs[2]
    ax.add_patch(Circle(P, r, fc="#e8eef6", ec=LD)); ax.text(*P, "P", ha="center", va="center", fontweight="bold")
    arrow(ax, P[0], P[1], P[0], P[1] - 1.7, color=LD); ax.text(P[0] + 0.1, P[1] - 1.75, "900 N", fontsize=8)
    arrow(ax, P[0] - r - 1.2, P[1], P[0] - r, P[1], color=CC); ax.text(P[0] - r - 1.2, P[1] + 0.15, "R$_A$ = 900 N", fontsize=8, color=CC)
    arrow(ax, P[0], P[1] - r - 1.3, P[0], P[1] - r, color=CC); ax.text(P[0] + 0.15, P[1] - r - 1.2, "R$_B$ = 1800 N", fontsize=8, color=CC)
    s1 = np.array(P) + d * r
    arrow(ax, *(s1 + d * 1.3), *s1, color=TC); ax.text(*(s1 + d * 1.35), "N = 1273 N", fontsize=8, color=TC)
    ax.set_title("(c) FBD of P", fontsize=9)
    for a in axs:
        a.set_aspect("equal"); a.axis("off"); a.margins(0.15)
    save(fig, "c1_cyl")

if want("c1_roller"):
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    r, h = 300, 75
    cx = 0; cy = r
    a = math.sqrt(r ** 2 - (r - h) ** 2)
    ax.add_patch(Circle((cx, cy), r, fc="#e8eef6", ec=LD, lw=1.4))
    ax.plot([-600, a, a, 500], [0, 0, h, h], color=LD, lw=2)
    ax.plot([a], [h], "o", color=CC)
    ax.text(a + 10, h - 25, "corner K", fontsize=8.5, color=CC)
    arrow(ax, cx, cy, cx, cy - 260); ax.text(cx + 8, cy - 270, "W = 900 N", fontsize=8.5, va="top")
    th = math.radians(30)
    arrow(ax, cx - 380 * math.cos(th), cy + 380 * math.sin(th), cx, cy, color=TC)
    ax.text(cx - 390 * math.cos(th), cy + 390 * math.sin(th), "F (pushed, 30° below horizontal)\nF = 1867 N", fontsize=8, color=TC, ha="center", va="bottom")
    arrow(ax, a, h, cx + 0.45 * (a - cx), h + 0.45 * (cy - h), color=CC)
    ax.text(a + 15, h + 70, "R (passes through centre O)", fontsize=8, color=CC)
    ax.plot([cx, a], [cy, cy], ":", color=GR); ax.plot([a, a], [cy, h], ":", color=GR)
    ax.text(0.5 * a, cy + 8, f"a = {a:.1f} mm", fontsize=8, ha="center", va="bottom")
    ax.text(a + 8, 0.5 * (cy + h), "r − h = 225 mm", fontsize=8, va="center")
    ax.text(cx - 15, cy + 15, "O", fontsize=9, fontweight="bold", ha="right")
    ax.text(-560, -40, "ground reaction = 0 at the instant of lift-off", fontsize=8, color=GR, va="top")
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(0.05)
    ax.set_title("Lawn roller just leaving the ground: a three-force body", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c1_roller")

if want("c1_incline"):
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    al = math.atan2(3, 4)
    L = 6
    ax.plot([0, L * math.cos(al), L * math.cos(al), 0], [0, L * math.sin(al), 0, 0], color=LD, lw=1.6)
    t = np.array([math.cos(al), math.sin(al)]); n = np.array([-math.sin(al), math.cos(al)])
    c0 = t * 3.0
    blk = [c0 - 0.6 * t, c0 + 0.6 * t, c0 + 0.6 * t + 0.9 * n, c0 - 0.6 * t + 0.9 * n]
    ax.add_patch(Polygon(blk, fc="#e8eef6", ec=LD))
    cm = c0 + 0.45 * n
    arrow(ax, *cm, *(cm + np.array([0, -1.6]))); ax.text(*(cm + np.array([0.1, -1.7])), "500 N", fontsize=8.5)
    arrow(ax, *(cm + 0.6 * t), *(cm + 2.2 * t), color=TC); ax.text(*(cm + 2.3 * t), "T = W", color=TC, fontsize=8.5)
    arrow(ax, *(c0 - 1.4 * n), *c0, color=CC); ax.text(*(c0 - 1.6 * n), "N = 400 N", color=CC, fontsize=8.5, ha="center")
    arrow(ax, *(c0 + 0.3 * n), *(c0 + 0.3 * n - 1.3 * t), color="#7d3c98")
    ax.text(*(c0 + 0.3 * n - 1.9 * t + 0.25 * n), "f ≤ 0.5N = 200 N\n(up or down slope)", color="#7d3c98", fontsize=8)
    ax.text(0.9, 0.12, "α (3-4-5)", fontsize=8.5)
    ax.text(3.2, -0.6, "W$_{min}$ = 500(0.6 − 0.5·0.8) = 100 N;   W$_{max}$ = 500(0.6 + 0.5·0.8) = 500 N", fontsize=8.5, ha="center")
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(0.08)
    ax.set_title("FBD of the block on the incline", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c1_incline")

if want("c1_drum"):
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.4), gridspec_kw={"width_ratios": [1, 1.2]})
    ax = axs[0]
    ax.add_patch(Circle((0, 0), 1, fc="#eeeeee", ec=LD)); ax.plot([0], [0], "k.")
    th = np.linspace(0, np.pi, 100); ax.plot(np.cos(th) * 1.03, np.sin(th) * 1.03, color=TC, lw=3)
    ax.plot([-1.03, -1.03], [0, -1.6], color=TC, lw=3); ax.plot([1.03, 1.03], [0, -2.3], color=TC, lw=3)
    ax.add_patch(Rectangle((-1.4, -2.1), 0.75, 0.5, fc="#ddd", ec=LD)); ax.text(-1.03, -1.85, "1 kN", ha="center", va="center", fontsize=8)
    ax.add_patch(Rectangle((0.6, -2.9), 0.85, 0.6, fc="#ddd", ec=LD)); ax.text(1.03, -2.6, "4 kN", ha="center", va="center", fontsize=8)
    ax.text(-1.15, 0.1, "A", ha="right", fontweight="bold"); ax.text(1.15, 0.1, "B", fontweight="bold")
    ax.text(0, 1.2, "β = π (contact)", ha="center", fontsize=8.5)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_title("(a) set-up", fontsize=9)
    ax = axs[1]
    mu = math.log(4) / math.pi; tt = np.linspace(0, math.pi, 200)
    ax.plot(np.degrees(tt), np.exp(mu * tt), color=TC, lw=2)
    ax.fill_between(np.degrees(tt), 0, np.exp(mu * tt), color=TC, alpha=0.15)
    ax.set_xlabel("θ from A (deg)"); ax.set_ylabel("T(θ) (kN)"); ax.grid(alpha=0.3)
    ax.text(10, 3.3, "T = T$_1$e$^{μθ}$, μ = ln4/π = 0.441\nδ = (r/AE)∫T dθ ⇒ shaded area × r/AE\n   = 0.325 mm", fontsize=8.3)
    ax.set_title("(b) tension along the contact", fontsize=9)
    save(fig, "c1_drum")

if want("c1_truss"):
    s = math.radians(30)
    nd = {"A": (0, 0), "D": (3, 0), "B": (6, 0), "C": (3, 2.25)}
    mem = [("A", "C"), ("B", "C"), ("C", "D"), ("A", "D"), ("B", "D")]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("B", "y")], [("C", 20 * math.sin(s), -20 * math.cos(s)), ("D", 0, -10)])
    truss("c1_q12", nd, mem, f, [("C", 20 * math.sin(s), -20 * math.cos(s)), ("D", 0, -10)], [("A", "pin"), ("B", "roller")],
          "A-frame truss: member forces (kN)", label_off={("C", "D"): (0.35, 0)})
    h = 1.5 * math.tan(math.radians(60))
    nd = {"A": (0, 0), "B": (3, 0), "C": (6, 0), "D": (1.5, h), "E": (4.5, h)}
    mem = [("A", "B"), ("B", "C"), ("A", "D"), ("B", "D"), ("B", "E"), ("C", "E"), ("D", "E")]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("C", "y")], [("D", 0, -2000), ("E", 0, -4000)])
    truss("c1_q13", nd, mem, f, [("D", 0, -2000), ("E", 0, -4000)], [("A", "pin"), ("C", "roller")], "Warren truss: member forces (N)", unit="N")
    nd = {"A": (0, 1.8), "B": (2.4, 1.8), "C": (4.8, 1.8), "E": (0, 0), "D": (2.4, 0)}
    mem = [("A", "B"), ("B", "C"), ("A", "D"), ("B", "D"), ("C", "D"), ("E", "D")]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("E", "x")], [("B", 0, -30), ("C", 0, -30)])
    truss("c1_q14", nd, mem, f, [("B", 0, -30), ("C", 0, -30)], [("A", "fixedL"), ("E", "fixedL")], "Cantilever truss: member forces (kN)",
          label_off={("A", "D"): (-0.3, 0.2), ("B", "D"): (0.3, 0)})
    nd = {"A": (0, 0), "B": (4, 0), "C": (8, 0), "D": (12, 0), "G": (4, 3), "F": (8, 3), "E": (12, 3)}
    nd = {"A": (0, 0), "B": (4, 0), "C": (8, 0), "D": (12, 0), "G": (4, 3), "E": (8, 3)}
    mem = [("A", "B"), ("B", "C"), ("C", "D"), ("A", "G"), ("G", "B"), ("G", "C"), ("G", "E"), ("E", "C"), ("E", "D")]
    loads = [("E", 400, 0), ("C", 0, -1200)]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("D", "y")], loads)
    truss("c1_q16", nd, mem, f, loads, [("A", "pin"), ("D", "roller")], "Section a–a through GE, GC, BC (N) — full solve for checking", unit="N",
          label_off={("G", "C"): (0.4, 0.3)})
    nd = {"A": (0, 0), "D": (3, 0), "F": (6, 0), "H": (9, 0), "J": (12, 0), "B": (0, 3), "C": (3, 3), "E": (6, 3), "G": (9, 3), "I": (12, 3)}
    mem = [("A", "D"), ("D", "F"), ("F", "H"), ("H", "J"), ("B", "C"), ("C", "E"), ("E", "G"), ("G", "I"), ("A", "B"), ("C", "D"), ("E", "F"),
           ("G", "H"), ("I", "J"), ("A", "C"), ("C", "F"), ("F", "G"), ("G", "J")]
    loads = [("B", 20, 0)]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("J", "y")], loads)
    truss("c1_q17", nd, mem, f, loads, [("A", "pin"), ("J", "roller")], "Truss with 20 kN horizontal load at B (kN)", figw=7.2)
    W = 100
    nd = {"A": (0, 4), "B": (6, 4), "C": (12, 4), "D": (18, 4), "G": (0, 0), "F": (6, 0), "E": (12, 0)}
    mem = [("A", "B"), ("B", "C"), ("C", "D"), ("G", "F"), ("F", "E"), ("A", "G"), ("B", "F"), ("C", "E"), ("G", "B"), ("F", "C"), ("E", "D")]
    loads = [("B", 0, -W), ("C", 0, -W), ("D", 0, -W)]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("G", "x"), ("G", "y")], loads)
    truss("c1_q20", nd, mem, f, loads, [("A", "fixedL"), ("G", "fixedL")], "PYQ 2014 T1-Q1 with W = 100 kN: F$_{BC}$ = 450 kN (T) ✓", figw=7.2)

# =====================================================================  CH 2
if want("c2_afd"):
    step_diagram("c2_q1", [0, 0.6, 1.6, 2.8], [50, -30, 10], ["A", "B", "C", "D"], "Brass bar: axial force diagram (tension +)",
                 "P (kN)", "kN", arrows=[(0, -1, "50"), (0.6, 1, "80"), (1.6, -1, "40"), (2.8, 1, "10")])
    step_diagram("c2_q2", [0, 1.2, 1.8, 2.7], [45, -320, 130], ["A", "B", "C", "D"], "Member ABCD: axial force diagram (tension +)",
                 "P (kN)", "kN", bar_widths=[625, 2500, 1250], arrows=[(0, -1, "45"), (1.2, 1, "P$_2$=365"), (1.8, -1, "450"), (2.7, 1, "130")])
    step_diagram("c2_q5", [0, 150, 300, 450, 600], [323, 23, 23, -577], ["A", "D", "C", "K", "B"],
                 "Bar fixed at A and B (drawn horizontal, A at left): final axial force (kN)", "P (kN)", "kN", bar_widths=[250, 250, 400, 400],
                 arrows=[(150, 1, "300"), (450, 1, "600")])

if want("c2_disp"):
    fig, axs = plt.subplots(1, 2, figsize=(7.4, 3.4))
    ax = axs[0]
    ax.plot([0, 3], [0, 0], color=CC, lw=3); ax.plot([0, 3], [3, 0], color=TC, lw=3)
    support(ax, 0, 0, "fixedL", 0.25); support(ax, 0, 3, "fixedL", 0.25)
    ax.text(-0.15, 3, "B", ha="right", fontweight="bold"); ax.text(-0.15, 0, "C", ha="right", fontweight="bold"); ax.text(3.1, 0.1, "D", fontweight="bold")
    arrow(ax, 3, 0, 3, -1); ax.text(3.05, -1, "20 kN", fontsize=8.5)
    ax.text(1.6, 1.7, "BD: 28.28 kN T\nδ = 1.192 mm", color=TC, fontsize=8.5); ax.text(1.0, -0.35, "CD: 20 kN C, δ = 0.0915 mm", color=CC, fontsize=8.5)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_title("(a) bracket", fontsize=9)
    ax = axs[1]
    D = np.array([0, 0]); u = -0.0915
    ax.plot(*D, "ko"); ax.text(0.03, 0.05, "D", fontweight="bold")
    e = np.array([0.7071, -0.7071])
    p1 = D + 1.192 * e
    ax.annotate("", p1, D, arrowprops=dict(arrowstyle="-|>", color=TC)); ax.text(*(p1 * 0.5 + np.array([0.08, 0.05])), "δ$_{BD}$ along BD", color=TC, fontsize=8)
    p2 = D + np.array([u, 0]) * 6
    ax.annotate("", (u, 0), D, arrowprops=dict(arrowstyle="-|>", color=CC)); ax.text(u - 0.05, 0.08, "δ$_{CD}$", color=CC, fontsize=8, ha="right")
    n1 = np.array([0.7071, 0.7071])
    ax.plot([p1[0] - 1.3 * n1[0], p1[0] + 0.3 * n1[0]], [p1[1] - 1.3 * n1[1], p1[1] + 0.3 * n1[1]], "--", color=TC)
    ax.plot([u, u], [0.2, -1.9], "--", color=CC)
    Dp = np.array([u, -1.777])
    ax.plot(*Dp, "s", color="#27ae60"); ax.annotate("", Dp, D, arrowprops=dict(arrowstyle="-|>", color="#27ae60", lw=1.8))
    ax.text(Dp[0] + 0.07, Dp[1] - 0.05, "D′: v = 1.78 mm ↓\nu = 0.092 mm ←", color="#1e8449", fontsize=8.5, va="top")
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(0.25)
    ax.set_title("(b) Williot diagram (displacements in mm)", fontsize=9)
    save(fig, "c2_q7")

    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    A_ = (0, 4.5); B_ = (6, 4.5); C_ = (0, 0)
    ax.plot([0, 6], [4.5, 4.5], color=TC, lw=3); ax.plot([0, 6], [0, 4.5], color=CC, lw=3)
    support(ax, 0, 4.5, "fixedL", 0.3); support(ax, 0, 0, "fixedL", 0.3)
    ax.text(-0.2, 4.6, "A", ha="right", fontweight="bold"); ax.text(-0.2, 0, "C", ha="right", fontweight="bold"); ax.text(6.1, 4.6, "B", fontweight="bold")
    arrow(ax, 6, 4.5, 6, 3.0); ax.text(6.1, 3.0, "P = 20 kN", fontsize=8.5)
    arrow(ax, 6, 4.5, 7.2, 4.5, color="#e67e22"); ax.text(7.25, 4.5, "Q (fictitious)", color="#e67e22", fontsize=8.5, va="center")
    ax.text(2.5, 4.75, "F$_{AB}$ = Q + 1.333P (T), 6 m", color=TC, fontsize=8.5)
    ax.text(3.4, 1.9, "F$_{BC}$ = −1.667P (C), 7.5 m", color=CC, fontsize=8.5, rotation=36.87)
    ax.text(0.2, -0.9, "δ$_v$ = Σ F(∂F/∂P)L/AE = 3.94 mm ↓      δ$_h$ = Σ F(∂F/∂Q)L/AE |$_{Q=0}$ = 1.00 mm →", fontsize=8.5)
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(0.12)
    ax.set_title("Castigliano set-up for the two-bar bracket", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c2_q11")

    h = 2.3 * math.tan(math.radians(60))
    nd = {"A": (0, 0), "J1": (4.6, 0), "J2": (9.2, 0), "R": (13.8, 0), "T1": (2.3, h), "T2": (6.9, h), "T3": (11.5, h)}
    mem = [("A", "J1"), ("J1", "J2"), ("J2", "R"), ("T1", "T2"), ("T2", "T3"), ("A", "T1"), ("T1", "J1"), ("J1", "T2"), ("T2", "J2"), ("J2", "T3"), ("T3", "R")]
    loads = [("J1", 0, -180), ("J2", 0, -270)]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("R", "y")], loads)
    truss("c2_q13", nd, mem, f, loads, [("A", "pin"), ("R", "roller")],
          "Bridge truss (end loads go straight to supports): roller moves ΣFL/AE of bottom chord = 3.68 mm", figw=7.2)

if want("c2_springs"):
    fig, ax = plt.subplots(figsize=(5.4, 2.6))
    def spring(x0, y0, y1, n=7, w=0.25):
        ys = np.linspace(y0, y1, 2 * n + 1); xs = [x0 + (w if i % 2 else -w) * (0 < i < 2 * n) for i in range(2 * n + 1)]
        ax.plot(xs, ys, color=LD, lw=1.3)
    ax.plot([-1.5, 1.5], [0, 0], color=LD, lw=2)
    spring(-0.6, 0, 2); spring(0.6, 0, 2)
    ax.add_patch(Rectangle((-1.2, 2), 2.4, 0.3, fc="#ccc", ec=LD))
    arrow(ax, 0, 3.3, 0, 2.3); ax.text(0.1, 3.0, "F", fontsize=10)
    ax.text(-0.95, 1, "k$_A$", fontsize=10); ax.text(0.85, 1, "k$_B$", fontsize=10)
    ax.text(2.0, 1.6, "parallel springs:\nsame δ, forces add\nk$_{eq}$ = k$_A$ + k$_B$\nF$_A$ = F k$_A$/(k$_A$+k$_B$)", fontsize=9, va="center")
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.8, 5.2)
    save(fig, "c2_springs")

# =====================================================================  CH 3
if want("c3_sign"):
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 2.4))
    for ax, ttl in zip(axs, ("Positive V (Crandall / slides)", "Positive M$_b$ (sagging)")):
        ax.add_patch(Rectangle((0, 0), 1, 1, fc="#eee", ec=LD)); ax.set_xlim(-1, 2); ax.set_ylim(-0.6, 1.6)
        ax.set_aspect("equal"); ax.axis("off"); ax.set_title(ttl, fontsize=9.5)
    arrow(axs[0], 1.15, 0.0, 1.15, 1.0, color=TC); arrow(axs[0], -0.15, 1.0, -0.15, 0.0, color=TC)
    axs[0].text(1.25, 0.5, "+V on +x face\nacts in +y", fontsize=8, color=TC, va="center")
    axs[0].text(-0.25, 0.5, "−x face:\n−y", fontsize=8, color=TC, ha="right", va="center")
    curved_arrow(axs[1], 1.25, 0.5, 0.3, ccw=True, color=TC); curved_arrow(axs[1], -0.25, 0.5, 0.3, ccw=False, color=TC)
    axs[1].text(0.5, -0.4, "top in compression, bottom in tension", ha="center", fontsize=8)
    save(fig, "c3_sign")

if want("c3_beams"):
    beam("c3_q1", 3, {0: "pin", 3: "roller"}, P=[(1, -10), (2, -10)], labels={0: "A", 1: "C", 2: "D", 3: "B"}, title="Two 10 kN loads: SFD and BMD")
    beam("c3_q2", 4, {0: "pin", 4: "roller"}, P=[(1, -10)], C=[(1, -10)], labels={0: "A", 1: "B", 4: "C"},
         title="Bracket load P = 10 kN at L/2 transferred to B as P + couple PL/4 (L = 4 m)")
    beam("c3_q6", 3, {0: "pin", 3: "roller"}, W=[(0, 3, -50, -30)], labels={0: "A", 3: "B"}, extra_x=[1.5], title="Trapezoidal load 50 → 30 kN/m")
    beam("c3_q7", 6, {0: "pin", 6: "roller"}, W=[(0, 3, 0, -4), (3, 6, -4, 0)], labels={0: "A", 6: "B"},
         title="Symmetric triangular load, W = 12 kN, L = 6 m: M$_{max}$ = WL/6 = 12 kN·m")
    beam("c3_q8", 5, {0: "pin", 5: "roller"}, W=[(0, 3, -10, -10)], labels={0: "A", 5: "B"},
         title="Partial UDL (w$_0$ = 10 kN/m over a = 3 m, L = 5 m): M$_{max}$ = w$_0$a²(2L−a)²/8L² = 24.5 kN·m")
    beam("c3_q9", 12, {0: "pin", 12: "roller"}, W=[(0, 9, 0, -2), (9, 12, -2, 0)], labels={0: "A", 9: "", 12: "B"},
         title="Triangular load peaking at 2 kN/m (x = 9 m)")
    beam("c3_q10", 10, {0: "pin", 10: "roller"}, P=[(2, -4), (9, -8)], W=[(3, 7, -2, -2)], labels={0: "A", 2: "C", 3: "D", 7: "E", 9: "F", 10: "B"},
         title="4 kN, 2 kN/m, 8 kN on a 10 m span")
    beam("c3_q11", 8, {0: "pin", 8: "roller"}, P=[(2, -3), (5, -2)], W=[(2, 5, -2, -2)], labels={0: "A", 2: "C", 5: "D", 8: "B"},
         title="3 kN + 2 kN/m + 2 kN: M$_{max}$ = 15.6 kN·m at 3.69 m")
    beam("c3_q12", 8, {0: "pin", 8: "roller"}, W=[(0, 2, -5, -5), (6, 8, -5, -5)], C=[(4, -20)], labels={0: "A", 2: "C", 4: "D", 6: "E", 8: "B"},
         title="5 kN/m segments + 20 kN·m clockwise couple at D")
    beam("c3_q13", 1.414, {0: "pin", 1: "roller"}, W=[(0, 1.414, -1, -1)], labels={0: "A", 1: "B"},
         title="Uniform load with overhang a = 0.414L (L = 1 m, w$_0$ = 1 kN/m): |M$^+$| = |M$_B$|")
    beam("c3_q14", 5.25, {0: "pin", 3.75: "roller"}, P=[(1.5, -1.5)], W=[(3.75, 5.25, -1.5, -1.5)], labels={0: "A", 1.5: "", 3.75: "B"},
         title="Crandall Prob 3.8: overhanging beam")
    beam("c3_q15", 6, {0: "pin", 4.6154: "roller"}, W=[(0, 6, -1, -1)], labels={0: "A", 4.6154: "S", 6: "end"}, extra_x=[4.2],
         title="Carpenter's plank (w$_0$ = 1 kN/m): sawhorse at 4.62 m gives M = 0 at x = 4.2 m")
    beam("c3_q16", 40, {0: "pin", 30: "roller"}, P=[(10, -90)], C=[(20, -10)], W=[(30, 40, -10, -10)], labels={0: "A", 10: "C", 20: "D", 30: "B", 40: "E"},
         title="PYQ 2014 T1-Q4 (singularity functions)")
    beam("c3_q17", 5, {0: "fixedL"}, P=[(1, -30), (3, 80), (5, -20)], labels={0: "A", 1: "B", 3: "C", 5: "D"},
         title="PYQ 2014 Compre A Q17–18: cantilever")
    beam("c3_q3", 6, {0: "pin", 6: "roller"}, P=[(2, -10.8)], labels={0: "A", 2: "B", 4: "C", 6: "D"},
         title="Beam ABCD: vertical part of the pulley force at B (axial force −21.6 kN in A–C not shown)")

if want("c3_frame"):
    b = 1.0; P = 1.0
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.2), gridspec_kw={"width_ratios": [1.2, 1]})
    ax = axs[0]
    pts = {"A": (0, 0), "B": (6, 0), "C": (6, -2), "D": (4, -2)}
    ax.plot([0, 6, 6, 4], [0, 0, -2, -2], color=LD, lw=3)
    support(ax, 0, 0, "fixedL", 0.3)
    for k, (x, y) in pts.items():
        ax.text(x + 0.1, y + 0.12, k, fontweight="bold")
    arrow(ax, 4, -2, 2.9, -2, color=LD); arrow(ax, 4, -2, 4, -0.9, color=LD)
    ax.text(2.9, -1.85, "P", fontsize=9); ax.text(3.6, -1.0, "P", fontsize=9)
    for (x, y, v) in ((0, 0, 2), (6, 0, -4), (6, -2, -2), (4, -2, 0), (2, 0, 0)):
        ax.text(x, y + (0.45 if y == 0 else -0.45), f"{v}Pb" if v else "0", color=CC, fontsize=8.5, ha="center")
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(0.15)
    ax.set_title("(a) bracket ABCD (dimensions in b); M values at joints", fontsize=9)
    ax = axs[1]
    s = np.linspace(0, 10, 300)
    def Ms(sv):
        if sv <= 6: return P * (2 - sv)
        if sv <= 8: return P * (-4 + (sv - 6) * 1.0)
        return P * (-2 + (sv - 8))
    m = [Ms(v) for v in s]
    m = []
    for v in s:
        if v <= 6: m.append(2 - v)
        elif v <= 8: m.append(-4 + (v - 6))
        else: m.append(-2 + (v - 8))
    ax.plot(s, m, color=LD); ax.fill_between(s, 0, m, where=np.array(m) < 0, color=CC, alpha=0.25); ax.fill_between(s, 0, m, where=np.array(m) >= 0, color=TC, alpha=0.25)
    ax.axhline(0, color=LD, lw=0.8); ax.grid(alpha=0.3)
    for x, lab in ((0, "A"), (6, "B"), (8, "C"), (10, "D")):
        ax.axvline(x, color=GR, ls=":"); ax.text(x, 2.3, lab, ha="center", fontweight="bold")
    ax.set_xlabel("arc length from A (units of b)"); ax.set_ylabel("M / (Pb)")
    ax.text(6.2, -4.2, "|M|max = 4Pb at B", color=CC, fontsize=8.5)
    ax.set_ylim(-4.8, 2.8); ax.set_title("(b) M along A→B→C→D", fontsize=9)
    save(fig, "c3_q18")

    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    th = np.linspace(0, 90, 200); t = np.radians(th)
    ax.plot(th, np.cos(t), label="N/P = cos θ (compression)", color=CC)
    ax.plot(th, np.sin(t), label="V/P = sin θ", color=TC)
    ax.plot(th, np.cos(t), ls="--", color="#7d3c98", label="M/(PR) = cos θ")
    ax.set_xlabel("θ (deg) from fixed end A"); ax.grid(alpha=0.3); ax.legend(fontsize=8)
    ax.set_title("Curved cantilever (tip load P): internal forces vs θ", fontsize=10, fontweight="bold", loc="left")
    save(fig, "c3_q19")

# =====================================================================  CH 4
if want("c4_concept"):
    element("c4_posshear", 0, 0, 1, title="Positive τxy (Crandall): ↑ on +x face, → on +y face", principal=False, figw=3.6, labs={"t": "+τxy"})
    mohr("c4_mohr_construct", 50, -10, 40, title="Mohr's circle construction (example σx=50, σy=−10, τxy=+40 MPa)",
         note="1) X = (σx, τxy plotted DOWN)  2) Y = (σy, τxy UP)  3) XY crosses σ-axis at C\n4) R = CX  5) σ1,2 = C ± R  6) rotate 2θ on circle = θ on element, same sense")
    fig, axs = plt.subplots(1, 4, figsize=(7.4, 2.2))
    cases = [("uniaxial tension", 1, 0, 0), ("uniaxial compression", -1, 0, 0), ("pure shear", 0, 0, 1), ("equal biaxial", 1, 1, 0)]
    for ax, (t, sx, sy, tx) in zip(axs, cases):
        c = (sx + sy) / 2; R = math.hypot((sx - sy) / 2, tx)
        th = np.linspace(0, 2 * np.pi, 200)
        ax.plot(c + R * np.cos(th), R * np.sin(th), color=TC, lw=1.5)
        if R == 0: ax.plot([c], [0], "o", color=TC)
        ax.axhline(0, color=LD, lw=0.7); ax.axvline(0, color=LD, lw=0.7)
        ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.1, 1.1); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(t, fontsize=8.5)
    save(fig, "c4_signature")

if want("c4_mohr"):
    mohr("c4_q1", 110, 50, 40, rot=45, title="Q1: rotate 45° (2θ = 90° on the circle): σa = 120, σb = 40, τab = −30 MPa")
    mohr("c4_q2", 27, -45, 18, rot=105, title="Q2: oblique face, normal at θ = 105°: σ = −49.2, τ = 2.41 MPa")
    mohr("c4_q3", 125, 0, 0, rot=14.34, title="Q3: weld at β = 14.3°: τ = 30 MPa, σ = 117.3 MPa")
    mohr("c4_q4", 50, -10, 40, title="Q4: σ1 = 70, σ2 = −30 MPa, θp = 26.6° ccw")
    element("c4_q4e", 50, -10, 40, title="Q4 elements: given, principal, max shear")
    mohr("c4_q5", 100, 60, -48, rot=30, title="Q5: X′ after 30° ccw: σx′ = 48.4, τx′y′ = −41.3 MPa")
    element("c4_q5e", 100, 60, -48, title="Q5 elements")
    mohr("c4_q8", 0, 71.6, 19.9, title="Q8 (PYQ 2014 T2-Q1): σ1 = 76.8, σ2 = −5.2 MPa (axis along y)")
    mohr("c4_q9", -193.1, -356.9, -102.2, sigma3=0, title="Q9 (PYQ 2014 C-B1): both principal stresses compressive",
         note="dashed: circles with σ3 = 0 → τabs,max = 406/2 = 203 MPa > R")
    element("c4_q9e", -193.1, -356.9, -102.2, title="Q9 resultant element (x–y) and principal element")
    mohr("c4_q10", -200, 1000, 450, strain=True, rot=-30, unit="μ", title="Q10: strain circle (γ/2 axis); x′ at 30° cw",
         note="ε1 = 1150μ, ε2 = −350μ;  εx′ = −290μ, γx′y′ = −590μ")
    mohr("c4_q11", 800, 100, -400, strain=True, unit="μ", title="Q11 (Crandall 4.20): ε1 = 981.5μ, ε2 = −81.5μ")
    mohr("c4_q12", 60, 246, -74.5, strain=True, unit="μ", title="Q12: 60° rosette → ε1 = 272μ, ε2 = 33.8μ")
    mohr("c4_q14", 5.8, -31.6, -32.3, title="Q14 (PYQ 2019 A-Q2): from σ1 = −50.2, σ2 = 24.5 back to x–y",
         note="axis 1 is 60° from x: rotate 120° on the circle")
    mohr("c4_q16", 250, -75, 0, strain=True, unit="μ", title="Q16: uniaxial bar strains; γabs,max = 250 − (−75) = 325μ")

if want("c4_ellipse"):
    fig, ax = plt.subplots(figsize=(4.8, 4.2))
    th = np.linspace(0, 2 * np.pi, 300)
    k = 300  # exaggeration
    e1, e2, tp = 569.3e-6, -61.8e-6, math.radians(5.94)
    a, b = 1 + k * e1, 1 + k * e2
    x = a * np.cos(th); y = b * np.sin(th)
    ax.plot(np.cos(th), np.sin(th), "--", color=GR, label="original circle d = 250 mm")
    ax.plot(x * math.cos(tp) - y * math.sin(tp), x * math.sin(tp) + y * math.cos(tp), color=TC, lw=2, label="ellipse (strain ×300)")
    ax.plot([-a * math.cos(tp), a * math.cos(tp)], [-a * math.sin(tp), a * math.sin(tp)], color=CC)
    ax.plot([b * math.sin(tp), -b * math.sin(tp)], [-b * math.cos(tp), b * math.cos(tp)], color="#27ae60")
    ax.text(1.2, 0.2, "major 250.142 mm\nat 5.94°", color=CC, fontsize=8.5); ax.text(-0.25, 1.05, "minor 249.985 mm", color="#1e8449", fontsize=8.5)
    ax.set_aspect("equal"); ax.axis("off"); ax.legend(fontsize=8, loc="lower center", bbox_to_anchor=(0.5, -0.15))
    ax.set_title("Q15: circle → ellipse (exaggerated)", fontsize=10, fontweight="bold", loc="left")
    save(fig, "c4_q15")

# =====================================================================  CH 5
if want("c5"):
    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    Y = 1
    hexa = np.array([[Y, 0], [Y, Y], [0, Y], [-Y, 0], [-Y, -Y], [0, -Y], [Y, 0]])
    ax.plot(hexa[:, 0], hexa[:, 1], color=CC, lw=1.8, label="Tresca (hexagon)")
    t = np.linspace(0, 2 * np.pi, 400)
    # ellipse s1^2 - s1 s2 + s2^2 = 1 : principal axes along 45°
    u = np.sqrt(2) * np.cos(t); v = np.sqrt(2 / 3) * np.sin(t)
    ax.plot((u - v) / np.sqrt(2), (u + v) / np.sqrt(2), color=TC, lw=1.8, label="von Mises (ellipse)")
    ax.axhline(0, color=LD, lw=0.8); ax.axvline(0, color=LD, lw=0.8)
    p = (80 / 270, 15 / 270)
    ax.plot(*p, "ko"); ax.annotate("PYQ 2019 A-Q4 (80, 15 MPa)/Y\nTresca n = 3.38, vM n = 3.67", p, xytext=(10, -40), textcoords="offset points", fontsize=8,
                                   arrowprops=dict(arrowstyle="-", color=GR))
    ax.plot([0.577, -0.577], [-0.577, 0.577], "^", color="#7d3c98")
    ax.annotate("pure shear: vM τY = 0.577Y\nTresca τY = 0.5Y", (0.577, -0.577), xytext=(10, -10), textcoords="offset points", fontsize=8, color="#7d3c98")
    ax.plot([0.5, -0.5], [-0.5, 0.5], "v", color=CC)
    ax.set_xlabel("σ1 / Y"); ax.set_ylabel("σ2 / Y"); ax.set_aspect("equal"); ax.grid(alpha=0.3); ax.legend(fontsize=8, loc="upper left")
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)
    ax.set_title("Yield surfaces in plane stress (σ3 = 0)", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c5_yield")
    mohr("c5_q14", 60, 35, -30, sigma3=0, title="Q14 (PYQ 2019 A-Q4): σ1 = 80, σ2 = 15, σ3 = 0 MPa",
         note="largest circle is σ1–σ3 (dashed): Tresca uses 80 − 0, not 80 − 15")
    fig, axs = plt.subplots(1, 4, figsize=(7.4, 2.1))
    e = np.linspace(0, 1, 100)
    axs[0].plot(e, e, color=TC); axs[0].set_title("linear elastic", fontsize=8.5)
    axs[1].plot([0, 0, 1], [0, 0.6, 0.6], color=TC); axs[1].set_title("rigid–perfectly plastic", fontsize=8.5)
    axs[2].plot([0, 0.4, 1], [0, 0.6, 0.6], color=TC); axs[2].set_title("elastic–perfectly plastic", fontsize=8.5)
    axs[3].plot([0, 0.4, 1], [0, 0.6, 0.85], color=TC); axs[3].set_title("linear strain hardening", fontsize=8.5)
    for a in axs:
        a.set_xticks([]); a.set_yticks([]); a.set_xlabel("ε", fontsize=8); a.set_ylabel("σ", fontsize=8); a.set_ylim(0, 1); a.set_xlim(0, 1)
    save(fig, "c5_ideal")
    fig, ax = plt.subplots(figsize=(6.0, 2.6))
    for i, (yy, t) in enumerate(((2.2, "(a) free: grows δT = αΔTL, no stress"), (1.1, "(b) push back with P: δP = PL/AE"), (0, "(c) fixed: δT + δP = 0 ⇒ σ = −EαΔT"))):
        ax.add_patch(Rectangle((0, yy), 4 + (0.4 if i == 0 else 0), 0.45, fc="#f3d1c9" if i == 0 else "#ddd", ec=LD))
        ax.plot([0, 0], [yy - 0.15, yy + 0.6], color=LD, lw=2)
        ax.text(5.0, yy + 0.22, t, va="center", fontsize=8.5)
    ax.plot([4, 4], [-0.15, 0.6], color=LD, lw=2)
    arrow(ax, 4.9, 1.32, 4.02, 1.32, color=CC); ax.text(4.5, 1.6, "P", color=CC)
    ax.set_xlim(-0.3, 10); ax.set_ylim(-0.4, 2.9); ax.axis("off")
    ax.set_title("Thermal stress by superposition", fontsize=10, fontweight="bold", loc="left")
    save(fig, "c5_thermal")

# =====================================================================  CH 6
if want("c6"):
    fig, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
    for ax, (ro, ri, t) in zip(axs, ((1, 0, "solid: τ = Tr/J, max at surface"), (1, 0.6, "hollow: τmin = τmax·ri/ro"))):
        th = np.linspace(0, 2 * np.pi, 200)
        ax.add_patch(Circle((0, 0), ro, fc="#e8eef6", ec=LD))
        if ri: ax.add_patch(Circle((0, 0), ri, fc="white", ec=LD))
        r = np.linspace(ri, ro, 8)
        for rr in r:
            if rr > 0:
                arrow(ax, rr, 0, rr, 0.55 * rr, color=TC, lw=1.2, ms=8)
        ax.plot([ri, ro], [0.55 * ri, 0.55 * ro], color=TC)
        ax.plot([0, ro], [0, 0], color=LD, lw=0.8)
        ax.set_aspect("equal"); ax.axis("off"); ax.set_title(t, fontsize=9)
        ax.set_xlim(-1.2, 1.4); ax.set_ylim(-1.2, 1.2)
    save(fig, "c6_dist")
    step_diagram("c6_q5", [0, 0.9, 1.6, 2.1], [6, 20, -6], ["A", "B", "C", "D"], "Four-gear shaft: internal torque (kN·m)", "T (kN·m)", "kN·m",
                 bar_widths=[1, 1.6, 1], arrows=[(0, 1, "6"), (0.9, 1, "14"), (1.6, -1, "26"), (2.1, 1, "6")], kind="torque")
    step_diagram("c6_q7", [0, 0.6, 0.8, 1.2], [2250, 2250, 250], ["D", "C", "B", "A"], "Shaft AD (D fixed): internal torque (N·m)", "T (N·m)", "N·m",
                 bar_widths=[0.6, 0.6, 0.3], arrows=[(0.8, 1, "2000"), (1.2, 1, "250")], kind="torque")
    step_diagram("c6_q14", [0, 1.2, 2.4], [3.393, -1.696], ["A", "B", "C"], "PYQ 2023 A-Q1: internal torque (kN·m); segments partly cancel in φA/C",
                 "T (kN·m)", "kN·m", arrows=[(0, 1, "⅔T"), (1.2, -1, "T"), (2.4, 1, "⅓T")], kind="torque")
    step_diagram("c6_q19", [0, 0.6, 2.4], [52.5, -17.5], ["A", "B", "C"], "Fixed–fixed shaft: internal torque (N·m); O at 1.2 m from C",
                 "T (N·m)", "N·m", arrows=[(0.6, 1, "70")], kind="torque")
    fig, axs = plt.subplots(2, 1, figsize=(6.6, 4.6), sharex=True)
    xs = [0, 0.36, 0.72, 1.2]; T = [1200, 400, -1200]
    for i, v in enumerate(T):
        col = TC if v > 0 else CC
        axs[0].add_patch(Rectangle((xs[i], 0), xs[i + 1] - xs[i], v, fc=col, alpha=0.3, ec=col))
        axs[0].text(0.5 * (xs[i] + xs[i + 1]), v, f"{v} N·m", ha="center", va="bottom" if v > 0 else "top", fontsize=8.5)
    axs[0].axhline(0, color=LD, lw=0.8); axs[0].set_ylim(-1700, 1700); axs[0].set_ylabel("T (N·m)"); axs[0].grid(alpha=0.3)
    axs[0].set_title("PYQ 2024 B-Q1: internal torque and twist (T₀ = 800 N·m)", fontsize=10, fontweight="bold", loc="left")
    phi = [0, 1.231, 1.641, 0]
    axs[1].plot(xs, phi, "o-", color="#7d3c98"); axs[1].fill_between(xs, 0, phi, color="#7d3c98", alpha=0.15)
    for x, p, lab in zip(xs, phi, "ABCD"):
        axs[1].text(x, p + 0.12, f"{lab}: {p}°", ha="center", fontsize=8.5)
    axs[1].set_ylabel("φ (deg)"); axs[1].set_xlabel("x (m)"); axs[1].set_ylim(-0.2, 2.1); axs[1].grid(alpha=0.3)
    save(fig, "c6_q20")
    mohr("c6_q22", 63.66, 0, 97.78, title="Q22 helicopter shaft: σ1 = 134.7, σ2 = −71.0, τmax = 102.8 MPa")
    mohr("c6_q24", -139.9, 0, 54.4, title="Q24 axle at H: σ1 = 18.7, σ2 = −158.5 MPa;  σvm = 168.7 MPa < 350")
    element("c6_q24e", -139.9, 0, 54.4, title="Q24 stress element at H (x = axle axis)")
    mohr("c6_q25", 415.1, 0, 127.3, title="Q25 crank, element E₁: σmax = 451, σmin = −35.9, τmax = 243.5 MPa")
    mohr("c6_q26", -83.2, 0, -21.3, title="Q26 post, point B: σ1 = 5.15, σ2 = −88.4, τmax = 46.8 MPa")
    element("c6_q26e", -83.2, 0, -21.3, title="Q26 stress element at B (x = post axis)")
print("done")

# =====================================================================  v2 additions
if want("v2c1"):
    # Q11 rod on roller: three-force concurrency
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    b = 1.0; th = math.radians(30); x = b / math.cos(th) ** 3
    B = np.array([0, 0]); A = np.array([b, b * math.tan(th)]); Wp = x * np.array([math.cos(th), math.sin(th)])
    end = 1.25 * x * np.array([math.cos(th), math.sin(th)])
    ax.plot([0, 0], [-0.5, 1.6], color=LD, lw=2)
    for k in range(10):
        ax.plot([0, -0.08], [-0.5 + 0.2 * k, -0.58 + 0.2 * k], color=LD, lw=0.8)
    ax.plot([B[0], end[0]], [B[1], end[1]], color=TC, lw=3)
    ax.add_patch(Circle(A - np.array([0, 0.05]), 0.05, fc="white", ec=LD))
    K = np.array([x * math.cos(th), 0])
    arrow(ax, *(B - np.array([0, 0])), *(B + np.array([0.45, 0])), color=CC); ax.text(0.08, -0.12, "N$_B$ (smooth wall)", color=CC, fontsize=8.5)
    arrow(ax, *Wp, *(Wp + np.array([0, -0.7])), color=LD); ax.text(Wp[0] + 0.04, Wp[1] - 0.55, "W", fontsize=10)
    nA = np.array([-math.sin(th), math.cos(th)])
    arrow(ax, *A, *(A + 0.6 * nA), color=TC); ax.text(*(A + 0.65 * nA), "N$_A$ perpendicular to rod", color=TC, fontsize=8.5)
    for P0, d in ((B, np.array([1, 0])), (Wp, np.array([0, -1])), (A, -nA)):
        L = np.linalg.norm(K - P0)
        ax.plot([P0[0], K[0]], [P0[1], K[1]], ":", color=GR)
    ax.plot(*K, "o", color="#27ae60"); ax.text(K[0] + 0.03, K[1] - 0.14, "K: all three lines meet", color="#1e8449", fontsize=8.5)
    ax.annotate("", (b, -0.32), (0, -0.32), arrowprops=dict(arrowstyle="<->", color=GR)); ax.text(b / 2, -0.42, "b", ha="center", color=GR)
    ax.text(0.25, 0.05, "θ", fontsize=10)
    ax.text(0.55, 1.45, "x = b / cos³θ", fontsize=11, fontweight="bold", color="#1e8449")
    ax.set_aspect("equal"); ax.axis("off"); ax.margins(0.1)
    ax.set_title("Crandall 1.21: three-force member (θ = 30° shown)", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c1v_q11")
    # Q9 forearm FBD
    fig, ax = plt.subplots(figsize=(6.4, 2.6))
    ax.add_patch(Rectangle((0, -0.06), 370, 0.12 * 100 / 100 * 1, fc="#f3e3d3", ec=LD))
    ax.plot([0], [0], "ko")
    arrow(ax, 40, 0.06, 40, 0.9, color=TC); ax.text(48, 0.62, "F$_m$ = 782 N (muscle)", color=TC, fontsize=9)
    arrow(ax, 0, 0.9, 0, 0.06, color=CC); ax.text(-6, 0.55, "J = 686 N\n(humerus on ulna)", color=CC, fontsize=9, ha="right")
    arrow(ax, 105, -0.06, 105, -0.6, color=LD); ax.text(108, -0.55, "16 N", fontsize=9)
    arrow(ax, 370, -0.06, 370, -0.8, color=LD); ax.text(330, -0.75, "80 N", fontsize=9)
    ax.text(40, -0.12, "40", ha="center", va="top", fontsize=8, color=GR)
    for xx, lab in ((105, "105"), (370, "370 mm")):
        ax.text(xx, 0.12, lab, ha="center", fontsize=8, color=GR)
    ax.text(-20, -1.08, "moments about the joint:  40 F$_m$ = 80(370) + 16(105)  →  F$_m$ = 782 N", fontsize=8.5)
    ax.set_xlim(-130, 420); ax.set_ylim(-1.2, 1.1); ax.axis("off")
    ax.set_title("Crandall 1.42: FBD of the forearm (elbow at 90°)", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c1v_q9")
    # Q14 in-plane forces on incline
    fig, ax = plt.subplots(figsize=(4.8, 3.6))
    arrow(ax, 0, 0, 0, -0.6, color=LD); ax.text(0.03, -0.62, "W sinθ = 0.6W\n(down the slope)", fontsize=8.5, va="top")
    arrow(ax, 0, 0, 0.4, 0, color=TC); ax.text(0.42, 0.02, "P = 0.4W", color=TC, fontsize=8.5)
    arrow(ax, 0, 0, 0.4, -0.6, color="#7d3c98"); ax.text(0.42, -0.55, "resultant\n0.721W", color="#7d3c98", fontsize=8.5)
    arrow(ax, 0, 0, -0.4, 0.6, color=CC); ax.text(-0.75, 0.5, "friction\nμN = μ(0.8W)", color=CC, fontsize=8.5)
    ax.plot([0], [0], "ks")
    ax.text(-0.75, -0.95, "view normal to the incline;  μ = 0.721/0.8 = 0.90", fontsize=8.5)
    ax.set_aspect("equal"); ax.set_xlim(-0.9, 1.0); ax.set_ylim(-1.05, 0.85); ax.axis("off")
    ax.set_title("Crandall 1.39: forces in the plane of the incline", fontsize=10, fontweight="bold", loc="left")
    save(fig, "c1v_q14")
    # Q25 truss 1.31 (W = 1, L = 1)
    nd = {"A": (0, 1), "B": (1, 1), "C": (2, 1), "E": (0, 0), "D": (1, 0)}
    mem = [("A", "B"), ("B", "C"), ("E", "D"), ("B", "D"), ("E", "B"), ("D", "C")]
    f = solve_truss(nd, mem, [("A", "x"), ("A", "y"), ("E", "x"), ("E", "y")], [("C", 0, -1)])
    truss("c1v_q25", nd, mem, f, [("C", 0, -1)], [("A", "fixedL"), ("E", "fixedL")], "Crandall 1.31: member forces in units of W", unit="W")

if want("v2c2"):
    # Q13 kinked spring
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    d = np.linspace(0, 0.25, 200); kb, k2 = 1.178e6, 2.552e6
    P = np.where(d <= 0.08, kb * d, kb * 0.08 + k2 * (d - 0.08)) / 1e3
    ax.plot(d, P, color=TC, lw=2); ax.plot([0.08], [94.2], "o", color=CC)
    ax.annotate("kink: aluminium touches\nP = 94.2 kN at δ = 0.08 mm", (0.08, 94.2), xytext=(0.1, 40), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=GR))
    ax.text(0.02, 60, "brass only\nk = 1.18 MN/mm", fontsize=8.5); ax.text(0.16, 260, "brass + Al\nk = 2.55 MN/mm", fontsize=8.5)
    ax.set_xlabel("δ (mm)"); ax.set_ylabel("P (kN)"); ax.grid(alpha=0.3)
    ax.set_title("Crandall 2.14: load–deflection curve with a kink", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c2v_q13")
    # Q10 two rods, rigid member displaced
    fig, ax = plt.subplots(figsize=(5.6, 2.8))
    ax.plot([0, 675], [0, 0], color=GR, lw=6, alpha=0.4)
    s = 120
    ax.plot([0, 675], [-0.853 * s, -0.72 * s], color=TC, lw=4)
    ax.plot([375], [-(0.853 + (0.72 - 0.853) * 375 / 675) * s], "o", color=CC)
    ax.text(0, -0.853 * s - 18, "0.853 mm", ha="center", fontsize=8.5); ax.text(675, -0.72 * s - 18, "0.720 mm", ha="center", fontsize=8.5)
    ax.text(375, -0.779 * s + 10, "B: 0.78 mm", ha="center", fontsize=9, color=CC)
    ax.plot([0, 0], [0, 60], color=LD, lw=2); ax.plot([675, 675], [0, 80], color=LD, lw=2)
    ax.text(5, 40, "2 m, 625 mm²", fontsize=8); ax.text(560, 60, "2.7 m, 1250 mm²", fontsize=8)
    ax.set_ylim(-140, 100); ax.axis("off")
    ax.set_title("Crandall 2.17: displaced rigid member (deflections ×120)", fontsize=10, fontweight="bold", loc="left")
    save(fig, "c2v_q10")
    # Q16 three-bar framework forces vs theta
    th = np.linspace(0, 80, 200); t = np.radians(th)
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    den = 1 + 2 * np.cos(t) ** 3
    ax.plot(th, 1 / den, label="inner bar N$_i$/F", color=TC); ax.plot(th, np.cos(t) ** 2 / den, label="outer bar N$_o$/F", color=CC)
    ax.set_xlabel("θ (deg), with A₀ = A"); ax.grid(alpha=0.3); ax.legend(fontsize=8.5)
    ax.set_title("Crandall 2.12: bar forces vs angle (equal areas)", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c2v_q16")
    # Q23 truss deflection table figure: reuse member forces from Ch1 Q25 with f^2 L
    nd = {"P": (0, 1), "Q": (1, 1), "R": (2, 1), "T": (0, 0), "S": (1, 0)}
    mem = [("P", "Q"), ("Q", "R"), ("T", "S"), ("Q", "S"), ("T", "Q"), ("S", "R")]
    f = solve_truss(nd, mem, [("P", "x"), ("P", "y"), ("T", "x"), ("T", "y")], [("R", 0, -1)])
    truss("c2v_q23", nd, mem, f, [("R", 0, -1)], [("P", "fixedL"), ("T", "fixedL")], "Crandall 2.10: f = F/W per member; δ = Σf²L·W/AE = 12.66 WL/AE", unit="W")

if want("v2c3"):
    beam("c3v_q5a", 1, {0: "fixedL"}, P=[(1, -1)], labels={0: "wall", 1: "W"}, title="Crandall 3.1: cantilever, weight W at the tip (W = 1, L = 1)", unit_F="W", unit_L="L")
    beam("c3v_q5b", 1, {0: "fixedL"}, P=[(1, -1), (0.7, 1)], labels={0: "wall", 0.7: "", 1: "tip"}, title="Crandall 3.4: P down at the tip, P up at a = 0.3L from it (P = 1, L = 1)", unit_F="P", unit_L="L")
    beam("c3v_q6", 0.4, {0: "pin", 0.4: "roller"}, C=[(0.25, -60)], labels={0: "A", 0.25: "arm", 0.4: "B"}, title="Crandall 3.14: beam AB carries the arm's 60 N·m clockwise couple", unit_F="N", unit_L="m")
    beam("c3v_q12", 2, {0: "fixedL"}, W=[(0, 2, -5, -5)], labels={0: "wall", 2: "tip"}, title="Crandall 3.6: cantilever, full UDL (w₀ = 5 kN/m, L = 2 m)")
    beam("c3v_q13", 3, {0: "pin", 3: "roller"}, W=[(0, 3, 0, -16)], labels={0: "L", 3: "R"}, title="Crandall 3.10: sixty 400 N sandbags (triangular, 24 kN total)")
    beam("c3v_q14", 1.8, {0: "fixedL"}, W=[(0, 1.8, -42.38, 0)], labels={0: "bed", 1.8: "surface"}, title="Crandall 3.34: dam upright as a cantilever from the river bed (x up from bed)")
    beam("c3v_q21", 2, {2: "fixedR"}, P=[(0, -1)], W=[(1, 2, -1, -1)], labels={0: "A", 2: "B"}, title="Crandall 3.12: P = 1 kN at A, w₀ = 1 kN/m on the half next to the wall (L = 2 m)")
    beam("c3v_q23", 1, {0.2071: "pin", 0.7929: "roller"}, W=[(0, 1, -1, -1)], labels={0.2071: "", 0.7929: ""}, title="Crandall 3.25: bookshelf with bricks at 0.207L (w = 1, L = 1): equal ± peaks", unit_F="wL", unit_L="L")
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    th = np.linspace(0, 90, 200); t = np.radians(th)
    ax.plot(th, np.sin(t), color=TC, label="M$_b$/(Pa) = sin θ"); ax.plot(th, -(1 - np.cos(t)), color=CC, label="M$_t$/(Pa) = −(1 − cos θ)")
    ax.axhline(0, color=LD, lw=0.7); ax.grid(alpha=0.3); ax.legend(fontsize=8.5); ax.set_xlabel("θ from free end A (deg)")
    ax.set_title("Crandall Example 3.11: bending and twist in the pipe bend", fontsize=10, fontweight="bold", loc="left")
    save(fig, "c3v_q26")

if want("v2c4"):
    mohr("c4v_q9", -120, 50, 100, title="Crandall 4.7(c): σ1 = 96.2, σ2 = −166.2 MPa, θp = 65.2°")
    mohr("c4v_q10", 105, 21, -56, title="Crandall 4.8: σx = 105 gives σ2 = −7 MPa exactly")
    mohr("c4v_q11", -15, 75, 0, rot=-30, title="Crandall 4.15: faces a (θ = −30°) and b")
    mohr("c4v_q12", 13.12, -38.12, 20, title="Crandall 4.28: one of the two solutions (σx = 13.1, σy = −38.1)")
    element("c4v_q17", 1, 2, 0, title="Closed thin cylinder: wall element", principal=False, figw=3.8, labs={"sx": "σz = pr/2t", "sy": "σθ = pr/t"})
    mohr("c4v_q20", 20000, 0, 0, rot=30, unit="psi", title="Crandall 4.27(a): σz = 20 ksi, σθ = 0; m at 30°")
    mohr("c4v_q26", 700, -300, 0, strain=True, unit="μ", sigma3=300, title="Crandall 4.21: three strain circles; γmax = 1000μ",
         note="largest circle spans ε_I = 700μ to ε_III = −300μ")
    mohr("c4v_q27", -800, -200, -300, strain=True, unit="μ", sigma3=0, title="Crandall 4.23: in-plane γmax = 848μ; out-of-plane 924μ",
         note="dashed: circles to ε3 = 0 (plane strain)")
    mohr("c4v_q29", 100, 900, -300, strain=True, unit="μ", title="Crandall 4.22(a): ε1 = 1000μ, ε2 = 0")

if want("v2c5"):
    mohr("c5v_q3", 755, -545, 520, strain=True, unit="μ", title="Crandall 5.8: strain circle, ε1 = 937μ, ε2 = −727μ at 19.3°")
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    nu = np.linspace(0, 0.49, 200)
    ax.plot(nu, 1 / (1 - nu ** 2), label="one lateral direction fixed: 1/(1−ν²)", color=TC)
    ax.plot(nu, (1 - nu) / ((1 + nu) * (1 - 2 * nu)), label="two lateral directions fixed", color=CC)
    ax.set_ylim(0.9, 6); ax.set_xlabel("ν"); ax.set_ylabel("stiffness ÷ free-bar stiffness"); ax.grid(alpha=0.3); ax.legend(fontsize=8)
    ax.axvline(0.3, color=GR, ls=":"); ax.text(0.31, 4.5, "ν = 0.3:\n1.10 and 1.35", fontsize=8.5)
    ax.set_title("Lateral constraint stiffens a member (Q2, Q8)", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c5v_constraint")
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    dT = np.linspace(0, 100, 200); gap = 1.5; free = 0.0248 * dT
    ax.plot(25 + dT, np.where(free > gap, (free - gap) / (5.806e-5 + 5.966e-5) / 1e3, 0), color=CC, lw=2)
    ax.axvline(85.5, color=GR, ls=":"); ax.text(86.5, 1.0, "gap closes\nat 85.5°C", fontsize=8.5)
    ax.plot([100], [3.06], "o", color=TC); ax.text(92, 3.3, "3.06 kN at 100°C", fontsize=8.5, color=TC)
    ax.set_xlabel("temperature (°C)"); ax.set_ylabel("compressive force (kN)"); ax.grid(alpha=0.3)
    ax.set_title("PYQ 2014 T2-Q3: thermo-gate force vs temperature", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c5v_q21")

if want("v2c6"):
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ri = np.linspace(0, 0.95, 200)
    ax.plot(ri, 1 - ri ** 4, label="J (torque capacity at same τ)", color=TC)
    ax.plot(ri, 1 - ri ** 2, label="area (weight)", color=CC)
    ax.plot(ri, (1 - ri ** 4) / (1 - ri ** 2), label="strength / weight", color="#27ae60")
    ax.axvline(0.6, color=GR, ls=":"); ax.text(0.61, 1.5, "rᵢ = 0.6R (Q3)", fontsize=8.5)
    ax.set_xlabel("rᵢ / R (outer radius fixed)"); ax.set_ylabel("hollow ÷ solid"); ax.grid(alpha=0.3); ax.legend(fontsize=8)
    ax.set_title("Hollow vs solid shafts of the same outer radius", fontsize=10.5, fontweight="bold", loc="left")
    save(fig, "c6v_hollow")
