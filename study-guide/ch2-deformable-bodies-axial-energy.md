# Chapter 2 — Introduction to Mechanics of Deformable Bodies
### Axial deformation, statically indeterminate bars, displacement diagrams, strain energy, Castigliano

**Sources used:** Slides "Chapter 2" (Dr. Sharad Shrivastava), Crandall Ch. 2 (§2.2–2.6; Probs 2.1, 2.6, 2.7, 2.19, 2.24), PYQs 2014-15 (Test-1 Q2; Compre A Q8, Q11) and 2019-20 Compre A Q3(b).

---

## Concept 2.1 — The three-step method for deformable bodies

### A. Concept explanation

**1. Intuition.** Push down on a mattress that has two different springs side by side. You can't say how much each spring carries just by balancing forces, because one equation can't fix two unknowns. What settles it is that both springs squash **by the same amount**, and the stiffer one pushes back harder. Every deformable-body problem combines three facts in this way: *forces balance*, *pieces fit together*, and *force relates to stretch*.

**2. Why it matters.** This is the backbone of the whole course. Ch. 4 (stress/strain), Ch. 5 (Hooke's law) and Ch. 6 (torsion) all re-run these three steps with more refined ingredients.

**3. Formal treatment (Crandall eq. 2.1, slides):**
1. **Study of forces and equilibrium requirements**
2. **Study of deformation and conditions of geometric fit (compatibility)**
3. **Force–deformation relation** (material law)

For a statically determinate problem, step 1 alone gives the forces, and steps 2 and 3 are needed only for displacements. For an **indeterminate** problem you need all three at the same time.

**4. Derivation — two coaxial springs (Crandall Example 2.1, slides).** A piston carries $F$ and sits on two coaxial springs $k_A$ and $k_B$.
- Step 1, equilibrium of the piston: $F = F_A + F_B$ … (1)
- Step 2, geometric fit: the piston moves both springs equally, $\delta_A=\delta_B=\delta$ … (2)
- Step 3, force–deflection: $F_A = k_A\delta_A$, $F_B = k_B\delta_B$ … (3)

Substitute (2) and (3) into (1): $F = (k_A+k_B)\delta$. Dividing by $F_A = k_A\delta$ gives
$$\boxed{F_A = \frac{k_A}{k_A+k_B}F,\qquad \delta = \frac{F}{k_A+k_B}}$$

**5. Picture.** Springs in **parallel** share the deflection, so their stiffnesses add: $k_{eq} = k_A+k_B$. Springs in **series** share the force, so their flexibilities add: $1/k_{eq} = 1/k_A + 1/k_B$.

**6. Limiting cases.** $k_B\to0$ gives $F_A\to F$. $k_A = k_B$ gives $F_A = F/2$. *The stiffer member attracts the load.* This rule of thumb reappears in composite bars, bolt-and-sleeve problems and indeterminate shafts.

**7. Common traps.** Writing compatibility as "forces equal" instead of "deflections equal". Mixing up the series and parallel formulas.

**8. Summary.** Equilibrium + compatibility + constitutive law. Count unknowns versus equilibrium equations to decide whether you need compatibility.

---

## Concept 2.2 — Uniaxial loading: $\delta = PL/AE$ and bars with several segments

### A. Concept explanation

**1. Intuition.** Pull a rubber band. Doubling the force doubles the stretch. Doubling the length also doubles the stretch, because each piece stretches the same amount and there are twice as many pieces. Doubling the thickness halves the stretch, because twice as much material shares the load.

**2. Why it matters.** Truss deflections, bolts, cables, columns, thermal stresses (Ch. 5). It also introduces the material constant $E$.

**3. Formal treatment (slides, Crandall §2.3).** Test bars with different $L$ and $A$ (bars 1, 2, 3 in the slide) give **different** $P$–$\delta$ curves. When re-plotted as $P/A$ versus $\delta/L$, they **collapse onto a single curve**, a property of the material alone. For a linear material its slope is the **modulus of elasticity** $E$:
$$E = \frac{P/A}{\delta/L}\quad\Longrightarrow\quad \boxed{\delta = \frac{PL}{AE}}$$
$E$ measures the stiffness of the *material*. $AE/L$ is the axial stiffness $k$ of the *bar*.

**Several segments / non-uniform:**
$$\delta = \sum_i \frac{P_iL_i}{A_iE_i}\qquad\text{or}\qquad \delta = \int_0^L \frac{P(x)\,dx}{A(x)E}$$
Here $P_i$ is the **internal** force in segment $i$, found from an FBD of a cut. Sign: tension positive (elongation), compression negative.

**4. Derivation of the internal force in a segment.** Cut through segment $i$ and keep the left part. $\sum F_x = 0$ gives $P_i$ = (sum of external forces to the left of the cut that point left). Equivalently, $P_i$ = the force needed on the cut face to hold the left part in equilibrium. Draw $P_i$ as tension (pointing away from the cut face) and let the sign tell you the answer.

**5. Picture.** Draw an **axial force diagram** (AFD): a step plot of $P(x)$. The total elongation is $\frac{1}{E}\sum (\text{AFD area})/A$.

**6. Special cases.**
- Bar hanging under its own weight: $P(x)= \gamma A x$, which gives $\delta = \gamma L^2/(2E) = WL/(2AE)$, half of what you'd get with the whole weight at the end.
- Tapered bar: integrate with $A(x)$.

**7. Common traps.**
- Using the *external* load at a point instead of the *internal* force in the segment.
- Unit slips: N, mm and N/mm² (MPa) form a consistent set. So do N, m and Pa. Never mix kN with mm² without converting.
- Forgetting that compression gives a negative $\delta$.

**8. Summary box**
$$\delta = \sum \frac{P_iL_i}{A_iE_i},\quad k_{bar} = \frac{AE}{L},\quad 1\ \text{MPa} = 1\ \text{N/mm}^2,\quad 1\ \text{GPa} = 10^3\ \text{N/mm}^2$$

### B. Solved questions

#### Q1 (Slides Ch2) — Brass bar with four axial forces *(easy)*
**Given:** $A = 1000$ mm², $E = 1.05\times10^5$ N/mm². Lengths $L_{AB} = 600$ mm, $L_{BC} = 1000$ mm, $L_{CD} = 1200$ mm. Loads: 50 kN ← at A, 80 kN → at B, 40 kN ← at C, 10 kN → at D. **Find:** the total elongation.

**Check equilibrium:** $-50+80-40+10=0$ ✓.
**Internal forces (cut each segment, look left):**
- AB: the left part has 50 kN ←, so the cut face needs 50 kN →, which is **tension**. $P_{AB} = +50$ kN
- BC: $-50+80 = +30$ kN → to the left of the cut, so the cut face needs 30 kN ←, which is **compression**. $P_{BC} = -30$ kN
- CD: $-50+80-40 = -10$ ←, so $P_{CD} = +10$ kN (T). Check: this equals the 10 kN pulling at D ✓

$$\delta = \frac{1}{AE}\left[50(600) - 30(1000) + 10(1200)\right]\times10^3 = \frac{12\times10^6}{1000\times1.05\times10^5}$$
$$\boxed{\delta = 0.114\ \text{mm (extension)}}$$
⚠️ **The slide states 0.2857 mm.** That equals the AB contribution alone ($30\times10^6/1.05\times10^8$). With the loads as drawn, the BC shortening cancels it and only CD's 12 kN·m remains. Ask your instructor if your copy of the figure differs. Otherwise trust 0.114 mm.
**Takeaway:** examiners award most of the marks for the AFD. Draw it.

---

#### Q2 (Slides Ch2) — Stepped member ABCD, find $P_2$ *(easy)*
**Given:** $P_1 = 45$ kN ← at A, $P_2$ → at B, $P_3 = 450$ kN ← at C, $P_4 = 130$ kN → at D. $A_{AB}=625$ mm² ($L=1200$ mm), $A_{BC}=2500$ mm² ($L=600$ mm), $A_{CD}=1250$ mm² ($L=900$ mm). $E = 2.1\times10^5$ MPa.

- Equilibrium: $-45+P_2-450+130 = 0 \Rightarrow \boxed{P_2 = 365\ \text{kN}}$
- Internal forces: $P_{AB} = +45$ (T), $P_{BC} = 45-365 = -320$ (C), $P_{CD} = +130$ (T)

$$\delta = \frac{1}{2.1\times10^5}\left[\frac{45000(1200)}{625} - \frac{320000(600)}{2500} + \frac{130000(900)}{1250}\right] = \frac{86400-76800+93600}{2.1\times10^5}$$
$$\boxed{\delta = 0.491\ \text{mm (extension)}}$$
(The slide writes "0.4903 m". That is a units typo for mm, and a rounding difference.)

---

#### Q3 (Slides Ch2, Gere example) — Vertical bar with a side arm *(medium)*
**Given:** vertical bar ABC hanging from A. AB: $L_1 = 0.5$ m, $A_1 = 160$ mm². BC: $L_2 = 0.8$ m, $A_2 = 100$ mm². $P_1 = 10$ kN ↓ at C. Horizontal arm BDE is pinned to the bar at B, supported on a pin at D, with $a=b$, and $P_2 = 26$ kN ↓ at E. $E = 200$ GPa. **Find:** $\delta_C$.

**FBD of arm BDE:** take moments about D. $P_2(b) = F_B(a)$, so $F_B = 26$ kN. The arm is pushed down at B, so it pushes **up** on the bar with 26 kN.
**Internal forces in bar:** BC: $+10$ kN (T). AB: $10 - 26 = -16$ kN (C).
$$\delta_C = \frac{10000(800)}{100(200{,}000)} + \frac{-16000(500)}{160(200{,}000)} = 0.400 - 0.250 \Rightarrow \boxed{\delta_C = 0.150\ \text{mm}\ \downarrow}$$
**Takeaway:** a lever arm can turn a downward load into an upward push on the main bar. Always draw the arm's FBD separately.

---

#### Q4 (Slides Ch2, Beer) — Rigid bar on two links: deflections of B, D, E *(medium)*
**Given:** rigid bar BDE, with B at 0, D at 0.2 m, E at 0.6 m. 30 kN ↓ at E. Link AB is aluminium ($E = 70$ GPa, $A = 500$ mm², $L = 0.3$ m). Link CD is steel ($E = 200$ GPa, $A=600$ mm², $L = 0.4$ m). Both links are vertical, attached above the bar.

**Statics:** $\sum M_D$: $F_B(0.2) = 30(0.4) \Rightarrow F_{AB} = 60$ kN. The bar needs a downward force at B, so link AB **pushes** it: **compression**. $\sum F_y$: $F_{CD} = 90$ kN (**tension**).

**Deformations:**
$$\delta_{AB} = \frac{60000(300)}{500(70000)} = 0.514\ \text{mm (shortens} \Rightarrow B\ \text{moves up)}$$
$$\delta_{CD} = \frac{90000(400)}{600(200000)} = 0.300\ \text{mm (lengthens} \Rightarrow D\ \text{moves down)}$$

**Geometry (similar triangles):** B goes up 0.514 and D goes down 0.300. The bar pivots about point H between B and D, at $x_H = 200\cdot\frac{0.514}{0.514+0.300} = 126.3$ mm from B.
$$\delta_E = 0.300\cdot\frac{600-126.3}{200-126.3} \Rightarrow \boxed{\delta_B=0.514\uparrow,\ \delta_D=0.300\downarrow,\ \delta_E = 1.93\ \text{mm}\downarrow}$$

---

#### PYQs on this concept
**PYQ 2014-15 Compre A Q8** — A solid bar of diameter $D$ and a hollow bar ($D_o = D$, $D_i = D/2$) carry the same load $W$. Ratio of stresses (solid : hollow)?
$A_{solid} = \tfrac{\pi}{4}D^2$ and $A_{hollow} = \tfrac{\pi}{4}(D^2 - D^2/4) = \tfrac34\cdot\tfrac{\pi}{4}D^2$.
$$\frac{\sigma_s}{\sigma_h} = \frac{A_h}{A_s} \Rightarrow \boxed{0.75}$$

---

## Concept 2.3 — Statically indeterminate bars (superposition)

### A. Concept explanation

**1. Intuition.** A bar wedged tightly between two walls with a load in the middle. Both walls push, but statics gives one equation for two reactions. The extra fact is that **the bar's total length can't change**. The walls don't move.

**2. Why it matters.** Most real structures are indeterminate: bolted joints, composite columns, fixed–fixed shafts (Ch. 6), thermal stresses (Ch. 5).

**3. Formal treatment (slides).** *Indeterminate:* reactions or internal forces can't be found from statics alone. **Method of superposition / redundant force:**
1. Pick a redundant reaction (say $R_B$) and **release** that support.
2. Find the displacement at B due to the applied loads alone, $\delta_L$.
3. Find the displacement at B due to $R_B$ alone, $\delta_R$.
4. Compatibility: $\delta = \delta_L + \delta_R = 0$ (the support doesn't move).
5. Solve for $R_B$, then get the other reactions from statics.

This works because of **linearity**: the effects of loads add.

**4. Derivation (general bar fixed at both ends, load $P$ at distance $a$ from A, total $L$, uniform $AE$):**
- Release B. Under $P$, segment $a$ stretches and $b=L-a$ carries nothing. So $\delta_L = Pa/AE$ (B moves down).
- $R_B$ alone (upward) stretches the whole bar upward by $\delta_R = -R_BL/AE$.
- Compatibility: $Pa - R_BL = 0$, so $R_B = Pa/L$ and $R_A = Pb/L$.

*This is the same split as for a simply supported beam:* the support **nearer** the load carries more. Since $R_A = Pb/L$, a small $a$ makes $R_A$ close to $P$.

**5. Picture.** A "release diagram" with three sketches, as on the slide: (a) the actual bar = (b) the bar with B released under the loads + (c) the bar under $R_B$ only.

**6. Special case.** With different areas in different segments, use $\delta = \sum PL/AE$ in each step.

**7. Traps.** Sign of $\delta_R$ (it acts against $\delta_L$). Forgetting that segments beyond the last load carry zero force in the released structure.

**8. Summary.** $\delta_L + \delta_R = 0$. Redundant first, then statics.

### B. Solved questions

#### Q5 (Slides Ch2, Beer Ex. 2.04) — Steel bar fixed at both ends *(medium)*
**Given:** vertical bar, A on top, B at the bottom, both fixed. Segments from the top, each 150 mm: AD and DC with $A=250$ mm², CK and KB with $A=400$ mm². Loads: 300 kN ↓ at D, 600 kN ↓ at K. $E = 200$ GPa. **Find:** $R_A$, $R_B$.

**Release B.** Internal forces from the loads only: AD = 900 kN, DC = 600, CK = 600, KB = 0 (all tension).
$$\delta_L = \frac{1}{E}\left[\frac{900e3(150)}{250}+\frac{600e3(150)}{250}+\frac{600e3(150)}{400}+0\right] = \frac{1.125\times10^6}{E}\ \text{(B moves down)}$$
**$R_B$ alone (upward):** compresses the whole bar.
$$\delta_R = -\frac{R_B}{E}\left[\frac{300}{250}+\frac{300}{400}\right] = -\frac{1.95R_B}{E}$$
**Compatibility:** $1.125\times10^6 - 1.95R_B = 0$
$$\boxed{R_B = 577\ \text{kN}\uparrow,\qquad R_A = 900-577 = 323\ \text{kN}\uparrow}$$
**Check:** the lower half is stiffer (larger area) and closer to the big load, so $R_B > R_A$ ✓.

---

#### Q6 (Crandall Prob 2.24, Slides) — Bolt and sleeve, quarter turn *(medium)*
**Given:** bolt area 1 in², sleeve area 0.6 in², both steel ($E=30\times10^6$ psi). Length 6 in. 16 threads/in. The nut is turned an extra 90° after snug. **Find:** the bolt tension.

- **Equilibrium:** bolt tension $F$ = sleeve compression $F$.
- **Geometric fit:** the nut advances $\Delta = \frac{1}{4}\cdot\frac{1}{16} = \frac{1}{64}$ in. That gap is taken up by the bolt stretching plus the sleeve shortening: $\delta_b + \delta_s = \Delta$.
- **Force–deformation:** $\dfrac{FL}{A_bE} + \dfrac{FL}{A_sE} = \Delta$

$$F = \frac{\Delta E}{L\left(\frac{1}{A_b}+\frac{1}{A_s}\right)} = \frac{(1/64)(30\times10^6)}{6(1 + 1.667)} \Rightarrow \boxed{F \approx 29{,}300\ \text{lb}}$$
**Check:** bolt stress 29.3 ksi and sleeve stress 48.8 ksi. These are high but plausible for steel. The thinner sleeve is more highly stressed.
**Takeaway:** this is the **series** spring case. Same force, deformations add.

---

## Concept 2.4 — Displacement diagrams for pin-jointed structures

### A. Concept explanation

**1. Intuition.** Take two bars pinned together at B, with their other ends fixed to a wall. Load B and each bar changes length a little. B must end up where both bars, with their new lengths, can still reach it. For *small* deformations, each circle arc of possible positions can be replaced by a straight line **perpendicular** to the bar.

**2. Why it matters.** Gives joint deflections for trusses and links. These are often checked against Castigliano answers (Concept 2.5) and used in PYQs.

**3. Formal treatment (Williot diagram, small displacements).** A joint displacement $\mathbf u = (u, v)$ changes the length of a bar with unit vector $\mathbf e$ (pointing from the fixed end to the joint) by
$$\boxed{\delta_{bar} = \mathbf u\cdot\mathbf e}$$
That is, *only the displacement component along the bar changes its length*. Write one equation per bar, then solve for $u$ and $v$.

**4. Derivation.** The new length is $|\mathbf L + \mathbf u| = \sqrt{L^2 + 2\mathbf L\cdot\mathbf u + u^2} \approx L + \mathbf e\cdot\mathbf u$, dropping $u^2$ (small). ∎

**5. Graphical construction.** From the fixed end, lay off each bar's $\delta$ along the bar. At the tip, draw a line perpendicular to the bar. The two perpendiculars intersect at the displaced joint.

**6. Special cases.**
- **Two-bar bracket** (AB horizontal, BC inclined at θ to AB, load $P$ down at B): $F_{AB} = P\cot\theta$ (T) and $F_{BC} = P\csc\theta$ (C). Then $u = \delta_{AB}$ (to the right) and $v = (\delta_{BC} + u\cos\theta)/\sin\theta$ (downward), where $\delta_{BC}$ is the shortening.
- **Symmetric V** (two equal bars at ±β from the vertical, load $P$ down): $F = \dfrac{P}{2\cos\beta}$ and $\boxed{\delta_B = \dfrac{PL}{2AE\cos^2\beta}}$.

**7. Traps.** Forgetting that a *shortening* bar pulls the joint toward its support. Adding bar elongations as if they were displacements.

### B. Solved questions

#### Q7 (Slides Ch2) — Displacement of D: rod + beam bracket *(medium)*
**Given:** wall. Horizontal steel beam CD, $L=3$ m, $A=3200$ mm². Steel rod BD at 45°, $A=491$ mm², with B 3 m above C. $E = 205$ GPa. 20 kN ↓ at D. **Find:** the displacement of D.

**Forces (joint D):** $F_{BD}\sin45^\circ = 20 \Rightarrow F_{BD} = 28.28$ kN (T) and $F_{CD} = 20$ kN (C).
**Changes in length:**
$$\delta_{BD} = \frac{28284(4243)}{491(205000)} = 1.192\ \text{mm (lengthens)},\qquad \delta_{CD} = \frac{20000(3000)}{3200(205000)} = 0.0915\ \text{mm (shortens)}$$
**Compatibility** (u to the right, away from the wall, and v downward):
- CD: $u = -0.0915$ mm, so D moves 0.0915 mm toward the wall.
- BD, with unit vector $(0.707, -0.707)$ from B to D: $0.707u + 0.707v = 1.192 \Rightarrow v = 1.686 + 0.0915$

$$\boxed{v_D = 1.78\ \text{mm}\downarrow,\qquad u_D = 0.092\ \text{mm toward wall}}$$
**Check with Castigliano:** see Q10 below, which gives the same 1.777 mm ✓.

---

#### Q8 (Crandall Prob 2.6, Slides) — Stiff member on three bars *(hard)*
**Given:** stiff horizontal member AB. A at $x=0$, E at $x=12$ ft, B at $x=18$ ft. 5000 lb at A. Vertical bar ED (6 ft, 2 in²) down to D. Vertical bar BC (6 ft, 1 in²) down to C. Diagonal bar BD (from D up to B, at 45°, 1.5 in²). $E=30\times10^6$ psi. **Find:** (a) the force in BD, (b) the horizontal and vertical movement of A.

**(a) Statics of AB.** ED and BC are vertical and the load is vertical. Only BD has a horizontal component, so $\sum F_x=0$ gives
$$\boxed{F_{BD} = 0}$$
$\sum M_B$: $5000(18) = F_{ED}(6) \Rightarrow F_{ED} = 15{,}000$ lb. ED pushes up on AB, so it is in **compression**. $\sum F_y$: BC pulls B down with 10,000 lb, so it is in **tension**.

**Deformations:** $\delta_{ED} = \frac{15000(72)}{2(30\times10^6)} = 0.018$ in (shortens, so E moves **down** 0.018 in). $\delta_{BC} = \frac{10000(72)}{1(30\times10^6)}=0.024$ in (lengthens, so B moves **up** 0.024 in). $\delta_{BD}=0$.

**Fit at B.** BD has zero length change, with unit vector $(0.707, 0.707)$ from D to B: $0.707u_B + 0.707(0.024) = 0 \Rightarrow u_B = -0.024$ in (to the left).
**Rigid AB.** Every point has the same horizontal displacement, and the vertical displacement varies linearly: slope $=\frac{0.024-(-0.018)}{72} = 5.83\times10^{-4}$.
$v_A = -0.018 - 144(5.83\times10^{-4}) = -0.102$ in.
$$\boxed{A\ \text{moves}\ 0.024\ \text{in to the left and}\ 0.102\ \text{in down}}$$
**Takeaway:** a zero-force member can still **constrain** displacement. That is why Crandall asks for both parts.

---

## Concept 2.5 — Strain energy and Castigliano's theorem

### A. Concept explanation

**1. Intuition.** Stretching a spring takes work. That work is stored like charge in a battery. If you know how the stored energy depends on each load, the derivative tells you how far that load's point moves. A large derivative means a small increase in load stores a lot of energy, which means a big movement.

**2. Why it matters.** It is the fastest route to deflections of trusses, curved members and frames, and it works even where no load is applied (using a fictitious load). PYQs: 2014 Test-1 Q2 (truss) and 2019-20 Q3(b) (curved beam).

**3. Formal treatment (slides, Crandall §2.6).**
*Work done by a slowly applied load:* $dU = P\,dx$, so $U = \int_0^{x_1}P\,dx$, the area under the $P$–$x$ curve.
*Linear elastic:* $P = kx$, so $U = \tfrac12 kx_1^2 = \tfrac12 P_1x_1$.
*Axial bar:* $x_1 = P_1L/AE$, so
$$\boxed{U = \frac{P^2L}{2AE}}\qquad\text{(for a structure, } U = \sum \frac{F_i^2L_i}{2A_iE_i}\text{)}$$
*Castigliano's theorem:* for a linear elastic system with small displacements, the displacement at load $F_i$, **in the direction of $F_i$**, is
$$\boxed{\delta_i = \frac{\partial U}{\partial F_i}}$$
*Fictitious load (slides):* to find a deflection where no load acts, add a dummy load $Q$ there in the desired direction, compute $\partial U/\partial Q$, then set $Q=0$.

**4. Derivation (sketch).** For a linear system, $U = \tfrac12\sum P_j\delta_j$ and each $\delta_j = \sum_k c_{jk}P_k$, so $U$ is a quadratic form $\tfrac12\sum\sum c_{jk}P_jP_k$, with $c_{jk}=c_{kj}$ (Maxwell reciprocity). Then $\partial U/\partial P_i = \sum_k c_{ik}P_k = \delta_i$. ∎

*Working formula for trusses* (differentiate before squaring, which saves algebra):
$$\delta_i = \sum_{\text{members}} F_j\,\frac{\partial F_j}{\partial P_i}\,\frac{L_j}{A_jE_j}$$
*For beams and curved members* (bending energy; the bending formula comes in Ch. 7):
$$U = \int \frac{M^2}{2EI}ds + \int\frac{N^2}{2AE}ds \;\Rightarrow\; \delta_i = \int \frac{M}{EI}\frac{\partial M}{\partial P_i}ds + \int\frac{N}{AE}\frac{\partial N}{\partial P_i}ds$$

**5. Picture.** $U$ is the triangle under the linear $P$–δ line. The "complementary" triangle above the line is equal for linear materials, and that equality is why the theorem holds.

**6. Special cases.**
- A member whose force doesn't depend on $Q$ ($\partial F/\partial Q=0$) contributes nothing to that deflection.
- To get a rotation, use a dummy couple: $\theta = \partial U/\partial C$.

**7. Common traps.**
- Using $\partial U/\partial P$ when $P$ is applied to *two* points. The result is then the *sum* of those displacements. Give each load its own symbol.
- Forgetting the sign: a negative result means the displacement is opposite to the assumed load direction.
- Setting $Q=0$ **before** differentiating.

**8. Summary box**
| Item | Formula |
|---|---|
| Bar energy | $U = P^2L/2AE$ |
| Castigliano | $\delta_i = \partial U/\partial F_i$ |
| Truss form | $\delta = \sum F\,(\partial F/\partial P)\,L/AE$ |
| Beam form | $\delta = \int M(\partial M/\partial P)\,ds/EI$ |

### B. Solved questions

#### Q9 (Slides Ch2) — Truss, find P to move roller C by 0.2 mm *(medium)*
**Given:** A pin, C roller, $AC = 1.4$ m. Apex B is 0.8 m above, at 0.8 m from A, so $AB = 1.131$ m and $BC = 1.0$ m. Each $A = 400$ mm², $E = 200$ GPa. $P$ ↓ at B. Roller C must move right by 0.2 mm.

**Add a fictitious Q (→) at C.** Joint C: $\sum F_y$ gives $F_{BC} = -0.714P$, with no Q. $\sum F_x$ gives $F_{AC} = 0.429P + Q$. Joint A: $F_{AB} = -0.606P$, with no Q.
Only AC depends on Q, with $\partial F_{AC}/\partial Q = 1$:
$$\delta_C = \frac{F_{AC}(1)L_{AC}}{AE}\Big|_{Q=0} = \frac{0.4286P(1400)}{400(200000)} = 0.2 \Rightarrow \boxed{P = 26.7\ \text{kN}}$$
**Check:** C slides along AC (A is pinned), so its motion **is** the elongation of AC. ✓

---

#### Q10 (Slides Ch2) — Rod–beam bracket by Castigliano *(easy, check of Q7)*
$F_{BD}=\sqrt2P$ (T) and $F_{CD}=-P$ (C):
$$\delta_v = \frac{\sqrt2P\cdot\sqrt2\cdot4243}{491(205000)} + \frac{(-P)(-1)\cdot3000}{3200(205000)} = 1.686+0.0915 \Rightarrow \boxed{1.78\ \text{mm}\ \downarrow}\ ✓$$

---

#### Q11 (PYQ 2014-15 Test-1 Q2) — Two-bar bracket, H and V deflection by Castigliano only *(medium, 20 marks)*
**Given:** AB horizontal, 6 m. BC from C (on the wall below A) to B, 7.5 m, so $AC = 4.5$ m. 20 kN ↓ at B. $E = 200$ GPa, $A = 800$ mm² each.

**Forces (let the vertical load be $P$ and add a fictitious horizontal $Q$ → at B).** $\sin\theta = 4.5/7.5 = 0.6$ and $\cos\theta = 0.8$.
- $\sum F_y$ at B: $F_{BC} = -\dfrac{P}{0.6} = -1.667P$ (C). Independent of Q.
- $\sum F_x$ at B: $F_{AB} = Q + 0.8(1.667P) = Q + 1.333P$ (T).

**Vertical deflection:**
$$\delta_v = \frac{1}{AE}\left[F_{AB}\frac{\partial F_{AB}}{\partial P}L_{AB} + F_{BC}\frac{\partial F_{BC}}{\partial P}L_{BC}\right] = \frac{26667(1.333)(6000) + 33333(1.667)(7500)}{800(200000)}$$
$$\boxed{\delta_v = \frac{6.30\times10^8}{1.6\times10^8} = 3.94\ \text{mm}\ \downarrow}$$
**Horizontal deflection ($Q\to0$):**
$$\delta_h = \frac{F_{AB}(1)L_{AB}}{AE} = \frac{26667(6000)}{1.6\times10^8} \Rightarrow \boxed{\delta_h = 1.00\ \text{mm}\ \rightarrow}$$
**Check by displacement diagram:** $u = \delta_{AB} = 1.00$ mm. BC shortens by $33333(7500)/1.6\times10^8 = 1.5625$ mm. $v = (1.5625 + 1.00(0.8))/0.6 = 3.94$ mm ✓.
**Takeaway:** the paper said "Castigliano only", so a displacement diagram gets no marks there even though it gives the right number. Use it only as your private check.

---

#### Q12 (PYQ 2019-20 Compre A Q3(b)) — Curved cantilever, vertical deflection by Castigliano *(hard)*
**Given:** quarter-circle cantilever of radius $R$, fixed at A ($\theta=0$, at the base), free at B ($\theta = 90^\circ$, at the top). Vertical load $P$ ↓ at B. Neglect shear energy. **Find:** $\delta_{B,v}$.

**Internal forces at angle θ** (from Ch. 3; see Ch. 3 Q12): $M = PR\cos\theta$, $N = P\cos\theta$ (compression), $V = P\sin\theta$. Also $ds = R\,d\theta$.
$$\delta_B = \int_0^{\pi/2}\frac{M}{EI}\frac{\partial M}{\partial P}R\,d\theta + \int_0^{\pi/2}\frac{N}{AE}\frac{\partial N}{\partial P}R\,d\theta = \frac{PR^3}{EI}\int_0^{\pi/2}\cos^2\theta\,d\theta + \frac{PR}{AE}\int_0^{\pi/2}\cos^2\theta\,d\theta$$
Since $\int_0^{\pi/2}\cos^2\theta\,d\theta = \pi/4$:
$$\boxed{\delta_{B,v} = \frac{\pi PR^3}{4EI} + \frac{\pi PR}{4AE}}$$
**Check:** the ratio of axial to bending term is $I/(AR^2) = (d/4R)^2$, which is tiny for a slender member. That is why the axial term is often dropped too, but the question asked for it in terms of $A$ and $I$, so keep both.

---

#### Q13 (Crandall Prob 2.7, Slides) — Railroad bridge truss: how far does roller R move? *(hard)*
**Given:** Warren truss with 60° triangles and bottom panels of 4.6 m (span 13.8 m). All members have $A = 3250$ mm² and $E = 200$ GPa (steel). Bottom-joint loads: 270 kN at A (on the pin), 180 kN, 270 kN, 360 kN at R (on the roller).

**Idea:** A is pinned and R rolls horizontally, so R's movement equals the total elongation of the bottom chord. Loads sitting directly on supports go straight into the reactions. Only 180 and 270 kN create member forces.
Net reactions from those two loads: $R_R' = (180\times4.6 + 270\times9.2)/13.8 = 240$ kN and $R_A' = 210$ kN. Height $h = 2.3\tan60^\circ = 3.984$ m.

Bottom chord forces (method of sections, moments about the top joints):
- $F_1 = 210(2.3)/3.984 = 121.2$ kN (T)
- $F_2 = [210(6.9) - 180(2.3)]/3.984 = 259.8$ kN (T)
- $F_3 = 240(2.3)/3.984 = 138.6$ kN (T)

$$\delta_R = \frac{(121.2+259.8+138.6)\times10^3(4.6)}{3250\times10^{-6}(200\times10^9)} \Rightarrow \boxed{\delta_R \approx 3.68\ \text{mm (to the right)}}$$
**Check:** a full truss solve gives the same bottom-chord forces ✓.
**Takeaway:** "how far does the roller move" is a sum of member elongations along one line. No energy method is needed.

---

## Concept 2.6 — Beams/levers on springs and thin rings (extra slide problems)

#### Q14 (Crandall Prob 2.1, Slides) — Diving board on a spring *(easy)*
**Given:** board hinged at one end, spring ($k=35$ kN/m) 1.5 m from the hinge, person (600 N) at the far end, 1.35 m beyond the spring (2.85 m from the hinge). **Find:** spring deflection. Does it change if the board is made very rigid?

$$\sum M_{hinge}: F_s(1.5) = 600(2.85) \Rightarrow F_s = 1140\ \text{N},\qquad \boxed{\delta_s = \frac{1140}{35000} = 32.6\ \text{mm}}$$
**No**, the spring deflection is set by statics alone (the problem is determinate), so board stiffness doesn't matter. The **tip** deflection does change: it is $32.6(2.85/1.5) = 61.9$ mm for a rigid board, plus extra bending for a flexible one.

---

#### Q15 (Crandall Prob 2.19, Slides) — Where to put P for system stiffness $\frac{20}{9}k$ *(medium)*
**Given:** stiff beam hinged at its left end, springs $k$ at $a$ and $2a$, force $P$ at distance $c$.
**Rigid rotation** θ: spring deflections are $a\theta$ and $2a\theta$.
- Equilibrium about the hinge: $Pc = k(a\theta)a + k(2a\theta)(2a) = 5ka^2\theta$
- Deflection under P: $\delta_P = c\theta$

$$\frac{P}{\delta_P} = \frac{5ka^2}{c^2} = \frac{20}{9}k \Rightarrow \boxed{c = \tfrac32 a}$$
**Check:** at $c = 2a$, stiffness $= 5k/4$. Moving the load inward makes the system stiffer ✓.

---

#### Q16 (Slides Ch2, Crandall Ex.) — Thin ring under internal pressure *(easy; PYQ-type)*
**Given:** ring of mean radius $r$, width $b$, thickness $t \ll r$, internal pressure $p$.
**FBD of half the ring:** the pressure on element $r\,d\theta$ (width $b$) gives a vertical component $p\,b\,r\sin\theta\,d\theta$.
$$2F_T = \int_0^\pi pbr\sin\theta\,d\theta = 2pbr \Rightarrow \boxed{F_T = pbr,\quad \sigma_\theta = \frac{F_T}{bt} = \frac{pr}{t}}$$
**Deformation:** the hoop strain $\epsilon = \sigma/E$ stretches the circumference $2\pi r$ by $2\pi r\epsilon$. The radius grows by
$$\boxed{\delta_R = r\epsilon = \frac{pr^2}{Et}}$$

**PYQ 2014-15 Compre A Q11:** inner diameter 500 mm, width 10 mm, $t = 5$ mm, $p = 1.5$ MPa.
$\sigma = pr/t = 1.5(250)/5 = \boxed{75\ \text{MPa}}$. Using the mean radius 252.5 mm gives 75.75 MPa. Either is accepted at this level.

---

## Chapter 2 — Formula and convention sheet

| Topic | Formula / rule |
|---|---|
| Three steps | Equilibrium → geometric fit → force–deformation |
| Axial deformation | $\delta = \sum P_iL_i/(A_iE_i)$, with $P_i$ = **internal** force (T +) |
| Bar stiffness | $k = AE/L$; parallel springs add $k$, series add $1/k$ |
| Load sharing | $F_A = Fk_A/(k_A+k_B)$, so the stiffer member carries more |
| Indeterminate (superposition) | Release redundant: $\delta_L + \delta_R = 0$ |
| Displacement diagram | $\delta_{bar} = \mathbf u\cdot\mathbf e_{bar}$ (small displacements) |
| Two-bar bracket | $F_{AB}=P\cot\theta$, $F_{BC}=P\csc\theta$ |
| Symmetric V | $\delta = PL/(2AE\cos^2\beta)$ |
| Strain energy | $U = P^2L/2AE$; beams $\int M^2ds/2EI$ |
| Castigliano | $\delta_i = \partial U/\partial F_i$; truss: $\sum F(\partial F/\partial P)L/AE$; dummy load → set 0 *after* differentiating |
| Thin ring | $\sigma = pr/t$, $\delta_R = pr^2/(Et)$ |
| Units | N, mm, MPa (N/mm²) is a consistent set; GPa = $10^3$ MPa |

**Other Crandall Ch. 2 problems worth practising:** 2.2–2.5 (determinate links), 2.8–2.15 (indeterminate bars, composite members), 2.25+ (energy).
