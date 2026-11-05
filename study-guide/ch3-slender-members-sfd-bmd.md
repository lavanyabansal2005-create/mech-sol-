# Chapter 3 — Forces and Moments Transmitted by Slender Members
### Internal forces, shear-force and bending-moment diagrams, distributed loads, q–V–M relations, singularity functions, frames, curved and 3-D members

**Sources used:** Slides "Chapter 3" (Dr. Kushagra Tiwari); Crandall Ch. 3 (§3.1–3.8; Examples 3.1, 3.11; Probs 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.12, 3.14, 3.17, 3.23, 3.25, 3.34); PYQs 2014-15 (Test-1 Q4; Compre A Q6, Q7, Q14, Q17, Q18) and 2019-20 (Compre A Q1, Q3(a)).

**Layout.** Part A (eight items) for each concept, then Part B: slides → Crandall → PYQs, easy → hard. Each solution follows *Problem · Given/Find · Approach · FBD · Steps · Answer · Check · Takeaway*.

---

## ⚠ Read first: the sign convention for shear force in this course

The slides follow **Crandall's** convention, which is **opposite to Gere/Hibbeler/Beer for the shear force V** (but the same for the bending moment).

| Quantity | Crandall (slides, this guide) | Gere / Hibbeler |
|---|---|---|
| Axial F | + tension | + tension |
| Bending $M_b$ | + sagging (concave up, "smile") | + sagging (same) |
| Shear V | **+ when it acts on the positive (+x) face in the +y direction**, i.e. the right face of the left segment is pushed **up** | + when the left face of the right segment is pushed up (element rotates clockwise) |
| $dV/dx$ | $= -q$ (q upward +) | $= -w$ (w downward +) |
| $dM/dx$ | $\mathbf{= -V}$ | $= +V$ |

So **$V_{Crandall} = -V_{Gere}$** everywhere, while M is identical. In the slide's picture of "positive shear" the arrow is ↓ on the left face and ↑ on the right face of an element.

**Working rules used throughout this chapter** (cut at x, keep the left part):
$$V(x) = -\Big(\sum\text{upward forces to the left of the cut}\Big),\qquad M(x) = \sum\text{moments of the left-hand forces about the cut, clockwise } +$$
An upward force to the left of a cut produces sagging (positive) moment. A clockwise applied couple to the left of the cut adds positive moment.

If you learned shear from Gere, flip the sign of every V in this chapter; nothing else changes.

---

## Concept 3.1 — Internal forces at a section: the method of sections

### A. Concept explanation

**1. Intuition.** Cut a loaded beam with an imaginary saw. Each half would fly off unless something at the cut held it in place. Whatever the other half was supplying (a push or pull along the axis, a sideways shear, a bend, a twist) we draw at the cut. Equilibrium of either half then tells us their values. A slender member transmits load from where it is applied to where it is supported *through* these internal forces.

**2. Why it matters.** These internal forces feed everything that follows: $\sigma = F/A$ (Ch. 2, 4), $\tau = Tr/J$ (Ch. 6), later $\sigma = My/I$ for bending and $v'' = M/EI$ for deflection. Every combined-loading PYQ begins by finding F, V, $M_b$ and $M_t$ at a section. The maximum stress occurs where these are largest, which is why we draw diagrams of them along the member.

**3. Formal treatment (slides, Crandall §3.2).**
- *Slender member* (slides): length at least about five times the lateral dimensions. Examples: beams, columns, shafts, rods, stringers, struts, links.
- *General method* (slides): isolate the system and draw all external forces; find the support reactions from $\sum\mathbf F = 0$, $\sum\mathbf M = 0$; cut at the point of interest, isolate one segment and repeat equilibrium on it.
- *x-section:* a cut whose normal is the member axis x. In 3-D the resultant on it has six components:

| Component | Name | Usual symbol | Effect |
|---|---|---|---|
| $F_{xx}$ | axial force | F | elongates/shortens the member |
| $F_{xy},\ F_{xz}$ | shear forces | $V_y,\ V_z$ | slides one part past the other |
| $M_{xx}$ | twisting moment | $M_t$ (or T) | twists about the axis |
| $M_{xy},\ M_{xz}$ | bending moments | $M_{by},\ M_{bz}$ | bends the member |

(First subscript = face normal, second = direction of the component.)
- *Positive face:* outward normal along +x. *Negative face:* outward normal along −x.
- *Sign rule (slides):* a component is **positive** if it acts on a positive face in a positive coordinate direction, **or** on a negative face in a negative coordinate direction. Otherwise it is negative. By this rule tension is positive and compression negative.
- *Planar loading* (x–y plane): only three components survive, $F = F_{xx}$, $V = F_{xy}$ and $M_b = M_{xz}$.

**4. Derivation — Crandall Example 3.1 (simply supported beam, load W at distance a from A and b from B).**
1. *Reactions* (whole beam; slide assumptions: horizontal reactions negligible, self-weight neglected): $\sum M_B$ gives $R_A = Wb/L$, and $\sum M_A$ gives $R_B = Wa/L$.
2. *Cut at $x < a$, keep the left part.* On its right (positive) face draw F →, V ↑ and $M_b$ counter-clockwise, all positive by the sign rule.
   - $\sum F_x$: $F = 0$.
   - $\sum F_y$: $R_A + V = 0$, so $V = -\dfrac{Wb}{L}$.
   - $\sum M_{cut}$: $M_b - R_Ax = 0$, so $M_b = \dfrac{Wb}{L}x$.
3. *Cut at $x > a$:* $V = -\dfrac{Wb}{L} + W = \dfrac{Wa}{L}$ and $M_b = \dfrac{Wb}{L}x - W(x - a) = \dfrac{Wa}{L}(L - x)$.
4. *Peak:* $M_{max} = \dfrac{Wab}{L}$ under the load. V jumps by W there.

**5. Picture.** A positive $M_b$ is counter-clockwise on the right face of the left segment and clockwise on the left face of the right segment. The pair "opens upward" like a smile (sagging, top fibres in compression). The **shear-force diagram (SFD)** plots V(x) and the **bending-moment diagram (BMD)** plots $M_b(x)$, each drawn directly below a sketch of the loaded beam with matching x.

**6. Special cases.**
- $a = b = L/2$: $M_{max} = WL/4$.
- A load right at a support produces no internal moment anywhere.
- Point of **contraflexure** (slides): where the BMD **changes sign**. M is zero there, and the curvature of the deflected shape reverses.

**7. Common traps.**
- Drawing V and M in *assumed physical* directions instead of the **positive** convention. Always draw them positive and let the algebra give the sign.
- Mixing the Crandall and Gere signs for V (see the box above).
- Using a distributed load's *total* resultant when the cut lies inside it (Concept 3.2).
- Forgetting the axial force F in frames and inclined members.

**8. Summary box.** Cut → draw F, V, M as positive → equilibrium → read the signs. $V = -(\sum\text{up-forces on the left})$; $M = \sum(\text{moments of the left-hand forces about the cut, clockwise} +)$.

### B. Solved questions

#### Q1 (Slides Ch3, Ex 3.1 = Crandall Example 3.1) — Forces and moments at a section C *(easy, symbolic)*
**Problem.** A simply supported beam of span L carries a load W at distance a from A (b from B). Find the forces and moment acting at a section C at distance x from A, and sketch the SFD and BMD.

**Given:** L, W, a, b = L − a. Slide assumptions: the horizontal reactions $F_A$, $F_B$ are neglected, and the beam's self-weight is neglected. **Find:** F, V, $M_b$ as functions of x.

**Approach.** Reactions from the whole beam, then the method of sections on each side of the load.

**FBD in words.** Beam with $R_A$ ↑ at A, $R_B$ ↑ at B and W ↓ at a. For the cut, the left segment shows $R_A$ and, on its right face, positive F (→), V (↑) and $M_b$ (counter-clockwise).

**Solution.**
1. $R_A = Wb/L$ and $R_B = Wa/L$.
2. $0 < x < a$: $F = 0$, $V = -Wb/L$, $M_b = Wbx/L$.
3. $a < x < L$: $F = 0$, $V = +Wa/L$, $M_b = Wa(L - x)/L$.

$$\boxed{V = \begin{cases}-Wb/L & x<a\\ +Wa/L & x>a\end{cases},\qquad M_b = \begin{cases}Wbx/L & x<a\\ Wa(L-x)/L & x>a\end{cases},\qquad M_{max} = \frac{Wab}{L}\ \text{at } x = a}$$

**Check.** The jump in V at the load is $Wa/L + Wb/L = W$ ✓. $dM/dx = Wb/L = -V$ on the left, consistent with Crandall's relation $dM/dx = -V$ (Concept 3.3) ✓.

**Exam takeaway.** This one result covers every point-load beam by superposition. **Variation:** W at mid-span gives $M_{max} = WL/4$.

---

#### Q2 (Slides Ch3) — Two 10 kN loads on a 3 m span (four-point bending) *(easy)*
**Problem.** A simply supported beam AB of span 3 m carries $P = 10$ kN at C (1 m) and at D (2 m). Draw the SFD and BMD.

**Approach.** Symmetric loading, so the reactions are equal. Then sections in each of the three regions.

**FBD in words.** Beam with $R_A$, $R_B$ ↑ and 10 kN ↓ at 1 m and 2 m.

**Solution.**
1. $R_A = R_B = 10$ kN.
2. Region by region (Crandall V):

| Region | V | $M_b$ |
|---|---|---|
| A–C ($0<x<1$) | −10 kN | $10x$ (0 → 10 kN·m) |
| C–D ($1<x<2$) | 0 | 10 kN·m (constant) |
| D–B ($2<x<3$) | +10 kN | $10(3 - x)$ (10 → 0) |

$$\boxed{M_{max} = 10\ \text{kN·m, constant between C and D, where } V = 0}$$

**Check.** The BMD is a trapezoid. The flat top between the loads is **pure bending** (V = 0) ✓.

**Exam takeaway.** The four-point-bending test uses exactly this layout. Constant M with zero shear lets you measure bending stiffness without shear effects. **Variation:** Crandall Prob 3.5, loads P at distance a from each end: $M = Pa$ between the loads.

---

#### Q3 (Slides Ch3, Gere) — Beam loaded through a bracket *(medium)*
**Problem.** A simply supported beam ABC of span L carries a bracket BDE welded at B (at L/4 from A). A vertical load P acts at the end E of the bracket, whose line of action is at mid-span (x = L/2). Draw the SFD and BMD of ABC. (For the plotted diagram, P = 10 kN and L = 4 m.)

**Approach.** Replace the bracket load by an equivalent force plus a couple at B (Ch. 1, Concept 1.2), then analyse the beam.

**FBD in words.** Beam with $R_A$, $R_C$ ↑, P ↓ at B and a clockwise couple $P\cdot\frac L4$ at B (P is L/4 to the right of B).

**Solution.**
1. *Equivalent load at B:* force P ↓ plus a clockwise couple $C = P(L/2 - L/4) = PL/4$.
2. *Reactions:* the line of action of P is at mid-span, so $R_A = R_C = P/2$. (Moments about C: $R_A L - P(3L/4) + PL/4 = 0$, so $R_A = P/2$ ✓.)
3. *A to B⁻:* $V = -P/2$; M rises linearly from 0 to $PL/8$.
4. *At B:* V jumps by +P (to +P/2), and M **jumps up** by $PL/4$ (clockwise couple) to $3PL/8$.
5. *B⁺ to C:* $V = +P/2$; M falls linearly from $3PL/8$ to 0.

$$\boxed{M_{max} = \tfrac{3PL}{8}\ \text{just to the right of B}\quad(15\ \text{kN·m for } P = 10\ \text{kN},\ L = 4\ \text{m})}$$

**Check.** From the right end: $M(B^+) = R_C(3L/4) = (P/2)(3L/4) = 3PL/8$ ✓.

**Exam takeaway.** An applied **clockwise couple** makes the BMD **jump up** by the couple's magnitude (moving left to right); a counter-clockwise couple makes it jump down. Couples never change V. **Variation:** a bracket pointing the other way (P left of B), which gives a downward jump.

---

#### Q4 (Slides Ch3, Gere) — Beam with a pulley and cable: N, V and M at section C *(medium–hard)*
**Problem.** A simply supported beam ABCD has a pin at A (x = 0), a small frictionless pulley at B (x = 2 m), section C at x = 4 m and a roller at D (x = 6 m). A vertical arm at C rises 1.5 m to E. A cable carrying a weight W = 27 kN passes over the pulley at B and is tied to E. Find the axial force N, shear V and moment M at a section just to the left of the arm (at C).

**Given:** W = 27 kN; geometry as above. **Find:** N, V, M at C⁻.

**Approach.** Reactions from the whole system (beam + pulley + cable + arm), then the force that the pulley exerts on the beam at B, then cut just left of C.

**FBD in words.**
- *Whole system:* the only external load is W, hanging below B. Reactions $A_x$, $A_y$ at A and $D_y$ at D.
- *Pulley at B:* two cable segments pull on it, the hanging segment (27 kN ↓) and the segment from B to E.

**Solution.**
1. *Reactions:* $\sum M_A$: $D_y(6) = 27(2)$, so $D_y = 9$ kN and $A_y = 18$ kN. $A_x = 0$ (the cable forces are internal to the system).
2. *Cable direction B → E:* from (2, 0) to (4, 1.5): $(2, 1.5)/2.5 = (0.8, 0.6)$. With T = 27 kN throughout (frictionless pulley), the pulley's force on the beam is $(0, -27) + 27(0.8, 0.6) = (21.6, -10.8)$ kN.
3. *Cut just left of C, keep the left part* (A to C⁻), which carries $A_y = 18$ ↑ at 0 and the pulley force $(21.6, -10.8)$ at x = 2.
   - $\sum F_x$: $21.6 + N = 0$, so N = −21.6 kN (compression).
   - $\sum F_y$: $18 - 10.8 + V = 0$, so V = −7.2 kN (Crandall); Gere would write +7.2 kN.
   - $\sum M_C$: $M = 18(4) - 10.8(2) = 72 - 21.6 = 50.4$ kN·m.

$$\boxed{N = -21.6\ \text{kN (C)},\qquad V = -7.2\ \text{kN (Crandall)},\qquad M = 50.4\ \text{kN·m (sagging)}}$$

**Check.** Use the right part instead (C⁻ to D, including the arm, with the cable pulling E toward B with $27(-0.8, -0.6) = (-21.6, -16.2)$ kN). Horizontal: $-21.6 - N = 0$ gives N = −21.6 ✓. Moments about C: $D_y$ gives $9(2) = 18$ and the cable force at E gives $1.5(21.6) = 32.4$, total 50.4 kN·m ✓.

**Exam takeaway.** Pulleys transfer **both** cable forces to their axle. Forgetting the horizontal component loses the axial force. The slide adds: "disregard the widths of the beam and vertical arm". **Variation:** the section just to the right of the arm, where the cable's moment about C ($27\times0.8\times1.5 = 32.4$ kN·m) causes a jump in M.

---

#### Q5 (Crandall Probs 3.1, 3.2, 3.4, 3.5) — Four quick SFD/BMD drills *(easy)*
**Problem.** Sketch V and M for: (3.1) a cantilever of length L, built in at the left, with a weight W hung at the free end; (3.2) the same with W hung at distance a from the wall; (3.4) a cantilever with P down at the tip and P up at distance a from the tip; (3.5) a simply supported beam with P at distance a from each end (span L, b between the loads).

**Approach.** For each, find the wall reaction or support reactions, then use the working rules ($V = -\sum$ up-forces on the left, M = sum of left-hand moments). x is measured from the left end.

**Solution.**
1. *3.1:* wall gives R = W ↑ and a counter-clockwise couple WL. $V = -W$ everywhere; $M = Wx - WL = -W(L - x)$, hogging, largest at the wall: $|M|_{max} = WL$.
2. *3.2:* $V = -W$ for $x < a$ and 0 beyond; $M = -W(a - x)$ for $x < a$ and 0 beyond. The part beyond the load carries nothing.
3. *3.4:* the two forces form a couple, so the wall force is 0 and the wall moment is Pa (counter-clockwise). For $x < L - a$: V = 0 and $M = -Pa$ (constant hogging). For $L - a < x < L$: $V = -P$ (the upward P is now to the left of the cut) and $M = -Pa + P[x - (L - a)] = -P(L - x)$, reaching 0 at the tip.
4. *3.5:* $R = P$ at each support. $V = -P$, 0, +P in the three regions; M rises to Pa, stays at Pa between the loads, then falls to 0.

$$\boxed{\text{3.1: } |M|_{max} = WL;\quad \text{3.2: } |M|_{max} = Wa;\quad \text{3.4: } M = -Pa \text{ (const.)};\quad \text{3.5: } M_{max} = Pa \text{ (const.)}}$$

**Check.** In 3.4 the section between the wall and the upward load feels only the couple, so V = 0 and M is constant ✓. In 3.1 the magnitude grows linearly toward the wall ✓.

**Exam takeaway.** Cantilevers: the maximum |M| is at the wall, and its value equals the moment of all loads about the wall. **Variation:** Crandall 3.3, an inclined cantilever (resolve the load into axial and transverse parts).

---

#### Q6 (Crandall Prob 3.14) — Frame with a vertical arm: forces at two sections *(medium)*
**Problem.** A horizontal beam AB (pin at A, roller at B) is 400 mm long. A vertical arm 150 mm tall is welded at 250 mm from A, and a 400 N horizontal force (→) acts at its top C. Find the internal forces and moments at section 1 (in the arm just above the beam) and section 2 (in the beam just to the left of the arm).

**Given:** AB = 400 mm; arm at x = 250 mm; force 400 N → at height 150 mm. **Find:** F, V, M at sections 1 and 2.

**Approach.** Reactions from the whole frame, then cut each section and keep the simpler side.

**FBD in words.** Frame with $A_x$, $A_y$ at A, $B_y$ at B and 400 N → at C.

**Solution.**
1. *Reactions:* $\sum M_A$: $B_y(400) - 400(150) = 0$, so $B_y = 150$ N ↑. $\sum F_y$: $A_y = -150$ N (↓). $\sum F_x$: $A_x = -400$ N (←).
2. *Section 1 (arm, just above the joint), keep the top part:* the only load is 400 N → at C, 150 mm above the cut. Axial force (along the vertical arm) = 0; shear = 400 N (horizontal); moment = 400(0.150) = 60 N·m.
3. *Section 2 (beam at x = 250⁻ mm), keep the left part:* forces $A_x = 400$ ←, $A_y = 150$ ↓.
   - Axial: the cut face must pull right to balance $A_x$: F = +400 N (tension).
   - Shear (Crandall): $V = -(\text{up-forces on the left}) = -(-150) = +150$ N.
   - Moment: $M = A_y(0.25) = -150(0.25) = -37.5$ N·m (hogging).
4. *Just to the right of the arm,* the couple from the arm (60 N·m clockwise on the beam) makes M jump to $-37.5 + 60 = +22.5$ N·m. Check from the right: $B_y(0.15) = 22.5$ ✓.

$$\boxed{\text{Sec. 1: } F = 0,\ V = 400\ \text{N},\ M = 60\ \text{N·m};\qquad \text{Sec. 2: } F = 400\ \text{N (T)},\ V = 150\ \text{N},\ M = -37.5\ \text{N·m}}$$

**Check.** The 400 N horizontal force is carried along the beam as tension between A and the arm, and not at all between the arm and the roller ✓.

**Exam takeaway.** An offset horizontal load creates an axial force on one side and a moment jump at the joint. This is the same structure as Q18 (5 kN/m segments + couple). **Variation:** reverse the force direction; every sign flips.

---

#### Q7 (PYQ 2014-15 Compre A Q14) — Couple on a hinged beam *(easy)*
**Problem.** A beam AB, hinged at both ends, spans 2L with L = 2 m. At mid-span a couple is formed by two forces P = 20 kN, C = 1 m apart (20 kN·m). Find the magnitude of the shear force at any section.

**Solution.**
1. A pure couple needs an equal and opposite couple from the supports: $R_A = -R_B = \dfrac{20}{2L} = \dfrac{20}{4} = 5$ kN.
2. No other vertical loads, so V is constant along the beam.

$$\boxed{|V| = 5\ \text{kN everywhere}}$$

**Exam takeaway.** A couple causes no jump in the SFD, only in the BMD (a jump of 20 kN·m at mid-span, from −10 to +10 kN·m).

---

## Concept 3.2 — Distributed loads, their resultants and the limits of using them

### A. Concept explanation

**1. Intuition.** Spread sand on a plank. Each little strip Δx carries $q\,\Delta x$. For finding the **support reactions** you can pretend all the sand is piled at its centre of gravity. For the **bending inside the plank** you cannot, because sand piled in the middle bends the plank differently from sand spread evenly.

**2. Why it matters.** Self-weight, snow, water pressure on dams (Q14), sandbags (Q13), stored goods, the triangular and trapezoidal loads of the slides. Most beam PYQs include at least one distributed load.

**3. Formal treatment (slides).**
$$q = \lim_{\Delta x\to0}\frac{\Delta F}{\Delta x}\quad(\text{force per unit length; positive when acting in } +y,\ \text{i.e. upward})$$
Common distributions: **uniform**, q constant; **linearly varying**, $q(x) = Ax + B$.

*Resultant and its location (slides):*
$$R = \int_0^L q\,dx,\qquad \bar x = \frac{\int_0^L x\,q\,dx}{R}$$
The resultant equals the **area** of the load diagram and acts through its **centroid**.

| Load shape | R | $\bar x$ |
|---|---|---|
| Uniform $w_0$ over L | $w_0L$ | L/2 |
| Triangle from 0 to $w_0$ | $w_0L/2$ | 2L/3 from the zero end |
| Trapezoid $w_1\to w_2$ | $(w_1 + w_2)L/2$ | $\dfrac{L(w_1 + 2w_2)}{3(w_1 + w_2)}$ from the $w_1$ end |

*Limitations of the resultant (slides):*
1. Permissible when only evaluating external reactions on the member.
2. **Not** allowed when calculating internal forces and moments.

*Slide illustration:* beam (a) has P at each overhang tip, a distance a outside supports 2b apart. Beam (b) has 2P at the centre. Same resultant, same reactions ($R_A = R_B = P$). But (a) has **hogging** $M = -Pa$ between the supports, while (b) has **sagging** $M_{max} = +Pb$. The beams even bend in opposite directions.

**4. Derivation — cantilever with a triangular load (slides).** The load $w = w_0x/L$ acts downward, with the free end A at x = 0 and the wall B at x = L. Cut at x and keep the left part. The load on it is $\int_0^x w_0\xi/L\,d\xi = w_0x^2/2L$, acting at $2x/3$ from A, i.e. $x/3$ from the cut.
- $\sum F_y$: $-\dfrac{w_0x^2}{2L} + V = 0$, so $V = \dfrac{w_0x^2}{2L}$.
- $\sum M$: $M_b + \dfrac{w_0x^2}{2L}\cdot\dfrac x3 = 0$, so $M_b = -\dfrac{w_0x^3}{6L}$.

At the wall: $V = w_0L/2$ (the total load) and $M_b = -w_0L^2/6$ (hogging).

**5. Shape rules.** UDL gives a linear V and a parabolic M. A linearly varying load gives a parabolic V and a cubic M. Always use the portion of the load *on your free body*, placed at *its own* centroid.

**6. Special cases.**
- Simply supported beam with a full UDL: $V = -\tfrac{w_0L}{2} + w_0x$ and $M = \tfrac{w_0x(L - x)}{2}$, so $M_{max} = \tfrac{w_0L^2}{8}$ at mid-span, where V = 0.
- Cantilever with a full UDL: $|M|_{max} = w_0L^2/2$ at the wall.
- Simply supported beam with a triangular load of total W: $M_{max} = \dfrac{2WL}{9\sqrt3} = 0.128WL$, at $x = L/\sqrt3$ from the zero end (Q13).

**7. Common traps.**
- Using the resultant of the *whole* distributed load when cutting inside it.
- Putting a triangle's resultant at L/2 instead of 2L/3 from the zero end.
- Forgetting that the load intensity at the cut changes with x for a varying load.

**8. Summary.** For reactions, replace the load by its resultant (area at the centroid). For V and M, use only the part of the load on your free body, at its own centroid.

### B. Solved questions

#### Q8 (Slides Ch3, Gere) — Trapezoidal load: V and M at mid-span *(medium)*
**Problem.** A simply supported beam of span 3 m carries a load decreasing linearly from 50 kN/m at A to 30 kN/m at B. Find the shear force and bending moment at mid-span.

**Given:** L = 3 m; $w_A = 50$, $w_B = 30$ kN/m. **Find:** V and M at x = 1.5 m.

**Approach.** Reactions from the resultant of the whole trapezoid. Then cut at mid-span and use only the left part of the load, which is itself a trapezoid from 50 to 40 kN/m.

**FBD in words.** Left segment: $R_A$ ↑ at 0, a trapezoidal load from 50 to 40 kN/m over 1.5 m, and positive V and M at the cut.

**Solution.**
1. *Total load:* $\dfrac{50 + 30}{2}(3) = 120$ kN, at $\bar x = \dfrac{3(50 + 60)}{3(80)} = 1.375$ m from A.
2. *Reactions:* $R_B = 120(1.375)/3 = 55$ kN and $R_A = 65$ kN.
3. *Load on the left part:* intensity at 1.5 m is 40 kN/m. Resultant $= \dfrac{50 + 40}{2}(1.5) = 67.5$ kN at $\bar x = \dfrac{1.5(50 + 80)}{3(90)} = 0.722$ m from A, i.e. 0.778 m from the cut.
4. *Shear (Crandall):* $V = -(65 - 67.5) = +2.5$ kN (Gere: −2.5 kN).
5. *Moment:* $M = 65(1.5) - 67.5(0.778) = 97.5 - 52.5 = 45.0$ kN·m.

$$\boxed{V = +2.5\ \text{kN (Crandall)},\qquad M = 45.0\ \text{kN·m}}$$

**Check.** The true maximum (45.08 kN·m) is at x = 1.44 m, where V = 0, just left of mid-span. That makes sense because the load is heavier on the left ✓.

**Exam takeaway.** Split a trapezoid into a rectangle plus a triangle if the centroid formula slips your mind. **Variation:** find the position of $M_{max}$, by solving V(x) = 0 (a quadratic).

---

#### Q9 (Slides Ch3) — Symmetric triangular load of total W *(easy)*
**Problem.** A simply supported beam of span L carries a triangular load of total W, zero at both supports and peaking at mid-span. Find $M_{max}$. (Plotted for W = 12 kN, L = 6 m.)

**Approach.** Symmetry: $R_A = R_B = W/2$ and $M_{max}$ is at mid-span.

**Solution.**
1. Peak intensity $q_0$: $\tfrac12q_0L = W$, so $q_0 = 2W/L$. For $x \le L/2$: $q = 4Wx/L^2$.
2. Load to the left of x: $\int_0^x 4W\xi/L^2\,d\xi = 2Wx^2/L^2$, acting $x/3$ from the cut.
3. $M(x) = \dfrac W2x - \dfrac{2Wx^2}{L^2}\cdot\dfrac x3 = \dfrac W2x - \dfrac{2W}{3L^2}x^3$.
4. At x = L/2: $M = \dfrac{WL}{4} - \dfrac{WL}{12}$.

$$\boxed{M_{max} = \frac{WL}{6}\quad(12\ \text{kN·m for } W = 12\ \text{kN},\ L = 6\ \text{m})}$$

**Check.** A concentrated W at the centre gives WL/4, and a UDL of total W gives WL/8. A triangle concentrated toward the centre must lie between them: WL/6 ✓.

**Exam takeaway.** Compare against WL/4 and WL/8 as a quick sanity check on any distributed load. **Variation:** an unsymmetric triangle (Q11).

---

#### Q10 (Slides Ch3) — Partial UDL $w_0$ over length a from A (simply supported span L) *(medium)*
**Problem.** A simply supported beam of span L carries a UDL $w_0$ from A over a length a. Find the maximum bending moment and its position. (Plotted for $w_0 = 10$ kN/m, a = 3 m, L = 5 m.)

**Approach.** Reactions from the resultant $w_0a$ at $a/2$. The maximum is where V = 0, which must lie inside the loaded part.

**Solution.**
1. $R_B = \dfrac{w_0a(a/2)}{L} = \dfrac{w_0a^2}{2L}$ and $R_A = w_0a - R_B = \dfrac{w_0a(2L - a)}{2L}$.
2. V = 0 where the load to the left equals $R_A$: $w_0x_0 = R_A$, so $x_0 = \dfrac{a(2L - a)}{2L}$. This is always ≤ a ✓.
3. $M_{max} = R_Ax_0 - \dfrac{w_0x_0^2}{2} = \dfrac{R_A^2}{2w_0}$.

$$\boxed{x_0 = \frac{a(2L-a)}{2L},\qquad M_{max} = \frac{w_0a^2(2L-a)^2}{8L^2}}$$

For $w_0 = 10$, a = 3, L = 5: $R_A = 21$ kN, $x_0 = 2.1$ m, $M_{max} = 22.05$ kN·m.

**Check.** a = L gives $w_0L^2/8$ ✓.

**Exam takeaway.** $M_{max} = R_A^2/2w_0$ is a neat shortcut whenever V reaches zero inside a UDL that starts at a support. **Variation:** UDL over the middle third.

---

#### Q11 (Slides Ch3) — Triangular load rising to 2000 N/m over 9 m, falling to zero over 3 m *(medium)*
**Problem.** A simply supported 12 m beam carries a load rising linearly from 0 at A to 2000 N/m at x = 9 m, then falling linearly to 0 at B. Find the reactions and the maximum bending moment.

**Approach.** The whole load is one triangle with total $\tfrac12(2000)(12)$ at its centroid. For the cut, use the part of the rising triangle to the left.

**Solution.**
1. $R_{total} = \tfrac12(2000)(12) = 12\,000$ N, at the triangle's centroid $\bar x = (0 + 9 + 12)/3 = 7$ m.
2. $R_B = 12\,000(7)/12 = 7000$ N and $R_A = 5000$ N.
3. For $x \le 9$: intensity $2000x/9$, load to the left $1000x^2/9$ at $x/3$ from the cut.
4. V = 0: $5000 = 1000x^2/9$, so $x = \sqrt{45} = 6.708$ m.
5. $M = 5000x - \dfrac{1000x^2}{9}\cdot\dfrac x3$ at $x = 6.708$: $33\,541 - 11\,180 = 22\,360$ N·m.

$$\boxed{R_A = 5\ \text{kN},\quad R_B = 7\ \text{kN},\quad M_{max} = 22.36\ \text{kN·m at } x = 6.71\ \text{m}}$$

**Check.** The maximum lies inside the loaded part, slightly left of the load's centroid ✓.

**Exam takeaway.** The centroid of any triangle is at the average of its three vertices' x-coordinates. **Variation:** peak at mid-span gives Q9.

---

#### Q12 (Crandall Prob 3.6) — Cantilever with a full UDL *(easy)*
**Problem.** A cantilever of length L, built in at the left end, carries a UDL $w_0$ (force per unit length, downward) over its full length. Sketch V and M.

**Solution.**
1. *Wall reactions:* $R = w_0L$ ↑ and a counter-clockwise moment $w_0L^2/2$.
2. *Cut at x (keep the right part, length L − x, for simplicity):* the load on it is $w_0(L - x)$ at $(L - x)/2$ from the cut. Then V (Crandall, from the left part) $= -(w_0L - w_0x) = -w_0(L - x)$ and $M = -\dfrac{w_0(L - x)^2}{2}$.

$$\boxed{V = -w_0(L - x),\qquad M = -\frac{w_0(L-x)^2}{2},\qquad |M|_{max} = \frac{w_0L^2}{2}\ \text{at the wall}}$$

**Check.** $dM/dx = w_0(L - x) = -V$ ✓ (Crandall relation).

**Exam takeaway.** Keep whichever segment avoids the reactions; for a cantilever, keep the free end. **Variation:** Crandall 3.12 (Q21) adds a tip load.

---

#### Q13 (Crandall Prob 3.10) — Sixty 400 N sandbags piled in a triangle *(medium)*
**Problem.** Sixty 400 N sandbags are piled on a 3 m beam supported on rollers at both ends, with the pile height increasing linearly from zero at the left to a maximum at the right. Find the reactions and expressions for V and M as functions of x.

**Given:** total load W = 60(400) = 24 kN, triangular from 0 (left) to $q_0$ (right); L = 3 m. **Find:** reactions, V(x), M(x), $M_{max}$.

**Approach.** Treat the pile as a triangular distributed load: $\tfrac12q_0L = W$ gives $q_0 = 16$ kN/m. Use the resultant for reactions, and the left portion for V and M.

**Solution.**
1. *Reactions:* the resultant (24 kN) is at 2L/3 = 2 m from the left. $R_R = 24(2)/3 = 16$ kN and $R_L = 8$ kN.
2. *Intensity:* $q(x) = 16x/3$ kN/m. The load to the left of x is $\tfrac12x\cdot\tfrac{16x}{3} = \tfrac{8x^2}{3}$, at x/3 from the cut.
3. *Shear (Crandall):* $V(x) = -\left(8 - \dfrac{8x^2}{3}\right)$ kN.
4. *Moment:* $M(x) = 8x - \dfrac{8x^2}{3}\cdot\dfrac x3 = 8x - \dfrac{8x^3}{9}$ kN·m.
5. *Maximum:* V = 0 at $x^2 = 3$, so $x = \sqrt3 = 1.732$ m, and $M_{max} = 8(1.732) - \tfrac89(5.196) = 13.86 - 4.62 = 9.24$ kN·m.

$$\boxed{R_L = 8\ \text{kN},\ R_R = 16\ \text{kN};\quad V = -8 + \tfrac83x^2,\ M = 8x - \tfrac89x^3\ (\text{kN, m});\quad M_{max} = 9.24\ \text{kN·m at } x = 1.73\ \text{m}}$$

**Check.** The formula $M_{max} = 2WL/(9\sqrt3) = 2(24)(3)/15.59 = 9.24$ ✓. M(3) = 24 − 24 = 0 ✓.

**Exam takeaway.** A "pile of objects" is a distributed load; the slope of the pile gives the shape of q(x). **Variation:** a pile of uniform height gives the UDL result $WL/8 = 9$ kN·m. The triangle gives slightly more, because the maximum moves toward the heavy end where the arm is still large.

---

#### Q14 (Crandall Prob 3.34) — Wooden dam: SFD and BMD of an upright *(medium)*
**Problem.** A wooden dam consists of planks fastened to uprights driven into the river bed, 2.4 m apart. The water is 1.8 m deep. Draw the SFD and BMD for an upright.

**Given:** water (γ = 9.81 kN/m³), depth h = 1.8 m, spacing s = 2.4 m. Treat each upright as a cantilever fixed at the river bed and carrying the water pressure on a 2.4 m width of planks. **Find:** V and M along the upright.

**Approach.** Hydrostatic pressure γ(h − y) at height y above the bed, times the tributary width s, gives a triangular line load on the upright: zero at the surface, maximum at the bed.

**FBD in words.** Upright with y measured up from the bed. Load $q(y) = \gamma s(h - y)$ acting horizontally (downstream). Fixed base reactions: shear $V_0$ and moment $M_0$.

**Solution.**
1. *Load intensity at the bed:* $q_0 = 9.81(1.8)(2.4) = 42.38$ kN/m. In general $q(y) = 23.54(1.8 - y)$ kN/m.
2. *Shear at height y* (load above y): $V(y) = \tfrac12\gamma s(h - y)^2 = 11.77(1.8 - y)^2$ kN.
3. *Moment at height y:* that load acts at $(h - y)/3$ above y, so $M(y) = \tfrac16\gamma s(h - y)^3 = 3.924(1.8 - y)^3$ kN·m.
4. *At the bed (y = 0):* $V_0 = 11.77(3.24) = 38.1$ kN and $M_0 = 3.924(5.832) = 22.9$ kN·m.

$$\boxed{V_{max} = 38.1\ \text{kN},\qquad M_{max} = 22.9\ \text{kN·m, both at the river bed}}$$

**Check.** Total water force on 2.4 m of dam: $\tfrac12\gamma h^2s = \tfrac12(9.81)(3.24)(2.4) = 38.1$ kN, acting at h/3 = 0.6 m above the bed: $38.1(0.6) = 22.9$ ✓.

**Exam takeaway.** Hydrostatic loads are triangular, with the resultant at one-third of the depth from the bottom. The V diagram is a parabola and the M diagram a cubic, both maximum at the base. **Variation:** uprights also supported by a strut at the top, which turns the problem into a propped cantilever (indeterminate).

---

#### Q15 (PYQ 2014-15 Compre A Q6, Q7) — Simply supported beam with a full UDL *(easy)*
**Problem.** A simply supported beam carries w N/m over the whole span L. (Q6) What is the shear force at mid-span? (Q7) What is the bending moment at mid-span?

**Solution.**
1. $R_A = R_B = wL/2$.
2. At L/2 the load to the left is wL/2, which cancels $R_A$: V = 0.
3. $M(L/2) = \dfrac{wL}{2}\cdot\dfrac L2 - \dfrac{wL}{2}\cdot\dfrac L4 = \dfrac{wL^2}{8}$.

$$\boxed{V(L/2) = 0,\qquad M(L/2) = \frac{wL^2}{8}}$$

**Exam takeaway.** A one-line answer; memorise it.

---

## Concept 3.3 — Differential relations between q, V and M

### A. Concept explanation

**1. Intuition.** The load intensity is the "slope-maker" for the shear diagram, and the shear is the "slope-maker" for the moment diagram. Knowing this, you can sketch an SFD and BMD almost without algebra: the load tells you how V changes, V tells you how M changes, and the largest M sits where V crosses zero.

**2. Why it matters.** Fast, reliable diagrams; finding $M_{max}$ (where V = 0); and the starting point for the beam-deflection chapter ($EI\,v'''' = q$). The slides derive these relations explicitly.

**3–4. Formal treatment and derivation (slides; Crandall §3.5).** Take an element Δx with a distributed load q(x) (upward +). On its left (negative) face act V and $M_b$, drawn ↓ and clockwise (positive on a negative face). On its right (positive) face act $V + \Delta V$ and $M_b + \Delta M_b$, drawn ↑ and counter-clockwise.
- $\sum F_y = 0$: $(V + \Delta V) - V + q\,\Delta x = 0$, so $\dfrac{\Delta V}{\Delta x} = -q$.
- $\sum M_O = 0$ about the centre of the element: $(M_b + \Delta M_b) - M_b + (V + \Delta V)\dfrac{\Delta x}{2} + V\dfrac{\Delta x}{2} = 0$.

Let Δx → 0:
$$\boxed{\frac{dV}{dx} + q = 0,\qquad \frac{dM_b}{dx} + V = 0}\qquad\Rightarrow\qquad \frac{d^2M_b}{dx^2} = q$$
*Integral forms:* $V_2 - V_1 = -\int_1^2q\,dx$ (minus the load area) and $M_2 - M_1 = -\int_1^2V\,dx$ (minus the SFD area).

*Concentrated load P (↓) at a point:* integrate across it, so V jumps by **+P** (Crandall). *Concentrated clockwise couple C:* M jumps by **+C**.

**5. Reading diagrams (Crandall signs; a downward load means q < 0).**

| Load on the segment | SFD | BMD |
|---|---|---|
| None | constant | linear |
| UDL downward | linear, **rising** (slope $-q > 0$) | parabola, concave down (∩) |
| Linearly varying load | parabola | cubic |
| Concentrated downward P | jumps **up** by P | kink (slope change) |
| Clockwise couple C | no change | jumps **up** by C |

**M is extreme where V = 0**, or where V jumps through zero at a concentrated load.

**6. Special cases.**
- At a free end, or a pinned end with no applied couple: M = 0.
- At a free end with no point load: V = 0.
- Where q = 0 and V = 0 over a stretch: M is constant (pure bending).

**7. Common traps.**
- Using Gere's formulas ($dM/dx = +V$) with Crandall's signs for V turns the BMD upside down. Pick one convention and stay with it.
- Missing a maximum inside a distributed load: always solve V = 0 there.
- A **point of contraflexure** is where M **changes sign** (passes through zero), not where V = 0.
- At a support carrying an overhang, V changes sign at the support (Q20), so the hogging maximum is there.

**8. Summary.** $V' = -q$ and $M' = -V$ (Crandall). The area of the load diagram gives the change in V; minus the area of the SFD gives the change in M.

### B. Solved questions

#### Q16 (Slides Ch3) — 4 kN, 2 kN/m and 8 kN on a 10 m span *(medium)*
**Problem.** A simply supported beam (A at 0, B at 10 m) carries 4 kN at C (2 m), a UDL of 2 kN/m from D (3 m) to E (7 m) and 8 kN at F (9 m). Draw the SFD and BMD.

**Approach.** Reactions, then V at each key point using jumps and slopes, then M from the SFD areas.

**Solution.**
1. *Reactions:* $\sum M_A$: $R_B(10) = 4(2) + 8(5) + 8(9) = 120$, so $R_B = 12$ kN and $R_A = 20 - 12 = 8$ kN.
2. *Key values:*

| Point | A | C⁻ | C⁺ | D | x = 5 | E | F⁻ | F⁺ | B |
|---|---|---|---|---|---|---|---|---|---|
| V (kN, Crandall) | −8 | −8 | −4 | −4 | 0 | +4 | +4 | +12 | +12 |
| M (kN·m) | 0 | 16 | 16 | 20 | **24** | 20 | 12 | 12 | 0 |

3. *Between D and E:* $M = 8x - 4(x - 2) - (x - 3)^2$, and $dM/dx = 0$ at x = 5, where $M = 40 - 12 - 4 = 24$.

$$\boxed{M_{max} = 24\ \text{kN·m at mid-span (x = 5 m)};\ \text{no point of contraflexure}}$$

**Check.** The SFD area from A to the maximum is $8(2) + 4(1) + \tfrac12(4)(2) = 24$, which equals $M_{max}$ ✓ ($M = -\int V\,dx$ with Crandall's V negative there).

**Exam takeaway.** Tabulating V and M at every load point (with ⁻ and ⁺ sides) is exactly what the slide's table asks for. **Variation:** move the 8 kN onto an overhang beyond B; a hogging region then appears.

---

#### Q17 (Slides Ch3) — 3 kN + UDL + 2 kN: position and value of the maximum BM *(medium)*
**Problem.** A simply supported 8 m beam carries 3 kN at C (2 m), a UDL of 2 kN/m from C to D (2–5 m) and 2 kN at D (5 m). Draw the SFD and BMD and find the position and magnitude of the maximum bending moment.

**Solution.**
1. *Reactions:* $\sum M_A$: $R_B(8) = 3(2) + 6(3.5) + 2(5) = 37$, so $R_B = 4.625$ kN and $R_A = 11 - 4.625 = 6.375$ kN.
2. *V = 0 inside CD:* $6.375 - 3 - 2(x - 2) = 0$, so x = 3.6875 m (point E).
3. *Moments:* $M_C = 6.375(2) = 12.75$; $M_E = 6.375(3.6875) - 3(1.6875) - 2(1.6875)^2/2 = 23.508 - 5.063 - 2.848 = 15.60$; $M_D = 4.625(3) = 13.875$ kN·m.

| Point | A | C⁺ | E | D⁻ | D⁺ | B |
|---|---|---|---|---|---|---|
| V (Crandall) | −6.375 | −3.375 | 0 | +2.625 | +4.625 | +4.625 |
| M (kN·m) | 0 | 12.75 | **15.60** | 13.875 | 13.875 | 0 |

$$\boxed{M_{max} = 15.6\ \text{kN·m at } x = 3.69\ \text{m from A}}$$

**Check.** These match the slide's hand solution (6.38, 3.375, 2.625, 12.75, 15.59, 13.875) ✓.

**Exam takeaway.** "Position and value of maximum BM" means solve V = 0 inside the UDL.

---

#### Q18 (Slides Ch3) — 5 kN/m segments plus an offset couple *(medium–hard)*
**Problem.** A simply supported beam AB, 8 m long, carries 5 kN/m over AC (0–2 m) and over EB (6–8 m). At D (4 m) a vertical arm carries 10 kN → at 1 m above the beam and 10 kN ← at 1 m below it. Fill the V/M table at A, C, D⁻, D⁺, E and B.

**Approach.** The two arm forces cancel as forces but form a couple. Replace them by that couple at D (Concept 1.2).

**Solution.**
1. *Arm loads:* moment about D $= 10(1) + 10(1) = 20$ kN·m **clockwise**, applied at D; no net force.
2. *Reactions:* $\sum M_A$: $R_B(8) - 10(1) - 10(7) - 20 = 0$, so $R_B = 12.5$ kN and $R_A = 7.5$ kN.
3. *Moments:* AC: $M = 7.5x - 2.5x^2$; CD: $M = 10 - 2.5x$, falling to 0 at D⁻; at D, +20 (clockwise couple); DE: $M = 30 - 2.5x$; EB: $M = 30 - 2.5x - 2.5(x - 6)^2$.

| | A | C | D⁻ | D⁺ | E | B |
|---|---|---|---|---|---|---|
| V (kN, Crandall) | −7.5 | +2.5 | +2.5 | +2.5 | +2.5 | +12.5 |
| $M_b$ (kN·m) | 0 | 5 | 0 | **20** | 15 | 0 |

There is also a local maximum of 5.625 kN·m at x = 1.5 m (where V = 0 in AC).

$$\boxed{M_{max} = 20\ \text{kN·m at D}^+}$$

**Check.** From the right: $M(D^+) = 12.5(4) - 10(3) = 20$ ✓.

**Exam takeaway.** Horizontal forces on an offset arm add **no** vertical shear but do add a couple. The slide's "if any discontinuity point is left in the table please add it" is a hint about the jump at D.

---

#### Q19 (Crandall Prob 3.7) — Uniform load over a beam with an overhang *(medium)*
**Problem.** A beam is supported at x = 0 and x = L and overhangs a distance a beyond the right support. A uniform load $w_0$ acts over the whole length L + a. Sketch V and M and label the important values.

**Solution.**
1. *Reactions:* $\sum M_A$: $R_BL = w_0(L + a)\dfrac{L + a}{2}$, so $R_B = \dfrac{w_0(L + a)^2}{2L}$ and $R_A = \dfrac{w_0(L^2 - a^2)}{2L}$.
2. *Key values:*

| Point | V (Crandall) | M |
|---|---|---|
| A | $-R_A$ | 0 |
| In the span, V = 0 at $x_0 = (L^2 - a^2)/2L$ | 0 | $+\dfrac{w_0(L^2 - a^2)^2}{8L^2}$ |
| B⁻ | $+\dfrac{w_0(L^2 + a^2)}{2L}$ | $-\dfrac{w_0a^2}{2}$ |
| B⁺ | $-w_0a$ | $-\dfrac{w_0a^2}{2}$ |
| Tip | 0 | 0 |

$$\boxed{M^+_{max} = \frac{w_0(L^2-a^2)^2}{8L^2},\qquad M_B = -\frac{w_0a^2}{2}}$$

**Check.** a = 0 gives the simple-span result $w_0L^2/8$ ✓. Equalizing magnitudes gives $a = 0.414L$ (plotted).

**Exam takeaway.** Overhangs create hogging at the support and a contraflexure point in the span. **Variation:** Crandall 3.18, a scaffold plank with overhangs on both sides.

---

#### Q20 (Crandall Prob 3.8) — Overhanging beam with 1.5 kN and 1.5 kN/m *(medium)*
**Problem.** A pin at A (x = 0) and a roller at B (x = 3.75 m) support a beam with a 1.5 m overhang. 1.5 kN acts at x = 1.5 m and 1.5 kN/m over the overhang (3.75–5.25 m). Sketch V and M.

**Solution.**
1. *Reactions:* $R_B(3.75) = 1.5(1.5) + 2.25(4.5)$, so $R_B = 3.30$ kN and $R_A = 3.75 - 3.30 = 0.45$ kN.
2. *Key values:*

| | A | load⁻ | load⁺ | B⁻ | B⁺ | tip |
|---|---|---|---|---|---|---|
| V (kN, Crandall) | −0.45 | −0.45 | +1.05 | +1.05 | −2.25 | 0 |
| M (kN·m) | 0 | 0.675 | 0.675 | −1.69 | −1.69 | 0 |

3. *Contraflexure:* $0.45x - 1.5(x - 1.5) = 0$, so x = 2.14 m.

$$\boxed{M^+_{max} = 0.675\ \text{kN·m at the load};\quad M_B = -1.69\ \text{kN·m};\quad \text{contraflexure at } x = 2.14\ \text{m}}$$

**Check.** $M_B$ from the overhang: $-1.5(1.5)^2/2 = -1.6875$ ✓.

**Exam takeaway.** A support next to an overhang is usually where the largest moment sits. This same beam is re-solved with singularity functions in Q24.

---

#### Q21 (Crandall Prob 3.12) — Cantilever with a tip load and a UDL on the inner half *(medium)*
**Problem.** A cantilever AB is built in at B (right end) and free at A (left end). It carries a concentrated force P at A and a distributed load $w_0$ over the half nearest the wall (from L/2 to L). Sketch V and M.

**Approach.** Measure x from the free end A, so no reactions are needed.

**Solution.**
1. *$0 < x < L/2$:* only P is to the left. $V = -(-P) = +P$ (Crandall) and $M = -Px$.
2. *$L/2 < x < L$:* $V = P + w_0(x - L/2)$ and $M = -Px - \dfrac{w_0(x - L/2)^2}{2}$.
3. *At the wall B:* $V_B = P + \dfrac{w_0L}{2}$ and $M_B = -PL - \dfrac{w_0L^2}{8}$.

$$\boxed{V_B = P + \frac{w_0L}{2},\qquad M_B = -PL - \frac{w_0L^2}{8}\ \text{(hogging, the maximum)}}$$

**Check.** $dM/dx = -P - w_0(x - L/2) = -V$ ✓.

**Exam takeaway.** For cantilevers, start from the free end. The wall values equal the totals of the loads and of their moments about the wall.

---

#### Q22 (Crandall Prob 3.17) — The carpenter and the sawhorses *(medium, a classic)*
**Problem.** A carpenter has a 6 m plank of uniform weight $w_0$ per unit length and two sawhorses. He wants to cut off a 1.8 m length at a point where the bending moment is zero, to avoid splitting. If one sawhorse is at one end of the plank, where should he put the other?

**Approach.** Unknown position s of the second sawhorse. Its reaction from moments about the first, then set M = 0 at the cut (x = 4.2 m from the first sawhorse).

**Solution.**
1. *Reaction at s:* $R_s = \dfrac{w_0(6)(3)}{s} = \dfrac{18w_0}{s}$.
2. *For $4.2 < s < 6$,* take moments of the right part about the cut at 4.2 m: $R_s(s - 4.2) - w_0(1.8)(0.9) = 0$.
3. $18 - \dfrac{75.6}{s} = 1.62$, so $s = \dfrac{75.6}{16.38} = 4.615$ m.

$$\boxed{s = 4.62\ \text{m from the first end (1.38 m from the far end)}}$$

**Check.** If $s < 4.2$, the cut would lie in the overhang, where $M = -w_0(1.8)^2/2 \ne 0$, so there is no solution there ✓.

**Exam takeaway.** Zero-moment points (contraflexure) are where a member can be hinged or cut without disturbing equilibrium. **Variation:** Crandall 3.18 (scaffold) and Q23 (bookshelf) optimise the same idea.

---

#### Q23 (Crandall Prob 3.25) — Bookshelf on two bricks: minimise the maximum moment *(medium)*
**Problem.** A bookshelf is a plank of length L resting on two bricks placed symmetrically, a distance a from each end. With a uniform load w (books plus plank), where should the bricks go to make the maximum bending moment as small as possible?

**Approach.** Two candidates for $|M|_{max}$: hogging over a support and sagging at mid-span. The optimum makes them equal in magnitude.

**Solution.**
1. *Reactions:* each support carries wL/2.
2. *Over a support:* $M_s = -\dfrac{wa^2}{2}$.
3. *Mid-span:* $M_c = \dfrac{wL}{2}\left(\dfrac L2 - a\right) - \dfrac{w}{2}\left(\dfrac L2\right)^2 = \dfrac{w(L - 2a)^2}{8} - \dfrac{wa^2}{2}$.
4. *Equal magnitudes:* $\dfrac{(L - 2a)^2}{8} - \dfrac{a^2}{2} = \dfrac{a^2}{2}$, so $(L - 2a)^2 = 8a^2$, $L - 2a = 2\sqrt2a$ and $a = \dfrac{L}{2(1 + \sqrt2)}$.

$$\boxed{a = 0.207L,\qquad |M|_{max} = \frac{wa^2}{2} = 0.0214\,wL^2}$$

**Check.** Supports at the ends would give $wL^2/8 = 0.125wL^2$, nearly 6× larger ✓.

**Exam takeaway.** Balancing the hogging and sagging peaks is a standard optimisation. **Variation:** supports at the ends but a single load P anywhere on the shelf.

---

## Concept 3.4 — Singularity (Macaulay) functions

### A. Concept explanation

**1. Intuition.** Instead of writing a new M(x) for every segment, use "switches" $\langle x - a\rangle$ that are off (0) before x = a and on after it. One formula then covers the whole beam. This saves a lot of algebra in the deflection chapter, where you integrate twice.

**2. Why it matters.** PYQ 2014-15 Test-1 Q4 (25 marks) demanded this method *only*, and 2023-24 Part B Q3 uses it for deflection. Crandall Prob 3.23 asks you to redo Probs 3.1–3.8 with it.

**3. Formal treatment (slides).**
$$\langle x - a\rangle^n = \begin{cases}(x - a)^n & x\ge a\\ 0 & x<a\end{cases}\ (n\ge0),\qquad \langle x - a\rangle^0 = \text{unit step}$$
$\langle x - a\rangle_{-1}$ is a concentrated (Dirac) load and $\langle x - a\rangle_{-2}$ a concentrated couple (doublet).

*Integration rules (slides):* for $n \ge 0$, $\int_{-\infty}^x\langle x - a\rangle^ndx = \dfrac{\langle x - a\rangle^{n+1}}{n + 1}$. For $n < 0$, $\int\langle x - a\rangle_ndx = \langle x - a\rangle_{n+1}$.

*Loading representation (slide Rule 2):* a distributed load is zero order, $w_0\langle x - a\rangle^0$; a point load is order −1, $P\langle x - a\rangle_{-1}$; a moment is order −2, $M_0\langle x - a\rangle_{-2}$. To stop a UDL at b, add $-w_0\langle x - b\rangle^0$. A ramp is $\dfrac{w_0}{b - a}\langle x - a\rangle^1$.

*Slide Rule 4:* (1) set up w(x) including **all** forces (reactions too) from left to right; (2) integrate w once to get V, with **no** constants; (3) integrate V to get M, with **no** constants.

**4. Derivation — why no constants.** For x < 0 (just left of the beam) V and M are zero, and every term $\langle x - a\rangle_n$ with a ≥ 0 is zero there too. So the integration constants must be zero. ∎

**5. Working form you can use directly** (sagging M +, clockwise couples +, upward forces +):
$$M(x) = \sum_{\text{up}}P_i\langle x - a_i\rangle^1 - \sum_{\text{down}}P_j\langle x - a_j\rangle^1 + \sum_{\text{cw}}C_k\langle x - a_k\rangle^0 - \sum_{\text{UDL}\downarrow}\frac{w}{2}\langle x - a\rangle^2 + \dots,\qquad V_{Crandall} = -\frac{dM}{dx}$$

**6. Special cases.** A UDL that runs to the end of the beam needs no "stop" term. A UDL that ends early needs $+\frac{w}{2}\langle x - b\rangle^2$ in M.

**7. Traps.**
- Evaluating $\langle x - a\rangle$ as $(x - a)$ when $x < a$; it must be 0.
- Forgetting to end a UDL.
- Using $\langle x - a\rangle^1$ for a couple; in M it must be $\langle x - a\rangle^0$.
- Leaving reactions out of w(x).

**8. Summary.** One equation, switches on at each discontinuity, no constants for V and M.

### B. Solved questions

#### Q24 (Crandall Prob 3.23(h)) — Prob 3.8 again, using singularity functions *(medium)*
**Problem.** Obtain the SFD and BMD of Crandall Prob 3.8 (Q20) using singularity-function notation.

**Given:** pin at 0 ($R_A = 0.45$ kN ↑), 1.5 kN ↓ at 1.5 m, roller at 3.75 m ($R_B = 3.30$ kN ↑), 1.5 kN/m ↓ from 3.75 m to the end (5.25 m). **Find:** one equation each for M(x) and V(x).

**Solution.**
1. *Moment:*
$$M(x) = 0.45\langle x\rangle^1 - 1.5\langle x - 1.5\rangle^1 + 3.30\langle x - 3.75\rangle^1 - 0.75\langle x - 3.75\rangle^2\quad(\text{kN·m})$$
2. *Shear (Crandall):*
$$V(x) = -\frac{dM}{dx} = -0.45\langle x\rangle^0 + 1.5\langle x - 1.5\rangle^0 - 3.30\langle x - 3.75\rangle^0 + 1.5\langle x - 3.75\rangle^1\quad(\text{kN})$$
3. *Checks at key points:* $M(1.5) = 0.675$; $M(3.75) = 1.6875 - 3.375 = -1.6875$; $M(5.25) = 2.3625 - 5.625 + 4.95 - 1.6875 = 0$ ✓.

$$\boxed{\text{Same diagrams as Q20: } M^+_{max} = 0.675,\ M_B = -1.69\ \text{kN·m}}$$

**Exam takeaway.** The value at the free end must come out zero. That is your built-in check.

---

#### Q25 (PYQ 2014-15 Test-1 Q4) — Singularity functions: SFD, BMD and contraflexure *(hard, 25 marks)*
**Problem.** Using the singularity-function method **only**, calculate the shear force and bending moment at the salient points of the beam, draw the SFD and BMD and locate the point of contraflexure. A (pin) at 0; C at 10 m with 90 kN ↓; D at 20 m with a 10 kN·m couple (clockwise as drawn); B (roller) at 30 m; free end E at 40 m; UDL 10 kN/m over BE (30–40 m).

**Approach.** Reactions first, then one M(x) equation with singularity terms, then V = −dM/dx.

**Solution.**
1. *Reactions:* $\sum M_A$: $R_B(30) - 90(10) - 10 - 100(35) = 0$, so $R_B = 4410/30 = 147$ kN and $R_A = 190 - 147 = 43$ kN.
2. *Moment equation:*
$$M(x) = 43\langle x\rangle^1 - 90\langle x - 10\rangle^1 + 10\langle x - 20\rangle^0 + 147\langle x - 30\rangle^1 - 5\langle x - 30\rangle^2\quad(\text{kN·m})$$
3. *Shear (Crandall):*
$$V(x) = -43\langle x\rangle^0 + 90\langle x - 10\rangle^0 - 147\langle x - 30\rangle^0 + 10\langle x - 30\rangle^1\quad(\text{kN})$$
(The couple term differentiates to $\langle\rangle_{-1}$, which is zero except exactly at x = 20.)
4. *Salient values:*

| | A | C⁻ | C⁺ | D⁻ | D⁺ | B⁻ | B⁺ | E |
|---|---|---|---|---|---|---|---|---|
| V (kN, Crandall) | −43 | −43 | +47 | +47 | +47 | +47 | −100 | 0 |
| M (kN·m) | 0 | **430** | 430 | −40 | −30 | **−500** | −500 | 0 |

5. *Contraflexure:* in CD, $M = 43x - 90(x - 10) = 900 - 47x = 0$, so $x = 19.15$ m. After D, M stays negative (−30 to −500) and reaches zero only at the free end E, so there is only one point of contraflexure.

$$\boxed{M_{max}^+ = 430\ \text{kN·m at C},\quad M_{max}^- = -500\ \text{kN·m at B},\quad \text{contraflexure at } x = 19.15\ \text{m}}$$

**Check.** $M(40) = 43(40) - 90(30) + 10 + 147(10) - 5(100) = 1720 - 2700 + 10 + 1470 - 500 = 0$ ✓.

**Exam takeaway.** The marks are for the singularity equation itself, the table of salient values and the contraflexure location. **Variation:** reverse the couple; M at D then jumps **down** by 10.

---

## Concept 3.5 — Cantilevers, frames, curved and 3-D members

### A. Concept explanation

**1. Intuition.** The cut method works the same for bent or curved members. Just remember that "axial" and "shear" are measured along and across the **local** direction of the member at the cut. In 3-D, use vectors: $\mathbf F$ and $\mathbf M = \mathbf r\times\mathbf F$. An out-of-plane load on a curved or bent member makes it **twist** as well as bend.

**2. Why it matters.** Brackets, cranks, pipes, curved hooks, lamp posts. These are the first part of every combined-stress PYQ (Ch. 6): find F, V, $M_b$ and $M_t$ at a section, then stresses.

**3. Formal treatment (Crandall §3.8, Example 3.11).** For a cut segment with free-end load $\mathbf P$ at position $\mathbf r_{CA}$ relative to the cut C:
$$\mathbf V_C + \mathbf P = 0,\qquad \mathbf M_C + \mathbf r_{CA}\times\mathbf P = 0$$
Resolve into the component along the local axis (axial force and twist) and the components perpendicular to it (shear and bending).

*Crandall's observation:* along a straight member under point loads only, the maximum resultant bending moment always occurs at a load point, never between loads (the resultant moment diagram is made of straight lines or curves that are concave outward).

**4. Derivations.**

*(a) Frame moment formula.* For a free end D loaded by $(F_x, F_y)$, the in-plane bending moment at any point (x, y) of a planar frame is
$$M(x, y) = (x_D - x)F_y - (y_D - y)F_x$$
One formula covers every straight segment, so you need not redo FBDs for each leg (Q28).

*(b) Crandall Example 3.11, quarter-circle pipe with a transverse load (Q26).* At angle θ: $V = -P$, $M_b = Pa\sin\theta$ and $M_t = -Pa(1 - \cos\theta)$.

*(c) Curved cantilever with an in-plane tip load (Q29):* $N = P\cos\theta$, $V = P\sin\theta$ and $M = PR\cos\theta$.

**5. Picture.** For a bent bracket, draw the BMD *on* each member, on the tension side. Joints transmit M unchanged around a rigid corner, but the axial and shear forces swap roles when the member turns 90°.

**6. Special cases.** A bracket loaded so that its free end lies on the line of action of the load from a section: zero moment there. Out-of-plane loads on L-shaped members cause twist in the leg perpendicular to the load's arm.

**7. Traps.**
- For curved members the "axial" direction rotates with θ. Resolve the load into tangential and radial parts *at the cut*.
- In 3-D, mixing up which moment component is twist ($M_{xx}$) and which are bending.
- Forgetting the moment of a horizontal load about a vertical leg.

**8. Summary.** Vectors: $\mathbf M = \mathbf r\times\mathbf F$. Frame: $M = (x_D - x)F_y - (y_D - y)F_x$. Curved cantilever: $N = P\cos\theta$, $V = P\sin\theta$, $M = PR\cos\theta$.

### B. Solved questions

#### Q26 (Crandall Example 3.11) — Quarter-circle pipe with a transverse load *(medium, 3-D)*
**Problem.** A piece of refinery piping AB, anchored at B, is bent into a quadrant of a circle of radius a (centre O). A transverse load P acts at the free end A, perpendicular to the plane of the pipe. Find the shear force, bending moment and twisting moment at a general section C at angle θ from A.

**Given:** radius a; load P along the axis (call it i) perpendicular to the plane. At C use local unit vectors: $\mathbf u_t$ along the pipe and $\mathbf u_r$ radial. **Find:** V, $M_b$, $M_t$ at θ.

**Approach.** Free body from the cut C to the free end A. Force balance gives V; moment balance about C, with the cross product, gives $M_b$ and $M_t$.

**Solution.**
1. *Force:* $\mathbf V + P\mathbf i = 0$, so $V = -P$ (transverse shear, constant).
2. *Position of A relative to C:* $\mathbf r_{CA} = -a(1 - \cos\theta)\mathbf u_r - a\sin\theta\,\mathbf u_t$ (Crandall's eq. (e)).
3. *Moment balance:* $\mathbf M_C + \mathbf r_{CA}\times(P\mathbf i) = 0$. Working out the cross products and setting each component to zero gives the bending moment about the radial axis and the twist about the tangent.

$$\boxed{V = -P,\qquad M_b = Pa\sin\theta,\qquad M_t = -Pa(1 - \cos\theta)}$$

**Check.** At A (θ = 0) both moments vanish ✓. At the anchor B (θ = 90°): $M_b = Pa$ and $|M_t| = Pa$; the anchor resists equal bending and twisting moments ✓.

**Exam takeaway.** An out-of-plane load on a curved member produces **twist**. That is why pipe bends and crankshafts see torsion even without an applied torque. **Variation:** a semicircular pipe (θ up to 180°), where $|M_t|$ reaches 2Pa.

---

#### Q27 (PYQ 2014-15 Compre A Q17–18) — Cantilever with three loads *(easy–medium)*
**Problem.** A cantilever is fixed at A, with 30 kN ↓ at B (1 m), 80 kN **↑** at C (3 m) and 20 kN ↓ at D (5 m). Find the reaction and moment at A (Q17) and the position of the point of contraflexure from A (Q18).

**Solution.**
1. *$\sum F_y$:* $R_A - 30 + 80 - 20 = 0$, so $R_A = -30$ kN, i.e. **30 kN ↓**.
2. *$\sum M_A$:* $M_A - 30(1) + 80(3) - 20(5) = 0$, so $M_A = -110$ kN·m, i.e. **110 kN·m clockwise on the beam**.
3. *M along the beam (from the right):* CD: $M = -20(5 - x)$ (hogging); BC: $M = -20(5 - x) + 80(3 - x) = 140 - 60x$; AB: $M = 140 - 60x - 30(1 - x) = 110 - 30x$.
4. *Zero in BC:* $140 - 60x = 0$, so $x = 2.33$ m.

$$\boxed{R_A = 30\ \text{kN}\downarrow,\quad M_A = 110\ \text{kN·m (clockwise)},\quad \text{contraflexure at } 2.33\ \text{m from A}}$$

**Check.** M at A from the formula: 110 kN·m (sagging, since the upward 80 kN dominates near the wall) ✓; at D: 0 ✓.

**Exam takeaway.** An upward load on a cantilever can make the wall moment sagging. Don't assume "cantilever ⇒ hogging".

---

#### Q28 (PYQ 2019-20 Compre A Q1) — Bracket ABCD: BMD and minimum diameter *(medium, 8 marks)*
**Problem.** A bracket ABCD of solid circular section is fixed at A. AB is horizontal (6b), BC goes vertically down (2b), and CD runs horizontally back toward A (2b). At the free end D act P = 40 N ← (horizontal) and P = 40 N ↑ (vertical). b = 37 mm and $\sigma_{allow} = 30$ MPa. (a) Draw the BMD of each segment. (b) Find $d_{min}$ (neglect the bracket's weight).

**Approach.** Use the frame moment formula with D as the loaded free end. Then the bending stress in a solid circle, $\sigma = 32M/\pi d^3$ (from the flexure formula, covered later in the course).

**Solution.**
1. *Coordinates:* A(0, 0), B(6b, 0), C(6b, −2b), D(4b, −2b). Loads at D: $(F_x, F_y) = (-P, +P)$.
2. *Frame moment:* $M(x, y) = (x_D - x)F_y - (y_D - y)F_x = P(4b - x) - P(2b + y) = P(2b - x - y)$.

| Segment | Expression | End values |
|---|---|---|
| CD ($y = -2b$, x from 4b to 6b) | $P(4b - x)$ | D: 0 → C: −2Pb (linear) |
| BC ($x = 6b$, y from −2b to 0) | $P(-4b - y)$ | C: −2Pb → B: −4Pb (linear) |
| AB ($y = 0$, x from 6b to 0) | $P(2b - x)$ | B: −4Pb → A: +2Pb; zero at x = 2b |

3. *Maximum:* $|M|_{max} = 4Pb = 4(40)(37) = 5920$ N·mm at B. There is a point of contraflexure on AB at 2b from A.
4. *(b) Diameter:* $\sigma = \dfrac{32M}{\pi d^3} \le 30$, so $d^3 = \dfrac{32(5920)}{\pi(30)} = 2010$ mm³.

$$\boxed{|M|_{max} = 4Pb = 5.92\ \text{N·m at B};\qquad d_{min} = 12.6\ \text{mm}}$$

**Check.** The axial force in AB is only P = 40 N, so $P/A \approx 0.3$ MPa, negligible next to 30 MPa ✓.

**Exam takeaway.** The hint "show the variation along AB, BC, CD separately" is asking for exactly this table. **Variation:** load only the vertical P; then $M = P(4b - x)$ everywhere and the maximum moves to A (4Pb).

---

#### Q29 (PYQ 2019-20 Compre A Q3(a) = Crandall Prob 3.9) — Curved cantilever: forces at section θ *(medium)*
**Problem.** A quarter-circle cantilever of radius R is fixed at A (θ = 0, at ground level) and free at B (θ = 90°, at the top), with P ↓ at B. θ is measured at the centre O from the horizontal. Find the axial force, shear force and bending moment at any section θ.

**Given:** R, P. **Find:** N(θ), V(θ), M(θ).

**Approach.** Free body from the cut to B. Resolve P into tangential and radial components at the cut.

**Solution.**
1. *Position on the arc* relative to O: $(-R\cos\theta, R\sin\theta)$. Tangent direction (toward B): $\mathbf t = (\sin\theta, \cos\theta)$. Outward radial direction: $\mathbf n = (-\cos\theta, \sin\theta)$.
2. *Load* $(0, -P)$ at B = (0, R).
3. *Axial (along t):* $\mathbf P\cdot\mathbf t = -P\cos\theta$, so $N = P\cos\theta$ in compression.
4. *Shear (along n):* magnitude $|\mathbf P\cdot\mathbf n| = P\sin\theta$.
5. *Moment:* the horizontal lever arm from the cut to B is $R\cos\theta$, so $M = PR\cos\theta$.

$$\boxed{N = P\cos\theta\ \text{(compression)},\qquad V = P\sin\theta,\qquad M = PR\cos\theta}$$

**Check.** At B (θ = 90°): N = M = 0 and V = P (the load is purely transverse there) ✓. At A (θ = 0): N = P and M = PR (the maximum) ✓.

**Exam takeaway.** These expressions feed straight into Castigliano's theorem (Ch. 2 Q26): $\delta_B = \pi PR^3/4EI + \pi PR/4AE$.

---

## Chapter 3 — Formula and convention sheet

| Item | Crandall / slides |
|---|---|
| Positive face | outward normal along +x |
| + component | (+face, +dir) or (−face, −dir) |
| V | $= -\sum(\text{upward forces to the left of the cut})$, **opposite sign to Gere** |
| $M_b$ | sagging +; $= \sum$ moments of the left-hand forces about the cut (clockwise +) |
| Differential relations | $dV/dx = -q$, $dM_b/dx = -V$, $d^2M_b/dx^2 = q$ (q up +) |
| Max/min M | where V = 0 or changes sign |
| Contraflexure | where M changes sign |
| Concentrated load P↓ | V jumps by +P (Crandall); kink in M |
| Clockwise couple C | M jumps by +C; V unchanged |
| Resultant of a distributed load | $R = \int q\,dx$ at the centroid, **reactions only** |
| Standard results | SS + central W: WL/4; SS + UDL: $wL^2/8$; SS + W at a: Wab/L; cantilever + tip P: −PL; cantilever + UDL: $-wL^2/2$; SS + triangle W: 0.128WL |
| Hydrostatic upright | $V_0 = \tfrac12\gamma sh^2$, $M_0 = \tfrac16\gamma sh^3$ |
| Optimum overhangs | bookshelf a = 0.207L; overhang beam a = 0.414L |
| Singularity | $\langle x - a\rangle^n$ (0 for x < a); point load $\langle\rangle_{-1}$, couple $\langle\rangle_{-2}$; no constants for V and M |
| Frame moment | $M = (x_D - x)F_y - (y_D - y)F_x$ |
| Curved cantilever (tip load) | $N = P\cos\theta$, $V = P\sin\theta$, $M = PR\cos\theta$ |
| Pipe quadrant, transverse load | $V = -P$, $M_b = Pa\sin\theta$, $M_t = -Pa(1 - \cos\theta)$ |

**Other Crandall Ch. 3 problems worth practising:** 3.3 (inclined cantilever), 3.11 (semicircular arch), 3.13 and 3.15 (sections in 3-D members and frames), 3.16 (femur muscles), 3.18 (scaffold plank), 3.24 (diving board), 3.26–3.30 (flagpole, bent rods, antenna, trailer bars), 3.31 (cable sag).
