# Chapter 5 — Stress–Strain–Temperature Relations
### Tensile test, Hooke's law, Poisson's ratio, generalized Hooke's law, E–G–ν, volume change, thermal strain and thermal stresses, strain energy, yield criteria (Tresca and von Mises)

**Sources used:** Slides "Chapter 5", Crandall Ch. 5 (§5.2–5.8, 5.16), PYQs 2023-24 (A-Q3), 2024-25 (A-Q2), 2019-20 (A-Q4), 2021-22 (A-Q2c, B-Q1), 2014-15 (Compre A-Q1–Q4; Test-2 Q3).

---

## Concept 5.1 — The tensile test and material behaviour

### A. Concept explanation

**1. Intuition.** Pull a steel bar in a machine and plot force against stretch. At first it behaves like a stiff spring (straight line). Then it suddenly "gives" and stretches a lot for little extra force (yield). Then it hardens, necks down and breaks. Dividing force by area and stretch by length removes the size of the specimen, leaving a curve that belongs to the **material**.

**2. Why it matters.** Every design number ($E$, $\sigma_Y$, $\sigma_u$, ν) comes from this test. Yield strength is the limit in every factor-of-safety PYQ.

**3. Formal treatment (slides).**
- **Engineering stress** $\sigma = P/A_0$ and **engineering strain** $\epsilon = \delta/L_0$, both using the *original* dimensions.
- **True stress and strain** use the current area and length, which matters only after large deformation (necking).
- **Proportional limit:** end of the straight line. **Elastic limit:** the largest stress with no permanent set on unloading. **Yield point:** large strain increase with little stress increase. **Ultimate strength:** peak of the curve.
- **Ductile** materials (mild steel, aluminium, copper, brass) undergo large strain, absorb energy and give visible warning. They fail on **45° shear planes**: the cup-and-cone fracture.
- **Brittle** materials (cast iron, concrete, glass, stone) fail at small strain on planes **perpendicular to the maximum tensile stress**.
- **Elastic vs plastic:** strain recovers or does not recover on unloading. **Fatigue:** failure under cyclic stress below $\sigma_u$. **Creep:** time-dependent strain under constant stress.

**Hooke's law (uniaxial):** $\sigma = E\epsilon$, where $E$ is Young's modulus, the slope of the linear part. Typical values from the slides (GPa): mild steel 210, aluminium 70, concrete 18.5, wood 12.5, nylon 2.8, rubber 0.004.

**Idealized curves (Crandall §5.3):** linear elastic; rigid–perfectly plastic; elastic–perfectly plastic; linear strain-hardening. Choose the one that captures what matters for the problem at hand.

**7. Traps.** Using $\sigma_u$ where the question asks for yield. Using true stress where engineering stress is meant.

---

## Concept 5.2 — Poisson's ratio and generalized Hooke's law

### A. Concept explanation

**1. Intuition.** Stretch a rubber band and it gets thinner. The ratio of sideways shrinking to lengthwise stretching is Poisson's ratio. Most metals are about 0.3, rubber about 0.5 (incompressible), and cork about 0.

**2. Why it matters.** It explains why a plate under biaxial stress changes thickness, and it appears in every "change in thickness/volume" PYQ (2023 A-Q3 and 2024 A-Q2 are the same question type two years running).

**3. Formal treatment (slides).** For uniaxial $\sigma_x$: $\epsilon_x = \sigma_x/E$ and $\epsilon_y = \epsilon_z = -\nu\epsilon_x$, where
$$\nu = -\frac{\text{lateral strain}}{\text{axial strain}}$$
**Assumptions:** linear elastic, small deformations, **isotropic** (same properties in all directions).

**Isotropy arguments (slides, Crandall §5.4):**
- A normal stress produces **no shear strain**. With a hypothetical shear strain, rotating the element 180° about the loading axis would flip the sign of the shear strain but not the load, which contradicts isotropy.
- A shear stress produces **no normal strain**. Reversing τ would reverse the normal strain, but by symmetry the result must be the same, which contradicts linearity unless the strain is zero.

So normal stresses cause only normal strains, and shear stresses cause only their own shear strain.

**4. Derivation — superposition gives generalized Hooke's law:**
$$\boxed{\epsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y+\sigma_z)\right]+\alpha\Delta T,\quad \epsilon_y = \frac{1}{E}\left[\sigma_y - \nu(\sigma_z+\sigma_x)\right]+\alpha\Delta T,\quad \epsilon_z = \frac{1}{E}\left[\sigma_z - \nu(\sigma_x+\sigma_y)\right]+\alpha\Delta T}$$
$$\boxed{\gamma_{xy} = \frac{\tau_{xy}}{G},\quad \gamma_{yz} = \frac{\tau_{yz}}{G},\quad \gamma_{zx} = \frac{\tau_{zx}}{G}}$$
(The $\alpha\Delta T$ term is the thermal strain, Concept 5.4.)

**Plane stress ($\sigma_z=0$), inverted:**
$$\sigma_x = \frac{E}{1-\nu^2}(\epsilon_x+\nu\epsilon_y),\qquad \sigma_y = \frac{E}{1-\nu^2}(\epsilon_y+\nu\epsilon_x),\qquad \epsilon_z = -\frac{\nu}{E}(\sigma_x+\sigma_y) = -\frac{\nu}{1-\nu}(\epsilon_x+\epsilon_y)$$

**Isotropy ⇒ principal axes of strain = principal axes of stress** (slides). Since shear stress gives only shear strain, zero shear stress means zero shear strain.

**Volume change (dilatation).** For small strains,
$$e = \frac{\Delta V}{V} = \epsilon_x+\epsilon_y+\epsilon_z = \frac{1-2\nu}{E}(\sigma_x+\sigma_y+\sigma_z)$$
Under hydrostatic pressure $p$, this gives the bulk modulus $K = \dfrac{E}{3(1-2\nu)}$. As ν → 0.5, $K\to\infty$ (incompressible).

**5. Picture.** A circle drawn on a plate becomes an ellipse whose axes follow the principal directions (Ch. 4 Q15).

**6. Special cases.**
- **Uniaxial:** $\epsilon_y = -\nu\sigma/E$.
- **Plate between rigid walls (slide problem):** one strain is zero, so a stress appears in that direction (see Q3).
- **ν = 0.5:** $e = 0$, the volume is constant.

**7. Traps.**
- Using the *plane strain* formula where *plane stress* applies, or the other way round.
- Forgetting the Poisson terms when finding a dimension change. For example, in the 2024 PYQ the *y* diameter actually **shrinks** even though $\sigma_y$ is tensile.
- Mixing E in GPa with σ in MPa. Convert so that both are in MPa.

### B. Solved questions

#### Q1 (PYQ 2014-15 Compre A Q2) — Finding ν and E from a tension test *(easy)*
**Given:** bar 8 × 8 mm, pull 10 kN, lateral dimension reduced by $2\times10^{-3}$ mm, G = 80 GPa. **Find:** ν and E.
$\sigma = 10\,000/64 = 156.25$ MPa. Lateral strain $= -2\times10^{-3}/8 = -2.5\times10^{-4}$.
Since $\epsilon_{lat} = -\nu\sigma/E$ and $E = 2G(1+\nu)$:
$$2.5\times10^{-4} = \frac{\nu(156.25)}{2(80\,000)(1+\nu)} \Rightarrow 0.256(1+\nu) = \nu \Rightarrow \boxed{\nu = 0.344},\quad \boxed{E = 215\ \text{GPa}}$$
**Check:** axial strain $= 156.25/215\,000 = 7.27\times10^{-4}$ and $\nu = 2.5/7.27 = 0.344$ ✓.

---

#### Q2 (PYQ 2023-24 A Q3) — Plate in biaxial stress: γ_max, Δt, ΔV *(easy–medium, 10 marks)*
**Given:** $\sigma_x = 67$ MPa (T), $\sigma_y = -23$ MPa (C). Plate 400 × 550 × 20 mm, steel. *E* = 200 GPa (the paper's "200 MPa" is a typo), ν = 0.30.
**(a) Max in-plane shear strain:** no shear stress, so x and y are principal.
$$\gamma_{max} = \epsilon_x - \epsilon_y = \frac{(\sigma_x - \sigma_y)(1+\nu)}{E} = \frac{90(1.3)}{200\,000} = \boxed{585\times10^{-6}}$$
(Or $\tau_{max} = 45$ MPa and $G = 76.9$ GPa give $\gamma = 45/76\,923$, the same.)
**(b) Thickness change:** $\epsilon_z = -\frac{\nu}{E}(\sigma_x+\sigma_y) = -\frac{0.3(44)}{200\,000} = -66\times10^{-6}$.
$$\Delta t = 20(-66\times10^{-6}) = \boxed{-1.32\times10^{-3}\ \text{mm (thinner)}}$$
**(c) Volume change:**
$$\Delta V = V\frac{1-2\nu}{E}(\sigma_x+\sigma_y) = (4.4\times10^6)\frac{0.4(44)}{200\,000} = \boxed{+387\ \text{mm}^3}$$
**Check by strains:** $\epsilon_x = (67+6.9)/2\times10^5 = 369.5\mu$ and $\epsilon_y = (-23-20.1)/2\times10^5 = -215.5\mu$. Sum with $\epsilon_z$: $369.5 - 215.5 - 66 = 88\mu$, and $88\mu \times 4.4\times10^6 = 387$ ✓.

---

#### Q3 (PYQ 2024-25 A Q2) — Etched circle on a brass plate *(easy–medium, 10 marks)*
**Given:** $d = 200$ mm. Plate 400 × 400 × 20 mm. $\sigma_x = 42$, $\sigma_y = 14$ MPa. $E = 100$ GPa, ν = 0.34. Diameter ac is along x and bd along y.
$$\epsilon_x = \frac{42 - 0.34(14)}{100\,000} = 372.4\mu,\quad \epsilon_y = \frac{14-0.34(42)}{100\,000} = -2.8\mu,\quad \epsilon_z = -\frac{0.34(56)}{100\,000} = -190.4\mu$$
$$\boxed{\Delta_{ac} = 200\epsilon_x = 0.0745\ \text{mm}},\quad \boxed{\Delta_{bd} = 200\epsilon_y = -5.6\times10^{-4}\ \text{mm}},\quad \boxed{\Delta t = 20\epsilon_z = -3.81\times10^{-3}\ \text{mm}}$$
$$\boxed{\Delta V = (3.2\times10^6)(372.4-2.8-190.4)\times10^{-6} = 573\ \text{mm}^3}$$
**Takeaway:** bd **shrinks** even though $\sigma_y$ is tensile, because $\nu\sigma_x > \sigma_y$. Examiners set the numbers up for exactly this surprise.

---

#### Q4 (Slides Ch5, Crandall §5.6) — Thin plate between rigid walls *(medium)*
**Given:** plate of width b, thickness t, length L, fitted between rigid smooth walls a distance b apart (y direction). Axial compressive force P along x. **Find:** the deflection along P.
**Assumptions (slide):** $\sigma_z = 0$ (plane stress in thickness), $\epsilon_y = 0$ (walls), no friction.
$\epsilon_y = 0 = \frac{1}{E}(\sigma_y - \nu\sigma_x) \Rightarrow \sigma_y = \nu\sigma_x$.
$\epsilon_x = \frac{1}{E}(\sigma_x - \nu\sigma_y) = \frac{\sigma_x(1-\nu^2)}{E}$, with $\sigma_x = -P/(bt)$:
$$\boxed{\delta = \frac{PL(1-\nu^2)}{Ebt}\ \text{(shortening)}}$$
**Interpretation:** the walls make the plate *stiffer* by a factor $1/(1-\nu^2) \approx 1.1$. They also push back with $\sigma_y = -\nu P/(bt)$.

---

## Concept 5.3 — Relation between E, G and ν

### A. Concept explanation

**1. Intuition.** Shear and stretch are not independent. A square under pure shear is, viewed at 45°, a square stretched in one diagonal and squashed in the other. So the shear stiffness G must be fixed by E and ν.

**4. Derivation (slides, Crandall §5.4).** Pure shear τ on the x–y element ⇔ principal stresses $\sigma_1 = +\tau$ and $\sigma_2 = -\tau$ on the 45° element.
- Strain along the 1-direction (Hooke): $\epsilon_1 = \frac{\tau}{E} - \nu\frac{-\tau}{E} = \frac{\tau(1+\nu)}{E}$
- Strain along 45° from the shear strain (Ch. 4 transformation with $\epsilon_x = \epsilon_y = 0$): $\epsilon_{45} = \frac{\gamma}{2} = \frac{\tau}{2G}$

These are the same strain, so
$$\frac{\tau}{2G} = \frac{\tau(1+\nu)}{E}\ \Rightarrow\ \boxed{G = \frac{E}{2(1+\nu)}}$$
Only **two** of E, G, ν (and K) are independent for an isotropic material.

**Summary:** $E = 2G(1+\nu) = 3K(1-2\nu)$.

---

## Concept 5.4 — Thermal strain and thermal stresses

### A. Concept explanation

**1. Intuition.** Heat a rail and it wants to grow. If it is free, it grows and **no stress** develops. If it is clamped between walls, the walls must push it back to its original length, and that push is the thermal stress. A rail can buckle on a hot day for exactly this reason.

**2. Why it matters.** Rails, pipelines, bimetal strips, bolts in sleeves, thermostats. PYQ 2014 A-Q1 and Test-2 Q3.

**3. Formal treatment (slides).**
$$\epsilon_T = \alpha(T - T_0) = \alpha\Delta T,\qquad \text{total strain } \epsilon = \frac{\sigma}{E} + \alpha\Delta T$$
For isotropic materials, thermal strain is the same in all directions and **produces no shear strain**.

**4. Derivation — bar fixed at both ends (slides, superposition).**
- Release B and let it expand freely: $\delta_T = \alpha\Delta T L$.
- Apply the redundant P to push it back: $\delta_P = PL/AE$.
- Compatibility: $\delta_T + \delta_P = 0 \Rightarrow P = -AE\alpha\Delta T$
$$\boxed{\sigma = -E\alpha\Delta T}\quad\text{(compressive for heating; independent of L and A)}$$
*With a gap Δ:* $\alpha\Delta T L - \Delta = \dfrac{|P|L}{AE}$ if the expansion exceeds the gap. Otherwise there is no stress.

**General recipe for thermal indeterminate problems (the three steps of Ch. 2):**
1. Equilibrium of the members' forces.
2. Compatibility of total deformations, $\delta_i = \frac{F_iL_i}{A_iE_i} + \alpha_i\Delta T L_i$.
3. Solve.

**7. Traps.**
- Using $\Delta T$ in °F with α in /°C.
- Forgetting that a *temperature drop* adds **tension** to a pre-stressed wire.
- Sign of the gap. Close the gap first, *then* stress builds up.
- In composite systems (bolt + sleeve), the member with the **larger α** ends up in **compression**.

### B. Solved questions

#### Q5 (PYQ 2014-15 Compre A Q1) — Rod fixed at both ends, heated *(easy)*
**Given:** d = 20 mm, L = 1.5 m, ΔT = 60°C, E = 110 GPa, α = 1.2 × 10⁻⁵/°C.
$$\sigma = E\alpha\Delta T = 110\,000(1.2\times10^{-5})(60) = 79.2\ \text{MPa},\quad P = 79.2\times\pi(10)^2 \Rightarrow \boxed{R = 24.9\ \text{kN}}$$
(L doesn't matter. That is the classic trap.)

---

#### Q6 (Slides Ch5, Gere) — Copper bar with a gap *(easy)*
**Given:** L = 25 in, gap 0.008 in, ΔT = 50°F, α = 9.6 × 10⁻⁶/°F, E = 16 × 10⁶ psi.
Free expansion $= 9.6\times10^{-6}(50)(25) = 0.012$ in, which is greater than the gap. Excess $= 0.004$ in.
$$\sigma_c = E\frac{0.004}{25} = \boxed{2560\ \text{psi (compression)}}$$

---

#### Q7 (Slides Ch5, Gere) — Pre-stressed steel wire *(easy)*
**Given:** pre-stress 42 MPa at 20°C, α = 14 × 10⁻⁶/°C, E = 200 GPa.
- (a) Cooling to 0°C adds tension: $\Delta\sigma = E\alpha\Delta T = 200\,000(14\times10^{-6})(20) = 56$ MPa, so $\boxed{\sigma = 98\ \text{MPa}}$
- (b) Zero stress when $E\alpha(T-20) = 42 \Rightarrow T - 20 = 15$, so $\boxed{T = 35^\circ\text{C}}$

---

#### Q8 (Slides Ch5, Gere) — Three wires: when does steel carry everything? *(medium)*
**Given:** rigid bar, W = 750 lb, two steel wires and one aluminium wire (centre), each 1/8 in diameter, same initial length. $E_s = 30\times10^6$ psi, $\alpha_s = 6.5\times10^{-6}$/°F, $\alpha_a = 12\times10^{-6}$/°F.
**Idea:** aluminium expands more. When its force drops to zero it is just slack, so the bar is held by steel alone. The bar stays level (symmetry), so all three wires have the same length change.
$$\alpha_s\Delta T L + \frac{(W/2)L}{A_sE_s} = \alpha_a\Delta T L\ \Rightarrow\ \Delta T = \frac{W/2}{A_sE_s(\alpha_a-\alpha_s)}$$
$A_s = \frac{\pi}{4}(0.125)^2 = 0.01227$ in².
$$\Delta T = \frac{375}{0.01227(30\times10^6)(5.5\times10^{-6})} = \boxed{185^\circ\text{F}}$$
(The aluminium modulus isn't needed, because its force is zero at this instant.)

---

#### Q9 (Slides Ch5, Gere) — Brass sleeve on a steel bolt *(medium)*
**Given:** bolt $d_B = 25$ mm, $E_B = 200$ GPa, $\alpha_B = 10\times10^{-6}$/°C. Sleeve $d_1 = 26$ mm, $d_2 = 36$ mm, $E_S = 100$ GPa, $\alpha_S = 21\times10^{-6}$/°C. **Find:** ΔT that gives 25 MPa compression in the sleeve.
- **Equilibrium:** $P_S = P_B$ (sleeve compressed, bolt stretched).
- **Compatibility:** equal final lengths, so $\alpha_S\Delta T - \frac{P}{E_SA_S} = \alpha_B\Delta T + \frac{P}{E_BA_B}$
$$\Rightarrow\ \sigma_S = \frac{(\alpha_S-\alpha_B)\Delta T\,E_S E_BA_B}{E_SA_S+E_BA_B}\ \Rightarrow\ \Delta T = \frac{\sigma_S}{E_S(\alpha_S-\alpha_B)}\left(1+\frac{E_SA_S}{E_BA_B}\right)$$
$A_S = \frac{\pi}{4}(620) = 487$ mm², $A_B = \frac{\pi}{4}(625) = 491$ mm², ratio factor $= 1.496$.
$$\Delta T = \frac{25(1.496)}{100\,000(11\times10^{-6})} = \boxed{34^\circ\text{C}}$$

---

#### Q10 (Slides Ch5, Gere) — Rigid bar on two cables + temperature rise: allowable P *(hard)*
**Given:** rigid bar ABCD pinned at A. Cables at B (2b, $d_B = 12$ mm) and C (4b, $d_C = 20$ mm). P at D (5b). ΔT = 60°C. E = 140 GPa, α = 12 × 10⁻⁶/°C. FS = 5 on ultimate: $(T_B)_{ult} = 102$ kN and $(T_C)_{ult} = 231$ kN.
1. **Equilibrium:** $\sum M_A$: $2T_B + 4T_C = 5P$.
2. **Compatibility (rigid bar):** $\delta_C = 2\delta_B$.
3. **Force–displacement–temperature:** $\delta_i = \frac{T_iL}{EA_i} + \alpha\Delta T L$.

$$\frac{T_C}{EA_C} + \alpha\Delta T = \frac{2T_B}{EA_B} + 2\alpha\Delta T \Rightarrow 2T_BA_C - T_CA_B = -E\alpha\Delta T A_BA_C$$
With the effective areas $A_B = 76.7$ mm² and $A_C = 173$ mm² (the slide's values): $T_B = 0.2494P - 3480$ and $T_C = 1.1253P + 1740$ (N).
Allowables: $T_B \le 20.4$ kN gives $P \le 95.7$ kN. $T_C \le 46.2$ kN gives $P \le 39.5$ kN.
$$\boxed{P_{allow} = 39.5\ \text{kN (cable C governs)}}$$
**Takeaway:** heating *relieves* cable B (the −3480 term) and *loads* cable C, because the compatibility condition forces C to stretch twice as much as B.

---

#### Q11 (PYQ 2014-15 Test-2 Q3) — Thermo-gate: Al + Mg plates closing a gap *(medium, 20 marks)*
**Given:** Al plate AB, 600 mm, $E_{al} = 68.9$ GPa, $\alpha_{al} = 24\times10^{-6}$/°C. Mg plate CD, 400 mm, $E_{am} = 44.7$ GPa, $\alpha_{am} = 26\times10^{-6}$/°C. Both 15 mm wide × 10 mm thick, fixed at the outer ends. Gap 1.5 mm at $T_1 = 25$°C. **Find:** (a) T to close the gap, (b) the force at $T_2 = 100$°C.
**(a)** Free expansions must add up to the gap:
$$(24\times10^{-6}\cdot600 + 26\times10^{-6}\cdot400)\Delta T = 1.5 \Rightarrow 0.0248\,\Delta T = 1.5 \Rightarrow \Delta T = 60.5^\circ\text{C}\Rightarrow \boxed{T = 85.5^\circ\text{C}}$$
**(b)** At ΔT = 75°C the free expansion is $0.0248(75) = 1.86$ mm. The excess of 0.36 mm must be suppressed by a common compressive force F (equilibrium: the same F in both plates). With A = 150 mm²:
$$0.36 = F\left(\frac{600}{150(68\,900)} + \frac{400}{150(44\,700)}\right) = F(5.806+5.966)\times10^{-5}$$
$$\boxed{F = 3.06\ \text{kN (compression in both plates)},\quad \sigma = 20.4\ \text{MPa}}$$

---

## Concept 5.5 — Complete equations of elasticity and strain energy

### A. Concept explanation

**3. Formal treatment (slides, Crandall §5.6).** In 3-D, any elasticity problem combines:
- **Equilibrium:** $\dfrac{\partial\sigma_x}{\partial x}+\dfrac{\partial\tau_{xy}}{\partial y}+\dfrac{\partial\tau_{zx}}{\partial z}+X = 0$ (and similarly for y and z; X, Y, Z are body forces per unit volume)
- **Geometric compatibility:** $\epsilon_x = \partial u/\partial x$, $\gamma_{xy} = \partial v/\partial x+\partial u/\partial y$, …
- **Stress–strain–temperature:** generalized Hooke's law with $\alpha(T-T_0)$

That is 15 equations for 15 unknowns (6 stresses, 6 strains, 3 displacements). It is the continuum version of the three steps of Ch. 2.

**Strain energy density (Crandall §5.8, slides).** Work stored per unit volume:
$$u = \tfrac12(\sigma_x\epsilon_x + \sigma_y\epsilon_y+\sigma_z\epsilon_z + \tau_{xy}\gamma_{xy}+\tau_{yz}\gamma_{yz}+\tau_{zx}\gamma_{zx})$$
In principal stresses:
$$u = \frac{1}{2E}\left[\sigma_1^2+\sigma_2^2+\sigma_3^2 - 2\nu(\sigma_1\sigma_2+\sigma_2\sigma_3+\sigma_3\sigma_1)\right]$$
*Uniaxial:* $u = \sigma^2/2E$. *Pure shear:* $u = \tau^2/2G$.
Integrating over a bar gives Ch. 2's $U = P^2L/2AE$, and over a shaft Ch. 6's $U = T^2L/2GJ$.

---

## Concept 5.6 — Yield criteria: Tresca (maximum shear stress) and von Mises (distortion energy)

### A. Concept explanation

**1. Intuition.** A tensile test tells you when a material yields under *one* stress. Real parts feel combined stresses. A yield criterion is a rule that turns any combination into one "equivalent" number that you can compare with the tensile yield strength. Ductile metals yield by **slip** (shear), so both criteria are built on shear-related quantities. Hydrostatic pressure causes no slip, so it must not cause yield either.

**2. Why it matters.** Almost every compre has a "factor of safety by Tresca/von Mises" part (2019, 2021, 2024, 2014).

**3. Formal treatment (slides).**
*Fracture vs yield:* fracture is driven by normal stress (bonds break and can't reform). Yield is driven by shear stress (planes slide and bonds reform).

**Tresca (maximum shear stress):** yield starts when $\tau_{max}$ reaches the value at yield in a tension test, $\tau_Y = \sigma_Y/2$.
$$\boxed{\sigma_{max}-\sigma_{min} = \sigma_Y}\quad(\text{using all three principal stresses, including }\sigma_3 = 0\text{ in plane stress})$$
Plane stress cases (slides):
- $\sigma_1,\sigma_2$ of **opposite** sign: $|\sigma_1 - \sigma_2| = \sigma_Y$
- **Same** sign: $\max(|\sigma_1|,|\sigma_2|) = \sigma_Y$

The yield surface in the $\sigma_1$–$\sigma_2$ plane is a **hexagon**.

**von Mises (distortion energy):** yield starts when the distortion part of the strain energy density reaches its value at yield in simple tension.
$$\boxed{\sigma_{vm} = \sqrt{\frac{(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2}{2}} \ge \sigma_Y}$$
Plane stress: $\sigma_{vm} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2+\sigma_2^2}$. This is an **ellipse** that circumscribes the Tresca hexagon.
In terms of x–y components (no need for principal stresses):
$$\sigma_{vm} = \sqrt{\sigma_x^2 - \sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}$$
Shaft or beam point with only σ and τ:
$$\sigma_{vm} = \sqrt{\sigma^2+3\tau^2},\qquad \sigma_{Tresca} = \sqrt{\sigma^2+4\tau^2}$$

**Factor of safety:** $n = \sigma_Y/\sigma_{eq}$.

**4. Derivation of von Mises (slides).** Split each principal stress into a hydrostatic part $\sigma_{av} = (\sigma_1+\sigma_2+\sigma_3)/3$ and a distortional part $(\sigma_i - \sigma_{av})$.
- Total energy: $u = \frac{1}{2E}[\sum\sigma_i^2 - 2\nu\sum\sigma_i\sigma_j]$
- Volume-change energy: replace each $\sigma_i$ with $\sigma_{av}$, giving $u_v = \frac{3\sigma_{av}^2}{2E}(1-2\nu) = \frac{1-2\nu}{6E}(\sigma_1+\sigma_2+\sigma_3)^2$
- Distortion energy:
$$u_d = u - u_v = \frac{1+\nu}{3E}\left[\frac{(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2}{2}\right]\quad (1)$$
- In simple tension at yield ($\sigma_1 = \sigma_Y$, $\sigma_2 = \sigma_3 = 0$): $u_{d,Y} = \frac{1+\nu}{3E}\sigma_Y^2$ … (2)
- Setting (1) = (2) gives the criterion. ∎

**Tresca from Mohr's circle:** the tension test at yield has a circle of diameter $\sigma_Y$, so $\tau_Y = \sigma_Y/2$.

**5. Picture.** In the $\sigma_1$–$\sigma_2$ plane the hexagon (Tresca) sits inside the ellipse (von Mises). They touch at the six points of uniaxial and equal-biaxial stress. The largest gap is in pure shear: Tresca predicts $\tau_Y = 0.5\sigma_Y$ and von Mises predicts $\tau_Y = \sigma_Y/\sqrt3 = 0.577\sigma_Y$. Test data for steel, copper and nickel (Crandall Fig. 5.x, slide) fall closer to von Mises.

**6. Special cases.** Tresca is **always conservative** (it predicts yield earlier or equal), so it gives FS ≤ the von Mises FS. If the question asks "will it yield" and Tresca says no, von Mises says no too.

**7. Common traps.**
- Using in-plane $(\sigma_1 - \sigma_2)/2$ for Tresca when both principal stresses have the **same sign**. You must include $\sigma_3 = 0$.
- Plugging x–y stresses into $\sqrt{\sigma_1^2-\sigma_1\sigma_2+\sigma_2^2}$ without first computing principal stresses (or use the $3\tau^2$ form).
- Using $\sigma_u$ instead of $\sigma_Y$.

**8. Summary box**
| Criterion | Equivalent stress | Pure-shear yield |
|---|---|---|
| Tresca | $\sigma_{max}-\sigma_{min}$ (incl. σ₃) = $\sqrt{\sigma^2+4\tau^2}$ for σ–τ | $0.5\sigma_Y$ |
| von Mises | $\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}$ = $\sqrt{\sigma^2+3\tau^2}$ for σ–τ | $0.577\sigma_Y$ |

### B. Solved questions

#### Q12 (PYQ 2014-15 Compre A Q3) — Tresca with $\sigma_2 = -0.5\sigma_1$ *(easy)*
$\sigma_Y = 120$ MPa. Opposite signs, so $\sigma_1 - \sigma_2 = 1.5\sigma_1 = 120$.
$$\boxed{\sigma_1 = 80\ \text{MPa}}$$

---

#### Q13 (PYQ 2014-15 Compre A Q4) — Does it yield by von Mises? *(easy)*
$\sigma_x = 140$, $\sigma_y = -80$, $\tau_{xy} = 125$ MPa, $\sigma_Y = 250$ MPa.
$$\sigma_{vm} = \sqrt{140^2 - (140)(-80) + 80^2 + 3(125)^2} = \sqrt{84\,075} = 290\ \text{MPa} > 250\ \Rightarrow\ \boxed{\text{Yields (FS = 0.86)}}$$

---

#### Q14 (PYQ 2019-20 A Q4) — FS by Tresca and von Mises *(medium, 7 marks)*
**Given (from Fig Q4):** $\sigma_x = 60$ MPa (T), $\sigma_y = 35$ MPa (T), $\tau_{xy} = -30$ MPa (on the right face the shear points down). $\sigma_Y = 270$ MPa.
**Principal:** centre 47.5, $R = \sqrt{12.5^2 + 30^2} = 32.5$, so σ₁ = 80, σ₂ = 15 and σ₃ = 0 MPa.
- **(a) Tresca:** same sign, so $\sigma_{max}-\sigma_{min} = 80 - 0 = 80$. $\boxed{n = 270/80 = 3.38}$
- **(b) von Mises:** $\sqrt{80^2 - 80(15)+15^2} = 73.7$ MPa. $\boxed{n = 270/73.7 = 3.67}$

**Trap check:** using the in-plane value $\sigma_1-\sigma_2 = 65$ would give n = 4.15. That's wrong (unsafe), because both principal stresses are tensile.
**Check:** $n_{Tresca} < n_{vM}$ ✓ (Tresca is conservative).

---

#### Q15 (Slides Ch5) — Bolt diameter by Tresca and von Mises *(easy–medium)*
**Given:** axial pull 15 kN with shear 7.5 kN. $\sigma_Y = 95$ MPa (ν = 0.3 is given but not needed for these two criteria).
With $\sigma = P/A$ and $\tau = V/A$:
- **Tresca:** $\sqrt{\sigma^2+4\tau^2} = \dfrac{\sqrt{15^2+4(7.5)^2}\times10^3}{A} = \dfrac{21\,213}{A} = 95$, so $A = 223.3$ mm². $\boxed{d = 16.9\ \text{mm}}$
- **von Mises:** $\dfrac{\sqrt{15^2+3(7.5)^2}\times10^3}{A} = \dfrac{19\,843}{A} = 95$, so $A = 208.9$ mm². $\boxed{d = 16.3\ \text{mm}}$

(Taking τ as the average V/A, as the slide intends. ν would be needed for the max-principal-strain theory, a common variation.)

---

#### PYQs on this concept that appear in later chapters
- **2021-22 A-Q2(c)** — does the axle yield by von Mises (σ = 140 MPa, τ = 54.4 MPa, $\sigma_Y = 350$ MPa)? See Ch. 6 Q10. $\sigma_{vm} = 169$ MPa, so **no** (FS 2.07).
- **2024-25 B-Q2(d)** — FS at point B of the post by von Mises. See Ch. 6 Q11.

---

## Chapter 5 — Formula and convention sheet

| Item | Formula |
|---|---|
| Engineering stress/strain | $\sigma = P/A_0$, $\epsilon = \delta/L_0$ |
| Hooke + Poisson | $\epsilon_x = \frac1E[\sigma_x-\nu(\sigma_y+\sigma_z)]+\alpha\Delta T$ (cyclic), $\gamma = \tau/G$ |
| Plane stress inverse | $\sigma_x=\frac{E}{1-\nu^2}(\epsilon_x+\nu\epsilon_y)$, $\epsilon_z=-\frac{\nu}{E}(\sigma_x+\sigma_y)$ |
| Elastic constants | $G = \frac{E}{2(1+\nu)}$, $K=\frac{E}{3(1-2\nu)}$ |
| Volume change | $\Delta V/V = \epsilon_x+\epsilon_y+\epsilon_z = \frac{1-2\nu}{E}\sum\sigma$ |
| Dimension change | $\Delta L = L\epsilon$ (include Poisson terms) |
| Thermal (fixed ends) | $\sigma = -E\alpha\Delta T$; with gap: stress only after the gap closes |
| Composite thermal | equilibrium + equal total deformation; larger α goes into compression |
| Energy density | $u = \frac{1}{2E}[\sum\sigma_i^2-2\nu\sum\sigma_i\sigma_j]$; uniaxial $\sigma^2/2E$; shear $\tau^2/2G$ |
| Tresca | $\sigma_{max}-\sigma_{min}=\sigma_Y$ (include σ₃ = 0); σ–τ: $\sqrt{\sigma^2+4\tau^2}$ |
| von Mises | $\sqrt{\sigma_1^2-\sigma_1\sigma_2+\sigma_2^2}$; x–y: $\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau^2}$; σ–τ: $\sqrt{\sigma^2+3\tau^2}$ |
| Factor of safety | $n = \sigma_Y/\sigma_{eq}$; Tresca n ≤ von Mises n |

**Other Crandall Ch. 5 problems worth practising:** 5.1–5.10 (Hooke, Poisson), 5.15–5.25 (thermal, composite), 5.40+ (yield criteria).
