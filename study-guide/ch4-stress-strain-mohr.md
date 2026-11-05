# Chapter 4 — Stress and Strain
### Stress at a point, plane stress, stress transformation, Mohr's circle, principal and maximum shear stresses, plane strain, strain transformation, Mohr's circle of strain, strain rosettes

**Sources used:** Slides "Chapter 4 part 1" (stress) and "Ch 4 Part 2" (strain), Crandall Ch. 4 (§4.2–4.9, Example on sheet-metal strain, Prob 4.20), PYQs 2019-20 (A-Q2), 2021-22 (A-Q1, B-Q1), 2014-15 (Test-2 Q1, Q2; Compre A-Q12, Q13; Compre B-Q1).

---

## ⚠️ Read first: sign conventions for this chapter

1. **Stress sign (Crandall, slides):** a stress component is **positive** when it acts on a **positive face in a positive direction**, or on a **negative face in a negative direction**. Tension is +. $\tau_{xy}>0$ means that on the right (+x) face the shear points **up** (+y).
2. **Angle θ:** measured **counter-clockwise from x to x′** (the normal of the inclined face).
3. **Mohr's circle (Crandall and slides use the same rule):** σ is plotted to the right. **A positive $\tau_{xy}$ is plotted *downward* at point x and *upward* at point y.** With this rule, **a rotation of 2θ counter-clockwise on the circle equals a rotation of θ counter-clockwise on the element.** (Beer/Hibbeler say "positive shear (clockwise on element) plotted up", which is the same circle.)
   - If you plot $\tau_{xy}$ *upward* at x (the "math" convention), the circle is mirrored and **2θ rotations reverse direction**. This is the most common Mohr's-circle mistake in the exam.
4. **Strain Mohr's circle:** the vertical axis is **γ/2**, not γ. Same plotting rule: $+\gamma_{xy}/2$ is downward at x.

---

## Concept 4.1 — Stress at a point and the stress tensor

### A. Concept explanation

**1. Intuition.** Squeeze a sponge in your hand. Every tiny cube inside it is pushed and dragged by its neighbours. "Stress" is the intensity of that push or drag, force per unit area, on a particular imaginary cut. A single number isn't enough, because the answer depends on *which way* you slice. Slice it one way and the material is pulled apart; slice at 45° and it may be sliding.

**2. Why it matters (slides' motivating example).** A bracket ABC carries 30 kN at B. AC is 2 m horizontal and BC is a 20 mm rod rising 1.5 m. Statics gives $F_{BC} = 50$ kN (T) and $F_{AB} = 40$ kN (C), but that alone doesn't tell you whether rod BC survives. That depends on (1) the internal force, (2) the cross-sectional area and (3) the material.
$$\sigma_{BC} = \frac{50\,000}{\pi(10)^2} = 159\ \text{MPa}$$
Compare this with the allowable stress of the material (for example, 165 MPa for structural steel, which is safe). Stress is the bridge from forces (Ch. 1–3) to material failure (Ch. 5).

**3. Formal treatment (Crandall §4.2–4.3, slide figures 4.1–4.8).** Cut the body by a plane with normal $\mathbf n$ through point O. On a small area $\Delta A$ the internal force is $\Delta\mathbf F$. Resolve it into components on an x-face ($\Delta A_x = \Delta y\Delta z$):
$$\sigma_x = \lim_{\Delta A_x\to0}\frac{\Delta F_x}{\Delta A_x},\qquad \tau_{xy} = \lim\frac{\Delta F_y}{\Delta A_x},\qquad \tau_{xz} = \lim\frac{\Delta F_z}{\Delta A_x}$$
The first subscript is the **face normal** and the second is the **direction**. Doing this on all three faces gives the **stress tensor**:
$$\begin{bmatrix}\sigma_x & \tau_{xy} & \tau_{xz}\\ \tau_{yx} & \sigma_y & \tau_{yz}\\ \tau_{zx} & \tau_{zy} & \sigma_z\end{bmatrix}$$
**Plane stress (slides):** only the components in one plane are non-zero, $\sigma_z=\tau_{zx}=\tau_{zy}=0$. Two faces of the cube are stress-free. This is typical of thin plates loaded in their plane and of the free surface of any part (where all strain gauges sit).

**4. Derivation — equilibrium of a differential element (Crandall Fig. 4.10, slides).**
On an element $\Delta x\times\Delta y\times\Delta z$ in plane stress, the stresses change from face to face, for example $\sigma_x$ on the left and $\sigma_x + \frac{\partial\sigma_x}{\partial x}\Delta x$ on the right.
- *Moment about the z-axis through the centre:* $(\tau_{xy}\Delta y\Delta z)\Delta x - (\tau_{yx}\Delta x\Delta z)\Delta y + (\text{higher-order terms}) = 0$. Divide by $\Delta x\Delta y\Delta z$ and let the element shrink:
$$\boxed{\tau_{xy} = \tau_{yx}}\qquad\text{(shear stresses on perpendicular faces are equal; they point toward or away from the same corner)}$$
- *Force balance in x and y* (no body force):
$$\boxed{\frac{\partial\sigma_x}{\partial x}+\frac{\partial\tau_{xy}}{\partial y}=0,\qquad \frac{\partial\tau_{xy}}{\partial x}+\frac{\partial\sigma_y}{\partial y}=0}$$
So in 3-D only 6 of the 9 stress components are independent.

**5. Picture.** A positive $\tau_{xy}$ element (Crandall Fig. 4.11): arrows ↑ on the right face, ↓ on the left face, → on the top face, ← on the bottom face. The element is pushed into a rhombus that is "stretched along the 45° diagonal" (the diagonal joining the first-quadrant corner to the third-quadrant corner).

**6. Special cases.** Uniaxial: only $\sigma_x$. Hydrostatic: $\sigma_x=\sigma_y=\sigma_z=-p$ with no shear on any plane. Pure shear: only $\tau_{xy}$.

**7. Traps.** Drawing $\tau_{yx}$ opposite to $\tau_{xy}$ on adjacent faces. They must meet head-to-head or tail-to-tail at the corners. Forgetting that stress is force per area: you can't add stresses on differently-oriented faces without multiplying by the areas (that is the next concept).

**8. Summary.** Stress = force/area on a specified face. Plane stress is described by $(\sigma_x, \sigma_y, \tau_{xy})$, with $\tau_{xy} = \tau_{yx}$.

---

## Concept 4.2 — Stress transformation in plane stress

### A. Concept explanation

**1. Intuition.** The material at a point is in one definite physical state. Rotating the imaginary cube is like walking around a statue: you see it differently but the statue doesn't change. The transformation equations tell you what $\sigma$ and $\tau$ a cut at angle θ "sees".

**2. Why it matters.** Welded and glued joints at an angle, the grain of wood, failure planes (ductile metals fail on 45° shear planes, brittle ones on principal planes), and the starting point for principal stresses and Mohr's circle.

**3. Formal treatment.** Given $\sigma_x, \sigma_y, \tau_{xy}$, find $\sigma_{x'}, \tau_{x'y'}$ on the face whose outward normal $x'$ is at angle θ counter-clockwise from x.

**4. Derivation (wedge equilibrium, slides).** Cut a triangular wedge: the inclined face has area $\Delta A$ and normal $x'$. The vertical (−x) face has area $\Delta A\cos\theta$ and the horizontal (−y) face has area $\Delta A\sin\theta$.
Forces on the negative faces (multiply stress by area):
- −x face: $\sigma_x\Delta A\cos\theta$ (←) and $\tau_{xy}\Delta A\cos\theta$ (↓)
- −y face: $\sigma_y\Delta A\sin\theta$ (↓) and $\tau_{xy}\Delta A\sin\theta$ (←)

**Sum forces along $x'$** (unit vector $(\cos\theta, \sin\theta)$):
$$\sigma_{x'}\Delta A = \sigma_x\Delta A\cos^2\theta + \sigma_y\Delta A\sin^2\theta + 2\tau_{xy}\Delta A\sin\theta\cos\theta$$
**Sum forces along $y'$** (unit vector $(-\sin\theta,\cos\theta)$):
$$\tau_{x'y'} = -(\sigma_x - \sigma_y)\sin\theta\cos\theta + \tau_{xy}(\cos^2\theta-\sin^2\theta)$$
Use the double-angle identities $\cos^2\theta = \frac{1+\cos2\theta}{2}$, $\sin^2\theta = \frac{1-\cos2\theta}{2}$, $2\sin\theta\cos\theta = \sin2\theta$:
$$\boxed{\sigma_{x'} = \frac{\sigma_x+\sigma_y}{2} + \frac{\sigma_x-\sigma_y}{2}\cos2\theta + \tau_{xy}\sin2\theta}$$
$$\boxed{\tau_{x'y'} = -\frac{\sigma_x-\sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta}$$
$$\boxed{\sigma_{y'} = \frac{\sigma_x+\sigma_y}{2} - \frac{\sigma_x-\sigma_y}{2}\cos2\theta - \tau_{xy}\sin2\theta}$$
**Invariant:** $\sigma_{x'}+\sigma_{y'} = \sigma_x+\sigma_y$. Use it to check every answer.

**5. Picture.** All three equations depend on **2θ**, so rotating the element by 180° gives the same state (as it must, since a face and its opposite are the same plane).

**6. Special cases.**
- Uniaxial $\sigma_x = \sigma$: $\sigma_{\theta} = \sigma\cos^2\theta$ and $\tau = -\frac{\sigma}{2}\sin2\theta$, so $|\tau|_{max} = \sigma/2$ at 45°. This is why ductile bars fail at 45°.
- Pure shear $\tau$: $\sigma_{45^\circ} = +\tau$ and $\sigma_{135^\circ} = -\tau$, so the principal stresses are ±τ at 45°. This is the basis of torsion strain-gauge problems (Ch. 6).

**7. Traps.**
- Measuring θ from the *plane* instead of from its **normal**. If a weld line is at β to the cross-section, the weld's normal is at β to the axis.
- Using θ instead of 2θ in the trig functions.
- Mixing up the sign of $\tau_{xy}$ (check the right face: is the arrow up?).

### B. Solved questions

#### Q1 (Slides Ch4) — Stresses on a 45° plane *(easy)*
**Given:** $\sigma_x = 110$, $\sigma_y = 50$, $\tau_{xy} = +40$ MN/m² (MPa). **Find:** the stresses on faces a (normal at 45°) and b (normal at 135°).
$\frac{\sigma_x+\sigma_y}{2}=80$, $\frac{\sigma_x-\sigma_y}{2}=30$, and $2\theta = 90^\circ$ (cos = 0, sin = 1).
$$\sigma_a = 80+0+40 = \boxed{120\ \text{MPa}},\quad \tau_{ab} = -30+0 = \boxed{-30\ \text{MPa}},\quad \sigma_b = 80-0-40 = \boxed{40\ \text{MPa}}$$
**Check:** $120 + 40 = 160 = 110+50$ ✓. On face a the shear acts toward −b, i.e. clockwise on the rotated element.

---

#### Q2 (Slides Ch4, Beer Prob 7.x) — Oblique face by wedge equilibrium *(medium)*
**Given:** $\sigma_x = 27$ MPa, $\sigma_y = -45$ MPa, $\tau_{xy} = 18$ MPa. The shaded triangle's oblique face is 15° from the horizontal, so its outward normal is at θ = 105° (= 90° + 15°). **Find:** σ and τ on the oblique face.
$$\sigma = -9 + 36\cos210^\circ + 18\sin210^\circ = -9 - 31.18 - 9 = \boxed{-49.2\ \text{MPa}}$$
$$\tau = -36\sin210^\circ + 18\cos210^\circ = 18 - 15.59 = \boxed{2.41\ \text{MPa}}$$
✓ Matches the slide answer. The slide sets up the force balance on the wedge with areas $A\cos15^\circ$ and $A\sin15^\circ$, which is exactly the derivation above with numbers.

---

#### Q3 (Slides Ch4, Beer Prob 7.x) — Welded plates *(medium)*
**Given:** two steel plates 10 × 80 mm, welded along a line at angle β to the cross-section, axial force 100 kN. In-plane shear stress parallel to the weld = 30 MPa. **Find:** (a) β, (b) the normal stress perpendicular to the weld.
$\sigma_x = 100\,000/(10\times80) = 125$ MPa (uniaxial). The weld's normal is at β to the axis.
- (a) $|\tau| = \frac{\sigma_x}{2}\sin2\beta = 62.5\sin2\beta = 30 \Rightarrow \sin2\beta = 0.48 \Rightarrow \boxed{\beta = 14.3^\circ}$
- (b) $\sigma = \frac{\sigma_x}{2}(1+\cos2\beta) = 62.5(1+0.8773) = \boxed{117.3\ \text{MPa}}$

**Check by direct force balance (slides):** $F_s = 100\sin\beta = 24.77$ kN and $A_w = 800/\cos\beta = 825.7$ mm². $24770/825.7 = 30$ MPa ✓.

---

## Concept 4.3 — Mohr's circle, principal stresses and maximum shear stress

### A. Concept explanation

**1. Intuition.** As you spin the cut through 180°, the pair $(\sigma_{x'}, \tau_{x'y'})$ traces out a **circle**. The rightmost point of the circle is the largest normal stress any cut can feel, the leftmost is the smallest, and the top and bottom are the largest shear. Mohr's circle is a picture of *every possible cut at once*.

**2. Why it matters.** Failure criteria (Ch. 5) need principal stresses, and PYQs ask for "principal stresses and orientation" or "sketch the Mohr's circle" every year.

**3. Formal treatment / 4. Derivation (slides).** Move the average to the left side and square both transformation equations:
$$\left(\sigma_{x'} - \frac{\sigma_x+\sigma_y}{2}\right)^2 = \left(\frac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta\right)^2,\qquad \tau_{x'y'}^2 = \left(-\frac{\sigma_x-\sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta\right)^2$$
Add them. The cross terms cancel and $\sin^2+\cos^2 = 1$:
$$\boxed{(\sigma_{x'}-\sigma_{avg})^2 + \tau_{x'y'}^2 = R^2},\qquad \sigma_{avg} = \frac{\sigma_x+\sigma_y}{2},\quad R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}$$
This is a circle with centre $(\sigma_{avg}, 0)$ and radius $R$.

**Principal stresses** (shear = 0): set $\tau_{x'y'}=0$:
$$\boxed{\tan2\theta_p = \frac{2\tau_{xy}}{\sigma_x-\sigma_y}},\qquad \boxed{\sigma_{1,2} = \sigma_{avg}\pm R}$$
This gives two angles 90° apart. **To tell which angle gives σ₁, substitute it back into the $\sigma_{x'}$ equation.**
Equivalently, $d\sigma_{x'}/d\theta = 0$ gives the same condition, so principal stresses are the extremes of normal stress.

**Maximum in-plane shear:**
$$\boxed{\tau_{max} = R = \frac{\sigma_1-\sigma_2}{2}},\qquad \tan2\theta_s = -\frac{\sigma_x-\sigma_y}{2\tau_{xy}},\quad \theta_s = \theta_p\pm45^\circ$$
On the max-shear planes the normal stress is **not zero**. It equals $\sigma' = \sigma_{avg}$.

**Absolute maximum shear (3-D view of plane stress):** the out-of-plane principal stress is $\sigma_3 = 0$. Order the three as $\sigma_{max} \ge \sigma_{mid} \ge \sigma_{min}$. Then
$$\tau_{abs,max} = \frac{\sigma_{max} - \sigma_{min}}{2}$$
If $\sigma_1,\sigma_2$ have the **same sign**, $\tau_{abs} = |\sigma_1|/2$ (or $|\sigma_2|/2$), which is **larger than the in-plane $R$**. Examiners love this.

**5. Graphical construction (Crandall §4.5, slides). You must be able to draw this.**
1. Axes: σ horizontal (+ right) and τ vertical. Following Crandall, *positive τ plotted downward at x*.
2. Plot **X** $= (\sigma_x,\ \tau_{xy}$ *downward* if positive$)$.
3. Plot **Y** $= (\sigma_y,\ \tau_{xy}$ *upward* if positive$)$.
4. Join XY. It crosses the σ-axis at the centre C $= \sigma_{avg}$. Radius $R = CX$.
5. Points A (rightmost) and B (leftmost) give $\sigma_1$ and $\sigma_2$. Points D and E (top and bottom) give $\pm\tau_{max}$, both at $\sigma_{avg}$.
6. To find the stresses on a face rotated θ counter-clockwise, rotate the diameter XY by **2θ in the same sense** (counter-clockwise). The new ends are X′ and Y′.
7. The angle from CX to CA, measured on the circle, is $2\theta_p$. The element rotates by $\theta_p$ **in the same sense**.

**6. Special cases.**
| State | Circle |
|---|---|
| Uniaxial σ | passes through the origin, $R = \sigma/2$ |
| Pure shear τ | centred at the origin, $R=\tau$, principal stresses ±τ at 45° |
| Equal biaxial $\sigma_x=\sigma_y$, $\tau=0$ | shrinks to a point, every direction is principal |
| Hydrostatic | a point, no shear on any plane |

**7. Common traps.**
- **θ vs 2θ:** angles on the circle are double the element angles.
- **Direction of rotation:** consistent only if you plot +τ downward at X (Crandall convention).
- Using $\arctan$ blindly: $\tan2\theta_p$ has two solutions 180° apart. Pick by checking the quadrant on the circle, or substitute back.
- Reporting $\tau_{max}$ = R when both principal stresses have the same sign (the true maximum is out of plane).
- Forgetting $\sigma_{avg}$ on the max-shear planes when drawing the element.

**8. Summary box**
$$\sigma_{1,2}=\frac{\sigma_x+\sigma_y}{2}\pm\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2},\quad \tan2\theta_p=\frac{2\tau_{xy}}{\sigma_x-\sigma_y},\quad \tau_{max}=R,\ \theta_s=\theta_p\pm45^\circ,\ \sigma'=\sigma_{avg}$$

### B. Solved questions

#### Q4 (Slides Ch4, Beer Ex 7.1) — Principal planes, principal stresses, max shear *(easy, classic)*
**Given:** $\sigma_x = 50$, $\sigma_y = -10$, $\tau_{xy} = +40$ MPa.
**Equations:** $\tan2\theta_p = \frac{80}{60} = 1.333 \Rightarrow 2\theta_p = 53.1^\circ$, so $\theta_p = 26.6^\circ$ and $116.6^\circ$.
Substitute θ = 26.6°: $\sigma_{x'} = 20 + 30(0.6) + 40(0.8) = 70$, so this angle gives σ₁.
$$\boxed{\sigma_1 = 70\ \text{MPa at}\ 26.6^\circ,\quad \sigma_2 = -30\ \text{MPa at}\ 116.6^\circ}$$
$$\boxed{\tau_{max} = 50\ \text{MPa at}\ \theta_s = -18.4^\circ\ (\text{and } 71.6^\circ),\quad \sigma' = 20\ \text{MPa}}$$
**Mohr's circle:** C = 20, R = $\sqrt{30^2+40^2} = 50$. X = (50, 40 *below*), Y = (−10, 40 *above*). From X to A is 53.1° counter-clockwise, so the element rotates 26.6° counter-clockwise ✓.
**Absolute max shear:** σ₁ = 70, σ₂ = −30, σ₃ = 0, so $\tau_{abs} = (70-(-30))/2 = 50$ MPa (same as in-plane, because the signs are opposite).

---

#### Q5 (Slides Ch4, Beer Sample 7.2) — Principal stresses, then rotate the element 30° CCW *(medium)*
**Given:** $\sigma_x = 100$, $\sigma_y = 60$, $\tau_{xy} = -48$ MPa (shear on the right face points down).
C = 80, R = $\sqrt{20^2+48^2} = 52$.
$$\boxed{\sigma_1 = 132\ \text{MPa},\ \sigma_2 = 28\ \text{MPa},\ \theta_p = 33.7^\circ\ \text{clockwise}}$$
($\tan2\theta_p = -96/40 \Rightarrow 2\theta_p = -67.4^\circ$.)
**Rotate the element 30° CCW** (2θ = 60° on the circle):
$$\sigma_{x'} = 80+20\cos60^\circ-48\sin60^\circ = \boxed{48.4\ \text{MPa}},\quad \sigma_{y'}=\boxed{111.6\ \text{MPa}},\quad \tau_{x'y'} = -20\sin60^\circ-48\cos60^\circ = \boxed{-41.3\ \text{MPa}}$$
**Mohr's circle check:** X starts 67.4° *clockwise* from A (it is at 48 above, because τ is negative). Rotating 60° counter-clockwise puts X′ at φ = 180° − 60° − 67.4° = 52.6° from the negative σ-axis. So $\sigma_{x'} = 80 - 52\cos52.6^\circ = 48.4$ ✓ and $|\tau| = 52\sin52.6^\circ = 41.3$ ✓ (slide method).
**Invariant:** 48.4 + 111.6 = 160 ✓.

---

#### Q6 (PYQ 2014-15 Compre A Q12) — Principal stresses *(easy, 1-line answer)*
$\sigma_x = 50$, $\sigma_y=-10$, $\tau_{xy} = 40$ MPa, the same as Q4.
$$\boxed{\sigma_1 = 70\ \text{MPa},\quad \sigma_2 = -30\ \text{MPa}}$$

---

#### Q7 (PYQ 2014-15 Compre A Q13) — Which Mohr's circle? *(easy, conceptual)*
The element in the figure has **only shear** (no normal arrows), so it is **pure shear**. Its Mohr's circle is **centred at the origin** with radius τ. Choose the option whose circle is centred on the intersection of the axes (option **c** in the scanned paper, the circle centred on both axes).
**Takeaway:** know the four "signature" circles (uniaxial tension, uniaxial compression, pure shear, equal biaxial).

---

#### Q8 (PYQ 2014-15 Test-2 Q1) — Axial force + torque on a 40 mm shaft: principal stresses and Mohr's circle *(medium, 20 marks)*
**Given:** $P = 90$ kN (tension), $T = 250$ N·m, $d = 40$ mm. Point P is on the surface. **Find:** principal stresses, orientation, Mohr's circle.
- Axial: $\sigma = \dfrac{P}{A} = \dfrac{90\,000}{\pi(20)^2} = 71.6$ MPa
- Torsion (Ch. 6): $\tau = \dfrac{16T}{\pi d^3} = \dfrac{16(250\,000)}{\pi(40)^3} = 19.9$ MPa

With the bar axis vertical (the y-axis in the figure): $\sigma_y = 71.6$, $\sigma_x = 0$, $|\tau_{xy}| = 19.9$.
$\sigma_{avg} = 35.8$, $R = \sqrt{35.8^2+19.9^2} = 41.0$.
$$\boxed{\sigma_1 = 76.8\ \text{MPa},\quad \sigma_2 = -5.2\ \text{MPa},\quad \tau_{max} = 41.0\ \text{MPa}}$$
$\tan2\theta_p = \frac{2(19.9)}{71.6} \Rightarrow \theta_p = 14.5^\circ$, measured from the **bar axis** (the y-axis) to the σ₁ direction, i.e. 75.5° from the x-axis. The sense follows the direction of T.
**Mohr's circle:** centre 35.8, radius 41.0. It crosses the τ-axis because σ₂ < 0. Mark X(0, 19.9) and Y(71.6, 19.9) on opposite sides.
**Check:** σ₁σ₂ = −398 = −τ² (since $\sigma_x = 0$) ✓.

---

#### Q9 (PYQ 2014-15 Compre B Q1) — Superposing two stress states *(hard, 15 marks)*
**Given:** state 1 is biaxial compression (−350 MPa and −200 MPa) on an element rotated 60°. State 2 is pure shear of 58 MPa on an element rotated 25°. **Find:** the resultant on the x–y element, the Mohr's circle, principal stresses and strains ($E = 200$ GPa, ν = 0.3).

**Key idea:** you **cannot add stresses on differently oriented elements**. First transform each state to the *same* x–y axes (using the transformation equations with $\theta = -60^\circ$ and $\theta = -25^\circ$), *then* add component by component.

*State 1* (σ′ = −350 along x′ at 60°, σ″ = −200 along y′):
$$\sigma_x = -275 + (-75)\cos(-120^\circ) = -237.5,\quad \sigma_y = -312.5,\quad \tau_{xy} = -(-75)\sin(-120^\circ) = -65.0$$
*State 2* (pure shear τ′ = −58 on an element at 25°; the sign follows the arrows):
$$\sigma_x = \tau'\sin(-50^\circ) = 44.4,\quad \sigma_y = -44.4,\quad \tau_{xy} = \tau'\cos(-50^\circ) = -37.3$$
*Sum:*
$$\boxed{\sigma_x \approx -193\ \text{MPa},\quad \sigma_y \approx -357\ \text{MPa},\quad |\tau_{xy}| \approx 102\ \text{MPa}}$$
(This matches the textbook answer to the Hibbeler problem this question is taken from. The sign of τ depends on how the arrows are read. The principal values below don't depend on it.)

**Principal stresses:** $\sigma_{avg} = -275$ and $R = \sqrt{81.9^2+102.2^2} = 131.0$:
$$\boxed{\sigma_1 = -144\ \text{MPa},\quad \sigma_2 = -406\ \text{MPa}}\quad(\sigma_3 = 0)$$
**Principal strains (Hooke's law, plane stress; see Ch. 5):**
$$\epsilon_1 = \frac{\sigma_1-\nu\sigma_2}{E} = \frac{-144+121.8}{200\,000} = \boxed{-111\times10^{-6}},\quad \epsilon_2 = \frac{-406+43.2}{200\,000} = \boxed{-1814\times10^{-6}}$$
$$\epsilon_3 = -\frac{\nu}{E}(\sigma_1+\sigma_2) = \boxed{+825\times10^{-6}}\ \text{(thickness grows)}$$
**Checks:** the invariant $\sigma_x+\sigma_y = -550 = \sigma_1+\sigma_2$ ✓. Both principal stresses are compressive, so the circle lies entirely left of the τ-axis, and $\tau_{abs,max} = 406/2 = 203$ MPa > R.

---

## Concept 4.4 — Strain and strain–displacement relations (plane strain)

### A. Concept explanation

**1. Intuition.** Draw a circle on a rubber sheet and stretch it. The circle becomes an ellipse (slide picture of circle ABCD...). Some diameters get longer (normal strain) and right angles between lines change (shear strain). Strain is the *geometry* of deformation, just as stress is its *statics*.

**2. Why it matters.** Strain is what we actually **measure** (gauges, extensometers). Hooke's law (Ch. 5) turns measured strains into stresses. The PYQs that ask about a circle becoming an ellipse (2021 B-Q1, 2024 A-Q2) are strain problems.

**3. Formal treatment (Crandall §4.6–4.7, slides).** Let $u(x,y)$ and $v(x,y)$ be the displacements in x and y. For a small rectangle OCDE, with O→C along x ($\Delta x$) and O→E along y ($\Delta y$):
- **Normal strain** = change in length / original length:
$$\epsilon_x = \lim\frac{O'C'-OC}{OC} = \frac{\partial u}{\partial x},\qquad \epsilon_y = \frac{\partial v}{\partial y}$$
- **Shear strain** = decrease of the originally right angle COE:
$$\gamma_{xy} = \lim\left(\frac{\pi}{2} - \angle C'O'E'\right) = \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y}$$
**Plane strain:** $\epsilon_z = \gamma_{xz} = \gamma_{yz} = 0$. ⚠️ Plane strain ≠ plane stress. A thin plate in plane stress has $\epsilon_z \neq 0$ (it thins). A long dam or a plate between rigid walls is in plane strain, with $\sigma_z\ne0$.

**4. Derivation of $\epsilon_x$ and $\gamma_{xy}$.** Point C at $(x+\Delta x, y)$ moves by $u + \frac{\partial u}{\partial x}\Delta x$ in x and $v + \frac{\partial v}{\partial x}\Delta x$ in y. To first order, the new length of OC is $\Delta x(1 + \partial u/\partial x)$, which gives $\epsilon_x$. Line OC rotates counter-clockwise by $\frac{\partial v}{\partial x}$ and line OE rotates clockwise by $\frac{\partial u}{\partial y}$. The angle between them closes by the sum, which gives $\gamma_{xy}$. ∎
*Sign:* $\gamma_{xy} > 0$ means the angle between +x and +y **decreases**.

**7. Traps.** Engineering shear strain γ is *twice* the tensor shear strain. Mohr's circle uses γ/2.

---

## Concept 4.5 — Strain transformation and Mohr's circle of strain

### A. Concept explanation

**1. Intuition.** Same idea as for stress. Rotate the measuring axes and the stretch along each direction changes, following *exactly the same algebra* with $\sigma\to\epsilon$ and $\tau\to\gamma/2$.

**3–4. Derivation (slides, Crandall §4.8).** With $x = x'\cos\theta - y'\sin\theta$, $y = x'\sin\theta + y'\cos\theta$, $u' = u\cos\theta+v\sin\theta$ and $v' = -u\sin\theta+v\cos\theta$, the chain rule gives
$$\epsilon_{x'} = \frac{\partial u'}{\partial x'} = \left(\frac{\partial u}{\partial x}\cos\theta+\frac{\partial v}{\partial x}\sin\theta\right)\cos\theta + \left(\frac{\partial u}{\partial y}\cos\theta+\frac{\partial v}{\partial y}\sin\theta\right)\sin\theta$$
$$\Rightarrow\ \epsilon_{x'} = \epsilon_x\cos^2\theta + \epsilon_y\sin^2\theta + \gamma_{xy}\sin\theta\cos\theta$$
In double-angle form:
$$\boxed{\epsilon_{x'} = \frac{\epsilon_x+\epsilon_y}{2} + \frac{\epsilon_x-\epsilon_y}{2}\cos2\theta + \frac{\gamma_{xy}}{2}\sin2\theta}$$
$$\boxed{\frac{\gamma_{x'y'}}{2} = -\frac{\epsilon_x-\epsilon_y}{2}\sin2\theta + \frac{\gamma_{xy}}{2}\cos2\theta}$$
$$\epsilon_{1,2} = \frac{\epsilon_x+\epsilon_y}{2}\pm\sqrt{\left(\frac{\epsilon_x-\epsilon_y}{2}\right)^2+\left(\frac{\gamma_{xy}}{2}\right)^2},\qquad \tan2\theta_p = \frac{\gamma_{xy}}{\epsilon_x-\epsilon_y},\qquad \frac{\gamma_{max}}{2} = R$$

**5. Mohr's circle of strain:** horizontal axis ε, vertical axis **γ/2** (+γ/2 plotted **downward at x**, as for stress). Centre $\frac{\epsilon_x+\epsilon_y}{2}$, radius $R=\sqrt{(\frac{\epsilon_x-\epsilon_y}{2})^2+(\frac{\gamma_{xy}}{2})^2}$.

**6. Isotropy link (Ch. 5):** for an isotropic material, **principal strain axes = principal stress axes**, so you can use either circle to find directions.

**7. Traps.** Plotting γ instead of γ/2 doubles the radius. Remember $\gamma_{max} = 2R = \epsilon_1-\epsilon_2$ (in-plane).

### B. Solved questions

#### Q10 (Crandall Example, Slides Ch4 Part 2) — Sheet metal: strains on axes 30° clockwise, principal strains *(medium)*
**Given:** $\epsilon_x = -200\mu$, $\epsilon_y = 1000\mu$, $\gamma_{xy} = 900\mu$ ($\mu = 10^{-6}$). Axes x′y′ at 30° **clockwise** (θ = −30°).
Centre $= 400\mu$. $(\epsilon_x-\epsilon_y)/2 = -600\mu$ and $\gamma/2 = 450\mu$, so $R = \sqrt{600^2+450^2}=750\mu$.
$\cos(-60^\circ) = 0.5$ and $\sin(-60^\circ) = -0.866$:
$$\epsilon_{x'} = 400 + (-600)(0.5) + 450(-0.866) = \boxed{-290\mu}$$
$$\epsilon_{y'} = 800-(-290) = \boxed{1090\mu}$$
$$\frac{\gamma_{x'y'}}{2} = -(-600)(-0.866) + 450(0.5) = -295\mu\ \Rightarrow\ \boxed{\gamma_{x'y'} = -590\mu}$$
**Principal:** $\boxed{\epsilon_1 = 1150\mu,\ \epsilon_2 = -350\mu}$. Direction: $\tan2\theta_p = 900/(-1200)$, so ε₁ is at θ = 71.6° from x (and ε₂ at −18.4°).
**Circle check (slides):** the angle at the centre is $60^\circ - 36.8^\circ$ ✓. Point x′ lies above the axis, so $\gamma_{x'y'}<0$ ✓.

---

#### Q11 (Crandall Prob 4.20, Slides) — Principal strains *(easy)*
**Given:** $\epsilon_x = 800\mu$, $\epsilon_y = 100\mu$, $\gamma_{xy} = -800\mu$.
Centre $450\mu$. $R = \sqrt{350^2+400^2} = 531.5\mu$.
$$\boxed{\epsilon_1 = 981.5\mu,\quad \epsilon_2 = -81.5\mu},\quad \tan2\theta_p = \frac{-800}{700} \Rightarrow \boxed{\theta_{p1} = -24.4^\circ\ (\text{24.4° clockwise from x})}$$
**Check:** substitute θ = −24.4°: $450 + 350\cos(-48.8^\circ) - 400\sin(-48.8^\circ) = 450 + 230.5 + 301 = 981.5$ ✓. $\gamma_{max} = 1063\mu$.

---

## Concept 4.6 — Strain rosettes

### A. Concept explanation

**1. Intuition.** One strain gauge measures stretch in only one direction. A point in plane strain has *three* unknowns $(\epsilon_x, \epsilon_y, \gamma_{xy})$, so glue **three gauges** at different angles (a rosette) and solve three equations.

**2. Why it matters.** This is how real structures (bridges, aircraft, the bracket in the slide example) are monitored. Also PYQ 2021 A-Q1 (one gauge at 45° on a shaft).

**3. Formal treatment.** Each gauge at angle $\theta_i$ reads
$$\epsilon_i = \epsilon_x\cos^2\theta_i + \epsilon_y\sin^2\theta_i + \gamma_{xy}\sin\theta_i\cos\theta_i$$
**45° rectangular rosette** (0°, 45°, 90°): $\epsilon_x = \epsilon_a$, $\epsilon_y = \epsilon_c$, $\boxed{\gamma_{xy} = 2\epsilon_b - (\epsilon_a+\epsilon_c)}$.
**60° delta rosette** (0°, 60°, 120°): $\epsilon_x = \epsilon_a$, $\epsilon_y = \tfrac13(2\epsilon_b+2\epsilon_c-\epsilon_a)$, $\gamma_{xy} = \tfrac{2}{\sqrt3}(\epsilon_b-\epsilon_c)$.

**4. Derivation of the 45° case.** With θ = 45°, $\cos^2 = \sin^2 = \sin\cos = \tfrac12$, so $\epsilon_b = \tfrac12(\epsilon_x+\epsilon_y+\gamma_{xy})$, giving $\gamma_{xy} = 2\epsilon_b - \epsilon_a - \epsilon_c$. ∎

**7. Traps.** Angles must be measured counter-clockwise from your chosen x-axis (the gauge "a" direction). Mixing degrees and radians on calculators. Forgetting that the final principal *stresses* need Hooke's law with **plane stress** (the surface is free).

### B. Solved questions

#### Q12 (Slides Ch4 Part 2, Hibbeler Ex 10.8) — 60° rosette on a bracket *(medium)*
**Given:** $\epsilon_a = 60\mu$ (0°), $\epsilon_b = 135\mu$ (60°), $\epsilon_c = 264\mu$ (120°).
Equations: $60 = \epsilon_x$; $135 = 0.25\epsilon_x + 0.75\epsilon_y + 0.433\gamma$; $264 = 0.25\epsilon_x+0.75\epsilon_y - 0.433\gamma$.
Subtract the last two: $0.866\gamma = -129 \Rightarrow \gamma_{xy} = -149\mu$. Add them: $1.5\epsilon_y = 399 - 30 \Rightarrow \epsilon_y = 246\mu$.
(Formula check: $\epsilon_y = \tfrac13(270+528-60) = 246$ ✓ and $\gamma = \tfrac{2}{\sqrt3}(135-264) = -149$ ✓.)
Centre $153\mu$, $R = \sqrt{93^2 + 74.5^2} = 119.2\mu$.
$$\boxed{\epsilon_1 = 272\mu,\quad \epsilon_2 = 33.8\mu},\qquad \boxed{\theta_{p2} = 19.3^\circ\ \text{(counter-clockwise from x, direction of}\ \epsilon_2)}$$
⚠️ The slide writes "ε₂ = 246(10⁻⁶) − 119.2(10⁻⁶) = 33.8". The 246 is a typo for **153** (the centre). The result 33.8 is correct.

---

#### Q13 (PYQ 2021-22 A Q1) — Strain gauge at 45° on a twisted bar *(easy, 10 marks)*
**Given:** $d = 50$ mm, $T = 500$ N·m, the gauge at 45° reads $\epsilon = 350\mu$. **Find:** G.
Surface shear (Ch. 6): $\tau = \dfrac{16T}{\pi d^3} = \dfrac{16(500\,000)}{\pi(50)^3} = 20.37$ MPa.
Pure shear: the 45° direction is principal, and $\epsilon_{45} = \gamma/2$ (from the rosette formula with $\epsilon_x = \epsilon_y = 0$). So $\gamma = 700\mu$.
$$G = \frac{\tau}{\gamma} = \frac{20.37}{700\times10^{-6}} = \boxed{29.1\ \text{GPa}}$$
**Alternative via Hooke:** principal stresses ±τ give $\epsilon_{45} = \frac{\tau(1+\nu)}{E} = \frac{\tau}{2G}$, the same result ✓.
**Takeaway:** a gauge at 45° on a shaft reads γ/2. It is a popular closed-book question.

---

#### Q14 (PYQ 2019-20 A Q2) — From principal strains to $\sigma_x, \sigma_y, \tau_{xy}$ *(medium, 7 marks)*
**Given:** aluminium plate, $\epsilon_1 = -8.1\times10^{-4}$, $\epsilon_2 = 5.7\times10^{-4}$, $E = 72$ GPa, ν = 0.33. Principal direction 1 is at 60° from x (rotating toward y).
**Step 1, principal stresses (plane stress Hooke, Ch. 5):** $\dfrac{E}{1-\nu^2} = 80\,799$ MPa.
$$\sigma_1 = 80\,799(\epsilon_1+\nu\epsilon_2) = 80\,799(-8.1+1.881)\times10^{-4} = -50.2\ \text{MPa}$$
$$\sigma_2 = 80\,799(\epsilon_2+\nu\epsilon_1) = 80\,799(5.7-2.673)\times10^{-4} = 24.5\ \text{MPa}$$
**Step 2, Mohr's circle of stress:** centre $= -12.9$, $R = 37.4$. The x-axis is at θ = −60° from axis 1, so on the circle rotate 120° clockwise from point "1".
$$\sigma_x = -12.9 + (-37.35)\cos(-120^\circ) = \boxed{5.8\ \text{MPa}}$$
$$\sigma_y = -12.9 - 18.7 = \boxed{-31.6\ \text{MPa}}$$
$$\tau_{xy} = -(-37.35)\sin(-120^\circ) = \boxed{-32.3\ \text{MPa}}$$
**Checks:** $\sigma_x+\sigma_y = -25.8 = \sigma_1+\sigma_2$ ✓ and $\sqrt{(18.7)^2+32.3^2} = 37.4 = R$ ✓.
**Alternative:** transform the *strains* to x–y first (strain circle) and then apply Hooke's law. Same answer.

---

#### Q15 (PYQ 2021-22 B Q1) — Circle → ellipse: lengths and orientation of the axes *(medium–hard, 10 marks)*
**Given:** $d = 250$ mm circle on mild steel. $\sigma_x = 120$, $\sigma_y = 25$, $\tau_{xy} = 10$ MPa. $E = 200$ GPa, ν = 0.3.
**Idea:** the ellipse's major and minor axes lie along the **principal strain** directions, which equal the principal stress directions for an isotropic material.
Principal stresses: centre 72.5, $R = \sqrt{47.5^2+10^2} = 48.54$, so σ₁ = 121.04 and σ₂ = 23.96 MPa.
$\theta_p = \tfrac12\tan^{-1}\frac{20}{95} = 5.94^\circ$ (counter-clockwise from x for σ₁).
Principal strains (plane stress):
$$\epsilon_1 = \frac{121.04 - 0.3(23.96)}{200\,000} = 569.3\mu,\qquad \epsilon_2 = \frac{23.96-0.3(121.04)}{200\,000} = -61.8\mu$$
$$\boxed{\text{Major axis} = 250(1+\epsilon_1) = 250.142\ \text{mm at}\ 5.94^\circ\ \text{from x},\quad \text{Minor axis} = 249.985\ \text{mm at}\ 95.94^\circ}$$
**Sketch:** the ellipse is very slightly elongated, tilted about 6° counter-clockwise from x.
**Trap:** using $\sigma/E$ without the Poisson term would give minor axis = 250.030 mm (*longer* than d). That's wrong, because the Poisson contraction from σ₁ wins.

---

#### Q16 (PYQ 2014-15 Test-2 Q2) — Absolute maximum shear strain in a bar *(easy–medium, 15 marks)*
**Given:** steel bar 2 cm × 0.5 cm, tension 5 kN. $E = 200$ GPa, ν = 0.3. **Find:** the absolute maximum shear strain.
$\sigma = 5000/(20\times5) = 50$ MPa (uniaxial).
Principal strains: $\epsilon_1 = \sigma/E = 250\mu$ and $\epsilon_2=\epsilon_3 = -\nu\sigma/E = -75\mu$.
$$\gamma_{abs,max} = \epsilon_{max}-\epsilon_{min} = 250-(-75) = \boxed{325\times10^{-6}\ \text{rad}}$$
**Check:** $\tau_{max} = \sigma/2 = 25$ MPa and $G = E/2(1+\nu) = 76.9$ GPa give $\gamma = 25/76{,}900 = 325\mu$ ✓.
**Takeaway:** "absolute" means include the out-of-plane direction. Here, in-plane and absolute are equal because $\epsilon_2 = \epsilon_3$.

---

## Chapter 4 — Formula and convention sheet

| Item | Formula / rule |
|---|---|
| Sign of stress | +face & +direction, or −face & −direction |
| Symmetry | $\tau_{xy}=\tau_{yx}$ |
| Equilibrium | $\partial\sigma_x/\partial x+\partial\tau_{xy}/\partial y=0$, $\partial\tau_{xy}/\partial x+\partial\sigma_y/\partial y=0$ |
| Transformation | $\sigma_{x'}=\bar\sigma+\frac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta$; $\tau_{x'y'}=-\frac{\sigma_x-\sigma_y}{2}\sin2\theta+\tau_{xy}\cos2\theta$ |
| Invariant | $\sigma_{x'}+\sigma_{y'}=\sigma_x+\sigma_y$ |
| Principal | $\sigma_{1,2}=\bar\sigma\pm R$, $R=\sqrt{(\frac{\sigma_x-\sigma_y}{2})^2+\tau_{xy}^2}$, $\tan2\theta_p=\frac{2\tau_{xy}}{\sigma_x-\sigma_y}$ (verify which θ gives σ₁) |
| Max in-plane shear | $\tau_{max}=R$ at $\theta_p\pm45^\circ$, normal stress $\bar\sigma$ there |
| Absolute max shear | $(\sigma_{max}-\sigma_{min})/2$ including $\sigma_3=0$ |
| Mohr's circle | +τ plotted **down at X**, up at Y; 2θ on circle = θ on element, same sense |
| Strains | $\epsilon_x=\partial u/\partial x$, $\epsilon_y=\partial v/\partial y$, $\gamma_{xy}=\partial u/\partial y+\partial v/\partial x$ |
| Strain transformation | replace σ → ε and τ → γ/2 in the stress equations |
| Strain circle | vertical axis γ/2; $\gamma_{max}=\epsilon_1-\epsilon_2$ |
| 45° rosette | $\epsilon_x=\epsilon_a$, $\epsilon_y=\epsilon_c$, $\gamma=2\epsilon_b-\epsilon_a-\epsilon_c$ |
| 60° rosette | $\epsilon_y=\frac13(2\epsilon_b+2\epsilon_c-\epsilon_a)$, $\gamma=\frac{2}{\sqrt3}(\epsilon_b-\epsilon_c)$ |
| Gauge at 45° on shaft | $\epsilon_{45}=\gamma/2=\tau/2G$ |

**Other Crandall Ch. 4 problems worth practising:** 4.1–4.10 (transformation, Mohr), 4.12 (thin cylinder), 4.15–4.25 (strain and rosettes).
