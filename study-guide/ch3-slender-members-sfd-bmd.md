# Chapter 3 — Forces and Moments Transmitted by Slender Members
### Internal forces, shear-force and bending-moment diagrams, distributed loads, differential relations, singularity functions, 3-D/curved members

**Sources used:** Slides "Chapter 3" (Dr. Kushagra Tiwari), Crandall Ch. 3 (§3.1–3.8, Examples 3.1 and 3.11, Probs 3.7, 3.8, 3.17), PYQs 2014-15 (Test-1 Q4; Compre A Q6, Q7, Q14, Q17, Q18) and 2019-20 (Compre A Q1, Q3a).

---

## ⚠️ Read first: the sign convention for shear force in this course

The slides follow **Crandall's** convention, which is **opposite to Gere/Hibbeler/Beer for shear force V**.

| Quantity | Crandall (slides, this guide) | Gere / Hibbeler |
|---|---|---|
| Axial $F$ | + tension | + tension |
| Bending $M_b$ | + sagging (concave up, "smile") | + sagging (same) |
| Shear $V$ | **+ when it acts on the positive (+x) face in the +y direction**, i.e. the right face of the left segment pushes **up** | + when the left face is pushed up (element rotates clockwise) |
| $dV/dx$ | $= -q$ | $= -w$ (w is downward load) |
| $dM/dx$ | $\mathbf{= -V}$ | $= +V$ |

So **$V_{Crandall} = -V_{Gere}$** everywhere, while $M$ is the same. In the slides' picture of "Positive Shear", the arrow is ↓ on the left face and ↑ on the right face.
In every solution below, V is given in Crandall's convention, the one the slides and examiners use. If you learned from Gere, flip the sign of V.

Quick rule: with Crandall's convention, **$V(x) = -\big(\text{sum of upward forces to the left of the cut}\big)$** and **$M(x) = $ sum of moments, about the cut, of the forces to the left, clockwise positive.**

---

## Concept 3.1 — Internal forces at a section: the method of sections

### A. Concept explanation

**1. Intuition.** Cut a loaded beam with an imaginary saw. Each half would fly off unless something at the cut held it in place. Whatever the other half was supplying (a push or pull along the axis, a sideways shear, a twist, a bend) we now draw at the cut. Equilibrium of either half tells us their values.

**2. Why it matters.** These internal forces are the input for everything that follows: $\sigma = F/A$ (Ch. 4), $\tau = Tr/J$ (Ch. 6), and later $\sigma = My/I$ for bending and $v''=M/EI$ for deflection. Every "combined loading" PYQ starts by finding $F$, $V$, $M_b$ and $T$ at a section.

**3. Formal treatment (slides, Crandall §3.2).**
*Slender member:* length at least about 5 times the lateral dimensions. Examples: beams, columns, shafts, rods, struts, links.
*x-section:* a cut whose normal is the x-axis (the member's axis). In 3-D the resultant on it has 6 components:

| Component | Name | Symbol | Effect |
|---|---|---|---|
| $F_{xx}$ | axial force | $F$ | stretches/compresses |
| $F_{xy}, F_{xz}$ | shear forces | $V_y, V_z$ | slides one part past the other |
| $M_{xx}$ | twisting moment | $M_t$, $T$ | twists about the axis |
| $M_{xy}, M_{xz}$ | bending moments | $M_{by}, M_{bz}$ | bends |

(First subscript = face normal, second = direction of the component.)

*Positive face:* outward normal along +x. *Negative face:* outward normal along −x.
*Sign rule (slides):* a component is **positive** if it acts on a positive face in a positive direction **or** on a negative face in a negative direction. Otherwise it is negative. By this rule, tension is positive and compression negative.

For loading in the x–y plane, only three components survive: $F = F_{xx}$, $V = F_{xy}$ and $M_b = M_{xz}$.

**Procedure (slides):**
1. Idealize and isolate the structure; draw all external forces.
2. Find the reactions from $\sum F = 0$ and $\sum M = 0$.
3. Cut at the point of interest, keep **one** segment, draw $F, V, M_b$ in their **positive** senses, and apply equilibrium.

**4. Derivation — Example 3.1 (simply supported beam, load W at a from A, b from B).** Reactions: $R_A = Wb/L$ and $R_B = Wa/L$.
Cut at $x<a$ and keep the left part. On its right (positive) face draw $V$ ↑, $M_b$ counter-clockwise and $F$ →.
- $\sum F_x$: $F=0$
- $\sum F_y$: $R_A + V = 0 \Rightarrow V = -\dfrac{Wb}{L}$
- $\sum M_{cut}$: $M_b - R_Ax = 0 \Rightarrow M_b = \dfrac{Wb}{L}x$

For $x>a$: $V = \dfrac{Wa}{L}$ and $M_b = \dfrac{Wa}{L}(L-x)$. The peak is $M_{max} = \dfrac{Wab}{L}$ under the load.

**5. Picture.** For a **positive** $M_b$ on the right face of the left segment the arrow is counter-clockwise; on the left face of the right segment it is clockwise. The pair "opens upward" like a smile, which is sagging.

**6. Special cases.** $a = b = L/2$ gives $M_{max} = WL/4$. Load at a support gives zero internal moment.

**7. Common traps.**
- Drawing $V$ and $M$ in *assumed physical* directions instead of the **positive** convention. Always draw them positive and let algebra give the sign.
- Mixing up the Crandall and Gere sign for V (see the box above).
- Using a distributed load's resultant for the *whole* beam when the cut is inside the load. Only the part of the load on your segment counts.

**8. Summary box.** Cut → draw $F, V, M$ positive → equilibrium → read the signs.
$V = -(\Sigma\,\text{up-forces to the left})$ and $M = \Sigma\,(\text{moments to the left about the cut, clockwise} +)$.

### B. Solved questions

#### Q1 (Slides Ch3, Ex 3.1 numerical version) — Two 10 kN loads on a 3 m span *(easy)*
**Given:** simply supported AB, 3 m. $P=10$ kN at C (1 m) and at D (2 m). **Find:** SFD and BMD.

$R_A = R_B = 10$ kN.
| Region | $V$ (Crandall) | $M_b$ |
|---|---|---|
| A–C | $-10$ kN | $10x$ (0 → 10 kN·m) |
| C–D | $0$ | $10$ kN·m (constant) |
| D–B | $+10$ kN | $10(3-x)$ (10 → 0) |

**Shape:** the SFD has steps at the loads. The BMD is a trapezoid, with a flat top between C and D where there is **pure bending** ($V=0$).
**Takeaway:** the four-point-bending test uses exactly this setup. Constant M with V = 0 is used to measure bending stiffness.

---

#### Q2 (Slides Ch3, Gere) — Beam with a bracket *(medium)*
**Given:** simply supported ABC, length $L$. A bracket BDE hangs from B (at $L/4$) and carries $P$ at E, which lies at $x = L/2$. **Find:** SFD and BMD of ABC.

**Transfer the load to the beam at B:** a force $P$ ↓ plus a couple $P\cdot\frac{L}{4}$ clockwise.
Reactions: $\sum M_C$ gives $R_A = P/2$ (the line of action of P is at mid-span), so $R_C = P/2$.
| Point | $V$ (Crandall) | $M_b$ |
|---|---|---|
| A to B⁻ | $-P/2$ | $0 \to PL/8$ |
| B⁺ to C | $+P/2$ | jumps by $+PL/4$ (clockwise couple) to $3PL/8$, then falls linearly to 0 |

$$\boxed{M_{max} = \tfrac{3PL}{8}\ \text{just right of B}}$$
**Takeaway:** an applied **clockwise couple** makes the BMD **jump up** by the couple's magnitude (moving left to right). A counter-clockwise couple makes it jump down.

---

#### Q3 (Slides Ch3, Gere) — Beam with pulley and cable: N, V, M at C *(medium–hard)*
**Given:** simply supported ABCD with A (pin) at 0, B at 2 m, C at 4 m and D (roller) at 6 m. A vertical arm at C goes up to E (1.5 m). The cable from the weight $W = 27$ kN passes over a small pulley at B and is tied to E. **Find:** $N$, $V$, $M$ at section C, just left of the arm.

**Reactions (whole system):** the only external load is W, which hangs below B. $R_D(6) = 27(2) \Rightarrow R_D = 9$ kN and $R_A = 18$ kN.
**Force of the pulley on the beam at B:** the cable leaves B toward E with direction $(2, 1.5)/2.5 = (0.8, 0.6)$ and $T = 27$ kN. The two cable segments pull on the pulley with $(0,-27) + 27(0.8, 0.6) = (21.6, -10.8)$ kN.
**Cut just left of C, keep the left part:**
- $\sum F_x$: $21.6 + N = 0 \Rightarrow N = -21.6$ kN (compression)
- $\sum F_y$: $18 - 10.8 + V = 0 \Rightarrow V = -7.2$ kN (Crandall). Gere would write +7.2 kN.
- $\sum M_C$: $M = 18(4) - 10.8(2) = 50.4$ kN·m

$$\boxed{N = -21.6\ \text{kN},\quad V = -7.2\ \text{kN (Crandall)},\quad M = 50.4\ \text{kN·m}}$$

---

#### Q4 (PYQ 2014-15 Compre A Q14) — Couple on a hinged beam *(easy)*
**Given:** beam AB hinged at both ends, span $2L$ with $L = 2$ m. Midway, a couple is formed by two forces $P=20$ kN, $C = 1$ m apart, so the couple is 20 kN·m. **Find:** shear force at section x.

A pure couple: $R_A = -R_B = \dfrac{20}{2L} = \dfrac{20}{4} = 5$ kN, forming an equal and opposite couple.
$$\boxed{|V| = 5\ \text{kN, constant along the whole beam}}$$
**Takeaway:** a couple causes no jump in the SFD. It only jumps the BMD.

---

## Concept 3.2 — Distributed loads, resultants and their limitations

### A. Concept explanation

**1. Intuition.** Sand spread on a plank. Each little strip $\Delta x$ carries $q\,\Delta x$. For finding the **support reactions** you can pretend all the sand is piled at its centre of gravity. For the **bending inside the plank** you cannot, because a pile in the middle bends the plank differently from sand spread evenly.

**2. Why it matters.** Self-weight, snow, fluid pressure, the 2000 N/m triangular load and the trapezoidal load questions.

**3. Formal treatment.**
$$q = \lim_{\Delta x\to0}\frac{\Delta F}{\Delta x}\quad\text{(force per unit length; positive in } +y\text{, i.e. upward)}$$
Common forms: uniform ($q$ = const) and linear ($q = Ax+B$).
*Resultant and its location:*
$$R = \int_0^L q\,dx,\qquad \bar x = \frac{\int_0^L x\,q\,dx}{R}$$
Resultant = area of the load diagram, acting through its centroid.

| Load shape | $R$ | $\bar x$ from the zero/left end |
|---|---|---|
| Uniform $w_0$ over $L$ | $w_0L$ | $L/2$ |
| Triangle 0 → $w_0$ | $w_0L/2$ | $2L/3$ (from the zero end) |
| Trapezoid $w_1\to w_2$ | $(w_1+w_2)L/2$ | $\dfrac{L(w_1+2w_2)}{3(w_1+w_2)}$ from the $w_1$ end |

**Limitations (slides):**
1. Allowed when you only want external reactions.
2. **Not** allowed for internal forces and moments.

*Slide illustration:* beam (a) has loads $P$ at the two overhang tips, each a distance $a$ outside supports $2b$ apart. Beam (b) has $2P$ at the centre. The resultant is the same and so are the reactions ($R_A = R_B = P$). But (a) has **hogging** $M = -Pa$ between the supports, while (b) has **sagging** $M_{max} = +Pb$. The beams even bend in opposite directions.

**4. Derivation — cantilever with triangular load (slides).** Load $w = w_0x/L$ downward, free end A at $x=0$, wall at B. Cut at $x$ and keep the left part. The load on it is $\int_0^x w_0\xi/L\,d\xi = w_0x^2/2L$, acting at $2x/3$ from A, i.e. $x/3$ from the cut.
- $\sum F_y$: $-\dfrac{w_0x^2}{2L} + V = 0 \Rightarrow V = \dfrac{w_0x^2}{2L}$
- $\sum M$: $M_b + \dfrac{w_0x^2}{2L}\cdot\dfrac{x}{3} = 0 \Rightarrow M_b = -\dfrac{w_0x^3}{6L}$

At the wall: $V = w_0L/2$ and $M_b = -w_0L^2/6$ (hogging).

**5. Shape.** UDL gives a linear V and a parabolic M. Triangular load gives a parabolic V and a cubic M.

**6. Special cases.** Simply supported, full UDL: $V = -\frac{w_0L}{2} + w_0x$ and $M = \frac{w_0x(L-x)}{2}$, with $M_{max} = \frac{w_0L^2}{8}$ at mid-span where $V=0$.

**7. Common traps.** Using the resultant of the *whole* distributed load when cutting inside it. Putting a triangle's resultant at $L/2$.

**8. Summary.** For reactions, replace by the resultant. For V and M, only the portion on your free body counts, placed at *its own* centroid.

### B. Solved questions

#### Q5 (PYQ 2014-15 Compre A Q6, Q7) — Simply supported, UDL *(easy)*
Shear at mid-span: $\boxed{V(L/2) = 0}$. Moment at mid-span: $\boxed{M = wL^2/8}$.

---

#### Q6 (Slides Ch3, Gere) — Trapezoidal load: V and M at mid-span *(medium)*
**Given:** simply supported, $L=3$ m. Load decreases linearly from 50 kN/m at A to 30 kN/m at B. **Find:** $V$ and $M$ at $x = 1.5$ m.

Total load $= \frac{50+30}{2}(3) = 120$ kN at $\bar x = \frac{3(50+60)}{3(80)} = 1.375$ m. So $R_B = 120(1.375)/3 = 55$ kN and $R_A = 65$ kN.
Load on $0 \le x \le 1.5$: intensity at 1.5 m is 40 kN/m. Resultant $= \frac{50+40}{2}(1.5) = 67.5$ kN at $\bar x = \frac{1.5(50+80)}{3(90)} = 0.722$ m from A, i.e. 0.778 m from the cut.
- $V = -(65 - 67.5) = +2.5$ kN (Crandall). Gere gives −2.5 kN.
- $M = 65(1.5) - 67.5(0.778) = 97.5-52.5 = 45.0$ kN·m

$$\boxed{V = 2.5\ \text{kN (Crandall)},\qquad M = 45\ \text{kN·m}}$$
(The true maximum, 45.08 kN·m, is at $x = 1.44$ m where $V=0$, just left of mid-span. That makes sense because the load is heavier on the left.)

---

#### Q7 (Slides Ch3) — Symmetric triangular load, total W *(easy)*
Peak at mid-span, simply supported. $R_A=R_B=W/2$. For $x\le L/2$: $q = 4Wx/L^2$.
$M(x) = \frac{W}{2}x - \frac{2W}{3L^2}x^3$. At $x = L/2$:
$$\boxed{M_{max} = \frac{WL}{4}-\frac{WL}{12} = \frac{WL}{6}}$$
**Check:** a concentrated W at the centre gives $WL/4$. Spreading the load must give less ✓.

---

#### Q8 (Slides Ch3) — Partial UDL $q=-w_0$ over length a from A, simply supported span L *(medium)*
$R_A = \dfrac{w_0a(2L-a)}{2L}$ and $R_B = \dfrac{w_0a^2}{2L}$.
$V = 0$ at $x_0 = R_A/w_0 = \dfrac{a(2L-a)}{2L}$ (always ≤ a ✓).
$$\boxed{M_{max} = \frac{R_A^2}{2w_0} = \frac{w_0a^2(2L-a)^2}{8L^2}}$$
**Check:** $a = L$ gives $w_0L^2/8$ ✓.

---

#### Q9 (Slides Ch3) — Triangular load 0 → 2000 N/m over 9 m, then 2000 → 0 over 3 m *(medium)*
**Given:** simply supported, span 12 m. **Find:** reactions and maximum M.

$R_{total} = \tfrac12(2000)(12) = 12{,}000$ N acting at the triangle's centroid $\bar x = (0+9+12)/3 = 7$ m. So $R_B = 12000(7)/12 = 7000$ N and $R_A = 5000$ N.
For $x \le 9$: the load to the left is $\int_0^x \frac{2000}{9}\xi\,d\xi = \frac{1000x^2}{9}$.
$V = 0$: $5000 = 1000x^2/9 \Rightarrow x = \sqrt{45} = 6.708$ m.
$$M = 5000x - \frac{1000x^2}{9}\cdot\frac{x}{3}\Big|_{6.708} \Rightarrow \boxed{M_{max} = 22.36\ \text{kN·m at}\ x = 6.71\ \text{m}}$$

---

## Concept 3.3 — Differential relations between q, V and M

### A. Concept explanation

**1. Intuition.** The load intensity is the "slope-maker" for the shear diagram, and the shear is the "slope-maker" for the moment diagram. So you can sketch SFDs and BMDs almost without algebra: the load tells you the V slope, and the V tells you the M slope.

**2. Why it matters.** Fast and reliable diagrams, finding $M_{max}$ (where $V=0$), and the starting point of the beam-deflection chapter ($EIv'''' = q$).

**3. Formal treatment / 4. Derivation (slides, Crandall §3.5).** Take an element $\Delta x$ with $q(x)$ upward. On the left face are $V$ and $M_b$ (negative face, so drawn ↓ and clockwise). On the right face are $V+\Delta V$ and $M_b+\Delta M_b$ (positive face, ↑ and counter-clockwise).
- $\sum F_y$: $(V+\Delta V) - V + q\Delta x = 0 \Rightarrow \dfrac{\Delta V}{\Delta x} = -q$
- $\sum M_O$ (about the centre of the element): $(M_b+\Delta M_b) - M_b + (V+\Delta V)\dfrac{\Delta x}{2} + V\dfrac{\Delta x}{2} = 0$

Let $\Delta x\to0$:
$$\boxed{\frac{dV}{dx} + q = 0,\qquad \frac{dM_b}{dx} + V = 0}\qquad\Rightarrow\qquad \frac{d^2M_b}{dx^2} = q$$
Integral forms: $V_2 - V_1 = -\int_1^2 q\,dx$ and $M_2 - M_1 = -\int_1^2 V\,dx$.

**5. Reading diagrams (Crandall signs; q upward positive, so a downward load means $q<0$):**
| Load on segment | SFD | BMD |
|---|---|---|
| None | constant | linear |
| UDL downward | linear, **rising** (slope $=-q>0$) | parabola, concave down (∩) |
| Linear load | parabola | cubic |
| Concentrated downward $P$ | jumps **up** by $P$ | kink (slope change) |
| Clockwise couple $C$ | no change | jumps **up** by $C$ |

**$M$ is extreme where $V = 0$** (or where V jumps through zero at a concentrated load).

**6. Special cases.** At a free end or a pinned end with no applied couple, $M=0$. At a free end with no load, $V=0$.

**7. Common traps.**
- With Gere's formulas ($dM/dx = +V$) and Crandall's signs for V you get the BMD upside down. Pick one convention and stay with it.
- Missing a maximum inside a distributed load: always solve $V=0$ there.
- A **point of contraflexure** is where M **changes sign** (passes through zero), not where V = 0.

**8. Summary.** $V' = -q$, $M' = -V$ (Crandall). Area of the load diagram gives the change in V. Area of the SFD gives minus the change in M.

### B. Solved questions

#### Q10 (Slides Ch3) — 4 kN, 2 kN/m, 8 kN on a 10 m span *(medium)*
**Given:** simply supported, A at 0, B at 10. 4 kN at C (2 m). UDL 2 kN/m from D (3 m) to E (7 m). 8 kN at F (9 m).
**Reactions:** $\sum M_A$: $R_B(10) = 4(2)+8(5)+8(9) = 120 \Rightarrow R_B = 12$ kN and $R_A=8$ kN.

| Point | A | C⁻ | C⁺ | D | $x=5$ | E | F⁻ | F⁺ | B |
|---|---|---|---|---|---|---|---|---|---|
| $V$ (kN, Crandall) | −8 | −8 | −4 | −4 | 0 | +4 | +4 | +12 | +12 |
| $M$ (kN·m) | 0 | 16 | 16 | 20 | **24** | 20 | 12 | 12 | 0 |

$M$ in DE: $M = 8x-4(x-2)-(x-3)^2$, which peaks at $x=5$:
$$\boxed{M_{max} = 24\ \text{kN·m at mid-span}}$$
No point of contraflexure: M ≥ 0 everywhere.

---

#### Q11 (Slides Ch3) — 3 kN + UDL + 2 kN: position and value of maximum BM *(medium)*
**Given:** simply supported, 8 m. 3 kN at C (2 m). 2 kN/m from C to D (2 to 5 m). 2 kN at D (5 m).
**Reactions:** $\sum M_A$: $R_B(8) = 3(2)+6(3.5)+2(5) = 37 \Rightarrow R_B = 4.625$ kN and $R_A = 6.375$ kN.
$V = 0$ in CD: $6.375 - 3 - 2(x-2) = 0 \Rightarrow x = 3.6875$ m (point E).

| Point | A | C⁺ | E | D⁻ | D⁺ | B |
|---|---|---|---|---|---|---|
| $V$ (Crandall) | −6.375 | −3.375 | 0 | +2.625 | +4.625 | +4.625 |
| $M$ (kN·m) | 0 | 12.75 | **15.60** | 13.875 | 13.875 | 0 |

$$\boxed{M_{max} = 15.6\ \text{kN·m at}\ x = 3.69\ \text{m from A}}$$
✓ Matches the slide's hand solution (6.38, 3.375, 2.625, 12.75, 15.59, 13.875).

---

#### Q12 (Slides Ch3) — 5 kN/m segments plus an offset couple *(medium–hard; fill-the-table type)*
**Given:** simply supported AB, 8 m (A pin, B roller). 5 kN/m on AC (0–2 m) and on EB (6–8 m). At D (4 m) a vertical arm carries 10 kN → at 1 m above the beam and 10 kN ← at 1 m below. **Find:** the V/M table at A, C, D⁻, D⁺, E, B.

**Arm loads → a couple:** the two forces cancel. Their moment is $10(1)+10(1) = 20$ kN·m **clockwise**, applied at D.
**Reactions:** $\sum M_A$: $R_B(8) - 10(1) - 10(7) - 20 = 0 \Rightarrow R_B = 12.5$ kN and $R_A = 7.5$ kN.
**M:** AC: $7.5x-2.5x^2$. CD: $10-2.5x$. At D the moment jumps **up** by 20 (clockwise couple). DE: $30-2.5x$. EB: $30-2.5x-2.5(x-6)^2$.

| | A | C | D⁻ | D⁺ | E | B |
|---|---|---|---|---|---|---|
| $V$ (kN, Crandall) | −7.5 | +2.5 | +2.5 | +2.5 | +2.5 | +12.5 |
| $M_b$ (kN·m) | 0 | 5 | 0 | **20** | 15 | 0 |

There is a local max of 5.625 kN·m at $x = 1.5$ m in AC.
$$\boxed{M_{max} = 20\ \text{kN·m at D}^+}$$
**Takeaway:** horizontal forces on an offset arm add **no** vertical shear, but they do add a couple. The slide's "if any discontinuity point is left in the table please add it" is a hint about the jump at D.

---

#### Q13 (Crandall Prob 3.7) — Uniform load over a beam with an overhang *(medium)*
**Given:** load $w_0$ over the whole length $L+a$. Supports at $x=0$ and $x=L$, overhang $a$.
$R_A = \dfrac{w_0(L^2-a^2)}{2L}$ and $R_B = \dfrac{w_0(L+a)^2}{2L}$.

| Point | $V$ (Crandall) | $M$ |
|---|---|---|
| A | $-R_A$ | 0 |
| inside span, $V=0$ at $x_0 = (L^2-a^2)/2L$ | 0 | $+\dfrac{w_0(L^2-a^2)^2}{8L^2}$ |
| B⁻ | $+\dfrac{w_0(L^2+a^2)}{2L}$ | $-\dfrac{w_0a^2}{2}$ |
| B⁺ | $-w_0a$ | $-\dfrac{w_0a^2}{2}$ |
| tip | 0 | 0 |

**Variation (Crandall 3.18-type):** choose $a$ so that $|M^+_{max}| = |M_B|$. This gives $a\approx0.414L$ for this layout, the best support position for a plank.

---

#### Q14 (Crandall Prob 3.8) — Overhanging beam, 1.5 kN and 1.5 kN/m *(medium)*
**Given:** pin A at 0, roller B at 3.75 m. 1.5 kN at 1.5 m. 1.5 kN/m over the 1.5 m overhang (3.75–5.25 m).
Reactions: $R_B(3.75) = 1.5(1.5)+2.25(4.5) \Rightarrow R_B = 3.30$ kN and $R_A = 0.45$ kN.

| | A | load⁻ | load⁺ | B⁻ | B⁺ | tip |
|---|---|---|---|---|---|---|
| $V$ (kN, Crandall) | −0.45 | −0.45 | +1.05 | +1.05 | −2.25 | 0 |
| $M$ (kN·m) | 0 | 0.675 | 0.675 | −1.69 | −1.69 | 0 |

Contraflexure: $0.45x - 1.5(x-1.5) = 0 \Rightarrow \boxed{x = 2.14\ \text{m from A}}$. $|M|_{max} = 1.69$ kN·m (hogging) at B.

---

#### Q15 (Crandall Prob 3.17) — The carpenter and the sawhorses *(medium, a classic)*
**Given:** 6 m plank, uniform $w_0$. One sawhorse at end A. Where should the second go so that $M = 0$ at 1.8 m from the other end ($x = 4.2$ m)?
Let the second sawhorse be at $s$, with $4.2 < s < 6$. $R_s = \dfrac{w_0(6)(3)}{s} = \dfrac{18w_0}{s}$.
$M(4.2)$ from the right: $R_s(s-4.2) - w_0(1.8)(0.9) = 0 \Rightarrow 18 - \dfrac{75.6}{s} = 1.62$
$$\boxed{s = 4.62\ \text{m from A}\ (\text{i.e. 1.38 m from the far end})}$$
**Check:** if $s<4.2$, the cut would be in the overhang where $M = -w_0(1.8)^2/2 \neq 0$, so no solution there ✓.

---

## Concept 3.4 — Singularity (Macaulay) functions

### A. Concept explanation

**1. Intuition.** Instead of writing a new $M(x)$ for every segment, use "switches" $\langle x-a\rangle$ that are off ($0$) before $x=a$ and on afterwards. One formula then covers the whole beam. This is very useful in the deflection chapter, where you integrate twice.

**2. Why it matters.** PYQ 2014-15 Test-1 Q4 (25 marks!) demanded this method *only*, and 2023-24 Part B Q3 uses it for deflection.

**3. Formal treatment (slides).**
$$\langle x-a\rangle^n = \begin{cases}(x-a)^n & x\ge a\\ 0 & x<a\end{cases}\quad(n\ge0),\qquad \langle x-a\rangle^0 = \text{unit step}$$
$\langle x-a\rangle_{-1}$ is a concentrated (Dirac) load and $\langle x-a\rangle_{-2}$ a concentrated couple (doublet).
*Integration rules:* for $n\ge0$, $\int_{-\infty}^x\langle x-a\rangle^n dx = \dfrac{\langle x-a\rangle^{n+1}}{n+1}$. For $n<0$, $\int\langle x-a\rangle_n dx = \langle x-a\rangle_{n+1}$. So $\int\langle\rangle_{-2} = \langle\rangle_{-1}$ and $\int\langle\rangle_{-1} = \langle\rangle^0$.
*Loading representation (Rule 2):*
- UDL $w_0$ starting at $a$: $w_0\langle x-a\rangle^0$. To stop it at $b$, add $-w_0\langle x-b\rangle^0$.
- Ramp: $\dfrac{w_0}{b-a}\langle x-a\rangle^1$.
- Point load $P$ at $a$: $P\langle x-a\rangle_{-1}$.
- Couple $M_0$ at $a$: $M_0\langle x-a\rangle_{-2}$.

*Rule 4:* write $q(x)$ including **all** forces (reactions too) from left to right. Integrate once to get $V$ and again to get $M$. **No integration constants** are needed, because the reactions are already inside the $\langle\ \rangle_{-1}$ terms.

**4. Derivation — why no constants.** $V$ and $M$ are zero just left of the beam ($x<0$), and every term $\langle x-a\rangle_n$ is zero there too. So the constants must be 0.

**5. Working form you can use directly** (sagging $M$ +, clockwise couples +, upward forces +):
$$M(x) = \sum_{\text{up forces}} P_i\langle x-a_i\rangle^1 - \sum_{\text{down}} P_j\langle x-a_j\rangle^1 + \sum_{\text{cw couples}} C_k\langle x-a_k\rangle^0 - \sum_{\text{UDL down}}\frac{w}{2}\langle x-a\rangle^2 + \dots$$
and $V_{Crandall} = -dM/dx$.

**6. Special cases.** A UDL that runs to the end of the beam needs no "stop" term.

**7. Traps.**
- Evaluating $\langle x-a\rangle$ as $(x-a)$ when $x<a$. It must be 0.
- Forgetting to end a UDL.
- Using $\langle x-a\rangle^1$ for a couple: it must be $\langle x-a\rangle^0$ in $M$.

**8. Summary.** One equation, switches on at each discontinuity, no constants (for V and M).

### B. Solved questions

#### Q16 (PYQ 2014-15 Test-1 Q4) — Singularity functions: SFD, BMD and contraflexure *(hard, 25 marks)*
**Given:** A (pin) at 0, C at 10 m (90 kN ↓), D at 20 m (10 kN·m couple, **clockwise** as drawn), B (roller) at 30 m, E (free end) at 40 m. UDL 10 kN/m over BE (30–40 m).
**Reactions:** $\sum M_A$: $R_B(30) - 90(10) - 10 - 100(35) = 0 \Rightarrow R_B = 147$ kN and $R_A = 190-147 = 43$ kN.

**Singularity equation for M:**
$$M(x) = 43\langle x\rangle^1 - 90\langle x-10\rangle^1 + 10\langle x-20\rangle^0 + 147\langle x-30\rangle^1 - 5\langle x-30\rangle^2\ \ \text{(kN·m)}$$
$$V(x) = -\frac{dM}{dx} = -43\langle x\rangle^0 + 90\langle x-10\rangle^0 - 147\langle x-30\rangle^0 + 10\langle x-30\rangle^1\ \ \text{(Crandall)}$$
(The couple's term differentiates to $\langle\rangle_{-1}$, which is zero except at $x=20$ exactly.)

| | A | C⁻ | C⁺ | D⁻ | D⁺ | B⁻ | B⁺ | E |
|---|---|---|---|---|---|---|---|---|
| $V$ (kN, Crandall) | −43 | −43 | +47 | +47 | +47 | +47 | −100 | 0 |
| $M$ (kN·m) | 0 | **430** | 430 | −40 | −30 | **−500** | −500 | 0 |

**Contraflexure:** in CD, $M = 43x - 90(x-10) = 900-47x = 0$, so
$$\boxed{x = 19.15\ \text{m from A}}$$
After D, $M$ stays negative (−30 to −500) and reaches 0 only at the free end E, so there is only one point of contraflexure.
**Max moments:** $+430$ kN·m at C (sagging) and $-500$ kN·m at B (hogging).
**Check:** $M(40) = 43(40)-90(30)+10+147(10)-5(100) = 0$ ✓.

---

## Concept 3.5 — Cantilevers, frames, curved members and 3-D problems

### A. Concept explanation

**1. Intuition.** The cut method works the same for bent or curved members. Just remember that "axial" and "shear" are now measured along and across the **local** direction of the member at the cut. In 3-D, use vectors: $\mathbf F$ and $\mathbf M = \mathbf r\times\mathbf F$.

**2. Why it matters.** Brackets, crank shafts, pipes, curved hooks. These appear in every compre as the first part of a combined-stress question (see Ch. 4 Concept 4.6).

**3. Formal treatment (Crandall §3.8, Example 3.11).** For a cut segment with free-end loads $\mathbf P$ at position $\mathbf r_{CA}$ relative to the cut C:
$$\mathbf V_C + \mathbf P = 0,\qquad \mathbf M_C + \mathbf r_{CA}\times\mathbf P = 0$$
Resolve into components along the local axis (twist and axial force) and perpendicular to it (bending and shear).
*Crandall Ex. 3.11:* for a quarter-circle pipe of radius $a$ with a transverse (out-of-plane) load $P$, $V = -P$, $M_b = Pa\sin\theta$ and $M_t = -Pa(1-\cos\theta)$. An out-of-plane load on a curved member produces **twist**.
*Crandall's observation:* for straight members under point loads, the maximum bending moment always occurs at a load point, never between loads.

**4. Derivation — in-plane moment in a bent bracket.** For a free end D loaded by $(F_x, F_y)$, the bending moment at any point $(x,y)$ of the frame is
$$M(x,y) = (x_D - x)F_y - (y_D-y)F_x$$
This one formula covers every straight segment, so there is no need to redo FBDs for each leg.

**7. Traps.** For curved members, the "axial" direction rotates with θ. Resolve the load into tangential and radial components *at the cut*.

### B. Solved questions

#### Q17 (PYQ 2014-15 Compre A Q17–18) — Cantilever with three loads *(easy–medium)*
**Given:** fixed at A. 30 kN ↓ at B (1 m), 80 kN **↑** at C (3 m), 20 kN ↓ at D (5 m). **Find:** $R_A$, $M_A$ and the point of contraflexure.
- $\sum F_y$: $R_A - 30 + 80 - 20 = 0 \Rightarrow R_A = -30$ kN, so $\boxed{30\ \text{kN}\downarrow}$
- $\sum M_A$: $M_A - 30(1) + 80(3) - 20(5) = 0 \Rightarrow M_A = -110$ kN·m, so $\boxed{110\ \text{kN·m clockwise on the beam}}$

**M along the beam (from the right):** CD: $M = -20(5-x)$ (hogging). BC: $M = 140-60x$. AB: $M = 110-30x$.
$M = 0$ in BC at $\boxed{x = 2.33\ \text{m from A}}$.

---

#### Q18 (PYQ 2019-20 Compre A Q1) — Bracket ABCD: BMD and minimum diameter *(medium, 8 marks)*
**Given:** fixed at A. AB horizontal, $6b$. BC vertical (down), $2b$. CD horizontal back toward A, $2b$. At free end D: $P=40$ N ← and $P = 40$ N ↑. $b = 37$ mm. Solid circular section, $\sigma_{allow} = 30$ MPa. **Find:** (a) the BMD, (b) $d_{min}$.

**Coordinates:** A(0,0), B(6b, 0), C(6b, −2b), D(4b, −2b). Loads at D: $(F_x, F_y) = (-P, +P)$.
Using $M = (x_D-x)F_y - (y_D-y)F_x$:
$$M(x,y) = P(4b-x) - P(2b+y) = P(2b - x - y)$$
| Segment | Expression | End values |
|---|---|---|
| CD ($y=-2b$, $x$: $4b\to6b$) | $P(4b-x)$ | D: 0 → C: $-2Pb$ (linear) |
| BC ($x=6b$, $y$: $-2b\to0$) | $P(-4b-y)$ | C: $-2Pb$ → B: $-4Pb$ (linear) |
| AB ($y=0$, $x$: $6b\to0$) | $P(2b-x)$ | B: $-4Pb$ → A: $+2Pb$; zero at $x = 2b$ |

The BMD is linear on every leg. The largest magnitude is $|M|_{max} = 4Pb$ at B. The sign changes at $x=2b$ from A, a point of contraflexure.
$$M_{max} = 4(40)(37) = 5920\ \text{N·mm}$$
**(b)** Bending stress in a solid circle (from the flexure formula, Ch. 7): $\sigma = \dfrac{32M}{\pi d^3}$.
$$d^3 = \frac{32(5920)}{\pi(30)} = 2010\ \text{mm}^3 \Rightarrow \boxed{d_{min} = 12.6\ \text{mm}}$$
**Check:** the axial force in AB is only $P = 40$ N, giving $P/A \approx 0.3$ MPa, which is negligible next to 30 MPa ✓.
**Takeaway:** the hint "show the variation along AB, BC, CD separately" is asking for exactly this table.

---

#### Q19 (PYQ 2019-20 Compre A Q3(a)) — Curved cantilever, forces at section θ *(medium)*
**Given:** quarter circle of radius $R$, fixed at A (θ = 0, at ground level), free at B (θ = 90°, top), with $P$ ↓ at B. θ is measured at the centre O from the horizontal.
**Position on the arc** relative to O: $(-R\cos\theta, R\sin\theta)$. The tangent direction (toward B) is $\mathbf t = (\sin\theta, \cos\theta)$ and the outward radial direction is $\mathbf n = (-\cos\theta, \sin\theta)$.
**Segment from the cut to B:** load $(0,-P)$ at B $(0,R)$.
- Axial (along $\mathbf t$): $\mathbf P\cdot\mathbf t = -P\cos\theta$, so $\boxed{N = P\cos\theta\ \text{(compression)}}$
- Shear (along $\mathbf n$): $\boxed{V = P\sin\theta}$
- Moment: the horizontal lever arm from the cut to B is $R\cos\theta$, so $\boxed{M = PR\cos\theta}$ (tension on the outer fibre)

**Check:** at B (θ = 90°): $N = M = 0$ and $V = P$ (the load is purely transverse there) ✓. At A (θ = 0): $N = P$ and $M = PR$, the maximum ✓.
These expressions feed Castigliano's theorem in Ch. 2 Q12: $\delta_B = \pi PR^3/4EI + \pi PR/4AE$.

---

## Chapter 3 — Formula and convention sheet

| Item | Crandall / slides |
|---|---|
| Positive face | outward normal along +x |
| + component | (+face, +dir) or (−face, −dir) |
| $V$ | $= -\Sigma(\text{upward forces left of cut})$ — **opposite sign to Gere** |
| $M_b$ | sagging +; $= \Sigma$ moments of left-hand forces about the cut (clockwise +) |
| Differential relations | $dV/dx = -q$, $dM_b/dx = -V$, $d^2M_b/dx^2 = q$ (q up +) |
| Max/min M | where $V = 0$ or V changes sign |
| Contraflexure | where $M$ changes sign |
| Concentrated load P↓ | V jumps by $+P$ (Crandall), kink in M |
| Clockwise couple C | M jumps by $+C$, V unchanged |
| Resultant of distributed load | $R = \int q\,dx$ at the centroid — **reactions only** |
| Standard results | SS + central W: $WL/4$; SS + UDL: $wL^2/8$; SS + W at a: $Wab/L$; cantilever + tip P: $-PL$; cantilever + UDL: $-wL^2/2$ |
| Singularity | $\langle x-a\rangle^n$ (0 for $x<a$); point load $\langle\rangle_{-1}$, couple $\langle\rangle_{-2}$; no constants for V and M |
| Frame moment | $M = (x_D-x)F_y-(y_D-y)F_x$ |
| Curved cantilever (tip load) | $N=P\cos\theta$, $V=P\sin\theta$, $M=PR\cos\theta$ |

**Other Crandall Ch. 3 problems worth practising:** 3.1–3.6 (basic SFD/BMD), 3.9–3.11 (arcs and curved bars), 3.13–3.15 (sections in frames), 3.18 (scaffold plank optimisation).
