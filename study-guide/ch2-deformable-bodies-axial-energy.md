# Chapter 2 — Introduction to Mechanics of Deformable Bodies
### Axial deformation, springs, statically indeterminate bars, displacement diagrams, strain energy and Castigliano's theorem, rings and belts

**Sources used:** Slides "Chapter 2" (Dr. Sharad Shrivastava); Crandall Ch. 2 (§2.1–2.6; Examples 2.1, 2.3, 2.5; Probs 2.1, 2.6, 2.7, 2.10, 2.11, 2.12, 2.14, 2.17, 2.18, 2.19, 2.20, 2.24, 2.29, 2.31, 2.32, 2.45); PYQs 2014-15 (Test-1 Q2; Compre A Q8, Q11) and 2019-20 (Compre A Q3(b)).

**Layout.** Part A (eight items) for each concept, then Part B: slides → Crandall → PYQs, easy → hard. Each solution follows *Problem · Given/Find · Approach · FBD · Steps · Answer · Check · Takeaway*.

---

## Concept 2.1 — The three-step method for deformable bodies; springs in parallel and series

### A. Concept explanation

**1. Intuition.** Press down on a mattress resting on two different springs side by side. You can't say how much each spring carries just by balancing forces, because one equation can't fix two unknowns. What settles it is that both springs squash **by the same amount**, and the stiffer one pushes back harder. Every deformable-body problem combines three facts in this way: forces balance, pieces still fit together after deforming, and each piece's force is tied to its stretch by its stiffness.

**2. Why it matters.** This is the backbone of the whole course. Ch. 4 replaces "force" by stress and "stretch" by strain. Ch. 5 supplies the material law (Hooke's law, thermal strain). Ch. 6 repeats the three steps for twisting. Every indeterminate PYQ (fixed–fixed shafts, beam plus column, bolts in sleeves) is solved this way.

**3. Formal treatment (Crandall eq. 2.1; slides).** To analyse a deformable body:
1. **Study of forces and equilibrium requirements.**
2. **Study of deformation and conditions of geometric fit (compatibility).**
3. **Force–deformation relation** (the material/component law, e.g. $F = k\delta$ or $\delta = FL/AE$).

*Linear spring:* a force proportional to deflection, $F = k\delta$, where k (N/m or N/mm) is the **spring constant**: the force needed for a unit deflection. Its reciprocal $1/k$ is the **flexibility** (deflection per unit force).

*Statically determinate problem:* step 1 alone gives every force. Steps 2–3 are needed only for displacements. *Indeterminate problem:* more unknown forces than equilibrium equations, so all three steps are needed **simultaneously**.

**4. Derivations.**

*(a) Two coaxial springs under a piston (Crandall Example 2.1, slides).* A piston carrying F compresses springs $k_A$ and $k_B$ side by side.
- Step 1, equilibrium of the piston: $F = F_A + F_B$ … (1). The slide notes that the spring equilibrium and $\sum M$ are automatically satisfied.
- Step 2, geometric fit: the rigid piston moves both springs equally, $\delta_A = \delta_B = \delta$ … (2).
- Step 3, force–deflection: $F_A = k_A\delta_A$, $F_B = k_B\delta_B$ … (3).

Substituting (2) and (3) into (1): $F = (k_A + k_B)\delta$ … (4). Dividing (4) by $F_A = k_A\delta$:
$$\boxed{F_A = \frac{k_A}{k_A+k_B}F,\qquad \delta = \frac{F}{k_A+k_B}}$$

*(b) Springs in series (Crandall Prob 2.18).* The same force F passes through both springs (equilibrium of each spring and of the connector), and the total deflection is the sum: $\delta = \delta_1 + \delta_2 = F/k_1 + F/k_2$. Hence
$$\boxed{\frac{1}{k_{eq}} = \frac{1}{k_1}+\frac{1}{k_2},\qquad k_{eq} = \frac{k_1k_2}{k_1+k_2}}$$

*(c) Springs in parallel:* the same δ and forces add, so $k_{eq} = k_1 + k_2$.

**5. Picture.** Parallel springs look like "‖": same δ, forces add, **stiffnesses add**. Series springs look like a chain "—o—o—": same force, deflections add, **flexibilities add**. A rigid bar supported by springs at different positions is neither. Its deflections vary linearly along the bar (Q4, Q6).

**6. Special / limiting cases.**
- $k_B \to 0$: $F_A \to F$. $k_A = k_B$: each carries F/2. *The stiffer member attracts the load.* This rule of thumb reappears in composite bars, the RC pier, the bolt and sleeve, and indeterminate shafts.
- In series, the softer spring dominates: if $k_2 \ll k_1$, then $k_{eq} \approx k_2$.

**7. Common traps.**
- Writing compatibility as "forces equal" instead of "deflections equal" (parallel), or the other way round (series).
- Mixing up the series and parallel formulas.
- For a rigid bar on springs, forgetting that the deflection at each spring is (rotation) × (its distance from the hinge).

**8. Summary box**
$$\text{equilibrium} + \text{compatibility} + \text{force–deformation};\qquad k_{par} = \sum k_i,\qquad \frac{1}{k_{ser}} = \sum\frac{1}{k_i},\qquad F_i = \frac{k_i}{\sum k}F\ \text{(parallel)}$$

### B. Solved questions

#### Q1 (Slides Ch2 / Crandall Example 2.1) — Piston on two coaxial springs *(easy)*
**Problem.** A machine part carrying a load F ends in a piston that fits into a cavity containing two coaxial springs of constants $k_A$ and $k_B$. How much of F is carried by spring A?

**Given:** F; linear springs $k_A$, $k_B$; flat spring ends (slide assumption), so each spring force acts along its axis. **Find:** $F_A$ (and the piston deflection).

**Approach.** Two unknown spring forces, one useful equilibrium equation, so the problem is indeterminate and needs all three steps.

**FBD in words.** Piston with F ↓ on top and $F_A$ ↑ and $F_B$ ↑ from the springs underneath.

**Solution.**
1. Equilibrium: $F_A + F_B = F$.
2. Geometric fit: $\delta_A = \delta_B = \delta$ (the piston is rigid and both springs start in contact).
3. Force–deformation: $F_A = k_A\delta$, $F_B = k_B\delta$.
4. Substitute: $(k_A + k_B)\delta = F$, so $\delta = F/(k_A + k_B)$ and $F_A = k_A\delta$.

$$\boxed{F_A = \frac{k_A}{k_A + k_B}F,\qquad \delta = \frac{F}{k_A+k_B}}$$

**Check.** If $k_A = k_B$, $F_A = F/2$ ✓. Dimensions: k/k is dimensionless ✓.

**Exam takeaway.** This is the template for every "two members share one load" question. **Variation:** if spring B is initially 1 mm shorter (a gap), A alone carries the load until δ = 1 mm, after which both act. That gives a "kinked" load–deflection curve (Q13).

---

#### Q2 (Slides Ch2, Q2.1 = Crandall Prob 2.1) — Diving board on a spring *(easy)*
**Problem.** A wooden diving board is hinged at one end and supported 1.5 m from the hinge by a spring of constant 35 kN/m. How much does the spring deflect when a 600 N person stands at the end of the board, 1.35 m beyond the spring? Is the spring deflection changed if the board is made very rigid?

**Given:** k = 35 kN/m at 1.5 m; W = 600 N at 2.85 m from the hinge. **Find:** $\delta_s$, and whether board stiffness matters.

**Approach.** Hinge plus one spring is statically determinate, so the spring force follows from statics alone.

**FBD in words.** Board with hinge reactions $H_x$, $H_y$ at the hinge, spring force $F_s$ ↑ at 1.5 m and 600 N ↓ at 2.85 m.

**Solution.**
1. $\sum M_{hinge} = 0$: $F_s(1.5) = 600(2.85)$, so $F_s = 1140$ N.
2. $\delta_s = F_s/k = 1140/35\,000 = 0.0326$ m.

$$\boxed{\delta_s = 32.6\ \text{mm}}$$

**No:** the spring force (hence its deflection) is fixed by statics, whatever the board's stiffness. The **tip** deflection does change. For a rigid board it is $32.6(2.85/1.5) = 61.9$ mm; a flexible board adds its own bending.

**Check.** Spring force about 2× the weight because of lever action ✓.

**Exam takeaway.** Before writing compatibility, check whether the problem is determinate; if it is, deformation never changes the forces. **Variation:** two springs under the board (Q3), which is indeterminate.

---

#### Q3 (Slides Ch2, Q2.19 = Crandall Prob 2.19) — Where to put P for system stiffness 20k/9 *(medium)*
**Problem.** A stiff beam is hinged at its left end and supported by two springs of constant k at distances a and 2a from the hinge. Where should a force P be applied so that the system's spring constant $P/\delta_P$ is $\tfrac{20}{9}k$?

**Given:** springs k at a and 2a; P at unknown distance c from the hinge. **Find:** c.

**Approach.** The rigid beam rotates by a small angle θ about the hinge. Spring deflections are $a\theta$ and $2a\theta$ (compatibility), forces follow from $F = k\delta$, and moments about the hinge give equilibrium.

**FBD in words.** Beam with hinge reactions at the hinge, spring forces $k(a\theta)$ ↑ at a and $k(2a\theta)$ ↑ at 2a, and P ↓ at c.

**Solution.**
1. Compatibility: $\delta_1 = a\theta$, $\delta_2 = 2a\theta$, $\delta_P = c\theta$.
2. Force–deflection: $F_1 = ka\theta$, $F_2 = 2ka\theta$.
3. Equilibrium about the hinge: $Pc = F_1a + F_2(2a) = ka^2\theta + 4ka^2\theta = 5ka^2\theta$.
4. System stiffness: $\dfrac{P}{\delta_P} = \dfrac{5ka^2\theta/c}{c\theta} = \dfrac{5ka^2}{c^2}$.
5. Set $\dfrac{5ka^2}{c^2} = \dfrac{20}{9}k$: $c^2 = \dfrac{9a^2}{4}$.

$$\boxed{c = \tfrac32a}$$

**Check.** At $c = 2a$ the stiffness is $5k/4$; moving the load inward ($c = 1.5a$) makes the system stiffer ($20k/9 = 2.22k$) ✓. At $c = a$ it is 5k ✓ (very stiff near the hinge).

**Exam takeaway.** For rigid bars on springs, the stiffness felt at a point depends on $1/c^2$: one factor of c comes from the lever arm for force, the other from the lever arm for displacement. **Variation:** three springs, or springs of different k.

---

#### Q4 (Crandall Prob 2.18) — Two springs in series *(easy)*
**Problem.** Two linear springs $k_1$ and $k_2$ are connected in series and loaded by F. Find the overall spring constant.

**Approach.** Series: same force, deflections add.

**Solution.**
1. Equilibrium of each spring: both carry F.
2. Deflections: $\delta_1 = F/k_1$, $\delta_2 = F/k_2$.
3. Total: $\delta = F\left(\dfrac{1}{k_1}+\dfrac{1}{k_2}\right)$, so $k = F/\delta$.

$$\boxed{k_{eq} = \frac{k_1k_2}{k_1+k_2}}$$

**Check.** $k_1 = k_2 = k$ gives k/2: two equal springs in a chain are twice as soft ✓. $k_2\to\infty$ (a rigid link) gives $k_1$ ✓.

**Exam takeaway.** A bar is a spring with $k = AE/L$. A stepped bar is springs in series, and a composite (concentric) bar is springs in parallel. **Variation:** used inside Q5.

---

#### Q5 (Crandall Prob 2.20) — Stiff bar on three springs: keep it level *(medium)*
**Problem.** A stiff horizontal bar AB of length a hangs from springs $k_1$ and $k_2$ in series at end A and from spring $k_3$ at end B. Where should a force P be applied (distance b from A) so that the bar stays horizontal? How far does it then move down?

**Given:** $k_1, k_2$ in series at A; $k_3$ at B; length a. **Find:** b and δ.

**Approach.** "Stays horizontal" is a compatibility condition: both ends move down by the same δ. Combine the series pair into one spring and use moment equilibrium.

**FBD in words.** Bar with $F_A$ ↑ at A, $F_B$ ↑ at B and P ↓ at b from A.

**Solution.**
1. Series pair at A: $k_A = \dfrac{k_1k_2}{k_1+k_2}$.
2. Level bar: $\delta_A = \delta_B = \delta$, so $F_A = k_A\delta$ and $F_B = k_3\delta$.
3. Vertical equilibrium: $F_A + F_B = P$, so $\delta = \dfrac{P}{k_A + k_3}$.
4. Moments about A: $Pb = F_B a = k_3\delta a$, so $b = \dfrac{k_3a}{k_A + k_3}$.

$$\boxed{b = \frac{k_3\,a}{\dfrac{k_1k_2}{k_1+k_2}+k_3},\qquad \delta = \frac{P}{\dfrac{k_1k_2}{k_1+k_2}+k_3}}$$

**Check.** If all three springs are equal (k): $k_A = k/2$, so $b = \dfrac{k}{1.5k}a = \tfrac23a$. P must sit nearer the stiffer end B ✓.

**Exam takeaway.** P must go through the "centre of stiffness". This is exactly how a load on a composite column must be placed so that the column shortens without bending. **Variation:** P at the middle; find the tilt of the bar.

---

## Concept 2.2 — Uniaxial loading: δ = PL/AE and bars with several segments

### A. Concept explanation

**1. Intuition.** Pull a rubber band. Doubling the force doubles the stretch. Doubling the length also doubles the stretch, because each half stretches the same amount as before. Doubling the thickness halves the stretch, because twice as much material shares the load. Stretch is proportional to force × length / (area × stiffness of the material).

**2. Why it matters.** This is the simplest force–deformation law, used in trusses, bolts, cables, columns, links, thermal stress (Ch. 5) and composite members. It also introduces the material constant E, which reappears in every chapter.

**3. Formal treatment (slides, Crandall §2.3).** Test three bars of different length and area (bars 1, 2, 3 in the slide). Their load–elongation (P–δ) curves differ. But when re-plotted as $P/A$ against $\delta/L$, they **collapse onto a single curve**, which is a property of the material alone (the slide's "slope of curve" figure). For a linear material its slope is the **modulus of elasticity** E:
$$E = \frac{P/A}{\delta/L}\quad\Longrightarrow\quad \boxed{\delta = \frac{PL}{AE}}$$
E measures the stiffness of the **material**. $k = AE/L$ measures the stiffness of the **bar**, a spring constant. The slide stresses that E "represents the stiffness of the material" and $AE/L$ that of the member.

*Several segments or non-uniform conditions:*
$$\delta = \sum_i \frac{P_iL_i}{A_iE_i}\qquad\text{or}\qquad \delta = \int_0^L \frac{P(x)\,dx}{A(x)E(x)}$$
$P_i$ is the **internal** axial force in segment i, found from an FBD of a cut. Sign: tension +, elongation +.

**4. Derivations.**

*(a) Internal force in a segment.* Cut through segment i and keep the left part. Draw the unknown internal force $P_i$ on the cut face as **tension** (pointing away from the cut). Then $\sum F_x = 0$ gives $P_i$ = −(sum of external forces on the left part, + to the right). A positive result means tension.

*(b) Bar hanging under its own weight.* A bar of specific weight γ hangs from its top. At distance x above the free end the internal force is the weight below: $P(x) = \gamma Ax$. Then
$$\delta = \int_0^L\frac{\gamma Ax}{AE}dx = \frac{\gamma L^2}{2E} = \frac{WL}{2AE}\quad(W = \gamma AL)$$
This is half what the whole weight would cause if hung at the end.

*(c) Tapered bar.* With $A(x)$ varying linearly from $A_1$ to $A_2$: $\delta = \dfrac{PL}{E}\dfrac{\ln(A_2/A_1)}{A_2 - A_1}$. It reduces to $PL/AE$ when $A_1 = A_2$.

**5. Picture.** Draw an **axial force diagram** (AFD), a step plot of P(x) along the bar. The total elongation is $\frac{1}{E}\sum(\text{AFD area}_i/A_i)$. For a rigid bar hung on rods, draw the bar's displaced position: a straight line joining the rod-end displacements.

**6. Special cases.**
- Equal and opposite end forces: P is constant and $\delta = PL/AE$.
- A segment with zero internal force does not stretch, even if loads act elsewhere.
- A rigid member on two deformable rods: the end displacements differ, so the rigid member rotates, and points beyond the rods move more (Q8).

**7. Common traps.**
- Using the **external** load at a point instead of the **internal** force in the segment.
- Units: N, mm and MPa (N/mm²) form a consistent set, as do N, m and Pa. Never mix kN with mm² and GPa without converting.
- Forgetting that compression gives a negative δ, which shortens the total.
- Applying δ = PL/AE outside the linear elastic range.

**8. Summary box**
$$\delta = \sum \frac{P_iL_i}{A_iE_i}\ (P_i\ \text{internal, T}+),\qquad k_{bar} = \frac{AE}{L},\qquad \delta_{self} = \frac{WL}{2AE},\qquad 1\ \text{MPa} = 1\ \text{N/mm}^2,\ 1\ \text{GPa} = 10^3\ \text{N/mm}^2$$

### B. Solved questions

#### Q6 (Slides Ch2) — Brass bar with four axial forces *(easy)*
**Problem.** A brass bar of area 1000 mm² carries axial forces of 50 kN ← at A, 80 kN → at B, 40 kN ← at C and 10 kN → at D. $L_{AB} = 600$ mm, $L_{BC} = 1000$ mm, $L_{CD} = 1200$ mm, $E = 1.05\times10^5$ N/mm². Find the total elongation.

**Given:** as above. **Find:** δ_total.

**Approach.** Segment-by-segment internal forces (AFD), then $\delta = \sum PL/AE$.

**FBD in words.** For each segment, cut and keep the part to the left of the cut, drawing the internal force as tension.

**Solution.**
1. *Equilibrium check:* $-50 + 80 - 40 + 10 = 0$ ✓.
2. *AB:* the left part carries 50 kN ←, so the cut face needs +50 kN → (tension): $P_{AB} = +50$ kN.
3. *BC:* external forces to the left sum to $-50 + 80 = +30$ kN →, so the cut face needs 30 kN ← (compression): $P_{BC} = -30$ kN.
4. *CD:* $-50 + 80 - 40 = -10$ kN ←, so $P_{CD} = +10$ kN (T). Check: equals the 10 kN pull at D ✓.
5. *Elongation:*
$$\delta = \frac{1}{AE}\left[50(600) - 30(1000) + 10(1200)\right]\times10^3 = \frac{(30-30+12)\times10^6}{1000\times1.05\times10^5} = \frac{12\times10^6}{1.05\times10^8}$$

$$\boxed{\delta = 0.114\ \text{mm (extension)}}$$

**Check.** AB stretches 0.286 mm, BC shortens 0.286 mm, CD stretches 0.114 mm. The first two cancel ✓.

**Exam takeaway.** ⚠ The slide states 0.2857 mm. That is AB's contribution alone. With the loads as drawn, BC's shortening cancels it, so trust 0.114 mm unless your copy of the figure differs. Most of the marks go for the AFD, so draw it. **Variation:** a different area per segment (Q7).

---

#### Q7 (Slides Ch2) — Stepped member ABCD: find $P_2$ and the total elongation *(easy)*
**Problem.** Member ABCD carries $P_1 = 45$ kN ← at A, $P_2$ → at B, $P_3 = 450$ kN ← at C and $P_4 = 130$ kN → at D. Areas: AB 625 mm² (1200 mm), BC 2500 mm² (600 mm), CD 1250 mm² (900 mm). $E = 2.1\times10^5$ MPa. Find $P_2$ for equilibrium and the total elongation.

**Approach.** Overall equilibrium for $P_2$, then the AFD, then $\sum PL/AE$ with a different A in each segment.

**Solution.**
1. *Equilibrium:* $-45 + P_2 - 450 + 130 = 0$, so $P_2 = 365$ kN.
2. *Internal forces:* $P_{AB} = +45$ kN (T); $P_{BC} = 45 - 365 = -320$ kN (C); $P_{CD} = +130$ kN (T).
3. *Elongation:*
$$\delta = \frac{1}{2.1\times10^5}\left[\frac{45\,000(1200)}{625} - \frac{320\,000(600)}{2500} + \frac{130\,000(900)}{1250}\right] = \frac{86\,400 - 76\,800 + 93\,600}{2.1\times10^5}$$

$$\boxed{P_2 = 365\ \text{kN},\qquad \delta = 0.491\ \text{mm (extension)}}$$

**Check.** The largest force (BC) is in the fattest segment, so its stress (128 MPa) is no bigger than AB's (72 MPa) or CD's (104 MPa); all are reasonable for steel ✓.

**Exam takeaway.** The slide writes "0.4903 m". That is a units typo for mm. **Variation:** "find the maximum stress", giving 128 MPa in BC (compressive).

---

#### Q8 (Slides Ch2, Gere) — Vertical bar with a side arm *(medium)*
**Problem.** A vertical steel bar ABC hangs from A. Segment AB has length $L_1 = 0.5$ m and area $A_1 = 160$ mm²; BC has $L_2 = 0.8$ m and $A_2 = 100$ mm². $P_1 = 10$ kN acts down at C. A horizontal arm BDE is pinned to the bar at B and rests on a support at D (with a = b), and carries $P_2 = 26$ kN down at E. E = 200 GPa. Find the vertical deflection of C.

**Given:** as above. **Find:** $\delta_C$.

**Approach.** First find the force the arm exerts on the bar at B (statics of the arm), then the AFD of the bar, then $\sum PL/AE$.

**FBD in words.**
- *Arm BDE:* pin force $F_B$ at B (from the bar), support reaction at D, $P_2$ ↓ at E.
- *Bar ABC:* reaction at A, $F_B$ from the arm at B (equal and opposite to the arm's), $P_1$ ↓ at C.

**Solution.**
1. *Arm, moments about D:* $P_2$ ↓ at E (distance b) tips the arm clockwise, so end B rises and the bar must hold it down. $F_{B,\text{on arm}}\,a = P_2b$ with a = b, so $F_B = 26$ kN. The bar pushes **down** on the arm; by Newton's third law the arm pushes **up** on the bar with 26 kN.
2. *Bar, internal forces:* $P_{BC} = +10$ kN (T). In AB: $10 - 26 = -16$ kN (C).
3. *Deflection of C:*
$$\delta_C = \frac{10\,000(800)}{100(200\,000)} + \frac{(-16\,000)(500)}{160(200\,000)} = 0.400 - 0.250$$

$$\boxed{\delta_C = 0.150\ \text{mm}\ \downarrow}$$

**Check.** BC stretches 0.40 mm while AB shortens 0.25 mm (its upper part is pushed up), so the net drop of C is 0.15 mm ✓.

**Exam takeaway.** A lever arm can turn a downward load into an upward push on the main bar. Always draw the arm's FBD separately. **Variation:** a = 2b gives $F_B = 13$ kN, so AB carries $10 - 13 = -3$ kN (still slightly compressed) and $\delta_C = 0.400 - 0.047 = 0.353$ mm ↓.

---

#### Q9 (Slides Ch2, Beer Sample 2.1) — Rigid bar on two links: deflections of B, D and E *(medium)*
**Problem.** The rigid bar BDE is supported by two links. Link AB is aluminium (E = 70 GPa, A = 500 mm², L = 0.3 m). Link CD is steel (E = 200 GPa, A = 600 mm², L = 0.4 m). B is at 0, D at 0.2 m and E at 0.6 m along the bar; 30 kN acts down at E. Find the deflections of B, D and E.

**Approach.** Statics for the two link forces, $\delta = FL/AE$ for each link, then similar triangles for the rigid bar.

**FBD in words.** Bar BDE with link force $F_{AB}$ at B, $F_{CD}$ at D and 30 kN ↓ at E. Both links are vertical and attached above the bar.

**Solution.**
1. *Moments about D:* $F_B(0.2) = 30(0.4)$, so $F_{AB} = 60$ kN. To balance, the force at B must act **down** on the bar, so link AB pushes: **compression**.
2. *Vertical sum:* $F_{CD} = 60 + 30 = 90$ kN ↑ on the bar: CD pulls, **tension**.
3. *Link deformations:*
$$\delta_{AB} = \frac{60\,000(300)}{500(70\,000)} = 0.514\ \text{mm}\ (\text{shortens} \Rightarrow B\ \text{moves up})$$
$$\delta_{CD} = \frac{90\,000(400)}{600(200\,000)} = 0.300\ \text{mm}\ (\text{lengthens} \Rightarrow D\ \text{moves down})$$
4. *Rigid-bar geometry.* B goes up 0.514 mm and D down 0.300 mm, so the bar pivots about a point H between them: $\dfrac{x_H}{0.514} = \dfrac{200 - x_H}{0.300}$, giving $x_H = 126.3$ mm from B.
5. *Point E* (600 mm from B): $\delta_E = 0.300\cdot\dfrac{600 - 126.3}{200 - 126.3} = 0.300(6.43) = 1.93$ mm.

$$\boxed{\delta_B = 0.514\ \text{mm}\uparrow,\quad \delta_D = 0.300\ \text{mm}\downarrow,\quad \delta_E = 1.93\ \text{mm}\downarrow}$$

**Check.** The slope of the bar is $(0.514 + 0.300)/200 = 4.07\times10^{-3}$ rad. From D to E (400 mm): $0.300 + 400(4.07\times10^{-3}) = 1.93$ ✓.

**Exam takeaway.** Points beyond the supports amplify small link deformations. **Variation:** "the maximum allowable deflection at E is 1 mm; find the maximum load".

---

#### Q10 (Crandall Prob 2.17) — Stiff member on two steel rods of different size *(medium)*
**Problem.** A very stiff horizontal member hangs from two vertical steel rods. The left rod is 2 m long with area 625 mm²; the right rod is 2.7 m long with area 1250 mm². A vertical load of 120 kN acts at B, 375 mm from the left rod and 300 mm from the right rod. Estimate the vertical deflection of B (E = 200 GPa).

**Approach.** Determinate: statics gives the rod forces. Then each rod's stretch, and linear interpolation along the rigid member.

**FBD in words.** Rigid member with $F_L$ ↑ at the left rod, $F_R$ ↑ at the right rod and 120 kN ↓ at B.

**Solution.**
1. *Rod forces* (moments about each rod): $F_L = 120\dfrac{300}{675} = 53.33$ kN and $F_R = 120\dfrac{375}{675} = 66.67$ kN.
2. *Stretches:*
$$\delta_L = \frac{53\,333(2000)}{625(200\,000)} = 0.853\ \text{mm},\qquad \delta_R = \frac{66\,667(2700)}{1250(200\,000)} = 0.720\ \text{mm}$$
3. *Interpolate to B* (375 mm from the left rod, 675 mm span): $\delta_B = 0.853 + (0.720 - 0.853)\dfrac{375}{675} = 0.853 - 0.074$.

$$\boxed{\delta_B \approx 0.78\ \text{mm}\ \downarrow}$$

**Check.** The answer lies between the two rod stretches ✓. The member tilts down toward the left.

**Exam takeaway.** "Very stiff member" means rigid: deflections vary linearly between the rods. **Variation:** "where must the load go so that the member stays level?" The rod stiffnesses are $k_L = AE/L = 62\,500$ N/mm and $k_R = 92\,590$ N/mm. Equal stretches need $F_L/F_R = k_L/k_R = 0.675$, so the load must sit at the "centre of stiffness": $675\,k_R/(k_L+k_R) = 403$ mm from the left rod.

---

#### PYQ on this concept

#### Q11 (PYQ 2014-15 Compre A Q8) — Stress ratio: solid vs hollow bar *(easy)*
**Problem.** A solid bar of diameter D carries an axial load W. The same load is applied to a hollow bar of outer diameter D and inner diameter D/2. Find the ratio of the stress in the solid bar to that in the hollow bar.

**Solution.**
1. $A_{solid} = \tfrac{\pi}{4}D^2$ and $A_{hollow} = \tfrac{\pi}{4}\left(D^2 - \tfrac{D^2}{4}\right) = \tfrac34\cdot\tfrac{\pi}{4}D^2$.
2. With the same load: $\dfrac{\sigma_s}{\sigma_h} = \dfrac{A_h}{A_s}$.

$$\boxed{\dfrac{\sigma_s}{\sigma_h} = 0.75}$$

**Exam takeaway.** A 1-mark "trap": the hollow bar has the higher stress. Ratios invert relative to areas.

---

## Concept 2.3 — Statically indeterminate axial problems

### A. Concept explanation

**1. Intuition.** Wedge a bar tightly between two walls and load it in the middle. Both walls push back, but statics gives one equation for two reactions. The extra fact you need is that **the bar's total length can't change**, because the walls don't move. More generally, whenever members are tied together, their deformations must fit, and that supplies the missing equations.

**2. Why it matters.** Most real structures are indeterminate: bolted joints, reinforced-concrete columns, composite rods, rings shrunk onto each other, fixed–fixed shafts (Ch. 6), thermal stresses (Ch. 5), beam-plus-column PYQs. "Stiffer attracts more load" lets you sanity-check every answer.

**3. Formal treatment.**

*Indeterminate (slides):* the internal forces and reactions cannot be found from statics alone.

*Method of superposition (slides, "redundant force method"):*
1. Choose a redundant reaction (say $R_B$) and **release** that support.
2. Find the displacement at B due to the applied loads alone, $\delta_L$.
3. Find the displacement at B due to $R_B$ alone, $\delta_R$ (as a function of $R_B$).
4. Compatibility: $\delta = \delta_L + \delta_R = 0$ (or equal to a known gap or settlement).
5. Solve for $R_B$, then get the remaining reactions from statics.

This works because the material and geometry are **linear**, so the effects of separate loads add.

*Direct (stiffness) method:* when several members join at a rigid plate or pin, write each member's force in terms of a common displacement, as in the piston of Q1. This is often quicker for composite members and frameworks.

**4. Derivations.**

*(a) Uniform bar fixed at both ends, load P at distance a from A (b = L − a).* Release B. Under P the segment a stretches and b carries nothing, so $\delta_L = Pa/AE$ (B moves down). $R_B$ alone, pushing up, compresses the whole bar: $\delta_R = -R_BL/AE$. Compatibility: $Pa - R_BL = 0$, giving
$$R_B = \frac{Pa}{L},\qquad R_A = \frac{Pb}{L}$$
This is the same split as a simply supported beam: the support **nearer** the load carries more.

*(b) Composite (parallel) members between rigid plates.* Members 1 and 2 must shorten equally, $\delta_1 = \delta_2$, so $P_i = \dfrac{(AE)_i}{\sum (AE)}P$ and stresses $\sigma_i = E_i\epsilon$, where $\epsilon = P/\sum(AE)$. All members have **the same strain**, and the stiffer material has the larger stress.

*(c) Three-bar framework (Crandall Prob 2.12).* An inner vertical bar (area A, length L) and two outer bars (area $A_0$) at angle θ to the vertical meet at a joint carrying F. The joint moves down by δ. The inner bar stretches δ; each outer bar stretches $\delta\cos\theta$ over length $L/\cos\theta$. Then
$$N_i = \frac{AE\delta}{L},\qquad N_o = \frac{A_0E\delta\cos^2\theta}{L},\qquad N_i + 2N_o\cos\theta = F$$
$$\Rightarrow\ \delta = \frac{FL}{E(A + 2A_0\cos^3\theta)},\qquad N_i = \frac{FA}{A + 2A_0\cos^3\theta},\qquad N_o = \frac{FA_0\cos^2\theta}{A + 2A_0\cos^3\theta}$$

**5. Picture.** Use a "release diagram" with three sketches, as on the slide: (a) the actual structure = (b) the structure with the redundant support released, under the loads + (c) the same released structure under the redundant force alone. The displacement at the released point must add up to the real value (usually zero).

**6. Special cases.**
- Different areas in different segments: use $\delta = \sum PL/AE$ in each step.
- A **gap** Δ before contact: compatibility becomes $\delta_L + \delta_R = \Delta$ once the gap closes. If the free deflection is less than Δ, the second support carries nothing.
- Pre-tension or misfit (bolt turned by a known amount, Q15): compatibility is "deformation of bolt + deformation of sleeve = misfit".

**7. Common traps.**
- Sign of $\delta_R$: it acts against $\delta_L$.
- Forgetting that segments beyond the last load carry no force in the released structure.
- In composite members, assuming equal **stress** instead of equal **strain**.
- Using statics alone and "assuming" a share of the load.

**8. Summary box**
$$\delta_L + \delta_R = 0\ (\text{or gap});\qquad \text{parallel members: } P_i = \frac{(AE)_i}{\sum(AE)}P,\ \ \epsilon\ \text{common};\qquad \text{series: same } P,\ \delta\text{'s add}$$

### B. Solved questions

#### Q12 (Slides Ch2, Beer Example 2.04) — Steel bar fixed at both ends *(medium)*
**Problem.** A vertical steel bar is fixed at A (top) and B (bottom), with a close fit before loading. From the top there are four 150 mm segments: AD and DC with area 250 mm², CK and KB with area 400 mm². Loads: 300 kN down at D and 600 kN down at K. E = 200 GPa. Find the reactions at A and B.

**Given:** as above. **Find:** $R_A$, $R_B$.

**Approach.** Two unknown reactions, one equilibrium equation: indeterminate. Release B (the redundant) and use superposition.

**FBD in words.** Bar with $R_A$ ↑ at A, $R_B$ ↑ at B, 300 kN ↓ at D and 600 kN ↓ at K.

**Solution.**
1. *Released bar, loads only.* Internal forces (tension +): AD = 900, DC = 600, CK = 600, KB = 0 kN.
$$\delta_L = \frac{1}{E}\left[\frac{900\,000(150)}{250}+\frac{600\,000(150)}{250}+\frac{600\,000(150)}{400}+0\right] = \frac{540\,000 + 360\,000 + 225\,000}{E} = \frac{1.125\times10^6}{E}\ (\text{B moves down})$$
2. *Released bar, $R_B$ alone (↑):* compresses the whole bar.
$$\delta_R = -\frac{R_B}{E}\left[\frac{300}{250}+\frac{300}{400}\right] = -\frac{1.95R_B}{E}$$
3. *Compatibility:* $\delta_L + \delta_R = 0$, so $1.125\times10^6 = 1.95R_B$ and $R_B = 577$ kN.
4. *Statics:* $R_A = 900 - 577 = 323$ kN.

$$\boxed{R_B = 577\ \text{kN}\uparrow,\qquad R_A = 323\ \text{kN}\uparrow}$$

**Check.** The lower half is stiffer (larger area) and closer to the larger load, so $R_B > R_A$ ✓. These match Beer's answers ✓. Final forces: AD = +323, DC = CK = +23, KB = −577 kN; their $\sum PL/AE$ is 0 ✓.

**Exam takeaway.** Write the released displacement as a sum over segments. The slide's three-picture superposition is exactly what examiners want to see. **Variation:** a 4.5 mm gap at B. Then $\delta_L + \delta_R = 4.5$ mm before contact matters, and you should check whether the gap closes at all.

---

#### Q13 (Crandall Prob 2.14) — A spring with a "kink": two cylinders of different length *(medium)*
**Problem.** A very stiff spring with a kink in its load–deflection curve is made from a brass cylinder (diameter 150 mm, wall 6.25 mm) and an aluminium cylinder (diameter 250 mm, wall 6.25 mm), both 250 mm long. The aluminium cylinder is 0.08 mm shorter than the brass one. A rigid plate loads both. Sketch the load–deflection relation. Take $E_{brass} = 100$ GPa and $E_{Al} = 70$ GPa.

**Given:** thin walls (A ≈ πdt); L = 250 mm; gap 0.08 mm. **Find:** P–δ curve and the kink point.

**Approach.** Before the gap closes only the brass carries load (a single spring). After that both act in parallel.

**FBD in words.** Rigid top plate with P ↓; brass reaction ↑ always; aluminium reaction ↑ only after the plate has moved 0.08 mm.

**Solution.**
1. *Areas:* $A_b = \pi(150)(6.25) = 2945$ mm² and $A_{Al} = \pi(250)(6.25) = 4909$ mm².
2. *Stiffnesses:* $k_b = \dfrac{2945(100\,000)}{250} = 1.178\times10^6$ N/mm and $k_{Al} = \dfrac{4909(70\,000)}{250} = 1.374\times10^6$ N/mm.
3. *Stage 1* ($\delta \le 0.08$ mm): $P = k_b\delta$. At the kink, $P_k = 1.178\times10^6(0.08) = 94.2$ kN.
4. *Stage 2* ($\delta > 0.08$ mm): $P = 94.2\ \text{kN} + (k_b + k_{Al})(\delta - 0.08)$, with slope $2.55\times10^6$ N/mm.

$$\boxed{P = 1.18\times10^6\,\delta\ \ (\delta\le0.08\ \text{mm});\qquad P = 94.2\ \text{kN} + 2.55\times10^6(\delta-0.08)\ \ (\delta>0.08)\ \ [\text{N, mm}]}$$

**Check.** The slope more than doubles after the kink, because aluminium has a larger area even though its E is lower ✓.

**Exam takeaway.** Gaps make the response piecewise linear, so always ask "does the gap close?" **Variation:** given a load of 300 kN, find each cylinder's force. $\delta = 0.08 + 205.8\times10^3/2.55\times10^6 = 0.161$ mm; brass carries $1.178\times10^6\times0.161 = 190$ kN and aluminium 110 kN.

---

#### Q14 (Crandall Prob 2.11) — Reinforced-concrete pier *(medium)*
**Problem.** A square reinforced-concrete pier, 0.3 × 0.3 m in cross-section and 1.2 m high, carries 670 kN through a rigid cover plate. It is strengthened by eight vertical 25 × 25 mm square steel bars placed symmetrically. Find the stress in the steel and in the concrete, and the shortening. Take $E_c = 17$ GPa and $E_s = 200$ GPa.

**Given:** $A_s = 8(625) = 5000$ mm²; $A_c = 90\,000 - 5000 = 85\,000$ mm²; L = 1200 mm; P = 670 kN. **Find:** $\sigma_s$, $\sigma_c$, δ.

**Approach.** The rigid cover plate makes steel and concrete shorten equally (compatibility: equal strain). Equilibrium: $P_s + P_c = P$.

**FBD in words.** Cover plate with 670 kN ↓ on top and $P_s$ ↑ (steel) and $P_c$ ↑ (concrete) from below.

**Solution.**
1. *Equal strain:* $\epsilon = \dfrac{P}{A_sE_s + A_cE_c} = \dfrac{670\,000}{5000(200\,000) + 85\,000(17\,000)} = \dfrac{670\,000}{(1.000 + 1.445)\times10^9} = 2.740\times10^{-4}$.
2. *Stresses:* $\sigma_s = E_s\epsilon = 54.8$ MPa and $\sigma_c = E_c\epsilon = 4.66$ MPa (both compressive).
3. *Shortening:* $\delta = \epsilon L = 2.74\times10^{-4}(1200) = 0.329$ mm.

$$\boxed{\sigma_s = 54.8\ \text{MPa (C)},\qquad \sigma_c = 4.66\ \text{MPa (C)},\qquad \delta = 0.33\ \text{mm}}$$

**Check.** The steel is only 5.6% of the area but carries $54.8(5000)/670\,000 = 41\%$ of the load, because it is 11.8× stiffer ✓. $\sigma_s/\sigma_c = E_s/E_c = 11.8$ ✓.

**Exam takeaway.** Composite parallel members share **strain**, not stress. **Variation:** "the concrete may carry at most 4 MPa", giving $P_{max} = 4/E_c\times\sum AE = 575$ kN.

---

#### Q15 (Slides Ch2 = Crandall Prob 2.24) — Bolt and sleeve: a quarter turn of the nut *(medium)*
**Problem.** A bolt passes through a tubular sleeve, and the nut is turned up just tight by hand. The nut is then given an extra quarter turn. The bolt has 16 threads per inch. Both parts are steel ($E = 30\times10^6$ psi), the bolt area is 1 in², the sleeve area 0.6 in², and the length 6 in. Estimate the tensile force in the bolt.

**Given:** misfit Δ = pitch × turns = $\frac{1}{16}\times\frac14 = \frac{1}{64}$ in; L = 6 in. **Find:** F.

**Approach.** Bolt (tension) and sleeve (compression) carry the same force: series springs. Compatibility says the misfit is taken up by the bolt stretching plus the sleeve shortening.

**FBD in words.** Cut the bolt and sleeve between the head and the nut. The bolt carries F (T) and the sleeve F (C). The equilibrium of the head gives the same F in both.

**Solution.**
1. *Equilibrium:* $F_{bolt} = F_{sleeve} = F$.
2. *Compatibility:* $\delta_b + \delta_s = \Delta = 1/64$ in.
3. *Force–deformation:* $\dfrac{FL}{A_bE} + \dfrac{FL}{A_sE} = \Delta$.
4. Solve:
$$F = \frac{\Delta E}{L\left(\frac{1}{A_b}+\frac{1}{A_s}\right)} = \frac{(1/64)(30\times10^6)}{6(1 + 1.667)} = \frac{468\,750}{16.0}$$

$$\boxed{F \approx 29\,300\ \text{lb}}$$

**Check.** Bolt stress 29.3 ksi; sleeve stress $29\,300/0.6 = 48.8$ ksi. Both are high but plausible for steel, and the thinner sleeve is more highly stressed ✓.

**Exam takeaway.** Misfit problems are series springs: same force, deformations add to the misfit. **Variation:** sleeve of aluminium ($E = 10\times10^6$ psi), giving $F = \Delta/(L/A_bE_b + L/A_sE_s) = 0.0156/(2\times10^{-7} + 1\times10^{-6}) = 13\,000$ lb.

---

#### Q16 (Crandall Prob 2.12) — Three-bar pin-connected framework *(medium–hard)*
**Problem.** A vertical inner bar of area A and two outer bars of area $A_0$ (each at angle θ to the vertical) hang from a ceiling and meet at a joint carrying a load F. The inner bar has length L. All bars have the same E. Find the axial force in each bar.

**Approach.** The joint has two equilibrium equations but three unknown bar forces (two equal by symmetry, so effectively two unknowns with one useful equation). Compatibility: the joint moves straight down by δ, by symmetry.

**FBD in words.** Joint with F ↓, $N_i$ ↑ along the inner bar and $N_o$ along each outer bar, up and outward at θ from the vertical.

**Solution.**
1. *Equilibrium (vertical):* $N_i + 2N_o\cos\theta = F$. Horizontal is satisfied by symmetry.
2. *Compatibility:* joint displacement δ ↓. Elongation of the inner bar is δ. Elongation of an outer bar is the component of δ along it, $\delta\cos\theta$.
3. *Force–deformation:* $N_i = \dfrac{AE\delta}{L}$ and $N_o = \dfrac{A_0E\,\delta\cos\theta}{L/\cos\theta} = \dfrac{A_0E\delta\cos^2\theta}{L}$.
4. *Substitute:* $\dfrac{E\delta}{L}\left(A + 2A_0\cos^3\theta\right) = F$, so $\delta = \dfrac{FL}{E(A + 2A_0\cos^3\theta)}$.

$$\boxed{N_i = \frac{F\,A}{A + 2A_0\cos^3\theta},\qquad N_o = \frac{F\,A_0\cos^2\theta}{A + 2A_0\cos^3\theta}}$$

**Check.** θ → 0 (all bars vertical and equal length): $N_i = FA/(A + 2A_0)$ and $N_o = FA_0/(A + 2A_0)$, ordinary parallel sharing ✓. θ → 90°: the outer bars carry no vertical load and $N_i = F$ ✓.

**Exam takeaway.** The inclined bar's elongation is $\delta\cos\theta$ (the projection of the joint displacement onto the bar). Students who use $\delta/\cos\theta$ get the wrong compatibility. **Variation:** A = A₀ and θ = 30°: $\cos^3 30^\circ = 0.6495$, so $N_i = F/2.299 = 0.435F$ and $N_o = 0.435F\times0.75 = 0.326F$.

---

#### Q17 (Crandall Probs 2.31 and 2.32) — Composite hoop under internal pressure *(medium–hard)*
**Problem.** A brass hoop (internal radius 300 mm, thickness 3 mm) fits snugly inside a steel hoop (internal radius 303 mm, radial thickness 6 mm). Both are 6 mm wide. A radial pressure of 1.4 MPa acts inside the brass hoop. Estimate the tangential (hoop) forces in each hoop, and the radial expansion of the brass hoop. Take $E_b = 100$ GPa and $E_s = 200$ GPa.

**Given:** $p = 1.4$ MPa on inner radius $r_i = 300$ mm, width w = 6 mm; $A_b = 3\times6 = 18$ mm², $A_s = 6\times6 = 36$ mm²; mean radii $r_b = 301.5$ mm and $r_s = 306$ mm. **Find:** $T_b$, $T_s$, $\Delta r_b$.

**Approach.** Thin rings (Concept 2.6). Equilibrium of a half-ring gives the **total** hoop force. Compatibility: both rings expand by the same radial amount at the interface (they stay in contact). Each ring's radial expansion is $r\,\epsilon_\theta = rT/(AE)$.

**FBD in words.** Cut both hoops across a diameter. The pressure on the half-circle pushes up with $2pr_iw$; four hoop forces (T_b and T_s on each side) hold it down.

**Solution.**
1. *Equilibrium:* $2(T_b + T_s) = 2pr_iw$, so $T_b + T_s = 1.4(300)(6) = 2520$ N.
2. *Compatibility:* $\Delta r_b = \Delta r_s$, i.e. $\dfrac{r_bT_b}{A_bE_b} = \dfrac{r_sT_s}{A_sE_s}$.
3. So $\dfrac{T_s}{T_b} = \dfrac{r_b}{r_s}\cdot\dfrac{A_sE_s}{A_bE_b} = \dfrac{301.5}{306}\cdot\dfrac{36(200)}{18(100)} = 0.985(4) = 3.941$.
4. $T_b = \dfrac{2520}{1 + 3.941} = 510$ N and $T_s = 2010$ N.
5. *Radial expansion of the brass (2.32):* $\Delta r_b = \dfrac{r_bT_b}{A_bE_b} = \dfrac{301.5(510)}{18(100\,000)} = 0.0854$ mm.

$$\boxed{T_b \approx 510\ \text{N},\quad T_s \approx 2010\ \text{N},\quad \Delta r_b \approx 0.085\ \text{mm}}$$

**Check.** The steel hoop is 4× stiffer (twice the area, twice the E), so it carries about 4/5 of the load ✓. Stresses: brass 28.3 MPa, steel 55.8 MPa ✓.

**Exam takeaway.** Exactly the same "equal deformation, forces add" logic as the RC pier, applied around a circle. **Variation:** with a radial gap of 0.05 mm between the hoops, brass alone resists until it has expanded 0.05 mm.

---

## Concept 2.4 — Displacement (Williot) diagrams for pin-jointed structures

### A. Concept explanation

**1. Intuition.** Take two bars pinned together at B, with their other ends fixed to a wall. Load B and each bar changes length a little. B must end up where both bars, at their new lengths, can still reach it, i.e. at the intersection of two arcs. For **small** deformations each arc can be replaced by a straight line **perpendicular** to its bar. That is the Williot construction.

**2. Why it matters.** It gives joint deflections of trusses and links without energy methods. It is the independent check for Castigliano answers (Concept 2.5). PYQ 2014 Test-1 Q2 asks for exactly these deflections.

**3. Formal treatment (small displacements).** If a joint moves by $\mathbf u = (u, v)$ and the other end of a bar is fixed, the bar's change in length is the component of $\mathbf u$ along the bar:
$$\boxed{\delta_{bar} = \mathbf u\cdot\mathbf e}\qquad(\mathbf e = \text{unit vector from the fixed end toward the joint})$$
If both ends move, use the relative displacement: $\delta = (\mathbf u_j - \mathbf u_i)\cdot\mathbf e_{ij}$. Write one such equation per bar, then solve for the unknown joint displacements.

**4. Derivation.** The new length is
$$|\mathbf L + \mathbf u| = \sqrt{L^2 + 2\mathbf L\cdot\mathbf u + u^2} = L\sqrt{1 + \frac{2\mathbf e\cdot\mathbf u}{L} + \frac{u^2}{L^2}} \approx L + \mathbf e\cdot\mathbf u$$
using $\sqrt{1+x}\approx 1 + x/2$ and dropping $u^2/L^2$ (small displacements). So $\delta = \mathbf e\cdot\mathbf u$. ∎ A displacement **perpendicular** to the bar changes its length only to second order; that is why each arc becomes a perpendicular line.

**5. Graphical construction.** From the fixed end of each bar, lay off its δ along the bar (toward the joint for stretching, away for shortening). At the tip of each δ vector, draw a line perpendicular to the bar. The intersection of these perpendiculars is the displaced joint. Measure u and v.

**6. Special cases.**
- **Two-bar bracket** (AB horizontal; BC inclined at θ to AB; load P down at B). $F_{AB} = P\cot\theta$ (T) and $F_{BC} = P\csc\theta$ (C). Then $u_B = \delta_{AB}$ (away from the wall) and $v_B = (\delta_{BC} + u_B\cos\theta)/\sin\theta$ (downward), where $\delta_{BC}$ is the shortening of BC.
- **Symmetric V** (two equal bars at ±β from the vertical, load P down at the joint). Each bar force is $P/(2\cos\beta)$, each stretch is $\delta_b = \dfrac{PL}{2AE\cos\beta}$, and the joint moves $\delta_b/\cos\beta$:
$$\boxed{\delta_{joint} = \frac{PL}{2AE\cos^2\beta}}$$
This is the slides' "find the deflection of joint B" example.

**7. Common traps.**
- Forgetting that a **shortening** bar pulls the joint toward its support.
- Adding bar elongations as if they were the joint displacement.
- Using large-angle trigonometry; all angles stay the undeformed ones.

**8. Summary box**
$$\delta_{bar} = \mathbf u\cdot\mathbf e\ (\text{small }u);\qquad \text{two-bar: } u = \delta_{AB},\ v = \frac{\delta_{BC}+u\cos\theta}{\sin\theta};\qquad \text{symmetric V: } \delta = \frac{PL}{2AE\cos^2\beta}$$

### B. Solved questions

#### Q18 (Slides Ch2) — Displacement of D in a rod–beam bracket *(medium)*
**Problem.** A horizontal steel beam CD (L = 3 m, A = 3200 mm²) is pinned to a wall at C. A steel rod BD (A = 491 mm²) runs from B on the wall, 3 m above C, to D at 45°. E = 205 GPa. 20 kN hangs at D. Find the displacement of D.

**Given:** $L_{BD} = 3\sqrt2 = 4.243$ m. **Find:** $u_D$, $v_D$.

**Approach.** Statics at joint D for the bar forces, then δ = FL/AE, then the Williot conditions for each bar.

**FBD in words.** Joint D with 20 kN ↓, $F_{BD}$ along DB (up-left at 45°) and $F_{CD}$ along DC (←), both assumed tensile.

**Solution.**
1. *Joint D:* vertical: $F_{BD}\sin45^\circ = 20$, so $F_{BD} = 28.28$ kN (T). Horizontal: $F_{CD} + F_{BD}\cos45^\circ = 0$ (both point toward the wall), so $F_{CD} = -20$ kN (C).
2. *Length changes:*
$$\delta_{BD} = \frac{28\,284(4243)}{491(205\,000)} = 1.192\ \text{mm (lengthens)},\qquad \delta_{CD} = \frac{20\,000(3000)}{3200(205\,000)} = 0.0915\ \text{mm (shortens)}$$
3. *Compatibility* (u positive away from the wall, v positive downward):
   - CD (horizontal): $u_D = -0.0915$ mm (D moves toward the wall).
   - BD (unit vector from B to D, $(0.7071, +0.7071)$ in (u, v)): $0.7071u + 0.7071v = 1.192$, so $v = 1.686 + 0.0915 = 1.777$ mm.

$$\boxed{v_D = 1.78\ \text{mm}\downarrow,\qquad u_D = 0.092\ \text{mm toward the wall},\qquad |\Delta_D| = 1.78\ \text{mm}}$$

**Check (Castigliano, Q22).** The vertical deflection comes to 1.777 mm, the same ✓.

**Exam takeaway.** In a bracket the inclined tie's stretch dominates. **Variation:** "find the angle through which CD rotates", $1.777/3000 = 5.9\times10^{-4}$ rad.

---

#### Q19 (Slides Ch2 = Crandall Prob 2.6) — Stiff member on three bars: a zero-force member that still matters *(hard)*
**Problem.** A stiff member AB is horizontal before a 5000 lb load is applied at A. E is 12 ft from A and B is 18 ft from A. Three steel bars ($E = 30\times10^6$ psi) are pinned at their ends: ED vertical, 6 ft (2 in²); BC vertical, 6 ft (1 in²); BD diagonal from D up to B at 45° (1.5 in²). Find (a) the force in BD and (b) the horizontal and vertical movement of A.

**Approach.** Statics first. Then each bar's stretch, then compatibility at B and the rigid-body motion of AB.

**FBD in words.** Member AB with 5000 lb ↓ at A, $F_{ED}$ at E (vertical), $F_{BC}$ at B (vertical) and $F_{BD}$ at B (along the 45° line).

**Solution.**
1. *(a) Horizontal equilibrium:* only BD has a horizontal component, so $F_{BD} = 0$.
2. *Moments about B:* $5000(18) = F_{ED}(6)$, so $F_{ED} = 15\,000$ lb. ED pushes **up** on AB, so it is in **compression**.
3. *Vertical sum:* $15\,000 - 5000 - F_{BC} = 0$, so BC pulls B **down** with 10 000 lb (**tension**).
4. *Deformations:* $\delta_{ED} = \dfrac{15\,000(72)}{2(30\times10^6)} = 0.018$ in (shortens, so E moves **down** 0.018 in). $\delta_{BC} = \dfrac{10\,000(72)}{1(30\times10^6)} = 0.024$ in (lengthens, so B moves **up** 0.024 in). $\delta_{BD} = 0$.
5. *Fit at B:* BD's length is unchanged, with unit vector from D to B $(0.707, 0.707)$: $0.707u_B + 0.707(0.024) = 0$, so $u_B = -0.024$ in (toward A, i.e. left).
6. *Rigid AB:* every point moves the same horizontal amount (small rotation), so $u_A = -0.024$ in. The vertical displacement varies linearly. Slope = $\dfrac{0.024 - (-0.018)}{72\ \text{in}} = 5.83\times10^{-4}$, so $v_A = -0.018 - 144(5.83\times10^{-4}) = -0.102$ in.

$$\boxed{(a)\ F_{BD} = 0;\qquad (b)\ A\ \text{moves}\ 0.024\ \text{in left and}\ 0.102\ \text{in down}}$$

**Check.** A is 12 ft beyond E on the side away from B, so it must drop more than E ✓.

**Exam takeaway.** A zero-force member can still **constrain** displacement. That is why Crandall asks for both parts. **Variation:** remove BD; then AB is a mechanism (it can slide horizontally).

---

#### Q20 (Slides Ch2 = Crandall Prob 2.7) — Railroad bridge: how far does the roller move? *(hard)*
**Problem.** A small Warren-truss bridge (60° triangles, bottom panels 4.6 m, span 13.8 m) has every member of area 3250 mm², steel E = 200 GPa. A stopped train loads the bottom joints with 270 kN (at the pin A), 180 kN, 270 kN and 360 kN (at the roller R). Estimate how far R moves horizontally.

**Approach.** A is pinned and R rolls horizontally, so R's movement equals the total elongation of the bottom chord. Loads directly over supports go straight into the reactions and cause no member forces.

**FBD in words.** The truss with the two interior loads (180 and 270 kN) and the reactions they cause.

**Solution.**
1. *Reactions from the interior loads only:* $R_R' = (180\times4.6 + 270\times9.2)/13.8 = 240$ kN and $R_A' = 210$ kN.
2. *Height:* $h = 2.3\tan60^\circ = 3.984$ m.
3. *Bottom-chord forces* (sections, moments about the top joints at x = 2.3, 6.9 and 11.5 m):
   - $F_1 = 210(2.3)/3.984 = 121.2$ kN (T)
   - $F_2 = [210(6.9) - 180(2.3)]/3.984 = 259.8$ kN (T)
   - $F_3 = 240(2.3)/3.984 = 138.6$ kN (T)
4. *Roller movement:*
$$\delta_R = \frac{(121.2 + 259.8 + 138.6)\times10^3(4600)}{3250(200\,000)} = \frac{2.390\times10^9}{6.5\times10^8}$$

$$\boxed{\delta_R \approx 3.68\ \text{mm (to the right)}}$$

**Check.** A full computer solve of the truss gives the same bottom-chord forces ✓.

**Exam takeaway.** "How far does the roller move" is a sum of member elongations along one line. No energy method is needed. **Variation:** Crandall 2.8 asks for the horizontal movement of a top joint. Add the bottom-chord stretch up to that joint plus the effect of the diagonals (use a dummy load).

---

## Concept 2.5 — Strain energy and Castigliano's theorem

### A. Concept explanation

**1. Intuition.** Stretching a spring takes work, and that work is stored like charge in a battery. If you know how the stored energy depends on each load, its rate of change tells you how far that load's point moves. A large rate means a small increase in load stores a lot of extra energy, which means the point moves a long way.

**2. Why it matters.** It is the fastest route to deflections of trusses, curved members, frames and rings, and it works even where no load acts (using a fictitious load). PYQs: 2014 Test-1 Q2 (truss, 20 marks), 2019-20 A-Q3(b) (curved beam), 2024 B-Q1(c) (torsional energy).

**3. Formal treatment (slides, Crandall §2.6).**
- *Work of a slowly increasing load:* $dU = P\,dx$, so $U = \int_0^{x_1}P\,dx$, the area under the P–x curve.
- *Linear elastic:* $P = kx$ gives $U = \tfrac12kx_1^2 = \tfrac12P_1x_1$.
- *Axial bar:* $x_1 = P_1L/AE$, so
$$\boxed{U = \frac{P^2L}{2AE}}\qquad\text{(structure: } U = \sum\frac{F_i^2L_i}{2A_iE_i}\text{; varying force: } U = \int\frac{N^2dx}{2AE}\text{)}$$
- *Castigliano's theorem (slides):* "When forces act on elastic systems subject to small displacements, the displacement corresponding to any force, in the direction of the force, is equal to the partial derivative of the total strain energy with respect to that force."
$$\boxed{\delta_i = \frac{\partial U}{\partial F_i}}$$
- *Fictitious load (slides):* to find a deflection where no load acts, apply a fictitious force Q there in the desired direction, include it in U, take $\partial U/\partial Q$, and **only then** set Q = 0.

**4. Derivations.**

*(a) Why the theorem holds.* In a linear system each displacement is a linear combination of the loads, $\delta_j = \sum_k c_{jk}P_k$, with $c_{jk} = c_{kj}$ (Maxwell's reciprocal theorem; Crandall Prob 2.13 asks you to verify this). The stored energy is
$$U = \tfrac12\sum_j P_j\delta_j = \tfrac12\sum_j\sum_k c_{jk}P_jP_k$$
Differentiating with respect to $P_i$ and using symmetry gives $\dfrac{\partial U}{\partial P_i} = \sum_k c_{ik}P_k = \delta_i$. ∎

*(b) Working formula for trusses.* Differentiate before squaring, which saves algebra:
$$\delta_i = \sum_{\text{members}} F_j\,\frac{\partial F_j}{\partial P_i}\,\frac{L_j}{A_jE_j}$$

*(c) Beams and curved members* (bending energy; the bending formula comes later in the course):
$$U = \int\frac{M^2}{2EI}ds + \int\frac{N^2}{2AE}ds\ \Rightarrow\ \delta_i = \int\frac{M}{EI}\frac{\partial M}{\partial P_i}ds + \int\frac{N}{AE}\frac{\partial N}{\partial P_i}ds$$

*(d) Energy of a bar including its own weight (Crandall Prob 2.45).* With an end load $F_0$ and weight w per unit length, measuring x up from the free end, $N(x) = F_0 + wx$ and
$$U = \frac{1}{2AE}\int_0^L(F_0 + wx)^2dx = \frac{1}{2AE}\left(F_0^2L + F_0wL^2 + \frac{w^2L^3}{3}\right)$$

**5. Picture.** U is the triangle under the straight P–δ line, area ½Pδ. For a linear material the "complementary" triangle above the line has the same area. Castigliano's theorem is really about that complementary area, which is why it needs linearity.

**6. Special cases.**
- A member whose force doesn't depend on Q ($\partial F/\partial Q = 0$) contributes nothing to that deflection. You only need the members that feel Q.
- A rotation is found with a dummy couple: $\theta = \partial U/\partial C$.
- Indeterminate structures: choose a redundant R and impose $\partial U/\partial R = 0$ (zero displacement at a rigid support). This is Castigliano's second theorem, used for Crandall 2.42.

**7. Common traps.**
- Using $\partial U/\partial P$ when the same symbol P is applied at **two** points; that gives the *sum* of the two displacements. Give each load its own symbol.
- A negative result means the displacement is opposite to the direction assumed for the load.
- Setting Q = 0 **before** differentiating.
- Mixing units inside $\sum FfL/AE$ (keep N and mm throughout).

**8. Summary box**

| Item | Formula |
|---|---|
| Bar energy | $U = P^2L/2AE$ |
| Castigliano | $\delta_i = \partial U/\partial F_i$ |
| Truss form | $\delta = \sum F(\partial F/\partial P)L/AE$ |
| Beam/curved form | $\delta = \int M(\partial M/\partial P)\,ds/EI\ (+\int N(\partial N/\partial P)ds/AE)$ |
| Dummy load | include Q, differentiate, then set Q = 0 |

### B. Solved questions

#### Q21 (Slides Ch2) — Truss: P needed to move roller C by 0.2 mm *(medium)*
**Problem.** A truss of three steel members, each 400 mm², has a pin at A and a roller at C, with AC = 1.4 m. Apex B is 0.8 m above the base, 0.8 m horizontally from A (so AB = 1.131 m and BC = 1.0 m). P acts down at B. Using Castigliano's method, find P such that roller C moves 0.2 mm to the right. E = 200 GPa.

**Approach.** No load acts horizontally at C, so add a fictitious Q (→) there. Express every member force in terms of P and Q, then $\delta_C = \partial U/\partial Q|_{Q=0}$.

**FBD in words.** Joint C with roller reaction $C_y$ ↑, Q →, $F_{CB}$ toward B and $F_{CA}$ toward A (both assumed tensile).

**Solution.**
1. *Reactions:* $\sum M_A$: $C_y(1.4) = P(0.8)$, so $C_y = 0.5714P$ (Q passes through A's line and adds no moment).
2. *Joint C, vertical:* $0.8F_{CB} + 0.5714P = 0$, so $F_{CB} = -0.714P$ (C). Independent of Q.
3. *Joint C, horizontal:* $-0.6F_{CB} - F_{CA} + Q = 0$, so $F_{CA} = Q + 0.4286P$ (T).
4. *Joint A:* $F_{AB}$ depends only on P ($F_{AB} = -0.606P$). Independent of Q.
5. *Castigliano:* only AC depends on Q, with $\partial F_{AC}/\partial Q = 1$:
$$\delta_C = \frac{F_{AC}(1)L_{AC}}{AE}\Big|_{Q=0} = \frac{0.4286P(1400)}{400(200\,000)} = 0.2\ \text{mm}$$
6. $P = \dfrac{0.2(8\times10^7)}{600} = 26\,670$ N.

$$\boxed{P \approx 26.7\ \text{kN}}$$

**Check.** A is pinned and C slides along AC, so its movement is just the elongation of AC: $F_{AC}L/AE = 11\,430(1400)/(8\times10^7) = 0.2$ mm ✓.

**Exam takeaway.** Only the members whose force depends on the dummy load contribute. **Variation:** the vertical deflection of B, $\sum F(\partial F/\partial P)L/AE$ over all three members.

---

#### Q22 (Slides Ch2) — The rod–beam bracket again, by Castigliano *(easy)*
**Problem.** Use Castigliano's theorem to find the vertical deflection of D in the bracket of Q18.

**Solution.**
1. Member forces in terms of P: $F_{BD} = \sqrt2P$ (T), $F_{CD} = -P$ (C).
2. $\delta_v = \sum F\dfrac{\partial F}{\partial P}\dfrac{L}{AE} = \dfrac{\sqrt2P(\sqrt2)(4243)}{491(205\,000)} + \dfrac{(-P)(-1)(3000)}{3200(205\,000)}$.
3. With P = 20 000 N: $1.686 + 0.0915$.

$$\boxed{\delta_v = 1.78\ \text{mm}\downarrow}$$

**Check.** Same as the Williot diagram in Q18 ✓.

**Exam takeaway.** Two independent methods, the same number. Use one as the answer and the other as a private check.

---

#### Q23 (Crandall Prob 2.10) — Tip deflection of the six-member cantilever truss *(medium)*
**Problem.** For the pin-jointed cantilever truss of Ch. 1 Q25 (A, E on the wall; AB = BC = BD = L; load W at C), with every member of area A and modulus E, find (a) the member forces and (b) the vertical deflection of the loaded joint C.

**Approach.** (a) is Ch. 1 Q25. (b) Castigliano: every member force is proportional to W, so $\partial F/\partial W = F/W$.

**Solution.**
1. *(a) Forces:* AB = 2W (T), BC = W (T), BD = W (T), ED = W (C), EB = √2W (C), DC = √2W (C).
2. *Lengths:* AB, BC, BD and ED are L; EB and DC are √2L.
3. *(b)* $\delta_C = \sum F\dfrac{\partial F}{\partial W}\dfrac{L_i}{AE} = \dfrac{W}{AE}\sum f_i^2L_i$, with $f_i = F_i/W$:
$$\sum f_i^2L_i = (4 + 1 + 1 + 1)L + (2 + 2)\sqrt2L = (7 + 5.657)L = 12.66L$$

$$\boxed{\delta_C = 12.66\,\frac{WL}{AE}\ \downarrow}$$

**Check.** All terms are positive (squares), so the deflection is in the direction of W, as it must be ✓. The diagonals (compression) contribute 45% of the deflection.

**Exam takeaway.** For a single load, $\delta = \sum f^2L/AE \times W$. Tabulate member, f, L, f²L. **Variation:** the horizontal deflection of C needs a dummy horizontal load. Only members whose force changes with it contribute.

---

#### Q24 (Crandall Prob 2.45) — Strain energy of a bar with and without its own weight *(medium)*
**Problem.** A uniform bar of length L hangs vertically, carries an end load $F_0$ at its lower end and has weight w per unit length. Calculate the stored energy with and without the bar's weight.

**Approach.** The internal force varies along the bar, so integrate $N^2/2AE$.

**Solution.**
1. *Internal force* at distance x above the free end: $N(x) = F_0 + wx$.
2. *Energy with weight:*
$$U = \int_0^L\frac{(F_0 + wx)^2}{2AE}dx = \frac{1}{2AE}\left[F_0^2L + F_0wL^2 + \frac{w^2L^3}{3}\right]$$
3. *Without weight* (w = 0): $U_0 = \dfrac{F_0^2L}{2AE}$.

$$\boxed{U = \frac{F_0^2L}{2AE} + \frac{F_0wL^2}{2AE} + \frac{w^2L^3}{6AE}}$$

**Check.** Castigliano: $\partial U/\partial F_0 = \dfrac{F_0L}{AE} + \dfrac{wL^2}{2AE}$. That is the end deflection, which matches the end-load stretch plus the self-weight stretch $WL/2AE$ (Concept 2.2) ✓.

**Exam takeaway.** Energy is **not** additive in loads (the cross term $F_0wL^2/2AE$ appears), because U is quadratic. Only displacements superpose. **Variation:** a mine-hoist cable (Crandall 2.15) with $wL$ comparable to $F_0$.

---

#### Q25 (PYQ 2014-15 Test-1 Q2) — Two-bar bracket: horizontal and vertical deflection by Castigliano only *(medium, 20 marks)*
**Problem.** AB is horizontal, 6 m long, from the wall at A to B. BC runs from C on the wall (4.5 m below A) to B, 7.5 m long. 20 kN acts down at B. E = 200 GPa and A = 800 mm² for each member. Using **Castigliano's theorem only**, find the vertical and horizontal deflections of B.

**Given:** $\sin\theta = 4.5/7.5 = 0.6$ and $\cos\theta = 0.8$ for BC. **Find:** $\delta_v$, $\delta_h$.

**Approach.** Vertical deflection: differentiate with respect to the real load P. Horizontal deflection: add a fictitious Q → at B and differentiate with respect to Q, then set Q = 0.

**FBD in words.** Joint B with P ↓, Q →, $F_{AB}$ toward A (←, tensile) and $F_{BC}$ toward C (down-left, tensile).

**Solution.**
1. *Joint B, vertical:* $-F_{BC}(0.6) - P = 0$, so $F_{BC} = -1.667P$ (C), independent of Q.
2. *Joint B, horizontal:* $-F_{AB} - F_{BC}(0.8) + Q = 0$, so $F_{AB} = Q + 1.333P$ (T).
3. *Vertical deflection* (Q = 0, P = 20 kN):
$$\delta_v = \frac{1}{AE}\left[F_{AB}\frac{\partial F_{AB}}{\partial P}L_{AB} + F_{BC}\frac{\partial F_{BC}}{\partial P}L_{BC}\right] = \frac{26\,667(1.333)(6000) + 33\,333(1.667)(7500)}{800(200\,000)}$$
$$\delta_v = \frac{2.133\times10^8 + 4.167\times10^8}{1.6\times10^8} = 3.94\ \text{mm}$$
4. *Horizontal deflection:* only AB depends on Q ($\partial F_{AB}/\partial Q = 1$):
$$\delta_h = \frac{F_{AB}(1)L_{AB}}{AE} = \frac{26\,667(6000)}{1.6\times10^8} = 1.00\ \text{mm}$$

$$\boxed{\delta_v = 3.94\ \text{mm}\downarrow,\qquad \delta_h = 1.00\ \text{mm}\rightarrow}$$

**Check (Williot, private).** $u = \delta_{AB} = 1.00$ mm. BC shortens by $33\,333(7500)/1.6\times10^8 = 1.5625$ mm. $v = (1.5625 + 1.00(0.8))/0.6 = 3.94$ mm ✓.

**Exam takeaway.** The paper said "Castigliano only", so a displacement diagram earns no marks there even though it gives the right number. **Variation:** load inclined at 30° to the vertical. Resolve it into P and Q components and use both derivatives.

---

#### Q26 (PYQ 2019-20 Compre A Q3(b)) — Curved cantilever: vertical tip deflection by Castigliano *(hard)*
**Problem.** A quarter-circle cantilever of radius R (circular cross-section) is fixed at A (θ = 0, at the base) and free at B (θ = 90°, at the top), with a vertical load P down at B. Using Castigliano's method, find the vertical deflection of B in terms of P, E, R, A and I. Neglect shear energy.

**Approach.** The internal forces at angle θ come from Ch. 3 Q29: $M = PR\cos\theta$, $N = P\cos\theta$ (compression) and $V = P\sin\theta$. Shear energy is neglected. Use $ds = R\,d\theta$.

**Solution.**
1. *Derivatives:* $\partial M/\partial P = R\cos\theta$ and $\partial N/\partial P = \cos\theta$.
2. *Castigliano:*
$$\delta_B = \int_0^{\pi/2}\frac{M}{EI}\frac{\partial M}{\partial P}R\,d\theta + \int_0^{\pi/2}\frac{N}{AE}\frac{\partial N}{\partial P}R\,d\theta = \frac{PR^3}{EI}\int_0^{\pi/2}\cos^2\theta\,d\theta + \frac{PR}{AE}\int_0^{\pi/2}\cos^2\theta\,d\theta$$
3. $\displaystyle\int_0^{\pi/2}\cos^2\theta\,d\theta = \Big[\tfrac\theta2 + \tfrac{\sin2\theta}{4}\Big]_0^{\pi/2} = \frac\pi4$.

$$\boxed{\delta_{B,v} = \frac{\pi PR^3}{4EI} + \frac{\pi PR}{4AE}}$$

**Check.** Ratio of the axial to the bending term: $I/(AR^2) = (d/4R)^2$, tiny for a slender member. That is why it is often dropped, but the question asked for it in terms of A and I, so keep both ✓. Dimensions: $PR^3/EI$ = N·m³/(N/m²·m⁴) = m ✓.

**Exam takeaway.** Write M(θ), N(θ), their derivatives and $ds = R\,d\theta$ before integrating. Marks are given for each. **Variation:** horizontal deflection of B, using a dummy horizontal load Q: $M = PR\cos\theta + QR(1 - \sin\theta)$, which gives $\delta_h = PR^3/(2EI)$ (bending only).

---

## Concept 2.6 — Flexible members: thin rings and belts

### A. Concept explanation

**1. Intuition.** Blow into a balloon or pump a bicycle tyre. The wall is thin, so it can't bend much; it carries the pressure by being stretched **around** the circumference, like a hoop of rope. A rope wrapped round a post is the opposite case: the post pushes radially on the rope, and friction makes the tension grow around the wrap.

**2. Why it matters.** Pipes, pressure vessels (Ch. 4 extends this to cylinders and spheres), shrink-fitted hoops (Q17), drum brakes, capstans, belts. PYQ 2014 Compre A Q11 asks for the hoop stress of a thin ring.

**3. Formal treatment.**
- *Thin ring* of mean radius r, width b and thickness t ≪ r, under internal pressure p (force per unit area). Hoop force $F_T = pbr$ and hoop stress $\sigma_\theta = \dfrac{pr}{t}$.
- *Radial expansion:* the hoop strain $\epsilon_\theta = \sigma_\theta/E$ stretches the circumference $2\pi r$ by $2\pi r\epsilon_\theta$, so the radius grows by $\delta_R = r\epsilon_\theta = \dfrac{pr^2}{Et}$.
- *Belt/rope on a drum:* $T_2/T_1 = e^{\mu\beta}$ (derived in Ch. 1 Concept 1.4). The normal pressure per unit length of rope is $T/r$.

**4. Derivation — hoop force (slides, Crandall example).** Cut the ring along a diameter and take the upper half as a free body. The pressure on a small arc $r\,d\theta$ (width b) is $p\,b\,r\,d\theta$, acting radially. Its vertical component is $pbr\sin\theta\,d\theta$. Summing over the half:
$$2F_T = \int_0^{\pi}pbr\sin\theta\,d\theta = pbr\big[-\cos\theta\big]_0^\pi = 2pbr\ \Rightarrow\ \boxed{F_T = pbr,\quad \sigma_\theta = \frac{F_T}{bt} = \frac{pr}{t}}$$
The shortcut: the net upward pressure force on a half-ring equals p times its **projected** area, $p(2r)b$.

**5. Picture.** The deformed ring (slide figure) is a slightly bigger concentric circle. Each point moves radially out by $\delta_R$, and there is no bending because the load is uniform.

**6. Special cases.**
- The answer depends only on $r/t$, not on the width b.
- Use the inner radius for a thin ring unless told otherwise; the mean radius differs by t/2r (about 1% here).
- For a rope, "four turns" means β = 8π, which amplifies tension enormously (Q29).

**7. Common traps.**
- Using the diameter instead of the radius in $pr/t$.
- Forgetting that the pressure acts over the **projected** area (2rb), not the curved area (πrb).
- Degrees in $e^{\mu\beta}$.

**8. Summary box**
$$\sigma_\theta = \frac{pr}{t},\qquad F_T = pbr,\qquad \delta_R = \frac{pr^2}{Et},\qquad \frac{T_2}{T_1} = e^{\mu\beta}$$

### B. Solved questions

#### Q27 (Slides Ch2, Crandall example) — Thin ring under internal pressure *(easy)*
**Problem.** Determine the forces in a thin ring (mean radius r, width b, thickness t) under internal pressure p, and its deformation.

**Solution.** From the derivation above:

$$\boxed{F_T = pbr,\qquad \sigma_\theta = \frac{pr}{t},\qquad \delta_R = \frac{pr^2}{Et}}$$

**Check.** Doubling the pressure doubles everything ✓. A thinner wall gives larger stress and larger expansion ✓.

**Exam takeaway.** Remember the "projected area" shortcut: $2F_T = p(2r)b$.

---

#### Q28 (PYQ 2014-15 Compre A Q11) — Hoop stress in a thin ring *(easy)*
**Problem.** A thin ring has inner diameter 500 mm, width 10 mm and thickness 5 mm, and carries an internal pressure of 1.5 MPa. Find the hoop stress.

**Solution.**
1. $r = 250$ mm (inner radius).
2. $\sigma_\theta = \dfrac{pr}{t} = \dfrac{1.5(250)}{5}$.

$$\boxed{\sigma_\theta = 75\ \text{MPa}}$$

Using the mean radius 252.5 mm gives 75.75 MPa; either is accepted at this level.

**Exam takeaway.** The width (10 mm) is a distractor.

---

#### Q29 (Crandall Prob 2.29) — Hawser wrapped four times round a capstan *(easy)*
**Problem.** A hawser from a ship is wrapped four times around a rotating capstan. A deckworker pulls on the free end with 200 N. With μ = 0.3 between capstan and hawser, what is the largest force the man can exert on the boat?

**Given:** $T_1 = 200$ N; β = 4 turns = 8π rad; μ = 0.3. **Find:** $T_2$.

**Approach.** Belt friction: the capstan rotates and the hawser slips on it, so friction is fully developed. Use the kinetic value, taken here as μ = 0.3.

**Solution.**
1. $\mu\beta = 0.3(8\pi) = 7.540$.
2. $T_2 = T_1e^{\mu\beta} = 200e^{7.540} = 200(1881)$.

$$\boxed{T_2 \approx 3.8\times10^5\ \text{N} = 376\ \text{kN}}$$

**Check.** One turn alone gives $e^{0.6\pi} = 6.6$; four turns give $6.6^4 = 1881$ ✓. A person can hold a large ship ✓.

**Exam takeaway.** The exponential grows with every turn. **Variation:** "how many turns are needed to hold 50 kN with a 100 N pull?" $\beta = \ln(500)/0.3 = 20.7$ rad = 3.3 turns, so 4 turns.

---

## Chapter 2 — Formula and convention sheet

| Topic | Formula / rule |
|---|---|
| Three steps | Equilibrium → geometric fit → force–deformation |
| Springs | parallel: $k = \sum k_i$, same δ; series: $1/k = \sum 1/k_i$, same F |
| Rigid bar on springs | δ at a spring = θ × distance; stiffness at a point ∝ $1/c^2$ |
| Axial deformation | $\delta = \sum P_iL_i/(A_iE_i)$, $P_i$ internal, T + |
| Bar stiffness | $k = AE/L$; self-weight $\delta = WL/2AE$ |
| Composite (parallel) member | equal strain: $\epsilon = P/\sum(AE)$, $\sigma_i = E_i\epsilon$ |
| Misfit (bolt + sleeve) | same F; $\delta_b + \delta_s = \Delta$ |
| Indeterminate (superposition) | release the redundant: $\delta_L + \delta_R = 0$ (or gap) |
| Fixed–fixed bar, load at a | $R_A = Pb/L$, $R_B = Pa/L$ |
| Three-bar framework | $N_i = FA/(A + 2A_0\cos^3\theta)$, $N_o = FA_0\cos^2\theta/(\ldots)$ |
| Displacement diagram | $\delta_{bar} = \mathbf u\cdot\mathbf e$; symmetric V: $\delta = PL/(2AE\cos^2\beta)$ |
| Strain energy | $U = P^2L/2AE$; varying: $\int N^2dx/2AE$; beams $\int M^2ds/2EI$ |
| Castigliano | $\delta_i = \partial U/\partial F_i$; truss $\sum F(\partial F/\partial P)L/AE$; dummy load → set 0 after differentiating |
| Thin ring | $\sigma = pr/t$, $\delta_R = pr^2/(Et)$ |
| Belt | $T_2/T_1 = e^{\mu\beta}$ |
| Units | N, mm, MPa is a consistent set; GPa = $10^3$ MPa |

**Other Crandall Ch. 2 problems worth practising:** 2.2–2.5 (determinate links), 2.8–2.9 (truss joint movements), 2.15–2.16 (ropes and rigging), 2.21 (rigid board on three springs), 2.25 (rigid bars on rods), 2.26 (wooden-stave pipe), 2.27–2.28 (rope/band brakes), 2.36–2.38 (struts, screw clamps, coils in rings), 2.42–2.43 (energy methods, indeterminate trusses).
