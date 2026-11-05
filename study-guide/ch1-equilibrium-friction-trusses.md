# Chapter 1 — Fundamental Principles of Mechanics
### Equilibrium, free-body diagrams, friction, trusses

**Sources used:** Slides "chapter 1 slides" (Dr. Sharad Shrivastava), Crandall Ch. 1 (Probs 1.13, 1.37, 1.45), PYQ 2014-15 Test-1.

> Math is written in LaTeX (`$...$`). It renders on GitHub, in VS Code's Markdown preview, and in Obsidian/Typora.

---

## Concept 1.1 — What "mechanics of solids" is and the general procedure

### A. Concept explanation

**1. Intuition.** Picture a bookshelf with four books on it. Statics tells you how hard each bracket has to push up. Mechanics of solids goes further and asks what happens *inside* the shelf: how much it sags, how hard the wood fibres are pulled, and whether it will snap. The slide shows this with a beam carrying four loads of $w/4$: we use equilibrium to get the support reactions, but while those forces travel through the material from the loads to the supports, the material "develops resisting forces, generates stresses and undergoes deformation". That internal story is the subject.

**2. Why it matters.** Every later chapter depends on getting the external forces right first. If an FBD is wrong, the stress, deflection and buckling answers are all wrong too. In the compre papers, roughly the first 20–30% of the marks on most long questions go to "draw the FBD and find the reactions".

**3. Formal treatment — the 5-step procedure (slides, Crandall §1.1):**
1. Select the system of interest.
2. Idealize it (simplify: rigid bars, point loads, frictionless pins…).
3. Apply the principles of mechanics to make predictions.
4. Compare the predictions with the real system (tests).
5. If they don't agree, build a better idealized model and repeat.

The slides note that in research, steps 1 and 2 are the hardest.

**Rigid body:** the distance between any two points never changes. No real structure is perfectly rigid. A lever bends slightly, but if we only want its *equilibrium*, the distance from each weight to the fulcrum is still $L/2$, so we can treat it as rigid. If we want its *strength*, we must include the small deformation.

**Principle of transmissibility:** you can slide a force along its line of action without changing its effect on a *rigid* body. The slide's example: pushing a truck at the front bumper or pulling it at the rear bumper has the same effect.
⚠️ This applies **only** to the external equilibrium of rigid bodies. It is **not** valid for internal forces or deformation. Pulling a rubber band at its end is not the same as pushing at the other end.

**4–5. Derivations / geometry:** none needed here. This concept is about method.

**6. Limiting cases.** Treating a body as rigid is a limiting case of "stiffness → ∞". It always gives correct reactions for *statically determinate* systems. It fails for indeterminate ones (Ch. 2), where you need deformations to find the forces.

**7. Common traps.**
- Using transmissibility to move a load along a beam when computing bending moment. **Never** do this.
- Replacing a distributed load by its resultant *before* computing internal forces. This is fine for reactions only (Ch. 3).

**8. Summary box**
| Idea | When valid |
|---|---|
| Rigid-body idealization | Reactions of determinate structures |
| Transmissibility | External equilibrium only |
| Deformable-body analysis | Internal forces, stresses, indeterminate problems |

---

## Concept 1.2 — Supports, free-body diagrams and equilibrium

### A. Concept explanation

**1. Intuition.** An FBD is like cutting the object out of a photograph with scissors. Everything that was touching it (the floor, a pin, a rope, gravity) is replaced by an arrow showing the force it applied. If the object is not accelerating, those arrows must cancel exactly, both as pushes and as twists.

**2. Why it matters.** FBDs are step 1 of every problem in this course: trusses, beams (Ch. 3), shafts (Ch. 6) and columns.

**3. Formal treatment.**

*Constraint:* a restriction on free motion in some direction. Each prevented motion produces one reaction component.

| Support (slides) | Prevents | Reaction components (2-D) |
|---|---|---|
| Roller | motion ⟂ to surface | 1 force ⟂ surface |
| Hinge / pin | both translations | 2 forces ($R_x, R_y$) |
| Built-in / fixed / clamped | both translations + rotation | $R_x, R_y$ and a moment $M$ |
| Cable / rope | stretching | 1 tensile force along the cable |
| Smooth contact | penetration | 1 normal force |

*Equations of equilibrium (2-D):*
$$\sum F_x = 0,\qquad \sum F_y = 0,\qquad \sum M_O = 0$$
$\sum M_O$ includes the moments of all forces **and** any applied couples. Point $O$ can be anywhere, so pick it where the most unknowns pass through.

*In 3-D:* $\sum \mathbf F = 0$ and $\sum \mathbf M_O = 0$, which gives 6 scalar equations.

**Two-force member:** a body loaded at only two points, with no couples, is in equilibrium only if the two forces are **equal, opposite and collinear**, acting along the line joining the two points.

**Three-force member:** if three non-parallel forces act on a body in equilibrium, their lines of action **meet at one point** (concurrency).

**4. Derivation — why a two-force member's forces are collinear.** Let forces $\mathbf F_A$ at $A$ and $\mathbf F_B$ at $B$ act on the body.
- $\sum \mathbf F=0 \Rightarrow \mathbf F_B = -\mathbf F_A$, so they are equal and opposite.
- Take moments about $A$: $\mathbf r_{AB}\times\mathbf F_B = 0$. A cross product is zero only if $\mathbf F_B \parallel \mathbf r_{AB}$, so the force lies along line $AB$. ∎

*Three-force concurrency:* take moments about the point where two of the lines of action cross. Those two forces have zero moment there, so the third force's moment must also be zero, which means it passes through that point. ∎

**5. Graphical interpretation.** For a three-force body, draw the two known lines of action. Where they cross, the third force must also pass. This is the quickest check on a roller-over-step problem (see Problem 1.13 below).

**6. Special cases.**
- If all forces are parallel, $\sum F_x$ is trivially zero, so only 2 equations are useful.
- If all forces are concurrent, the moment equation is automatically satisfied, so only 2 force equations are useful.
- A 2-D rigid body has 3 independent equations. More than 3 unknown reactions means the problem is **statically indeterminate** (Ch. 2).

**7. Common mistakes.**
- Forgetting self-weight. It acts at the centroid ($mg$, with $g = 9.81$ m/s²).
- Giving a fixed support only forces and forgetting its **moment**.
- Assuming a reaction's direction and then "correcting" its sign halfway through. Assume a direction, keep it, and interpret a negative answer at the end.
- Units: kg is not N. Multiply by 9.81.

**8. Summary box**
$$\boxed{\ \sum F_x=0,\ \sum F_y=0,\ \sum M_{\text{any pt}}=0\ }$$
- Two-force member → force along the line joining the two pins.
- Three-force member → lines of action are concurrent.
- Pin = 2 unknowns, roller = 1, fixed = 3.

### B. Solved questions

#### Q1 (Slides Ch1, "Problem 3") — Simply supported beam, central load *(easy)*
**Given:** beam AB, $L = 5$ m, $P = 5000$ N at midpoint C. A is a pin, B is a roller. **Find:** reactions.

**Approach:** 3 unknowns ($A_x, A_y, B_y$) and 3 equations, so it is determinate.

**Solution:**
- $\sum F_x = 0 \Rightarrow A_x = 0$
- $\sum M_A = 0:\ B_y(5) - 5000(2.5) = 0 \Rightarrow B_y = 2500$ N
- $\sum F_y = 0:\ A_y = 5000 - 2500 = 2500$ N

$$\boxed{A_x = 0,\quad A_y = B_y = 2500\ \text{N}\ (\uparrow)}$$

**Check:** the load is symmetric, so the reactions should be equal. ✓
**Takeaway:** a variation could put $P$ at distance $a$ from A. Then $A_y = Pb/L$ and $B_y = Pa/L$. You will reuse this result constantly in Ch. 3.

---

#### Q2 (Slides Ch1, "Problem 2") — Cantilever with self-weight *(easy)*
**Given:** uniform beam, mass 100 kg, length 6 m, fixed at A. Load 1200 N at 2 m from A. **Find:** FBD and reactions.

**FBD in words:** at A draw $A_x$, $A_y$ and a moment $M_A$ (counter-clockwise assumed). Draw 1200 N down at $x = 2$ m and the weight $W = 100(9.81) = 981$ N down at the centroid $x = 3$ m.

**Solution:**
- $\sum F_x=0 \Rightarrow A_x=0$
- $\sum F_y=0 \Rightarrow A_y = 1200 + 981 = 2181$ N
- $\sum M_A=0:\ M_A - 1200(2) - 981(3) = 0 \Rightarrow M_A = 2400 + 2943 = 5343$ N·m

$$\boxed{A_y = 2181\ \text{N}\ \uparrow,\quad M_A = 5.34\ \text{kN·m (counter-clockwise on the beam)}}$$

**Takeaway:** the common slip is forgetting the 981 N self-weight or putting it at the wrong point. The weight acts at $L/2$, **not** at the load point.

---

#### Q3 (Slides Ch1) — Diving board *(easy–medium)*
**Given:** board mass 36 kg (centroid at 2.4 m from A), person 54 kg at 4.6 m. Pin at A ($x=0$), roller at B ($x=1.2$ m). **Find:** reactions at A and B.

**Solution:** $W_D = 36(9.81)=353.2$ N and $W_P = 54(9.81)=529.7$ N.
- $\sum M_A = 0:\ B(1.2) - 353.2(2.4) - 529.7(4.6) = 0 \Rightarrow B = \dfrac{847.6+2436.8}{1.2} = 2737$ N
- $\sum F_y=0:\ A + B - 353.2 - 529.7 = 0 \Rightarrow A = 882.9 - 2737 = -1854$ N

$$\boxed{B = 2737\ \text{N}\ (\uparrow),\qquad A = 1854\ \text{N}\ (\downarrow)}$$

**Check:** the board is a lever over the roller B, so the pin at A must hold the end **down**. A negative $A$ means "opposite to the direction assumed". ✓
**Takeaway:** examiners like supports that pull the wrong way. Don't flip the sign without saying so in words.

---

#### Q4 (Slides Ch1) — Two cylinders in a box *(medium)*
**Given:** cylinders P and Q, each weighing 900 N. P rests on the floor (B) and against the left wall (A). Q rests on P and against the right wall (C). The line of centres is at 45°. All surfaces smooth. **Find:** FBDs and reactions at A, B, C.

**FBD of Q:** weight 900 N ↓, wall reaction $R_C$ ← (horizontal), and contact force $N$ from P along the line of centres, pointing up and to the right at 45°.
- $\sum F_y:\ N\sin45^\circ = 900 \Rightarrow N = 1272.8$ N
- $\sum F_x:\ R_C = N\cos45^\circ = 900$ N

**FBD of P:** weight 900 N ↓, $R_A$ → (wall), $R_B$ ↑ (floor), and $N = 1272.8$ N from Q pointing down and to the left at 45° (Newton's 3rd law).
- $\sum F_x:\ R_A = N\cos45^\circ = 900$ N
- $\sum F_y:\ R_B = 900 + N\sin45^\circ = 1800$ N

**Both cylinders together:** the internal force $N$ cancels. $R_B = 1800$ N (total weight) and $R_A = R_C$ ✓.
$$\boxed{R_A = 900\ \text{N},\quad R_B = 1800\ \text{N},\quad R_C = 900\ \text{N}}$$
**Takeaway:** the combined FBD checks the individual ones. Variation: if the angle is $\theta$, then $R_A = R_C = W\cot\theta$.

---

#### Q5 (Crandall Prob 1.13, Slides) — Lawn roller over a step *(medium)*
**Given:** roller weight $W = 900$ N, diameter 0.6 m (so $r=300$ mm). Step height $h = 75$ mm. Handle at 30° to the horizontal, with the force $F$ acting through the axle. **Find:** $F$ to just start the roller over the step when (a) pushed (F points down at 30°) and (b) pulled (F points up at 30°).

**Key idea:** at the instant of "just starting", the roller leaves the ground, so the ground reaction is **zero**. Only three forces act: $W$, $F$, and the step-corner reaction $R$. Take moments about the corner so that $R$ drops out.

**Geometry:** the corner is at vertical distance $r-h = 225$ mm below the axle. Its horizontal offset is
$$a=\sqrt{r^2-(r-h)^2}=\sqrt{300^2-225^2}=198.4\ \text{mm}$$

**(a) Pushed:** $F$ has components $F\cos30^\circ$ toward the step and $F\sin30^\circ$ downward. About the corner:
$$F\cos30^\circ\,(225) = W(198.4) + F\sin30^\circ(198.4)$$
$$F = \frac{900(198.4)}{225\cos30^\circ - 198.4\sin30^\circ} = \frac{178{,}600}{194.9-99.2}\ \Rightarrow\ \boxed{F_{push}\approx 1867\ \text{N}}$$

**(b) Pulled:** now the vertical component helps lift the roller:
$$F\cos30^\circ(225) + F\sin30^\circ(198.4) = W(198.4)\ \Rightarrow\ \boxed{F_{pull}\approx 607.3\ \text{N}}$$
(The slides give 1866.05 N and 607.28 N. The difference is rounding.)

**Check by geometry:** $R$ must pass through the axle (three-force member, since all three forces are concurrent at the centre). ✓ Pulling is about 3× easier because pulling lifts the roller, while pushing presses it into the ground.
**Takeaway:** "just starts to move over" means the ground reaction is zero. Variation: find the *minimum* force and its direction. It is perpendicular to the line from the corner to the centre, giving $F_{min} = W\sin\phi$ where $\cos\phi = (r-h)/r$, so $F_{min} = 900(198.4/300) = 595$ N.

---

#### Q6 (Slides Ch1) — Pliers *(medium)*
**Given:** in the FBD of one handle, the bolt force $F_B$ acts downward at B, 25 mm left of pin C. The hand force of 20 N acts at 45° (down and to the left) at a point 80 mm right of and 50 mm below C. **Find:** $C_x$, $C_y$, $F_B$.

**Solution (C at the origin, x to the right, y up):** the 20 N force is $(-14.14, -14.14)$ N at $(80, -50)$ mm.
$$M_C^{(20N)} = x F_y - y F_x = 80(-14.14) - (-50)(-14.14) = -1838.5\ \text{N·mm (clockwise)}$$
$$\sum M_C = 0:\ F_B(25) - 1838.5 = 0 \Rightarrow \boxed{F_B = 73.5\ \text{N}}$$
- $\sum F_x:\ C_x - 14.14 = 0 \Rightarrow \boxed{C_x = 14.1\ \text{N}}$
- $\sum F_y:\ C_y - 73.5 - 14.14 = 0 \Rightarrow \boxed{C_y = 87.7\ \text{N}}$

**Check:** a 20 N squeeze gives a 73.5 N bite, a mechanical advantage of about 3.7. That is reasonable for pliers. ✓

---

#### Q7 (Slides Ch1) — Bicycle hand brake *(easy)*
**Given:** $P = 70$ N, the resultant of a uniform hand pressure acting between 50 mm and 100 mm from pivot A (so $P$ acts at 75 mm). Cable arm = 37.5 mm. Cable length 460 mm. **Find:** $T$.

$$\sum M_A = 0:\ T(37.5) = 70(75)\ \Rightarrow\ \boxed{T = 140\ \text{N}}$$
**Takeaway:** the 460 mm cable length is a **distractor**. It would only matter for a cable-stretch question (Ch. 2: $\delta = TL/AE$).

---

## Concept 1.3 — Dry (Coulomb) friction

### A. Concept explanation

**1. Intuition.** Push a heavy box lightly and it doesn't move. The floor pushes back sideways exactly as hard as you push, up to a limit. Past that limit it slides. The limit grows if the box is heavier (bigger normal force) but does **not** depend on how big its base is.

**2. Why it matters.** Wedges, belts, brakes, bolts, the trunk on a ramp, and (in a PYQ) a rope over a drum.

**3. Formal treatment (slides).**
- No relative motion → **static** friction $f_s$. It can take *any* value from 0 up to $f_{s,max}$, whatever equilibrium needs.
- Limiting (impending motion): $f_{s,max} = \mu_s N$.
- Sliding → **kinetic** friction $f_k = \mu_k N$, roughly constant and slightly less than $f_{s,max}$.
- Friction is independent of contact area (slides). If the area doubles at the same $N$, the force per unit area halves.
- Friction always acts **opposite to the impending relative motion**.

Slide example: $f_{s,max}=10$ N. With an 8 N push, $f = 8$ N and there is no motion. With a 12 N push, the block moves. With no push, $f=0$, **not** $\mu N$.

**4. Derivations.**

*(a) Block on an incline, angle $\alpha$, pulled up the slope by tension $T$:*
- Impending motion **up**: friction acts down the slope. $T = W(\sin\alpha + \mu\cos\alpha)$
- Impending motion **down**: friction acts up the slope. $T = W(\sin\alpha - \mu\cos\alpha)$

Equilibrium holds for any $T$ between these two values.

*(b) Angle of repose:* with no applied force, the block is about to slide when $W\sin\alpha = \mu W\cos\alpha$, so $\tan\alpha = \mu$.

*(c) Belt/rope friction (needed for PYQ 2014 Q3).* Take a small rope element subtending $d\theta$ on a drum. Tension is $T$ on one side and $T+dT$ on the other. Normal force is $dN$ and friction is $\mu\,dN$.
- Radial: $dN = T\,d\theta$ (since $\sin(d\theta/2)\approx d\theta/2$, and both tensions contribute).
- Tangential, at impending slip: $dT = \mu\,dN = \mu T\,d\theta$.
- Integrate: $\displaystyle\int_{T_1}^{T_2}\frac{dT}{T} = \mu\int_0^\beta d\theta$, so
$$\boxed{\frac{T_2}{T_1} = e^{\mu\beta}}$$
Here $T_2$ is the tight side and $\beta$ is the wrap angle **in radians**. Tension along the contact varies as $T(\theta) = T_1 e^{\mu\theta}$.

**5. Graphical picture.** The total reaction $R$ (combining $N$ and $f$) leans away from the normal by at most the friction angle $\phi$, where $\tan\phi = \mu$. Equilibrium is possible as long as the resultant of the applied forces falls inside this "friction cone".

**6. Special cases.** $\mu=0$ gives a smooth surface, where the reaction is purely normal. $\beta = \pi$ (half wrap) gives $T_2/T_1 = e^{\mu\pi}$.

**7. Common traps.**
- Writing $f = \mu N$ when the problem does **not** say motion is impending.
- Getting the friction direction wrong. Decide which way the body *would* slide.
- Forgetting that $N$ changes when the applied force has a component normal to the surface.
- Using degrees in $e^{\mu\beta}$.

**8. Summary box**
| Situation | Equation |
|---|---|
| Not slipping | $f \le \mu_s N$ (find $f$ from equilibrium) |
| Impending | $f = \mu_s N$, opposing impending motion |
| Incline, impending up/down | $T = W(\sin\alpha \pm \mu\cos\alpha)$ |
| Rope on drum | $T_2/T_1 = e^{\mu\beta}$ |

### B. Solved questions

#### Q8 (Slides Ch1) — Range of $W$ for a block on an incline *(easy)*
**Given:** a 500 N block on a 3-4-5 incline ($\sin\alpha = 0.6$, $\cos\alpha = 0.8$). The cable runs parallel to the incline over a frictionless pulley to a hanging weight $W$. $\mu_s = 0.5$. **Find:** the range of $W$ for equilibrium.

Cable tension $T = W$.
- Impending **down** (smallest $W$): $W_{min} = 500(0.6 - 0.5\times0.8) = 100$ N
- Impending **up** (largest $W$): $W_{max} = 500(0.6 + 0.5\times0.8) = 500$ N

$$\boxed{100\ \text{N} \le W \le 500\ \text{N}}$$
**Check:** $\tan\alpha = 0.75 > \mu = 0.5$, so the block would slide down on its own. That is why $W_{min} > 0$. ✓

---

#### Q9 (Crandall Prob 1.45, Slides) — Trunk on a ramp *(medium)*
**Given:** a man can *just start* pushing a trunk up a 30° ramp. With the same push (parallel to the ramp) he can *just hold it from sliding back* on a 60° ramp. **Find:** $\mu_s$.

- 30°, impending up: $P = W(\sin30^\circ + \mu\cos30^\circ)$
- 60°, impending down: $P = W(\sin60^\circ - \mu\cos60^\circ)$

Set them equal: $0.5 + 0.866\mu = 0.866 - 0.5\mu \Rightarrow 1.366\mu = 0.366$
$$\boxed{\mu_s = 0.268\ (=\tan 15^\circ = 2-\sqrt3)}$$
**Check:** $\mu < \tan30^\circ$, so the trunk would slide down the 30° ramp unaided. That is consistent with him needing to push. ✓
**Takeaway:** "barely start pushing up" and "barely hold from sliding" are the two impending-motion directions. Friction flips between them.

---

#### Q10 (Crandall Prob 1.37, Slides) — Cylinder on two half-cylinders *(hard)*
**Given:** cylinder A (weight $W$, radius $r$) rests on half-cylinders B and C (each $W/2$, radius $r$). Their flat faces sit on a table with friction coefficient $f$. The cylinder-to-cylinder contacts are smooth. **Find:** the maximum distance $d$ between the centres of B and C.

**Geometry:** the centres of A and B are $2r$ apart. The horizontal offset is $d/2$. Let $\theta$ be the angle of line AB from the vertical, so $\sin\theta = \dfrac{d}{4r}$.

**FBD of A:** by symmetry, the contact forces $N$ from B and C act along the lines of centres. $2N\cos\theta = W \Rightarrow N = \dfrac{W}{2\cos\theta}$.

**FBD of B:** $N$ pushes B down and outward. Its horizontal component is $N\sin\theta = \tfrac{W}{2}\tan\theta$. The table gives normal force $W/2 + W/2 = W$ and friction $F \le fW$.
$$\tfrac{W}{2}\tan\theta \le fW \Rightarrow \tan\theta \le 2f$$

With $\tan\theta = 2f$, $\sin\theta = \dfrac{2f}{\sqrt{1+4f^2}}$, so
$$\boxed{d_{max} = 4r\sin\theta = \frac{8rf}{\sqrt{1+4f^2}}}$$
**Check:** $f\to 0$ gives $d\to 0$ (no friction, so they must touch). $f\to\infty$ gives $d \to 4r$, which is the geometric limit where A falls through. ✓
**Takeaway:** the normal from table to B is $W$, not $W/2$. It carries half of A's weight as well as B's own weight.

---

#### Q11 (PYQ 2014-15 Test-1 Q3) — Rope over a fixed drum *(medium, combines Ch 1 and Ch 2)*
**Given:** steel rope $d = 10$ mm, $E = 200$ GPa, over a fixed drum of diameter 1.5 m. Hanging weights are 1 kN (at A) and 4 kN (at B), with 180° of contact. The rope is just about to slip. **Find:** (a) $\mu$, (b) the elongation of the rope segment AB (the part in contact with the drum).

**(a)** $T_2/T_1 = e^{\mu\pi} \Rightarrow 4 = e^{\mu\pi}$
$$\boxed{\mu = \frac{\ln 4}{\pi} = 0.441}$$

**(b)** The tension varies along the contact: $T(\theta) = T_1 e^{\mu\theta}$, with $ds = r\,d\theta$. The elongation of a segment with varying force is $\delta = \int \frac{T\,ds}{AE}$ (Ch. 2):
$$\delta = \frac{r}{AE}\int_0^\pi T_1 e^{\mu\theta}d\theta = \frac{rT_1}{AE\mu}\left(e^{\mu\pi}-1\right) = \frac{r(T_2-T_1)}{AE\mu}$$
Here $A = \tfrac{\pi}{4}(10)^2 = 78.54$ mm², $AE = 78.54\times200{,}000 = 1.571\times10^7$ N, and $r = 750$ mm.
$$\delta = \frac{750(3000)}{1.571\times10^7\times0.441} \Rightarrow \boxed{\delta_{AB} \approx 0.325\ \text{mm}}$$
**Check:** if the whole arc carried the average tension, $\bar T = (1+4)/2 = 2.5$ kN, then $\delta = 2500(\pi\times750)/1.571\times10^7 = 0.375$ mm. The exact value is a bit lower because the true tension curve is exponential, not linear. Same order of magnitude. ✓
**Takeaway:** this "friction plus axial deformation" combination shows exactly how Test-1 mixes Ch. 1 and Ch. 2.

---

## Concept 1.4 — Plane trusses

### A. Concept explanation

**1. Intuition.** A truss is a skeleton of straight sticks pinned at the ends, like a Meccano bridge. If loads are applied only at the joints, each stick is either pulled (tension) or squashed (compression) along its length. There is no bending. Solving a truss means finding that one number for every stick.

**2. Why it matters.** Bridges, roof trusses, cranes, towers. Every member is a **two-force member** (Concept 1.2), and in Ch. 2 we use the member forces to get deflections with $\delta = FL/AE$ and Castigliano's theorem.

**3. Formal treatment — ideal truss assumptions (slides):**
1. Members are connected only at their ends.
2. Connections are frictionless pins.
3. Loads are applied only at the joints.
4. Member weights are neglected.

Each member is therefore a two-force member, in tension or compression.

**Stability / determinacy (slides):** with $m$ members, $j$ joints and 3 support reactions:
- $m = 2j-3$: rigid and statically determinate ("perfect")
- $m < 2j-3$: unstable, collapsible
- $m > 2j-3$: over-rigid, statically indeterminate

*Why:* each joint gives 2 equations ($\sum F_x$, $\sum F_y$), so there are $2j$ equations. The unknowns are $m$ member forces plus 3 reactions. Determinate when $m + 3 = 2j$.
(Slide example: $m=13$, $j=8$, $13 = 2(8)-3$ ✓.)

**Zero-force members (slides):**
1. Two non-collinear members meet at an unloaded, unsupported joint → **both** are zero.
2. Three members meet at an unloaded joint and two are collinear → the **third** is zero.

*Why rule 2:* sum forces perpendicular to the collinear pair. Only the third member has a component in that direction, so it must be zero.

**Method of joints (slides):**
1. Find the support reactions from the whole truss. (Not needed for a cantilever truss if you start at the free end.)
2. Pick a joint with at most 2 unknowns. **Assume every unknown member force is tensile** (arrow pointing away from the joint).
3. Apply $\sum F_x = \sum F_y = 0$ and move from joint to joint.
4. Tabulate: member, force, T/C. A negative answer means compression.

**Method of sections (slides):** use it when only a few members are wanted.
1. Find reactions if needed.
2. Cut through **at most 3 members** (including the wanted ones). The cut must split the truss into two separate parts and pass through members, not joints.
3. Keep the part with fewer forces.
4. Use the 3 equilibrium equations. Take moments about the point where two of the unknown forces intersect, so you get one equation in one unknown.

**4. Derivation — moment trick.** If the cut members are a top chord (force $F_1$), a bottom chord ($F_2$) and a diagonal ($F_3$), then $F_2$ and $F_3$ meet at a bottom joint. Taking moments about that joint gives $F_1 h = M_{\text{external}}$, so $F_1 = M/h$. A truss chord behaves like the flange of a beam: chord force = bending moment / depth. This links forward to Ch. 3.

**5. Geometric check.** In a cantilever truss under downward loads, the top chord is in tension and the bottom chord in compression (the truss "hogs"). In a simply supported truss it is the opposite.

**6. Special cases.** A diagonal's vertical component equals the shear in that panel: $F_{diag}\sin\theta = V$.

**7. Common mistakes.**
- Mixing up "T assumed" and "C answer". Keep the sign convention fixed.
- Passing a section through a joint.
- Cutting 4 unknown members and expecting 3 equations to solve them.
- Getting angles wrong. Always compute $\tan\theta$ from the dimensions.

**8. Summary box**
| Tool | Use when |
|---|---|
| $m=2j-3$ | Check determinacy first |
| Zero-force rules | Spot them before starting; they save time |
| Joints | All member forces wanted |
| Sections | 1–3 specific members wanted; take moments about the intersection of the other two |

### B. Solved questions

#### Q12 (Slides Ch1) — A-frame truss *(easy–medium)*
**Given:** A (pin) and B (roller) are 6 m apart. Apex C is 2.25 m above midpoint D. Members AC, BC, CD, AD, BD. Loads: 10 kN down at D, and 20 kN at C acting down and to the right, 30° from the vertical. **Find:** reactions and all member forces.

**Geometry:** $AC = BC = \sqrt{3^2+2.25^2}=3.75$ m, so $\sin\theta = 0.6$ and $\cos\theta = 0.8$.
**Load at C:** $(+20\sin30^\circ, -20\cos30^\circ) = (10, -17.32)$ kN.

**Reactions:**
- $\sum F_x$: $A_x = -10$ kN (10 kN to the left)
- $\sum M_A$: $B_y(6) - 10(3) - [17.32(3) + 10(2.25)] = 0 \Rightarrow B_y = 17.41$ kN
- $A_y = 27.32 - 17.41 = 9.91$ kN

**Joints:**
- **D:** CD is the only vertical member, so $F_{CD} = 10$ kN (T). The horizontal members give $F_{AD}=F_{BD}$.
- **A:** $0.6F_{AC} + 9.91 = 0 \Rightarrow F_{AC} = -16.52$ kN (C). Then $0.8(-16.52)+F_{AD}-10=0 \Rightarrow F_{AD}=23.21$ kN (T).
- **B:** $0.6F_{BC} + 17.41 = 0 \Rightarrow F_{BC} = -29.02$ kN (C). $F_{BD} = 23.21$ kN (T) ✓.

| Member | Force (kN) | Nature |
|---|---|---|
| AC | 16.52 | C |
| BC | 29.02 | C |
| CD | 10.00 | T |
| AD | 23.21 | T |
| BD | 23.21 | T |

*(The slide table labels the first row "AB". It means AC, since there is no member AB.)*

---

#### Q13 (Slides Ch1) — Warren truss, 2000 N and 4000 N *(medium)*
**Given:** equilateral panels of 3 m. Bottom A (pin), B, C (roller). Top D (above $x=1.5$), E (above $x=4.5$). 2000 N at D and 4000 N at E. **Find:** all member forces.

$h = 1.5\tan60^\circ = 2.598$ m. Reactions: $C_y = (2000\times1.5+4000\times4.5)/6 = 3500$ N and $A_y = 2500$ N.

- **Joint A:** $F_{AD}\sin60^\circ + 2500 = 0 \Rightarrow F_{AD} = -2886.8$ (C). $F_{AB} = -F_{AD}\cos60^\circ = 1443.4$ (T).
- **Joint C:** $F_{CE} = -3500/\sin60^\circ = -4041.5$ (C). $F_{BC} = 2020.7$ (T).
- **Joint D:** $y$: $-0.866F_{DA} - 0.866F_{DB} - 2000 = 0 \Rightarrow F_{DB} = \dfrac{-2000 + 0.866(2886.8)}{0.866} = 577.4$ (T). $x$: $-0.5F_{DA}+0.5F_{DB}+F_{DE}=0 \Rightarrow F_{DE} = -1443.4-288.7 = -1732.1$ (C).
- **Joint E:** $y$: $-0.866F_{EB} - 0.866F_{EC} - 4000 = 0 \Rightarrow F_{EB} = \dfrac{-4000+3500}{0.866} = -577.4$ (C).

| Member | AB | BC | AD | BD | BE | CE | DE |
|---|---|---|---|---|---|---|---|
| Force (N) | 1443.4 T | 2020.7 T | 2886.8 C | 577.4 T | **577.4 C** | 4041.5 C | 1732.1 C |

⚠️ **The slide table lists BE = 500 N (C). That is a slip:** $500$ is the *vertical component*. The member force is $500/\sin60^\circ = 577.4$ N. A computer solve of the whole truss confirms this.
**Check:** BD and BE carry the panel shear (2500 − 2000 = 500 N) in opposite senses ✓.

---

#### Q14 (Slides Ch1) — Cantilever truss *(medium)*
**Given:** wall joints A (top, $y=1.8$ m) and E (bottom). Top chord A–B–C with panels of 2.4 m. Bottom joint D below B. Members AB, BC, AD, BD, CD, ED. 30 kN down at B and at C. **Find:** all forces (no reactions needed if you start at the free end C).

$\tan\theta = 1.8/2.4 \Rightarrow \theta = 36.87^\circ$.
- **Joint C:** $30 + F_{CD}\sin\theta = 0 \Rightarrow F_{CD} = -50$ kN (C). $F_{BC} = -F_{CD}\cos\theta = 40$ kN (T).
- **Joint B:** $F_{BA} = 40$ kN (T). $F_{BD} = -30$ kN (C).
- **Joint D:** $y$: $F_{DA}\sin\theta = 30 + 50\sin\theta \Rightarrow F_{DA}=100$ kN (T). $x$: $F_{DE} = -120$ kN (C).

$$\boxed{BC=40\,T,\ CD=50\,C,\ BD=30\,C,\ AB=40\,T,\ AD=100\,T,\ DE=120\,C\ (\text{kN})}$$
(The slides show 40.01, 50.01 and so on because they rounded θ to 36.86°.)

---

#### Q15 (Slides Ch1, "Question 2") — Find P from a member force *(medium, sections)*
**Given:** cantilever truss (60° triangles, height 2 m) with loads $P$ at C and E. The force in AC must be 3 kN. **Find:** $P$.

Cut through AC, CD and the bottom member at D. Take moments about D, where CD and the bottom chord meet. The slide's result is $F_{AC}(2) - P(1.5) - P(4.5) = 0$, so $F_{AC} = 3P$.
$$3P = 3\ \text{kN} \Rightarrow \boxed{P = 1\ \text{kN}}$$

---

#### Q16 (Slides Ch1, Hibbeler-type) — Sections: GE, GC, BC *(medium)*
**Given:** pin A, roller D. Panels of 4 m, height 3 m. 400 N horizontal at E and 1200 N down at C. **Find:** $F_{GE}, F_{GC}, F_{BC}$.

Reactions: $A_x = 400$ N ←. $\sum M_A$: $D_y(12) - 1200(8) - 400(3) = 0 \Rightarrow D_y = 900$ N. $A_y = 300$ N.
Section a–a cuts GE, GC and BC. Take the left part (A, B, G).
- $\sum M_G$ (G at $x=4$, $y=3$). $A_y=300$ ↑ at 4 m to the left gives −1200 N·m. $A_x=400$ ← at 3 m below gives −1200 N·m. $F_{BC}$ (tension, →) at 3 m below gives $+3F_{BC}$. So $-2400 + 3F_{BC} = 0 \Rightarrow F_{BC}=800$ N (T)
- $\sum M_C$ (C at $x = 8$, $y=0$). $A_y$ gives $-300(8) = -2400$. $A_x$ is on the line through C, so 0. $F_{GE}$ (→) at 3 m above gives $-3F_{GE}$. So $F_{GE} = -800$ N (C)
- $\sum F_y$: $300 - F_{GC}(3/5) = 0 \Rightarrow F_{GC} = 500$ N (T)

$$\boxed{F_{GE}=800\ \text{N (C)},\quad F_{GC}=500\ \text{N (T)},\quad F_{BC}=800\ \text{N (T)}}$$

---

#### Q17 (Slides Ch1) — Sections with a 20 kN horizontal load *(medium)*
**Given:** top B–C–E–G–I and bottom A–D–F–H–J, all panels 3 m, height 3 m. Diagonals AC, CF, FG, GJ. A is a pin, J a roller. 20 kN horizontal (→) at B. **Find:** $F_{CE}, F_{CF}, F_{FH}$.

Reactions: $A_x = 20$ ←. $\sum M_A$: $J_y(12) = 20(3) \Rightarrow J_y = 5$ kN ↑, so $A_y = 5$ kN ↓.
- Cut CE, CF, DF. Left part. Moments about F$(6,0)$: $-20(3) + 5(6) - 3F_{CE} = 0 \Rightarrow F_{CE} = -10$ kN (**C**)
- Same cut, $\sum F_y$: $-5 - F_{CF}/\sqrt2 = 0 \Rightarrow F_{CF} = -7.07$ kN (**C**)
- Cut EG, FG, FH. Right part. Moments about G$(9,3)$: $5(3) - 3F_{FH} = 0 \Rightarrow F_{FH} = 5$ kN (**T**)

$$\boxed{F_{CE}=10\ \text{kN C},\ F_{CF}=7.07\ \text{kN C},\ F_{FH}=5\ \text{kN T}}$$ ✓ matches the slide.

---

#### Q18 (Slides Ch1) — Zero-force members + one cut *(medium)*
**Given:** cantilever truss. Top B–C–E–G (3 m spacings). Bottom chord A–D–F–G sloping at 40° at G. Verticals CD and EF. Diagonal CF. 10 kN at G. **Find:** $F_{CE}$, $F_{CD}$.

- **Joint G:** $F_{GF}\sin40^\circ = -10 \Rightarrow F_{GF} = -15.56$ kN (C). $F_{GE} = -F_{GF}\cos40^\circ = 11.92$ kN (T).
- **Joint E:** CE and EG are collinear and EF is the third member, with no load → $F_{EF}=0$ (zero-force rule 2). So $F_{CE}=F_{EG}=11.92$ kN (T).
- **Joint F:** DF and FG are collinear, EF = 0, so CF is the odd one out → $F_{CF}=0$.
- **Joint C:** BC and CE are collinear, CF = 0, so the vertical CD is the odd one out → $F_{CD}=0$.

$$\boxed{F_{CE} = 11.92\ \text{kN (T)},\qquad F_{CD} = 0}$$

---

#### Q19 (Slides Ch1) — Identify zero-force members *(easy)*
Upper truss: $F_{FD}$ and $F_{GE}$ (the verticals at unloaded bottom joints F and G, where the bottom chord is collinear).
Lower truss: $F_{BC}, F_{FG}, F_{FI}, F_{HI}, F_{HK}, F_{JK}$. Apply rule 2 repeatedly, working inward from the unloaded joints.
**Takeaway:** after finding one zero member, remove it and check the neighbouring joint again. The rules cascade.

---

#### Q20 (PYQ 2014-15 Test-1 Q1) — Cantilever truss, find $W$ *(medium)*
**Given:** top A–B–C–D and bottom G–F–E. $AB=BC=CD=EF=FG=6$ m and $BF=CE=4$ m. Diagonals GB, FC, ED. Wall supports at A and G. Loads $W$ at B, C, D. $|F_{BC}| = 450$ kN. **Find:** $W$.

Cut BC, FC and FE. Keep the right part (C, D, E). Take moments about F, where FC and FE meet:
$$F_{BC}(4) - W(6) - W(12) = 0 \Rightarrow F_{BC} = 4.5W$$
$$4.5W = 450 \Rightarrow \boxed{W = 100\ \text{kN}}\quad (BC\ \text{in tension})$$
**Check:** a full joint-by-joint solve with W = 100 gives BC = 450.0 kN T, AB = 900 kN T and GF = 450 kN C. The top chord is in tension, as expected for a cantilever. ✓
**Takeaway:** "find the load that gives force X in member Y" means **method of sections** with moments about a cleverly chosen point. It is a 15-mark question that takes 3 lines once you see the right point.

---

## Chapter 1 — Formula and convention sheet

| Topic | Key relation |
|---|---|
| Equilibrium (2-D) | $\sum F_x=\sum F_y=\sum M_O=0$ |
| Two-force member | Forces equal, opposite, along the line of the pins |
| Three-force member | Lines of action concurrent (or all parallel) |
| Static friction | $f\le\mu_s N$; at impending motion $f=\mu_s N$ |
| Incline, impending | $T=W(\sin\alpha\pm\mu\cos\alpha)$; angle of repose $\tan\alpha=\mu$ |
| Belt friction | $T_2/T_1=e^{\mu\beta}$ ($\beta$ in rad) |
| Truss determinacy | $m=2j-3$ |
| Zero-force rules | 2 non-collinear unloaded → both 0; 3 with 2 collinear unloaded → third 0 |
| Sections | Cut ≤ 3 members; moments about the intersection of 2 unknowns |
| Sign | Assume tension; negative answer = compression |

**Other Crandall Ch. 1 problems worth practising** (same patterns): FBD drills (Probs 1.1–1.10), friction (Probs 1.38–1.46), trusses in the problem set.
