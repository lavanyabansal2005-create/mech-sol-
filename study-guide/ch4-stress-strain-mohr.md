# Chapter 4 — Stress and Strain
### Stress at a point, plane stress, stress transformation, Mohr's circle, principal and maximum shear stresses, thin-walled pressure vessels, plane strain, strain transformation, Mohr's circle of strain, strain rosettes

**Sources used:** Slides "Chapter 4 part 1" (stress) and "Ch 4 Part 2" (strain); Crandall Ch. 4 (§4.2–4.9; the sheet-metal strain example; Probs 4.6–4.15, 4.20–4.23, 4.25, 4.27, 4.28, 4.32, 4.34); PYQs 2019-20 (A-Q2), 2021-22 (A-Q1, B-Q1), 2014-15 (Test-2 Q1, Q2; Compre A-Q12, Q13; Compre B-Q1).

**Layout.** Part A (eight items) for each concept, then Part B: slides → Crandall → PYQs, easy → hard. Each solution follows *Problem · Given/Find · Approach · Sketch · Steps · Answer · Check · Takeaway*.

---

## ⚠ Read first: sign conventions for this chapter

1. **Stress sign (Crandall, slides):** a stress component is **positive** when it acts on a **positive face in a positive direction**, or on a **negative face in a negative direction**. Tension is +. $\tau_{xy} > 0$ means that on the right (+x) face the shear points **up** (+y).
2. **Angle θ:** measured **counter-clockwise from x to x′**, the outward **normal** of the face of interest.
3. **Mohr's circle (Crandall and slides use the same rule):** σ is plotted to the right (tension positive). **A positive $\tau_{xy}$ is plotted *downward* at point x and *upward* at point y.** With this rule, **a counter-clockwise rotation of 2θ on the circle corresponds to a counter-clockwise rotation θ of the element.** Beer/Hibbeler's "positive shear (clockwise on the element) plotted up" gives the same circle.
   - If you plot $\tau_{xy}$ *upward* at x (the "maths" convention), the circle is mirrored and the 2θ rotations reverse direction. This is the most common Mohr's-circle mistake in the exam.
4. **Strain Mohr's circle:** the vertical axis is **γ/2**, not γ. Same plotting rule: $+\gamma_{xy}/2$ is plotted downward at x.

---

## Concept 4.1 — Stress at a point and the stress tensor

### A. Concept explanation

**1. Intuition.** Squeeze a sponge in your hand. Every tiny cube inside it is pushed and dragged by its neighbours. "Stress" is the intensity of that push or drag, force per unit area, on a particular imaginary cut. A single number isn't enough, because the answer depends on *which way* you slice. Slice one way and the material is being pulled apart; slice at 45° and it may be sliding.

**2. Why it matters (the slides' motivating example).** A bracket ABC carries 30 kN at B: AC is 2 m horizontal and BC is a 20 mm diameter rod rising 1.5 m. Statics gives $F_{BC} = 50$ kN (T) and $F_{AC} = 40$ kN (C). "But still it cannot be said whether rod BC can support this load" (slide). That depends on (1) the internal force, (2) the cross-sectional area of the rod and (3) the material. Stress is the bridge from forces (Ch. 1–3) to material failure (Ch. 5).

**3. Formal treatment (Crandall §4.2–4.3; slide figures).** Cut the body through point O by a plane with normal **n**. On a small area ΔA the internal force is ΔF. For an x-face ($\Delta A_x = \Delta y\Delta z$):
$$\sigma_x = \lim_{\Delta A_x\to0}\frac{\Delta F_x}{\Delta A_x},\qquad \tau_{xy} = \lim\frac{\Delta F_y}{\Delta A_x},\qquad \tau_{xz} = \lim\frac{\Delta F_z}{\Delta A_x}$$
The first subscript is the **face normal** and the second the **direction**. Doing this on all three faces gives the **stress tensor**:
$$\begin{bmatrix}\sigma_x & \tau_{xy} & \tau_{xz}\\ \tau_{yx} & \sigma_y & \tau_{yz}\\ \tau_{zx} & \tau_{zy} & \sigma_z\end{bmatrix}$$
**Plane stress (slides):** the only non-zero stress components act in one plane: $\sigma_z = \tau_{zx} = \tau_{zy} = 0$. Two faces of the cubic element are free of stress. This is typical of thin plates loaded in their plane, and of the free surface of any part, which is where every strain gauge sits.

**4. Derivation — equilibrium of a differential element (Crandall Fig. 4.10; slides).** Take an element Δx × Δy × Δz in plane stress, with stresses varying from face to face (e.g. $\sigma_x$ on the left, $\sigma_x + \frac{\partial\sigma_x}{\partial x}\Delta x$ on the right).
- *Moments about the z-axis through the centre:* $(\tau_{xy}\Delta y\Delta z)\Delta x - (\tau_{yx}\Delta x\Delta z)\Delta y + (\text{higher-order terms}) = 0$. Dividing by $\Delta x\Delta y\Delta z$ and letting the element shrink:
$$\boxed{\tau_{xy} = \tau_{yx}}$$
Shear stresses on perpendicular faces are equal, and they point toward or away from the same corner.
- *Force balance in x and y* (no body force):
$$\boxed{\frac{\partial\sigma_x}{\partial x} + \frac{\partial\tau_{xy}}{\partial y} = 0,\qquad \frac{\partial\tau_{xy}}{\partial x} + \frac{\partial\sigma_y}{\partial y} = 0}$$
In 3-D, only six of the nine stress components are independent (Crandall Prob 4.1 adds the z-equation; Prob 4.2 adds body forces X, Y, Z).

**5. Picture.** A positive $\tau_{xy}$ element (Crandall Fig. 4.11): arrows ↑ on the right face, ↓ on the left face, → on the top face and ← on the bottom face. The element is pushed into a rhombus that is stretched along the diagonal joining the first-quadrant and third-quadrant corners.

**6. Special cases.** Uniaxial: only $\sigma_x$. Hydrostatic: $\sigma_x = \sigma_y = \sigma_z = -p$, with no shear on any plane. Pure shear: only $\tau_{xy}$.

**7. Traps.**
- Drawing $\tau_{yx}$ opposite to $\tau_{xy}$ on adjacent faces. They must meet head-to-head or tail-to-tail at the corners.
- Adding stresses that act on differently oriented faces. Stresses only add component by component on the **same** element orientation (PYQ 2014 Compre B Q1).

**8. Summary.** Stress = force/area on a specified face. Plane stress is described by $(\sigma_x, \sigma_y, \tau_{xy})$ with $\tau_{xy} = \tau_{yx}$.

### B. Solved questions

#### Q1 (Slides Ch4, motivating example) — Can rod BC carry 30 kN? *(easy)*
**Problem.** A bracket has a horizontal member AC (2 m) and a 20 mm diameter rod BC (B at 1.5 m below C). A load P = 30 kN hangs at B. Find the member forces and the stress in BC; compare with an allowable stress of 165 MPa (structural steel).

**Approach.** Joint B is a two-member joint; then σ = F/A.

**Solution.**
1. *Joint B* (BC rising at $\tan^{-1}(1.5/2)$, so $\sin = 0.6$ and $\cos = 0.8$): vertical: $0.6F_{BC} = 30$, so $F_{BC} = 50$ kN (T). Horizontal: $F_{AB} = 0.8(50) = 40$ kN (C).
2. *Stress:* $\sigma_{BC} = \dfrac{50\,000}{\pi(10)^2} = \dfrac{50\,000}{314.2} = 159$ MPa.

$$\boxed{F_{BC} = 50\ \text{kN (T)},\quad F_{AB} = 40\ \text{kN (C)},\quad \sigma_{BC} = 159\ \text{MPa} < 165\ \text{MPa} \Rightarrow \text{safe}}$$

**Check.** 50 kN on about 314 mm² gives about 160 MPa ✓.

**Exam takeaway.** "Find the stress" always means find the internal force first. **Variation:** design the rod diameter for 140 MPa: $d = \sqrt{4(50\,000)/(140\pi)} = 21.3$ mm.

---

## Concept 4.2 — Stress transformation in plane stress

### A. Concept explanation

**1. Intuition.** The material at a point is in one definite physical state. Rotating the imaginary cube is like walking around a statue: you see it differently, but the statue doesn't change. The transformation equations tell you what σ and τ a cut at angle θ "sees".

**2. Why it matters.** Welded and glued joints at an angle, wood grain, fibre directions, failure planes (ductile metals fail on 45° shear planes, brittle ones on principal planes) and the starting point for principal stresses and Mohr's circle.

**3. Formal treatment.** Given $\sigma_x$, $\sigma_y$, $\tau_{xy}$, find $\sigma_{x'}$ and $\tau_{x'y'}$ on the face whose outward normal x′ is at θ counter-clockwise from x.

**4. Derivation (wedge equilibrium; slides "stress components associated with arbitrarily oriented faces").** Cut a triangular wedge whose inclined face has area ΔA and normal x′. The vertical (−x) face then has area $\Delta A\cos\theta$ and the horizontal (−y) face $\Delta A\sin\theta$. The forces on the two negative faces are:
- on the −x face: $\sigma_x\Delta A\cos\theta$ (←) and $\tau_{xy}\Delta A\cos\theta$ (↓);
- on the −y face: $\sigma_y\Delta A\sin\theta$ (↓) and $\tau_{xy}\Delta A\sin\theta$ (←).

*Sum forces along x′* (unit vector $(\cos\theta, \sin\theta)$):
$$\sigma_{x'}\Delta A = \sigma_x\Delta A\cos^2\theta + \sigma_y\Delta A\sin^2\theta + 2\tau_{xy}\Delta A\sin\theta\cos\theta$$
*Sum forces along y′* (unit vector $(-\sin\theta, \cos\theta)$):
$$\tau_{x'y'} = -(\sigma_x - \sigma_y)\sin\theta\cos\theta + \tau_{xy}(\cos^2\theta - \sin^2\theta)$$
With the double-angle identities $\cos^2\theta = \frac{1 + \cos2\theta}{2}$, $\sin^2\theta = \frac{1 - \cos2\theta}{2}$ and $2\sin\theta\cos\theta = \sin2\theta$:
$$\boxed{\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos2\theta + \tau_{xy}\sin2\theta}$$
$$\boxed{\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta}$$
$$\boxed{\sigma_{y'} = \frac{\sigma_x + \sigma_y}{2} - \frac{\sigma_x - \sigma_y}{2}\cos2\theta - \tau_{xy}\sin2\theta}$$
**Invariant:** $\sigma_{x'} + \sigma_{y'} = \sigma_x + \sigma_y$. Use it to check every answer.

*Direction-cosine form (Crandall §4.10):* $\sigma_{x'} = \sigma_x\cos^2\theta + \sigma_y\sin^2\theta + 2\tau_{xy}\sin\theta\cos\theta$. In index notation $\sigma'_{ij} = l_{ik}l_{jl}\sigma_{kl}$; a quantity that transforms like this is a **tensor**, and Mohr's circle is a graphical picture of a tensor transformation.

**5. Picture.** All three equations depend on 2θ, so rotating the element by 180° gives the same state, as it must, since a face and its opposite are the same plane.

**6. Special cases.**
- Uniaxial $\sigma_x = \sigma$: $\sigma_\theta = \sigma\cos^2\theta$ and $\tau = -\frac{\sigma}{2}\sin2\theta$, so $|\tau|_{max} = \sigma/2$ at 45°. This is why ductile bars yield on 45° planes.
- Pure shear τ: $\sigma_{45^\circ} = +\tau$ and $\sigma_{135^\circ} = -\tau$, so the principal stresses are ±τ at 45°. This is the basis of torsion strain-gauge problems (Ch. 6).

**7. Traps.**
- Measuring θ from the *plane* instead of from its **normal**. If a weld line is at β to the cross-section, the weld's normal is at β to the axis.
- Using θ instead of 2θ in the trig functions.
- Getting the sign of $\tau_{xy}$ wrong. Look at the right face: is the arrow up?

**8. Summary.** $\sigma_{x'} = \bar\sigma + \frac{\sigma_x - \sigma_y}{2}\cos2\theta + \tau_{xy}\sin2\theta$; $\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta$; $\sigma_{x'} + \sigma_{y'}$ = constant.

### B. Solved questions

#### Q2 (Slides Ch4) — Stresses on a plane whose normal is at 45° *(easy)*
**Problem.** For $\sigma_x = 110$, $\sigma_y = 50$ and $\tau_{xy} = +40$ MN/m², find the stress components on faces a (normal at 45° to x) and b (normal at 135°).

**Approach.** Direct substitution; θ = 45° makes 2θ = 90°, so cos = 0 and sin = 1.

**Solution.**
1. $\bar\sigma = 80$ and $\frac{\sigma_x - \sigma_y}{2} = 30$ MPa.
2. $\sigma_a = 80 + 30(0) + 40(1) = 120$ MPa.
3. $\tau_{ab} = -30(1) + 40(0) = -30$ MPa.
4. $\sigma_b = 80 - 0 - 40 = 40$ MPa.

$$\boxed{\sigma_a = 120\ \text{MPa},\qquad \sigma_b = 40\ \text{MPa},\qquad \tau_{ab} = -30\ \text{MPa}}$$

**Check.** $120 + 40 = 160 = 110 + 50$ ✓. On Mohr's circle (C = 80, R = 50), X is at (110, 40 below); rotating 90° counter-clockwise gives X′ at (120, 30 above), i.e. $\tau_{x'y'} = -30$ ✓.

**Exam takeaway.** A negative $\tau_{ab}$ means the shear on face a acts in the −b direction (clockwise on the rotated element). **Variation:** θ = 30°.

---

#### Q3 (Slides Ch4, Beer) — Oblique face by wedge equilibrium *(medium)*
**Problem.** For $\sigma_x = 27$ MPa, $\sigma_y = -45$ MPa and $\tau_{xy} = 18$ MPa, find the normal and shearing stresses on the oblique face of the shaded triangular element, which is inclined at 15° to the horizontal. Use equilibrium of the element.

**Given:** the oblique face's outward normal is at θ = 90° + 15° = 105°. **Find:** σ, τ on that face.

**Approach.** The transformation equations are the wedge equilibrium written in general; using them with θ = 105° is the same as the slide's force balance with areas $A\cos15^\circ$ and $A\sin15^\circ$.

**Solution.**
1. $\bar\sigma = -9$, $\frac{\sigma_x - \sigma_y}{2} = 36$, 2θ = 210° ($\cos = -0.866$, $\sin = -0.5$).
2. $\sigma = -9 + 36(-0.866) + 18(-0.5) = -9 - 31.18 - 9 = -49.2$ MPa.
3. $\tau = -36(-0.5) + 18(-0.866) = 18 - 15.59 = 2.41$ MPa.

$$\boxed{\sigma = -49.2\ \text{MPa},\qquad \tau = 2.41\ \text{MPa}}$$

**Check.** This matches the slide's answer ✓. Mohr check: C = −9, R = 40.2; the face sits close to the leftmost point (σ₂ = −49.2) ✓.

**Exam takeaway.** The slide method (stresses → areas → forces → equilibrium) is required when the question says "use equilibrium of the element". The transformation formula is your check.

---

#### Q4 (Slides Ch4, Beer) — Welded plates: find the weld angle *(medium)*
**Problem.** Two steel plates of uniform cross-section 10 × 80 mm are welded along a line at angle β to the cross-section. Centric 100 kN forces act on the plates. The in-plane shear stress parallel to the weld is 30 MPa. Find (a) β and (b) the normal stress perpendicular to the weld.

**Given:** $\sigma_x = 100\,000/(10\times80) = 125$ MPa (uniaxial); the weld's normal is at β to the axis. **Find:** β, σ.

**Approach.** Uniaxial transformation, or the slide's direct force balance on the weld.

**Solution.**
1. *(a)* $|\tau| = \dfrac{\sigma_x}{2}\sin2\beta = 62.5\sin2\beta = 30$, so $\sin2\beta = 0.48$ and β = 14.34°.
2. *(b)* $\sigma = \dfrac{\sigma_x}{2}(1 + \cos2\beta) = 62.5(1 + 0.8773) = 117.3$ MPa.

$$\boxed{\beta = 14.3^\circ,\qquad \sigma = 117.3\ \text{MPa}}$$

**Check (slide's direct method).** $F_s = 100\sin\beta = 24.77$ kN, $A_{weld} = 800/\cos\beta = 825.7$ mm², so $\tau = 24\,770/825.7 = 30$ MPa ✓. $F_n = 100\cos\beta = 96.88$ kN gives $\sigma = 117.3$ MPa ✓.

**Exam takeaway.** The second solution of sin 2β = 0.48 (β = 75.7°) also gives 30 MPa shear but a normal stress of only 7.7 MPa. Both are valid weld angles; state both if asked "find β".

---

#### Q5 (Crandall Prob 4.9) — Rotate the state of 4.7(c) by 30° *(easy)*
**Problem.** For $\sigma_x = -120$, $\sigma_y = 50$ and $\tau_{xy} = 100$ MN/m² (Prob 4.7(c)), find the stress components on an element inclined at 30° (counter-clockwise) to the x–y axes.

**Solution.**
1. $\bar\sigma = -35$ and $\frac{\sigma_x - \sigma_y}{2} = -85$; 2θ = 60°.
2. $\sigma_{x'} = -35 + (-85)(0.5) + 100(0.866) = -35 - 42.5 + 86.6 = 9.1$ MPa.
3. $\sigma_{y'} = -70 - 9.1 = -79.1$ MPa.
4. $\tau_{x'y'} = -(-85)(0.866) + 100(0.5) = 73.6 + 50 = 123.6$ MPa.

$$\boxed{\sigma_{x'} = 9.1,\qquad \sigma_{y'} = -79.1,\qquad \tau_{x'y'} = 123.6\ \text{MN/m}^2}$$

**Check.** $9.1 - 79.1 = -70 = -120 + 50$ ✓. $|\tau_{x'y'}| = 123.6 < R = 131.2$ ✓.

**Exam takeaway.** Always report the result on a sketched rotated element with arrows. That is half the marks.

---

## Concept 4.3 — Mohr's circle, principal stresses and maximum shear stress

### A. Concept explanation

**1. Intuition.** As you spin the cut through 180°, the pair $(\sigma_{x'}, \tau_{x'y'})$ traces out a **circle**. The rightmost point of the circle is the largest normal stress any cut can feel, the leftmost the smallest, and the top and bottom the largest shear. Mohr's circle is a picture of *every possible cut at once*.

**2. Why it matters.** Failure criteria (Ch. 5) need principal stresses. PYQs ask for "principal stresses and orientation" or "sketch the Mohr's circle" every year.

**3–4. Formal treatment and derivation (slides).** Move the average to the left side and square both transformation equations:
$$\left(\sigma_{x'} - \frac{\sigma_x + \sigma_y}{2}\right)^2 = \left(\frac{\sigma_x - \sigma_y}{2}\cos2\theta + \tau_{xy}\sin2\theta\right)^2,\qquad \tau_{x'y'}^2 = \left(-\frac{\sigma_x - \sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta\right)^2$$
Adding them, the cross terms cancel and $\sin^2 + \cos^2 = 1$:
$$\boxed{(\sigma_{x'} - \sigma_{avg})^2 + \tau_{x'y'}^2 = R^2},\qquad \sigma_{avg} = \frac{\sigma_x + \sigma_y}{2},\qquad R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$
This is a circle with centre $(\sigma_{avg}, 0)$ and radius R.

*Principal stresses (zero shear):* set $\tau_{x'y'} = 0$:
$$\boxed{\tan2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}},\qquad \boxed{\sigma_{1,2} = \sigma_{avg} \pm R}$$
This gives two angles 90° apart. **To tell which gives σ₁, substitute back into the $\sigma_{x'}$ equation.** Equivalently, $d\sigma_{x'}/d\theta = 0$ gives the same condition (Crandall Prob 4.31), so principal stresses are the extremes of normal stress.

*Maximum in-plane shear:*
$$\boxed{\tau_{max} = R = \frac{\sigma_1 - \sigma_2}{2}},\qquad \tan2\theta_s = -\frac{\sigma_x - \sigma_y}{2\tau_{xy}},\qquad \theta_s = \theta_p \pm 45^\circ$$
On the max-shear planes the normal stress is **not** zero; it equals $\sigma' = \sigma_{avg}$.

*Absolute maximum shear (3-D view of plane stress).* The out-of-plane principal stress is $\sigma_3 = 0$. Order the three principal stresses as $\sigma_{max} \ge \sigma_{mid} \ge \sigma_{min}$; then $\tau_{abs,max} = (\sigma_{max} - \sigma_{min})/2$. If σ₁ and σ₂ have the **same sign**, $\tau_{abs}$ is $|\sigma_1|/2$ or $|\sigma_2|/2$, which is **larger than the in-plane R**. Examiners love this.

**5. Graphical construction (Crandall §4.5; slides). You must be able to draw this.**
1. Axes: σ horizontal (+ right) and τ vertical. *Positive τ is plotted downward at X* (Crandall).
2. Plot **X** = ($\sigma_x$, $\tau_{xy}$ *downward* if positive).
3. Plot **Y** = ($\sigma_y$, $\tau_{xy}$ *upward* if positive).
4. Join XY. It crosses the σ-axis at the centre C = $\sigma_{avg}$. The radius is R = CX.
5. A (rightmost) and B (leftmost) give σ₁ and σ₂. D and E (top and bottom) give ±τ_max, both at $\sigma_{avg}$.
6. For the face rotated θ counter-clockwise, rotate the diameter XY by **2θ in the same sense**. The new ends are X′ and Y′.
7. The angle on the circle from CX to CA is $2\theta_p$; the element rotates by $\theta_p$ in the **same** sense.

**6. Special cases (Crandall Prob 4.6).**

| State | Circle |
|---|---|
| Uniaxial tension σ₀ | passes through the origin and σ₀; R = σ₀/2 |
| Uniaxial compression | through the origin and −σ₀ |
| Equal biaxial σ₀, σ₀ | shrinks to a point: every direction is principal, no in-plane shear |
| Opposite biaxial σ₀, −σ₀ | centred at the origin, R = σ₀: the same circle as pure shear |
| Pure shear ±τ₀ | centred at the origin, R = τ₀; principal stresses ±τ₀ at 45° |
| Hydrostatic | a point, no shear on any plane |

**7. Common traps.**
- **θ vs 2θ:** angles on the circle are double the element angles.
- **Direction of rotation:** consistent only if +τ is plotted downward at X (Crandall convention).
- Using arctan blindly: $\tan2\theta_p$ has two solutions 180° apart. Pick by checking the quadrant on the circle, or substitute back.
- Reporting τ_max = R when both principal stresses have the same sign (the true maximum is out of plane).
- Forgetting $\sigma_{avg}$ on the max-shear faces when drawing the element.

**8. Summary box**
$$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2},\quad \tan2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y},\quad \tau_{max} = R,\ \theta_s = \theta_p \pm 45^\circ,\ \sigma' = \sigma_{avg}$$

### B. Solved questions

#### Q6 (Slides Ch4, Beer Example 7.1) — Principal planes, principal stresses and maximum shear *(easy, classic)*
**Problem.** For $\sigma_x = 50$, $\sigma_y = -10$ and $\tau_{xy} = +40$ MPa, find (a) the principal planes, (b) the principal stresses, (c) the maximum shearing stress and the corresponding normal stress. Then construct Mohr's circle.

**Solution (equations).**
1. $\tan2\theta_p = \dfrac{2(40)}{50 - (-10)} = 1.333$, so 2θp = 53.1° (or 233.1°) and θp = 26.6° (or 116.6°).
2. Substituting θ = 26.6°: $\sigma_{x'} = 20 + 30(0.6) + 40(0.8) = 70$, so this angle carries σ₁.
3. $R = \sqrt{30^2 + 40^2} = 50$, so σ₁ = 20 + 50 = 70 and σ₂ = 20 − 50 = −30 MPa.
4. τ_max = R = 50 MPa at θs = θp − 45° = −18.4° (and 71.6°), with σ′ = 20 MPa on those faces.

$$\boxed{\sigma_1 = 70\ \text{MPa at } 26.6^\circ,\quad \sigma_2 = -30\ \text{MPa at } 116.6^\circ,\quad \tau_{max} = 50\ \text{MPa at } -18.4^\circ,\quad \sigma' = 20\ \text{MPa}}$$

**Solution (Mohr's circle).** C = 20 and R = CX = 50 (CF = 30, FX = 40). X = (50, 40 *below*) and Y = (−10, 40 *above*). From X to A is 53.1° counter-clockwise, so the element rotates 26.6° counter-clockwise ✓ (slide: "tan 2θp = FX/CF = 40/30").

**Check.** Absolute max shear: σ₁ = 70, σ₂ = −30, σ₃ = 0, so $\tau_{abs} = (70 + 30)/2 = 50$, the same as in-plane because the signs are opposite ✓.

**Exam takeaway.** Show both the equations and the circle; the slides do exactly that.

---

#### Q7 (Slides Ch4, Beer Sample 7.2) — Principal stresses, then rotate the element 30° counter-clockwise *(medium)*
**Problem.** For $\sigma_x = 100$, $\sigma_y = 60$ and $\tau_{xy} = -48$ MPa (shear on the right face points down), find (a) the principal planes and stresses and (b) the stresses on the element rotated 30° counter-clockwise.

**Solution.**
1. C = 80; $R = \sqrt{20^2 + 48^2} = 52$.
2. σ₁ = 132 and σ₂ = 28 MPa. $\tan2\theta_p = -96/40$, so 2θp = −67.4° and θp = 33.7° **clockwise** for σ₁.
3. *Rotate 30° counter-clockwise* (2θ = 60°):
   - $\sigma_{x'} = 80 + 20\cos60^\circ - 48\sin60^\circ = 80 + 10 - 41.6 = 48.4$ MPa
   - $\sigma_{y'} = 160 - 48.4 = 111.6$ MPa
   - $\tau_{x'y'} = -20\sin60^\circ - 48\cos60^\circ = -17.3 - 24 = -41.3$ MPa

$$\boxed{\sigma_1 = 132,\ \sigma_2 = 28\ \text{MPa},\ \theta_p = 33.7^\circ\ \text{cw};\qquad \sigma_{x'} = 48.4,\ \sigma_{y'} = 111.6,\ \tau_{x'y'} = -41.3\ \text{MPa}}$$

**Check (slide's circle method).** X starts 67.4° *clockwise* from A (it sits 48 above the axis, because τ is negative). Rotating 60° counter-clockwise puts X′ at φ = 180° − 60° − 67.4° = 52.6° from the negative σ-axis. So $\sigma_{x'} = 80 - 52\cos52.6^\circ = 48.4$ ✓ and $|\tau| = 52\sin52.6^\circ = 41.3$ ✓. Invariant: 48.4 + 111.6 = 160 ✓.

**Exam takeaway.** "Rotate the element" means "rotate the diameter by twice that angle, in the same sense".

---

#### Q8 (Crandall Prob 4.6) — Sketch Mohr's circle for standard states *(easy, conceptual)*
**Problem.** Sketch Mohr's circle for each of the plane-stress cases drawn. They are built from normal stresses ±σ₀ on the x and/or y faces and shear ±τ₀.

**Solution.** Use the table in item 6.
1. One normal stress only: the circle passes through the origin; R = σ₀/2.
2. Equal normal stresses of the same sign on x and y: a single point (no shear on any plane).
3. Equal normal stresses of **opposite** sign: centred at the origin with R = σ₀, identical to the pure-shear circle.
4. Pure shear ±τ₀: centred at the origin with R = τ₀. Only the positions of X and Y swap between +τ₀ and −τ₀.

$$\boxed{\text{uniaxial: through O;\quad equal biaxial: a point;\quad } (\sigma_0, -\sigma_0) \equiv \text{pure shear } \tau_0 = \sigma_0}$$

**Exam takeaway.** "σ₀ in x plus −σ₀ in y" is pure shear of σ₀ on 45° planes. It is a favourite one-mark question (see Q14).

---

#### Q9 (Crandall Prob 4.7) — Principal stresses and orientations for five states *(medium)*
**Problem.** Find the principal stresses and the orientation of the principal axes for: (a) 40, 0, 80; (b) 140, 20, −60; (c) −120, 50, 100 (all MN/m², listed as $\sigma_x, \sigma_y, \tau_{xy}$); (d) 10 000, −4 000, 8 000 psi; (e) −10 000, 20 000, −6 000 psi.

**Approach.** For each case: $\bar\sigma$, R, σ₁,₂ = $\bar\sigma \pm R$, and $\theta_p = \tfrac12\tan^{-1}\frac{2\tau_{xy}}{\sigma_x - \sigma_y}$, choosing the branch (atan2) that gives σ₁.

**Solution.**

| Case | $\bar\sigma$ | R | σ₁ | σ₂ | θ (σ₁ from x) |
|---|---|---|---|---|---|
| (a) | 20 | 82.46 | **102.5** | **−62.5** | 38.0° |
| (b) | 80 | 84.85 | **164.9** | **−4.9** | −22.5° |
| (c) | −35 | 131.2 | **96.2** | **−166.2** | 65.2° |
| (d) psi | 3000 | 10 630 | **13 630** | **−7 630** | 24.4° |
| (e) psi | 5000 | 16 155 | **21 155** | **−11 155** | −79.1° (σ₂ at 10.9°) |

**Check.** Each row: σ₁ + σ₂ = σx + σy ✓. For (b), the σ₁ direction is clockwise from x because τ is negative ✓.

**Exam takeaway.** A table is the fastest way to present a multi-case question. The angle always belongs to σ₁ unless you say otherwise.

---

#### Q10 (Crandall Prob 4.8) — Find σx when the minimum principal stress is known *(medium)*
**Problem.** In a state of plane stress, $\sigma_y = 21$ MN/m² (tension) and the shear on the x faces is 56 MN/m², acting downward on the right face. If the minimum principal stress is −7 MN/m², find σx and the angle the principal axes make with x–y.

**Given:** $\sigma_y = 21$, $\tau_{xy} = -56$, $\sigma_2 = -7$ MPa. **Find:** σx, θp.

**Approach.** Write σ₂ = $\bar\sigma - R$ with σx unknown, and solve.

**Solution.**
1. $\dfrac{\sigma_x + 21}{2} - \sqrt{\left(\dfrac{\sigma_x - 21}{2}\right)^2 + 56^2} = -7$.
2. Rearrange: $\dfrac{\sigma_x + 21}{2} + 7 = \sqrt{\left(\dfrac{\sigma_x - 21}{2}\right)^2 + 3136}$.
3. Square both sides. Using $\left(\frac{\sigma_x + 21}{2}\right)^2 - \left(\frac{\sigma_x - 21}{2}\right)^2 = 21\sigma_x$: $21\sigma_x + 7(\sigma_x + 21) + 49 = 3136$, so $28\sigma_x = 2940$ and σx = 105 MPa.
4. Check: C = 63 and R = $\sqrt{42^2 + 56^2} = 70$, so σ₂ = −7 ✓ and σ₁ = 133 MPa.
5. $\tan2\theta_p = \dfrac{2(-56)}{105 - 21} = -1.333$, so 2θp = −53.1° and θp = −26.6°.

$$\boxed{\sigma_x = 105\ \text{MN/m}^2;\quad \sigma_1 = 133\ \text{at } 26.6^\circ\ \text{clockwise from x},\quad \sigma_2 = -7\ \text{at } 63.4^\circ\ \text{counter-clockwise}}$$

**Check.** The R is a 3-4-5 triangle scaled by 14 (42-56-70) ✓.

**Exam takeaway.** "Given one principal stress, find a component" is a squared-root equation; the difference-of-squares trick makes it linear. **Variation:** given σ₁ instead.

---

#### Q11 (Crandall Prob 4.15) — Deduce the state, then find stresses on rotated faces *(medium)*
**Problem.** A plate is in uniform plane stress. The maximum tensile stress on any face (normal in the x–y plane) is 75 MN/m². On the face perpendicular to x there is a compressive stress of 15 MN/m² and **no** shear. Find the stresses on faces perpendicular to axes a and b, where a is 30° below x (θ = −30°) and b is 60° above x.

**Approach.** Zero shear on the x face means x is a principal direction, so σx = −15 is a principal stress. The other principal stress is the 75 MPa maximum, acting along y. Then transform.

**Solution.**
1. *State:* $\sigma_x = -15$, $\sigma_y = 75$, $\tau_{xy} = 0$ (principal axes x, y).
2. $\bar\sigma = 30$, $\frac{\sigma_x - \sigma_y}{2} = -45$; for face a, θ = −30°, so 2θ = −60°.
3. $\sigma_a = 30 + (-45)\cos(-60^\circ) = 30 - 22.5 = 7.5$ MPa.
4. $\sigma_b = 60 - 7.5 = 52.5$ MPa.
5. $\tau_{ab} = -(-45)\sin(-60^\circ) = 45(-0.866) = -39.0$ MPa.

$$\boxed{\sigma_a = 7.5\ \text{MPa},\qquad \sigma_b = 52.5\ \text{MPa},\qquad \tau_{ab} = -39.0\ \text{MPa}}$$

**Check.** $|\tau_{ab}| \le R = 45$ ✓; 7.5 + 52.5 = 60 = −15 + 75 ✓.

**Exam takeaway.** "No shear on a face" ⇒ that face is a principal plane. Reading this from the wording is the whole problem.

---

#### Q12 (Crandall Prob 4.28) — Complete the picture from the principal stresses *(medium)*
**Problem.** At a point in plane stress, the shear on the x–y faces is 20 MN/m² as sketched (↑ on the right face, so $\tau_{xy} = +20$). The principal stresses are σ₁ = 20 and σ₂ = −45 MN/m². Find σx and σy.

**Approach.** The invariant gives σx + σy; the radius gives |σx − σy|. Expect two answers.

**Solution.**
1. *Sum:* $\sigma_x + \sigma_y = \sigma_1 + \sigma_2 = -25$, so $\bar\sigma = -12.5$.
2. *Radius:* $R = (20 + 45)/2 = 32.5$, so $\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 = 32.5^2 - 20^2 = 656.25$ and $\frac{\sigma_x - \sigma_y}{2} = \pm25.62$.
3. Two solutions: σx = −12.5 + 25.62 = 13.1 with σy = −38.1, **or** σx = −38.1 with σy = 13.1.

$$\boxed{(\sigma_x, \sigma_y) = (13.1,\ -38.1)\ \text{or}\ (-38.1,\ 13.1)\ \text{MN/m}^2\ \ (\tau_{xy} = +20)}$$

**Check.** Both give a circle with C = −12.5 and R = 32.5 ✓. They are the same physical state with the principal axes rotated 90°.

**Exam takeaway.** Without more information (e.g. the principal angle) both answers are correct; showing both earns full marks.

---

#### Q13 (PYQ 2014-15 Compre A Q12) — Principal stresses *(easy, one-line answer)*
**Problem.** For $\sigma_x = 50$, $\sigma_y = -10$ and $\tau_{xy} = 40$ MPa, find the maximum and minimum principal stresses.

**Solution.** The same state as Q6: C = 20, R = 50.

$$\boxed{\sigma_1 = 70\ \text{MPa},\qquad \sigma_2 = -30\ \text{MPa}}$$

---

#### Q14 (PYQ 2014-15 Compre A Q13) — Which Mohr's circle? *(easy, conceptual)*
**Problem.** The element shown carries only shear stresses (no normal arrows). Which of the four sketches is its Mohr's circle?

**Solution.** Pure shear gives a circle **centred at the origin**, with radius τ.

$$\boxed{\text{the circle centred on the origin (option c in the paper)}}$$

**Exam takeaway.** Know the four signature circles (uniaxial tension, uniaxial compression, pure shear, equal biaxial) from Q8.

---

#### Q15 (PYQ 2014-15 Test-2 Q1) — Axial force + torque on a 40 mm shaft: principal stresses and Mohr's circle *(medium, 20 marks)*
**Problem.** An axial force of 90 kN and a torque of 250 N·m act on a 40 mm diameter shaft. Find the principal stresses and the orientation of the principal axes (relative to the shaft axis) at a point P on the surface, and sketch Mohr's circle.

**Approach.** Axial stress P/A and torsional shear 16T/πd³ (Ch. 6) at the surface point, then the plane-stress formulas.

**Solution.**
1. $\sigma = \dfrac{90\,000}{\pi(20)^2} = 71.6$ MPa along the shaft axis (y in the figure).
2. $\tau = \dfrac{16(250\,000)}{\pi(40)^3} = 19.9$ MPa.
3. With $\sigma_y = 71.6$, $\sigma_x = 0$, $|\tau_{xy}| = 19.9$: C = 35.8 and $R = \sqrt{35.8^2 + 19.9^2} = 41.0$.
4. σ₁ = 76.8 MPa and σ₂ = −5.2 MPa; τmax = 41.0 MPa.
5. $\tan2\theta_p = \dfrac{2(19.9)}{71.6}$, so θp = 14.5°, measured from the **shaft axis** to the σ₁ direction; the sense follows the direction of the torque.

$$\boxed{\sigma_1 = 76.8\ \text{MPa},\quad \sigma_2 = -5.2\ \text{MPa},\quad \tau_{max} = 41.0\ \text{MPa},\quad \theta_p = 14.5^\circ\ \text{from the axis}}$$

**Check.** σ₁σ₂ = −398 = −τ² (as required when one normal stress is zero) ✓. The circle crosses the τ-axis because σ₂ < 0 ✓.

**Exam takeaway.** The axial stress tilts the principal direction toward the axis; pure torsion alone would give 45°. **Variation:** compressive axial load, which gives σ₂ the larger magnitude.

---

#### Q16 (PYQ 2014-15 Compre B Q1) — Superposing two stress states *(hard, 15 marks)*
**Problem.** A point on a thin plate is subjected to two successive states of stress. State 1 is biaxial compression (−350 MPa and −200 MPa) on an element rotated 60°; state 2 is pure shear of 58 MPa on an element rotated 25°. (a) Find the resultant stress on the x–y element. (b) Sketch Mohr's circle. (c) Find the principal stresses and principal strains. E = 200 GPa, ν = 0.3.

**Approach.** You **cannot add stresses on differently oriented elements**. Transform each state to the same x–y axes (θ = −60° and θ = −25° respectively), *then* add component by component.

**Solution.**
1. *State 1* (−350 along x′ at 60°, −200 along y′): $\sigma_x = -275 + (-75)\cos(-120^\circ) = -237.5$, $\sigma_y = -312.5$, $\tau_{xy} = -(-75)\sin(-120^\circ) = -65.0$.
2. *State 2* (pure shear τ′ = −58 on an element at 25°; the sign follows the arrows): $\sigma_x = \tau'\sin(-50^\circ) = 44.4$, $\sigma_y = -44.4$, $\tau_{xy} = \tau'\cos(-50^\circ) = -37.3$.
3. *Sum:* σx ≈ −193 MPa, σy ≈ −357 MPa, |τxy| ≈ 102 MPa. (This matches the textbook answer to the Hibbeler problem this question is taken from. The sign of τ depends on how the arrows are read; the principal values don't.)
4. *Principal stresses:* $\bar\sigma = -275$, $R = \sqrt{81.9^2 + 102.2^2} = 131.0$, so σ₁ = −144 and σ₂ = −406 MPa (σ₃ = 0).
5. *Principal strains (Hooke, plane stress; Ch. 5):*
$$\epsilon_1 = \frac{\sigma_1 - \nu\sigma_2}{E} = \frac{-144 + 121.8}{200\,000} = -111\times10^{-6},\qquad \epsilon_2 = \frac{-406 + 43.2}{200\,000} = -1814\times10^{-6}$$
$$\epsilon_3 = -\frac{\nu}{E}(\sigma_1 + \sigma_2) = +825\times10^{-6}\ \text{(the plate gets thicker)}$$

$$\boxed{\sigma_x \approx -193,\ \sigma_y \approx -357,\ |\tau_{xy}| \approx 102\ \text{MPa};\quad \sigma_{1,2} = -144,\ -406\ \text{MPa};\quad \epsilon_{1,2,3} = -111,\ -1814,\ +825\ \mu}$$

**Check.** $\sigma_x + \sigma_y = -550 = \sigma_1 + \sigma_2$ ✓. Both principal stresses are compressive, so the circle lies entirely left of the τ-axis and $\tau_{abs,max} = 406/2 = 203$ MPa > R ✓.

**Exam takeaway.** The rule "transform first, then add" is what is being tested. **Variation:** add a third, uniaxial state.

---

## Concept 4.4 — Thin-walled pressure vessels (Crandall Probs 4.10–4.14)

### A. Concept explanation

**1. Intuition.** A soft-drink can, a gas cylinder, a boiler, a balloon. The wall is thin compared with the radius, so it cannot resist pressure by bending; it does so by stretching like a membrane. A cylinder is stretched twice as hard around its circumference as along its length. That is why an overheated sausage splits lengthwise.

**2. Why it matters.** Pressure vessels, pipes, tanks, filament-wound cases, biological cells (Q23). They provide a ready-made biaxial stress state for Mohr's-circle and Hooke's-law problems (Ch. 5 Crandall 5.12, 5.20), and the ring case appeared in PYQ 2014 Compre A Q11.

**3. Formal treatment.** For a thin wall ($t \ll r$), use cylindrical coordinates (r, θ, z). By symmetry there are no shear stresses on r, θ and z faces, so **r, θ and z are principal directions** (Crandall Prob 4.10). The radial stress varies from −p on the inner surface to 0 on the outer, which is negligible against pr/t, so $\sigma_r \approx 0$.

| Vessel | $\sigma_\theta$ (hoop) | $\sigma_z$ or $\sigma_\phi$ (axial/meridional) |
|---|---|---|
| Open cylinder with axial force F (4.10) | $pr/t$ | $F/2\pi rt$ |
| Closed cylinder (4.12) | $pr/t$ | $pr/2t$ |
| Sphere (4.14) | $pr/2t$ | $pr/2t$ |

**4. Derivations.**

*(a) Hoop stress.* Cut a cylinder of length L along a diameter and keep half. Pressure acts on the projected area 2rL; the two cut walls carry $\sigma_\theta tL$ each:
$$2\sigma_\theta tL = p(2r)L\ \Rightarrow\ \sigma_\theta = \frac{pr}{t}$$
*(b) Axial stress, closed ends.* Cut across the cylinder. The pressure on the end cap, $p\pi r^2$, is carried by the wall ring of area $2\pi rt$:
$$\sigma_z(2\pi rt) = p\pi r^2\ \Rightarrow\ \sigma_z = \frac{pr}{2t}$$
*(c) Sphere.* Any great-circle cut gives the same balance as (b): $\sigma = pr/2t$ in every tangential direction.

*(d) Maximum in-plane shear, closed cylinder (Crandall Prob 4.13):* $\tau_{\theta z} = \dfrac{\sigma_\theta - \sigma_z}{2} = \dfrac{pr}{4t}$, one quarter of the hoop stress.

**5. Picture.** A wall element of a closed cylinder carries $\sigma_\theta$ around and $\sigma_z = \sigma_\theta/2$ along. Its Mohr's circle runs from pr/2t to pr/t, and the 3-D circle including $\sigma_r = 0$ is larger (absolute τ_max = pr/2t).

**6. Special cases.**
- An open-ended pipe with no axial force has $\sigma_z = 0$: uniaxial hoop stress.
- A sphere has equal biaxial stress, so its in-plane Mohr's circle is a point; it is the most efficient shape (half the hoop stress of a cylinder of the same r and t).
- Filament-wound vessels: fibres at ±54.7° to the axis carry closed-end pressure with equal fibre tension (Q22).

**7. Traps.**
- Using the diameter instead of the radius.
- Writing σz = pr/t (that is the hoop value).
- Forgetting that a strain gauge on the surface reads strain, not stress: use Hooke's law with both stresses (Ch. 5).

**8. Summary box**
$$\text{cylinder: } \sigma_\theta = \frac{pr}{t},\ \sigma_z = \frac{pr}{2t}\ \text{(closed)};\qquad \text{sphere: } \sigma = \frac{pr}{2t};\qquad \tau_{\theta z} = \frac{pr}{4t};\qquad \sigma_r \approx 0$$

### B. Solved questions

#### Q17 (Crandall Probs 4.10, 4.12, 4.14) — Derive the thin-wall stresses *(easy, derivation)*
**Problem.** (4.10) For a thin-walled cylinder with internal pressure p and axial force F, show that r, θ and z are principal directions and find the stresses. (4.12) Repeat with closed ends carrying the pressure. (4.14) Repeat for a thin sphere.

**Solution.**
1. *Principal directions:* the geometry and loading are symmetric about the axis and about any plane through it. A shear stress $\tau_{\theta z}$ on a wall element would have to reverse sign under reflection in such a plane, which leaves the loading unchanged. So it is zero; similarly for the other shears. Therefore r, θ and z are principal.
2. *Hoop:* derivation (a) gives $\sigma_\theta = pr/t$.
3. *Axial:* with F only (open ends), $\sigma_z = F/(2\pi rt)$. With closed ends, the cap force $p\pi r^2$ gives $\sigma_z = pr/2t$.
4. *Sphere:* $\sigma_\theta = \sigma_\phi = pr/2t$.
5. *Radial:* $|\sigma_r| \le p$, which is $t/r$ times smaller than σθ, so $\sigma_r \approx 0$.

$$\boxed{\sigma_r \approx 0;\quad \sigma_\theta = \frac{pr}{t};\quad \sigma_z = \frac{F}{2\pi rt}\ \text{(open)},\ \frac{pr}{2t}\ \text{(closed)};\quad \text{sphere } \sigma = \frac{pr}{2t}}$$

**Exam takeaway.** The "projected area" balance is a two-line derivation that examiners like to see.

---

#### Q18 (Crandall Prob 4.13) — Closed cylinder: τ_max in the θz plane is σmax/4 *(easy)*
**Solution.**
$$\tau_{\theta z,max} = \frac{\sigma_\theta - \sigma_z}{2} = \frac{pr/t - pr/2t}{2} = \frac{pr}{4t} = \frac14\sigma_\theta\quad\boxed{\text{shown}}$$
**Exam takeaway.** In 3-D (with σr = 0), the absolute maximum shear is $\sigma_\theta/2 = pr/2t$, on planes at 45° between θ and r.

---

#### Q19 (Crandall Prob 4.11) — Relation between F and p for two shear conditions *(medium)*
**Problem.** For the open cylinder of 4.10 (pressure p and axial force F), what relation between F and p makes (a) the maximum shear stress in the wall equal in magnitude to the maximum normal stress, and (b) half of it?

**Approach.** In the wall (θz plane): σθ = pr/t and σz = F/2πrt. The in-plane maximum shear is |σθ − σz|/2.

**Solution.**
1. *(a)* |σθ − σz|/2 = max(|σθ|, |σz|) requires σz = −σθ: equal and opposite. So $F/2\pi rt = -pr/t$, giving $F = -2\pi r^2p$ (an axial **compression** of magnitude 2πr²p).
2. *(b)* |σθ − σz|/2 = ½ max(|σθ|, |σz|) requires σz = 0, so F = 0 (an open pipe with no axial force).

$$\boxed{(a)\ F = -2\pi r^2p\ \text{(compressive)};\qquad (b)\ F = 0}$$

**Check.** (b) is uniaxial hoop stress, with τ_max = σ/2 ✓. If the 3-D view with σr = 0 is used for (b), any tensile F with 0 ≤ σz satisfies "τ_max = σmax/2". State which interpretation you use.

**Exam takeaway.** Pure-shear-like states arise when two principal stresses are equal and opposite.

---

#### Q20 (Crandall Prob 4.27) — Open cylinder: find p and F from rotated-element stresses *(medium)*
**Problem.** An open-ended thin cylinder (r = 10 in, t = 0.1 in) carries internal pressure p and axial force F. On an element whose m-axis is at 30° to the cylinder axis: (a) σm = 15 000 psi and σn = 5 000 psi; (b) σm = 15 000 psi and σn = 15 000 psi. Find p, F and τmn in each case.

**Approach.** z (axial) and θ (hoop) are principal. Transform from (z, θ) to (m, n) with m at 30° from z, and solve two equations for σz and σθ.

**Solution.**
1. $\sigma_m = \sigma_z\cos^230^\circ + \sigma_\theta\sin^230^\circ = 0.75\sigma_z + 0.25\sigma_\theta$ and $\sigma_n = 0.25\sigma_z + 0.75\sigma_\theta$.
2. *(a)* Sum: σz + σθ = 20 000. Then $0.75\sigma_z + 0.25(20\,000 - \sigma_z) = 15\,000$, so σz = 20 000 and σθ = 0. Hence p = 0 and $F = \sigma_z(2\pi rt) = 20\,000(2\pi)(10)(0.1) = 125\,700$ lb. $|\tau_{mn}| = \frac{\sigma_z - \sigma_\theta}{2}\sin60^\circ = 8\,660$ psi.
3. *(b)* σm = σn gives σz = σθ = 15 000 psi. So $p = \sigma_\theta t/r = 150$ psi and $F = 15\,000(2\pi)(1) = 94\,250$ lb; τmn = 0.

$$\boxed{(a)\ p = 0,\ F = 125.7\ \text{kip},\ |\tau_{mn}| = 8.66\ \text{ksi};\qquad (b)\ p = 150\ \text{psi},\ F = 94.2\ \text{kip},\ \tau_{mn} = 0}$$

**Check.** In (b) the in-plane state is equal biaxial, so every direction is principal and τmn must be zero ✓.

**Exam takeaway.** Reverse problems ("given rotated stresses, find the loads") are just two linear equations. *(Angle read from the figure: m at 30° to the axis.)*

---

#### Q21 (Crandall Prob 4.25) — Helically wound pressure vessel: maximum strip width *(medium–hard)*
**Problem.** A long closed-end pressure vessel of radius r is made by rolling a plastic strip of thickness t and width w into a helix and fusing the edges continuously. The fused joint may carry a tensile stress of only 80% of the maximum stress in the parent plastic. Find the maximum allowable strip width w.

**Approach.** Wall stresses σθ = pr/t (the maximum) and σz = pr/2t. The joint is a helix at angle α to the circumferential direction. Find the normal stress on the joint, limit it, and relate α to w.

**Solution.**
1. *Geometry:* one turn advances the helix axially by $2\pi r\tan\alpha$. The strip width perpendicular to the joint is $w = 2\pi r\tan\alpha\cos\alpha = 2\pi r\sin\alpha$.
2. *Normal stress on the joint:* the joint's normal makes angle α with z, so
$$\sigma_n = \sigma_z\cos^2\alpha + \sigma_\theta\sin^2\alpha = \frac{pr}{2t}(1 + \sin^2\alpha)$$
3. *Limit:* $\frac{pr}{2t}(1 + \sin^2\alpha) \le 0.8\frac{pr}{t}$, so $\sin^2\alpha \le 0.6$ and $\sin\alpha \le 0.775$.
4. $w_{max} = 2\pi r(0.775)$.

$$\boxed{w_{max} = 2\pi r\sqrt{0.6} \approx 4.87\,r}$$

**Check.** α → 0 (circumferential joints) gives σn = σz = 0.5σθ, comfortably allowed but needing w → 0 ✓. α → 90° (an axial seam) gives σn = σθ, not allowed ✓.

**Exam takeaway.** A joint carries the normal stress on its own plane, found by transformation. This is the cylinder version of the welded-plate problem (Q4).

---

#### Q22 (Crandall Prob 4.32) — Filament-wound vessel: the winding angle for equal fibre tension *(medium)*
**Problem.** Glass filaments in an epoxy binder resist the tensile forces in a closed-end pressure vessel. Find the winding angle α of the filaments (to the axis) such that the tensile forces in the filaments are equal.

**Approach.** Netting analysis: the filaments (at ±α to the axis) carry all the load and the binder carries none. A filament stress σf contributes $\sigma_f\cos^2\alpha$ axially and $\sigma_f\sin^2\alpha$ circumferentially.

**Solution.**
1. Axial: $\sigma_f\cos^2\alpha = \sigma_z = pr/2t$. Hoop: $\sigma_f\sin^2\alpha = \sigma_\theta = pr/t$.
2. Divide: $\tan^2\alpha = \sigma_\theta/\sigma_z = 2$.

$$\boxed{\alpha = \tan^{-1}\sqrt2 = 54.7^\circ\ \text{to the axis}}$$

**Check.** The same "magic angle" appears in garden hoses and braided pressure tubes ✓.

**Exam takeaway.** The fibres must follow the ratio of the principal stresses. **Variation:** a sphere gives $\tan^2\alpha = 1$, i.e. 45°.

---

#### Q23 (Crandall Prob 4.34) — Membrane stress in a sea-urchin egg *(easy)*
**Problem.** A sea-urchin egg, considered a thin-walled sphere, has a volume of 35 × 10⁻⁵ mm³ and wall thickness 1 μm. Its internal pressure is about 150 mm Hg. Find the membrane stresses.

**Given:** $V = 3.5\times10^{-4}$ mm³; t = 10⁻³ mm; p = 150 mm Hg = 150(133.3) Pa = 0.0200 MPa. **Find:** σ.

**Solution.**
1. $r = \left(\dfrac{3V}{4\pi}\right)^{1/3} = \left(\dfrac{3(3.5\times10^{-4})}{4\pi}\right)^{1/3} = 0.0437$ mm (an egg about 87 μm across).
2. $\sigma = \dfrac{pr}{2t} = \dfrac{0.0200(0.0437)}{2(0.001)}$.

$$\boxed{\sigma \approx 0.44\ \text{MPa (equal in all tangential directions)}}$$

**Check.** About 440 kPa, small in absolute terms but 22× the internal pressure, because r/2t ≈ 22 ✓.

**Exam takeaway.** Unit conversion is the real test (mm Hg → Pa; μm → mm).

---

## Concept 4.5 — Strain and the strain–displacement relations (plane strain)

### A. Concept explanation

**1. Intuition.** Draw a small circle on a rubber sheet and stretch the sheet. The circle becomes an ellipse. Some diameters get longer (normal strain) and right angles between lines change (shear strain). Strain is the **geometry** of deformation, just as stress is its statics.

**2. Why it matters.** Strain is what we actually **measure** (gauges, extensometers, digital image correlation). Hooke's law (Ch. 5) turns measured strains into stresses. The "circle becomes an ellipse" PYQs (2021 B-Q1, 2024 A-Q2) are strain problems.

**3. Formal treatment (Crandall §4.6–4.7; slides).** Let u(x, y) and v(x, y) be the displacements in x and y. For a small rectangle OCDE (OC along x, length Δx; OE along y, length Δy):
- **Normal strain** = change in length per unit original length:
$$\epsilon_x = \lim\frac{O'C' - OC}{OC} = \frac{\partial u}{\partial x},\qquad \epsilon_y = \frac{\partial v}{\partial y}$$
- **Shear strain** = the decrease of the originally right angle COE:
$$\gamma_{xy} = \lim\left(\frac{\pi}{2} - \angle C'O'E'\right) = \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}$$
**Plane strain:** $\epsilon_z = \gamma_{xz} = \gamma_{yz} = 0$. ⚠ Plane strain ≠ plane stress. A thin plate in plane stress has $\epsilon_z \ne 0$ (it thins). A long dam or a plate between rigid walls is in plane strain, with $\sigma_z \ne 0$.

*Three-dimensional (Crandall Prob 4.16):* $\epsilon_z = \partial w/\partial z$, $\gamma_{yz} = \partial w/\partial y + \partial v/\partial z$, $\gamma_{zx} = \partial u/\partial z + \partial w/\partial x$.
*Polar, axisymmetric (Crandall Prob 4.17):* with radial displacement u(r) only, $\epsilon_r = du/dr$, $\epsilon_\theta = u/r$ and $\gamma_{r\theta} = 0$. This is why a ring whose radius grows by u has hoop strain u/r (Ch. 2 Concept 2.6).

**4. Derivation of εx and γxy.** Point C at (x + Δx, y) moves by $u + \frac{\partial u}{\partial x}\Delta x$ in x and $v + \frac{\partial v}{\partial x}\Delta x$ in y. To first order the new length of OC is $\Delta x(1 + \partial u/\partial x)$, which gives εx. Line OC rotates counter-clockwise by $\partial v/\partial x$ and line OE rotates clockwise by $\partial u/\partial y$; the angle between them closes by the sum, which gives γxy. ∎ Sign: γxy > 0 means the angle between +x and +y **decreases**.

**5. Picture.** Sketch the rectangle OCDE and its deformed shape O′C′D′E′: shifted (rigid translation), rotated (rigid rotation $\omega = \frac12(\partial v/\partial x - \partial u/\partial y)$), stretched (ε) and sheared (γ). Only the last two are strains.

**6. Special cases.** A rigid-body rotation gives u = −ωy and v = ωx, so ε = γ = 0 (Crandall Prob 4.29). A uniform stretch $u = \epsilon_0x$ gives εx = ε₀ only.

**7. Traps.** Engineering shear strain γ is *twice* the tensor shear strain. Mohr's circle uses γ/2.

**8. Summary.** $\epsilon_x = u_{,x}$, $\epsilon_y = v_{,y}$, $\gamma_{xy} = u_{,y} + v_{,x}$; polar axisymmetric: $\epsilon_\theta = u/r$.

---

## Concept 4.6 — Strain transformation and Mohr's circle of strain

### A. Concept explanation

**1. Intuition.** The same idea as for stress. Rotate the measuring axes and the stretch along each direction changes, following *exactly the same algebra* with σ → ε and τ → γ/2.

**2. Why it matters.** Gauges measure strain in their own direction; to get strains along any other direction (and principal strains) you transform. Combined with Hooke's law, this turns gauge readings into stresses.

**3–4. Formal treatment and derivation (slides; Crandall §4.8).** With $x = x'\cos\theta - y'\sin\theta$, $y = x'\sin\theta + y'\cos\theta$, $u' = u\cos\theta + v\sin\theta$ and $v' = -u\sin\theta + v\cos\theta$, the chain rule gives
$$\epsilon_{x'} = \frac{\partial u'}{\partial x'} = \left(\frac{\partial u}{\partial x}\cos\theta + \frac{\partial v}{\partial x}\sin\theta\right)\cos\theta + \left(\frac{\partial u}{\partial y}\cos\theta + \frac{\partial v}{\partial y}\sin\theta\right)\sin\theta = \epsilon_x\cos^2\theta + \epsilon_y\sin^2\theta + \gamma_{xy}\sin\theta\cos\theta$$
In double-angle form:
$$\boxed{\epsilon_{x'} = \frac{\epsilon_x + \epsilon_y}{2} + \frac{\epsilon_x - \epsilon_y}{2}\cos2\theta + \frac{\gamma_{xy}}{2}\sin2\theta}$$
$$\boxed{\frac{\gamma_{x'y'}}{2} = -\frac{\epsilon_x - \epsilon_y}{2}\sin2\theta + \frac{\gamma_{xy}}{2}\cos2\theta}$$
$$\epsilon_{1,2} = \frac{\epsilon_x + \epsilon_y}{2} \pm \sqrt{\left(\frac{\epsilon_x - \epsilon_y}{2}\right)^2 + \left(\frac{\gamma_{xy}}{2}\right)^2},\qquad \tan2\theta_p = \frac{\gamma_{xy}}{\epsilon_x - \epsilon_y},\qquad \frac{\gamma_{max}}{2} = R$$

**5. Mohr's circle of strain:** horizontal axis ε, vertical axis **γ/2** (+γ/2 plotted **downward at x**, as for stress). Centre $\frac{\epsilon_x + \epsilon_y}{2}$, radius $R = \sqrt{(\frac{\epsilon_x - \epsilon_y}{2})^2 + (\frac{\gamma_{xy}}{2})^2}$.

**6. Special cases and the 3-D view.**
- For an isotropic material, **principal strain axes = principal stress axes** (Ch. 5), so either circle gives the directions.
- *Absolute maximum shear strain:* with all three principal strains, $\gamma_{abs,max} = \epsilon_{max} - \epsilon_{min}$. In plane strain the third principal strain is 0; in plane stress it is $\epsilon_z = -\frac{\nu}{1-\nu}(\epsilon_x + \epsilon_y)$, generally not zero.

**7. Traps.** Plotting γ instead of γ/2 doubles the radius. Remember $\gamma_{max} = 2R = \epsilon_1 - \epsilon_2$ (in-plane), and check whether the out-of-plane direction gives more.

**8. Summary.** Replace σ → ε and τ → γ/2 in every stress formula.

### B. Solved questions

#### Q24 (Slides Ch4 Part 2 = Crandall worked example) — Sheet metal: strains on axes 30° clockwise; principal strains *(medium)*
**Problem.** A sheet of metal is deformed uniformly in its own plane with $\epsilon_x = -200\mu$, $\epsilon_y = 1000\mu$ and $\gamma_{xy} = 900\mu$ (μ = 10⁻⁶). Find the strain components for axes x′y′ inclined 30° clockwise to xy, and the principal strains and their directions.

**Solution.**
1. Centre = 400μ; $(\epsilon_x - \epsilon_y)/2 = -600\mu$; γ/2 = 450μ; $R = \sqrt{600^2 + 450^2} = 750\mu$.
2. θ = −30°: cos(−60°) = 0.5 and sin(−60°) = −0.866.
3. $\epsilon_{x'} = 400 + (-600)(0.5) + 450(-0.866) = -290\mu$; $\epsilon_{y'} = 800 - (-290) = 1090\mu$.
4. $\dfrac{\gamma_{x'y'}}{2} = -(-600)(-0.866) + 450(0.5) = -295\mu$, so $\gamma_{x'y'} = -590\mu$.
5. *Principal:* ε₁ = 1150μ and ε₂ = −350μ. $\tan2\theta_p = 900/(-1200)$, so ε₁ lies at θ = 71.6° from x (ε₂ at −18.4°).

$$\boxed{\epsilon_{x'} = -290\mu,\ \epsilon_{y'} = 1090\mu,\ \gamma_{x'y'} = -590\mu;\qquad \epsilon_1 = 1150\mu\ (71.6^\circ),\ \epsilon_2 = -350\mu}$$

**Check (slide's circle).** The angle at the centre is 60° − 36.8°, and point x′ lies above the axis, so $\gamma_{x'y'} < 0$ ✓.

**Exam takeaway.** Mind the direction: "30° clockwise" means θ = −30°.

---

#### Q25 (Crandall Prob 4.20) — Principal strains *(easy)*
**Problem.** For $\epsilon_x = 800\mu$, $\epsilon_y = 100\mu$ and $\gamma_{xy} = -800\mu$, find the principal strains and their directions.

**Solution.**
1. Centre 450μ; $R = \sqrt{350^2 + 400^2} = 531.5\mu$.
2. ε₁ = 981.5μ and ε₂ = −81.5μ.
3. $\tan2\theta_p = \dfrac{-800}{700}$, so 2θp = −48.8° and θp1 = −24.4° (24.4° clockwise from x).

$$\boxed{\epsilon_1 = 981.5\mu\ \text{at } 24.4^\circ\ \text{clockwise},\qquad \epsilon_2 = -81.5\mu,\qquad \gamma_{max} = 1063\mu}$$

**Check.** Substitute θ = −24.4°: $450 + 350\cos(-48.8^\circ) - 400\sin(-48.8^\circ) = 450 + 230.5 + 301 = 981.5$ ✓.

---

#### Q26 (Crandall Prob 4.21) — Maximum shear strain from three principal strains *(easy)*
**Problem.** At a point, the principal strains are $\epsilon_I = 700\mu$, $\epsilon_{II} = 300\mu$ and $\epsilon_{III} = -300\mu$. Find the maximum shear strain and the orientation of the axes that experience it.

**Solution.**
1. $\gamma_{max} = \epsilon_{max} - \epsilon_{min} = 700 - (-300) = 1000\mu$.
2. It occurs in the I–III plane, on the pair of perpendicular axes bisecting the I and III directions (at 45° to each).

$$\boxed{\gamma_{max} = 1000\times10^{-6}\ \text{rad, on axes at } 45^\circ\ \text{between the I and III axes}}$$

**Exam takeaway.** The largest Mohr's circle is the one spanning the extreme principal values.

---

#### Q27 (Crandall Prob 4.23) — Plane strain: axes of maximum shear strain and the deformed element *(medium)*
**Problem.** A body is in plane strain in the x–y plane with $\epsilon_x = -800\mu$, $\epsilon_y = -200\mu$ and $\gamma_{xy} = -600\mu$. Show the axes associated with the maximum shear strain and the deformed shape of an element aligned with them.

**Solution.**
1. Centre −500μ; $R = \sqrt{300^2 + 300^2} = 424.3\mu$, so ε₁ = −75.7μ and ε₂ = −924.3μ.
2. $\tan2\theta_p = \dfrac{-600}{-600}$, so 2θp = −135° and ε₁ lies at θ = −67.5° (i.e. 112.5°); ε₂ lies at 22.5°.
3. *In-plane* $\gamma_{max} = 2R = 848.5\mu$, on axes at θp ± 45°, i.e. at −22.5° and 67.5°. An element aligned with these axes shrinks equally on both axes by the centre value (−500μ) and loses (or gains) 848.5 μrad of its right angle.
4. *Absolute (3-D):* in plane strain ε₃ = εz = 0, so $\gamma_{abs} = 0 - (-924.3) = 924.3\mu$, in the plane containing z and the ε₂ direction, on axes at 45° to them.

$$\boxed{\gamma_{in-plane,max} = 848.5\mu\ \text{on axes at } -22.5^\circ\ \&\ 67.5^\circ;\qquad \gamma_{abs,max} = 924.3\mu\ \text{(out of plane)}}$$

**Exam takeaway.** When both in-plane principal strains have the same sign, the out-of-plane direction wins.

---

## Concept 4.7 — Strain rosettes

### A. Concept explanation

**1. Intuition.** One strain gauge measures stretch in one direction only. A point in plane strain has *three* unknowns (εx, εy, γxy), so glue **three gauges** at different angles (a rosette) and solve three equations.

**2. Why it matters.** This is how real structures (bridges, aircraft, the bracket in the slide example) are monitored. PYQs: 2021 A-Q1 (one gauge at 45° on a shaft), 2019 A-Q2 (from principal strains back to x–y).

**3. Formal treatment (slides).** Each gauge at angle $\theta_i$ reads
$$\epsilon_i = \epsilon_x\cos^2\theta_i + \epsilon_y\sin^2\theta_i + \gamma_{xy}\sin\theta_i\cos\theta_i$$
**45° rectangular rosette** (0°, 45°, 90°): $\epsilon_x = \epsilon_a$, $\epsilon_y = \epsilon_c$, $\boxed{\gamma_{xy} = 2\epsilon_b - (\epsilon_a + \epsilon_c)}$.
**60° delta rosette** (0°, 60°, 120°): $\epsilon_x = \epsilon_a$, $\epsilon_y = \tfrac13(2\epsilon_b + 2\epsilon_c - \epsilon_a)$, $\gamma_{xy} = \tfrac{2}{\sqrt3}(\epsilon_b - \epsilon_c)$.

**4. Derivations.**
- *45°:* at θ = 45°, cos² = sin² = sin·cos = ½, so $\epsilon_b = \tfrac12(\epsilon_x + \epsilon_y + \gamma_{xy})$, giving $\gamma_{xy} = 2\epsilon_b - \epsilon_a - \epsilon_c$. ∎
- *60°:* at 60°: $\epsilon_b = 0.25\epsilon_x + 0.75\epsilon_y + 0.433\gamma$; at 120°: $\epsilon_c = 0.25\epsilon_x + 0.75\epsilon_y - 0.433\gamma$. Subtracting gives $\gamma = (\epsilon_b - \epsilon_c)/0.866$; adding gives $\epsilon_y = (\epsilon_b + \epsilon_c - 0.5\epsilon_a)/1.5$. ∎

**5. Picture.** Mohr's circle of strain through the three gauge readings: each gauge's ε is the horizontal coordinate of a point on the circle at 2θ apart.

**6. Special cases.** A single gauge at 45° on a shaft in pure torsion reads γ/2 (since εx = εy = 0).

**7. Traps.**
- Angles must be measured counter-clockwise from the gauge chosen as x (gauge a).
- Mixing degrees and radians on calculators.
- Final principal *stresses* need Hooke's law in **plane stress** (the surface is free).

**8. Summary.** 45°: γ = 2εb − εa − εc. 60°: εy = (2εb + 2εc − εa)/3 and γ = 2(εb − εc)/√3. Gauge at 45° on a shaft: γ/2.

### B. Solved questions

#### Q28 (Slides Ch4 Part 2, Hibbeler Example 10.8) — 60° rosette on a bracket *(medium)*
**Problem.** A 60° rosette at point A on a bracket gives $\epsilon_a = 60\mu$ (0°), $\epsilon_b = 135\mu$ (60°) and $\epsilon_c = 264\mu$ (120°). Find the in-plane principal strains and their directions.

**Solution.**
1. $\epsilon_x = 60\mu$.
2. 60° and 120° gauges: $135 = 0.25\epsilon_x + 0.75\epsilon_y + 0.433\gamma$ and $264 = 0.25\epsilon_x + 0.75\epsilon_y - 0.433\gamma$.
3. Subtract: $0.866\gamma = -129$, so γxy = −149μ. Add: $1.5\epsilon_y = 399 - 30$, so εy = 246μ.
4. Centre 153μ; $R = \sqrt{93^2 + 74.5^2} = 119.2\mu$.

$$\boxed{\epsilon_1 = 272\mu,\qquad \epsilon_2 = 33.8\mu,\qquad \theta_{p2} = 19.3^\circ\ \text{(counter-clockwise from x, direction of } \epsilon_2)}$$

**Check.** Formulas: $\epsilon_y = \tfrac13(270 + 528 - 60) = 246$ ✓ and $\gamma = \tfrac{2}{\sqrt3}(135 - 264) = -149$ ✓.

**Exam takeaway.** ⚠ The slide writes "ε₂ = 246(10⁻⁶) − 119.2(10⁻⁶) = 33.8". The 246 is a typo for **153** (the centre); the result 33.8 is correct.

---

#### Q29 (Crandall Prob 4.22) — 45° rosette readings to principal strains *(easy–medium)*
**Problem.** A 45° rosette reads (a) εa = 100μ, εb = 200μ, εc = 900μ; (b) εa = 1200μ, εb = 400μ, εc = 60μ. Find the principal strains in the plane of the rosette.

**Solution.**
1. *(a)* εx = 100, εy = 900, γ = 2(200) − 100 − 900 = −600μ. Centre 500; $R = \sqrt{400^2 + 300^2} = 500$, so ε₁ = 1000μ and ε₂ = 0.
2. *(b)* εx = 1200, εy = 60, γ = 2(400) − 1260 = −460μ. Centre 630; $R = \sqrt{570^2 + 230^2} = 614.7$, so ε₁ = 1244.7μ and ε₂ = 15.3μ.

$$\boxed{(a)\ \epsilon_1 = 1000\mu,\ \epsilon_2 = 0;\qquad (b)\ \epsilon_1 = 1245\mu,\ \epsilon_2 = 15\mu}$$

**Check.** In (a) the circle is a 3-4-5 triangle scaled by 100 ✓.

**Exam takeaway.** The middle gauge supplies the shear; the outer two supply εx and εy directly.

---

#### Q30 (PYQ 2021-22 Compre A Q1) — Strain gauge at 45° on a twisted bar: find G *(easy, 10 marks)*
**Problem.** A solid 50 mm bar is twisted until T = 500 N·m. A strain gauge at 45° to the axis reads ε = 350 × 10⁻⁶. Find the shear modulus G.

**Approach.** Surface shear from torsion (Ch. 6); in pure shear the 45° direction is principal and $\epsilon_{45} = \gamma/2$.

**Solution.**
1. $\tau = \dfrac{16T}{\pi d^3} = \dfrac{16(500\,000)}{\pi(50)^3} = 20.37$ MPa.
2. $\gamma = 2\epsilon_{45} = 700\times10^{-6}$.
3. $G = \tau/\gamma = \dfrac{20.37}{700\times10^{-6}}$.

$$\boxed{G = 29.1\ \text{GPa}}$$

**Check (via Hooke).** Principal stresses ±τ give $\epsilon_{45} = \frac{\tau(1+\nu)}{E} = \frac{\tau}{2G}$ ✓. The slide version of this problem (ε = 339μ) gives G = 30.0 GPa ✓.

**Exam takeaway.** "Gauge at 45° on a shaft" ⇒ reading = γ/2. **Variation:** given G, find T from the reading.

---

#### Q31 (PYQ 2019-20 Compre A Q2) — From principal strains to σx, σy, τxy *(medium, 7 marks)*
**Problem.** The principal strains in an aluminium plate loaded in its plane are ε₁ = −8.1 × 10⁻⁴ and ε₂ = 5.7 × 10⁻⁴, with principal direction 1 at 60° from x (toward y). Using Mohr's circle, find σx, σy and τxy. E = 72 GPa, ν = 0.33.

**Approach.** Principal strains → principal stresses (plane-stress Hooke, Ch. 5), then rotate the stress circle back to x–y.

**Solution.**
1. *Principal stresses:* $\dfrac{E}{1 - \nu^2} = 80\,799$ MPa.
   - $\sigma_1 = 80\,799(\epsilon_1 + \nu\epsilon_2) = 80\,799(-8.1 + 1.881)\times10^{-4} = -50.2$ MPa
   - $\sigma_2 = 80\,799(\epsilon_2 + \nu\epsilon_1) = 80\,799(5.7 - 2.673)\times10^{-4} = 24.5$ MPa
2. *Mohr's circle of stress:* centre −12.9, R = 37.4. The x-axis is at θ = −60° from axis 1, so rotate 120° clockwise from point "1" on the circle.
   - $\sigma_x = -12.9 + (-37.35)\cos(-120^\circ) = 5.8$ MPa
   - $\sigma_y = -12.9 - 18.7 = -31.6$ MPa
   - $\tau_{xy} = -(-37.35)\sin(-120^\circ) = -32.3$ MPa

$$\boxed{\sigma_x = 5.8\ \text{MPa},\qquad \sigma_y = -31.6\ \text{MPa},\qquad \tau_{xy} = -32.3\ \text{MPa}}$$

**Check.** σx + σy = −25.8 = σ₁ + σ₂ ✓; $\sqrt{18.7^2 + 32.3^2} = 37.4 = R$ ✓.

**Exam takeaway.** Alternatively, transform the *strains* to x–y first (strain circle), then apply Hooke's law; the answer is the same. Crandall Prob 5.10 is the same question with ε₁ = 3.2 × 10⁻⁴ and ε₂ = −5.4 × 10⁻⁴.

---

#### Q32 (PYQ 2021-22 Compre B Q1) — Circle → ellipse: lengths and orientation of the axes *(medium–hard, 10 marks)*
**Problem.** A 250 mm circle is scribed on a mild-steel plate, which is then stressed with σx = 120, σy = 25 and τxy = 10 MPa. The circle becomes an ellipse. Find the lengths of the major and minor axes and their orientation. E = 200 GPa, ν = 0.3.

**Approach.** The ellipse's axes lie along the **principal strain** directions, which equal the principal stress directions for an isotropic material.

**Solution.**
1. *Principal stresses:* centre 72.5, $R = \sqrt{47.5^2 + 10^2} = 48.54$, so σ₁ = 121.04 and σ₂ = 23.96 MPa. $\theta_p = \tfrac12\tan^{-1}\frac{20}{95} = 5.94^\circ$ counter-clockwise from x (for σ₁).
2. *Principal strains (plane stress):*
$$\epsilon_1 = \frac{121.04 - 0.3(23.96)}{200\,000} = 569.3\mu,\qquad \epsilon_2 = \frac{23.96 - 0.3(121.04)}{200\,000} = -61.8\mu$$
3. *Axes:* major = 250(1 + ε₁) = 250.142 mm; minor = 250(1 + ε₂) = 249.985 mm.

$$\boxed{\text{Major} = 250.142\ \text{mm at } 5.94^\circ\ \text{from x};\qquad \text{Minor} = 249.985\ \text{mm at } 95.94^\circ}$$

**Check.** Using σ/E without the Poisson term would give minor = 250.030 mm (longer than d), which is wrong: the contraction from σ₁ wins ✓.

**Exam takeaway.** A sketch of the tilted ellipse is required for full marks.

---

#### Q33 (PYQ 2014-15 Test-2 Q2) — Absolute maximum shear strain in a bar *(easy–medium, 15 marks)*
**Problem.** A steel bar 2 cm × 0.5 cm carries a tensile load of 5 kN. E = 200 GPa, ν = 0.3. Find the absolute maximum shear strain.

**Solution.**
1. $\sigma = \dfrac{5000}{20\times5} = 50$ MPa (uniaxial).
2. Principal strains: $\epsilon_1 = \sigma/E = 250\mu$ and $\epsilon_2 = \epsilon_3 = -\nu\sigma/E = -75\mu$.
3. $\gamma_{abs,max} = \epsilon_{max} - \epsilon_{min} = 250 - (-75)$.

$$\boxed{\gamma_{abs,max} = 325\times10^{-6}\ \text{rad}}$$

**Check.** $\tau_{max} = \sigma/2 = 25$ MPa and $G = E/2(1 + \nu) = 76.9$ GPa give γ = 25/76 900 = 325μ ✓.

**Exam takeaway.** "Absolute" means include the out-of-plane direction; here in-plane and absolute coincide because ε₂ = ε₃.

---

## Chapter 4 — Formula and convention sheet

| Item | Formula / rule |
|---|---|
| Sign of stress | +face & +direction, or −face & −direction |
| Symmetry | $\tau_{xy} = \tau_{yx}$ |
| Equilibrium | $\partial\sigma_x/\partial x + \partial\tau_{xy}/\partial y = 0$, $\partial\tau_{xy}/\partial x + \partial\sigma_y/\partial y = 0$ |
| Transformation | $\sigma_{x'} = \bar\sigma + \frac{\sigma_x - \sigma_y}{2}\cos2\theta + \tau_{xy}\sin2\theta$; $\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta$ |
| Invariant | $\sigma_{x'} + \sigma_{y'} = \sigma_x + \sigma_y$ |
| Principal | $\sigma_{1,2} = \bar\sigma \pm R$, $R = \sqrt{(\frac{\sigma_x - \sigma_y}{2})^2 + \tau_{xy}^2}$, $\tan2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}$ (check which θ gives σ₁) |
| Max in-plane shear | $\tau_{max} = R$ at θp ± 45°, with normal stress $\bar\sigma$ there |
| Absolute max shear | $(\sigma_{max} - \sigma_{min})/2$ including σ₃ = 0 |
| Mohr's circle | +τ plotted **down at X**, up at Y; 2θ on the circle = θ on the element, same sense |
| Thin cylinder | $\sigma_\theta = pr/t$, $\sigma_z = pr/2t$ (closed) or $F/2\pi rt$ (open); $\tau_{\theta z} = pr/4t$ |
| Thin sphere | $\sigma = pr/2t$ |
| Filament angle (closed cylinder) | $\tan^2\alpha = 2$, α = 54.7° |
| Strains | $\epsilon_x = \partial u/\partial x$, $\epsilon_y = \partial v/\partial y$, $\gamma_{xy} = \partial u/\partial y + \partial v/\partial x$; polar $\epsilon_\theta = u/r$ |
| Strain transformation | replace σ → ε and τ → γ/2 in the stress equations |
| Strain circle | vertical axis γ/2; $\gamma_{max} = \epsilon_1 - \epsilon_2$ (in-plane); absolute uses all three |
| 45° rosette | εx = εa, εy = εc, γ = 2εb − εa − εc |
| 60° rosette | εy = (2εb + 2εc − εa)/3, γ = 2(εb − εc)/√3 |
| Gauge at 45° on a shaft | $\epsilon_{45} = \gamma/2 = \tau/2G$ |

**Other Crandall Ch. 4 problems worth practising:** 4.1–4.4 (equilibrium equations in Cartesian and polar form), 4.5 (sign convention independence), 4.16–4.19 (strain–displacement in 3-D and polar), 4.24 and 4.29 (rigid-body motions), 4.26 (superposed states), 4.30 (stress-free boundary), 4.33 (beam equations from equilibrium).
