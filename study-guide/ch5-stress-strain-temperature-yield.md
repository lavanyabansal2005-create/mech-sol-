# Chapter 5 — Stress–Strain–Temperature Relations
### Tensile test, Hooke's law, Poisson's ratio, generalized Hooke's law, E–G–ν–K, volume change, thermal strain and thermal stresses, complete equations of elasticity, strain energy, yield criteria (Tresca and von Mises)

**Sources used:** Slides "Chapter 5"; Crandall Ch. 5 (§5.2–5.8, 5.16; Probs 5.1, 5.3–5.5, 5.7–5.9, 5.11–5.13, 5.17, 5.18, 5.20); PYQs 2023-24 (A-Q3), 2024-25 (A-Q2), 2019-20 (A-Q4), 2014-15 (Compre A-Q1–Q4; Test-2 Q3).

**Layout.** Part A (eight items) for each concept, then Part B: slides → Crandall → PYQs, easy → hard. Each solution follows *Problem · Given/Find · Approach · Sketch · Steps · Answer · Check · Takeaway*.

**Material values used when a problem doesn't state them:** steel E = 200 GPa, ν = 0.3, α = 12 × 10⁻⁶/°C; aluminium alloy 2024-T4 E = 73 GPa (10.6 × 10⁶ psi), ν = 0.33, α = 23 × 10⁻⁶/°C (12.6 × 10⁻⁶/°F). Each solution states the values it uses.

---

## Concept 5.1 — The tensile test and material behaviour

### A. Concept explanation

**1. Intuition.** Pull a steel bar in a testing machine and plot force against stretch. At first it behaves like a stiff spring (a straight line). Then it suddenly "gives" and stretches a lot for little extra force: it **yields**. Then it hardens, necks down and breaks. Dividing force by area and stretch by length removes the size of the specimen, leaving a curve that belongs to the **material**.

**2. Why it matters.** Every design number (E, σY, σu, ν) comes from this test. Yield strength is the limit in every factor-of-safety PYQ. Recognising ductile vs brittle behaviour tells you which failure theory and which failure plane apply.

**3. Formal treatment (slides).**
- *Test:* a load is applied along the axis of a circular specimen and stretched at a constant rate; force and elongation (extensometer) are recorded.
- *Engineering stress and strain:* $\sigma = P/A_0$ (Pa) and $\epsilon = \delta/L_0$ (dimensionless), using the **original** dimensions. *True stress and strain* use the current area and length, $\sigma_t = P/A$ and $\epsilon_t = \int dL/L = \ln(L/L_0)$; they differ only after large deformation.
- *Key points on the curve (slides):*
  - **Proportional limit**: the stress above which stress is no longer proportional to strain.
  - **Elastic limit**: the maximum stress that can be applied without permanent deformation on unloading.
  - **Yield point**: large increases in strain with little or no increase in stress.
  - **Ultimate strength**: the peak of the engineering curve, after which necking begins.
- *Ductile materials* (mild steel, aluminium and its alloys, copper, magnesium, nickel, brass, bronze) undergo large strains before failure, absorb a lot of energy and give visible warning. They usually fail on planes of **maximum shear (45°)**, giving the typical **cup-and-cone** fracture.
- *Brittle materials* (concrete, stone, cast iron, glass, plaster) fail at small strains, by **tensile (normal) stress**, on a surface perpendicular to the load.
- *Elastic vs plastic:* if the strain disappears when the stress is removed the behaviour is elastic; if not, it is plastic.
- *Fatigue:* failure at stresses well below the ultimate strength under many load cycles. *Creep:* time-dependent deformation under constant stress.
- *Hooke's law (uniaxial):* $\sigma = E\epsilon$, where Young's modulus E is the slope of the linear part. Young observed that this slope is a material constant, independent of specimen geometry. Typical values (slides, GPa): mild steel 210, aluminium 70, concrete 18.5, wood 12.5, nylon 2.8, rubber 0.004.
- *Idealized curves (slides, Crandall §5.3):* linear elastic; rigid–perfectly plastic; elastic–perfectly plastic; linear strain hardening. "It is impossible to describe the entire stress–strain curve with a simple mathematical expression." Choose the model that captures what matters for the problem at hand.

**4. Derivation — reduction of area in terms of true strain (Crandall Prob 5.11).** When plastic strains dominate, the material deforms at constant volume: $A_0L_0 = AL$. The true strain is $\epsilon_t = \ln(L/L_0) = \ln(A_0/A)$, so $A/A_0 = e^{-\epsilon_t}$ and
$$\text{Reduction of area} = \frac{A_0 - A}{A_0} = 1 - e^{-\epsilon_t}$$

**5. Picture.** Sketch two curves on the same axes: a ductile one (linear, a yield plateau, hardening, necking down to fracture at large strain) and a brittle one (linear almost to fracture at small strain). Beside them, the four idealized models (diagram below).

**6. Special cases.** Materials without a sharp yield point (aluminium) use the 0.2% offset yield strength. Rubber is nonlinear elastic; E is the initial slope.

**7. Traps.** Using σu where the question asks for yield; using true stress where engineering stress is meant; quoting E in MPa when the formula needs GPa (or vice versa).

**8. Summary.** $\sigma = P/A_0$, $\epsilon = \delta/L_0$, $\sigma = E\epsilon$; ductile → shear failure at 45°; brittle → tensile failure on the cross-section.

### B. Solved question

#### Q1 (Crandall Prob 5.11) — Reduction of area and true strain *(easy, derivation)*
**Problem.** A tensile specimen has original area A₀ and area A at some point in the test. If the elastic strains can be neglected compared with the plastic strains, show that the reduction of area is $1 - e^{-\epsilon_t}$, where εt is the true strain.

**Solution.** As derived in item 4: plastic flow conserves volume, so $A/A_0 = L_0/L = e^{-\epsilon_t}$.

$$\boxed{\text{RA} = 1 - e^{-\epsilon_t}}$$

**Check.** A true strain of 1 (length × 2.72) gives RA = 63% ✓, typical of a necked ductile bar.

**Exam takeaway.** Large-strain plasticity conserves volume (ν → 0.5); small elastic strains do not (Concept 5.2).

---

## Concept 5.2 — Poisson's ratio and the generalized Hooke's law

### A. Concept explanation

**1. Intuition.** Stretch a rubber band and it gets thinner. The ratio of sideways shrinking to lengthwise stretching is Poisson's ratio. Most metals are about 0.3, rubber about 0.5 (nearly incompressible) and cork about 0. When a plate is pulled in two directions, each pull also thins the plate and shrinks the other direction, and all these effects simply add.

**2. Why it matters.** It explains why a plate under biaxial stress changes thickness, and it appears in every "change in thickness/volume" PYQ (2023 A-Q3 and 2024 A-Q2 are the same question type two years running). It is also the step that turns gauge readings (strains) into stresses.

**3. Formal treatment (slides).** For uniaxial σx: $\epsilon_x = \sigma_x/E$ and $\epsilon_y = \epsilon_z = -\nu\epsilon_x$, where
$$\nu = -\frac{\text{lateral strain}}{\text{axial strain}}$$
*Assumptions (slides):* (1) the material is linearly elastic, (2) strain is linearly related to stress, (3) deformations are small, (4) the material is **isotropic** (no directional dependence).

*Isotropy arguments (slides; Crandall §5.4, Probs 5.5–5.6):*
- A normal stress produces **no shear strain**. Rotating the element 180° about the loading axis leaves the load unchanged but would flip the sign of any shear strain, which contradicts isotropy.
- A shear stress produces **no normal strain**. Reversing τ would reverse the normal strain, but by symmetry the result must be the same; by linearity it must therefore be zero.
- (Prob 5.5) τxy cannot produce γyz, and (Prob 5.6) τxy cannot produce a uniform expansion, by the same symmetry reasoning.

So normal stresses cause only normal strains, and each shear stress causes only its own shear strain.

**4. Derivation — superposition gives the generalized Hooke's law (slides).**
$$\boxed{\epsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right] + \alpha\Delta T,\quad \epsilon_y = \frac{1}{E}\left[\sigma_y - \nu(\sigma_z + \sigma_x)\right] + \alpha\Delta T,\quad \epsilon_z = \frac{1}{E}\left[\sigma_z - \nu(\sigma_x + \sigma_y)\right] + \alpha\Delta T}$$
$$\boxed{\gamma_{xy} = \frac{\tau_{xy}}{G},\quad \gamma_{yz} = \frac{\tau_{yz}}{G},\quad \gamma_{zx} = \frac{\tau_{zx}}{G}}$$
(The αΔT term is the thermal strain, Concept 5.4.)

*Plane stress ($\sigma_z = 0$), inverted:*
$$\sigma_x = \frac{E}{1-\nu^2}(\epsilon_x + \nu\epsilon_y),\qquad \sigma_y = \frac{E}{1-\nu^2}(\epsilon_y + \nu\epsilon_x),\qquad \epsilon_z = -\frac{\nu}{E}(\sigma_x + \sigma_y) = -\frac{\nu}{1-\nu}(\epsilon_x + \epsilon_y)$$
*Full inversion (Crandall Prob 5.7), with $e = \epsilon_x + \epsilon_y + \epsilon_z$:*
$$\sigma_x = \lambda e + 2G\epsilon_x - \frac{E\alpha\Delta T}{1-2\nu},\qquad \lambda = \frac{\nu E}{(1+\nu)(1-2\nu)}$$
and similarly for y and z.

*Isotropy ⇒ the principal axes of strain coincide with the principal axes of stress (slides).* Zero shear stress gives zero shear strain, so either Mohr's circle may be used to locate them.

*Volume change (Crandall Prob 5.2–5.3):* for small strains, $\dfrac{\Delta V}{V} = \epsilon_x + \epsilon_y + \epsilon_z = \dfrac{1 - 2\nu}{E}(\sigma_x + \sigma_y + \sigma_z)$.

**5. Picture.** A circle drawn on a plate becomes an ellipse whose axes follow the principal directions (Ch. 4 Q32). A thin plate under in-plane tension gets thinner.

**6. Special cases.**
- *Uniaxial:* $\epsilon_y = -\nu\sigma/E$.
- *Laterally constrained* (plate between rigid walls, Q2; elastic material in a rigid cavity, Q8): one or two strains are zero, so stresses appear in those directions and the member becomes stiffer.
- ν = 0.5: ΔV = 0, constant volume.

**7. Traps.**
- Using the plane-**strain** formula where plane **stress** applies, or the other way round.
- Forgetting the Poisson terms when finding a dimension change. In the 2024 PYQ the y diameter actually **shrinks** although σy is tensile.
- Mixing E in GPa with σ in MPa. Convert so both are in MPa.
- Using the shear stress τxy to find a normal strain. It has no effect on normal strains (Q4).

**8. Summary box**
$$\epsilon_i = \frac{1}{E}[\sigma_i - \nu(\sigma_j + \sigma_k)] + \alpha\Delta T,\quad \gamma = \tau/G,\quad \frac{\Delta V}{V} = \frac{1 - 2\nu}{E}\sum\sigma,\quad \text{plane stress: } \sigma_x = \frac{E}{1 - \nu^2}(\epsilon_x + \nu\epsilon_y)$$

### B. Solved questions

#### Q2 (Slides Ch5) — Plate squeezed between rigid walls *(medium)*
**Problem.** A long thin plate of width b, thickness t and length L is placed between two rigid walls a distance b apart and loaded by an axial (compressive) force P along its length. Find the deflection of the plate parallel to P.

**Given:** walls prevent lateral strain (εy = 0, y across the width); the faces are free (σz = 0, plane stress through the thickness); no friction. **Find:** δ along x.

**Approach.** Generalized Hooke's law with one stress unknown (σy) and one strain known (εy = 0).

**Solution.**
1. *Axial stress:* $\sigma_x = -P/(bt)$.
2. *Wall condition:* $\epsilon_y = \frac1E(\sigma_y - \nu\sigma_x) = 0$, so $\sigma_y = \nu\sigma_x$ (the walls push back).
3. *Axial strain:* $\epsilon_x = \frac1E(\sigma_x - \nu\sigma_y) = \frac{\sigma_x(1 - \nu^2)}{E}$.
4. *Deflection:* $\delta = |\epsilon_x|L$.

$$\boxed{\delta = \frac{PL(1-\nu^2)}{Ebt}\ \text{(shortening)},\qquad \sigma_y = -\frac{\nu P}{bt}}$$

**Check.** ν = 0 gives the free-plate result PL/AE ✓. The walls make the plate stiffer by $1/(1 - \nu^2) \approx 1.1$ ✓.

**Exam takeaway.** "Rigid walls" or "fits exactly between" is the signal for a zero strain. **Variation:** walls in both lateral directions (Q8).

---

#### Q3 (Crandall Prob 5.8) — Strains in a steel plate in plane stress *(easy)*
**Problem.** The stresses in a flat steel plate in plane stress are σx = 130, σy = −70 and τxy = 80 MN/m². Find the magnitude and orientation of the principal strains in the plane of the plate, and the third principal strain (perpendicular to the plate). E = 200 GPa, ν = 0.3.

**Approach.** Hooke's law for εx, εy and γ, then the strain circle (or principal stresses first, since the axes coincide).

**Solution.**
1. $G = \dfrac{E}{2(1 + \nu)} = 76.9$ GPa.
2. $\epsilon_x = \dfrac{130 - 0.3(-70)}{200\,000} = 755\mu$; $\epsilon_y = \dfrac{-70 - 0.3(130)}{200\,000} = -545\mu$; $\gamma_{xy} = \dfrac{80}{76\,923} = 1040\mu$.
3. *Strain circle:* centre 105μ; $R = \sqrt{650^2 + 520^2} = 832.4\mu$; so ε₁ = 937.4μ and ε₂ = −727.4μ. $\tan2\theta_p = \dfrac{1040}{1300}$, so θp = 19.3° (counter-clockwise from x).
4. *Third principal strain:* $\epsilon_z = -\dfrac{\nu}{E}(\sigma_x + \sigma_y) = -\dfrac{0.3(60)}{200\,000} = -90\mu$.

$$\boxed{\epsilon_1 = 937\mu\ \text{at } 19.3^\circ,\qquad \epsilon_2 = -727\mu,\qquad \epsilon_3 = \epsilon_z = -90\mu}$$

**Check.** Principal stresses first: σ₁ = 158.1, σ₂ = −98.1 MPa at the same 19.3°; $\epsilon_1 = (158.1 + 29.4)/200\,000 = 937\mu$ ✓.

**Exam takeaway.** The principal directions of stress and strain coincide, so you may work with either circle.

---

#### Q4 (Crandall Prob 5.9) — Find σy from the thickness strain *(easy, with a trap)*
**Problem.** In a flat steel plate loaded in the x–y plane, σx = 145 MN/m², τxy = 42 MN/m² and εz = −3.6 × 10⁻⁴. Find σy. E = 200 GPa, ν = 0.3.

**Approach.** In plane stress the thickness strain depends only on the in-plane **normal** stresses.

**Solution.**
1. $\epsilon_z = -\dfrac{\nu}{E}(\sigma_x + \sigma_y)$, so $\sigma_x + \sigma_y = \dfrac{-\epsilon_zE}{\nu} = \dfrac{3.6\times10^{-4}(200\,000)}{0.3} = 240$ MPa.
2. $\sigma_y = 240 - 145$.

$$\boxed{\sigma_y = 95\ \text{MN/m}^2}$$

**Check.** The 42 MPa shear stress plays no part, because shear produces no normal strain in an isotropic material ✓.

**Exam takeaway.** The shear stress is a **distractor**. Spotting that is the point of the question.

---

#### Q5 (PYQ 2014-15 Compre A Q2) — Find ν and E from a tension test *(easy)*
**Problem.** A bar 8 mm × 8 mm carries an axial pull of 10 kN. Its lateral dimensions reduce by 2 × 10⁻³ mm. Find ν and E, given G = 80 GPa.

**Solution.**
1. $\sigma = 10\,000/64 = 156.25$ MPa.
2. Lateral strain $= -2\times10^{-3}/8 = -2.5\times10^{-4}$.
3. $|\epsilon_{lat}| = \nu\sigma/E$ with $E = 2G(1 + \nu)$: $2.5\times10^{-4} = \dfrac{156.25\nu}{2(80\,000)(1 + \nu)}$, so $0.256(1 + \nu) = \nu$ and ν = 0.344.
4. $E = 2(80)(1.344) = 215$ GPa.

$$\boxed{\nu = 0.344,\qquad E = 215\ \text{GPa}}$$

**Check.** Axial strain $= 156.25/215\,000 = 7.27\times10^{-4}$, and $2.5/7.27 = 0.344$ ✓.

**Exam takeaway.** G given, ν wanted: combine $\epsilon_{lat} = -\nu\sigma/E$ with $E = 2G(1 + \nu)$.

---

#### Q6 (Crandall Prob 5.12) — Pressure in a tank from an axial strain gauge *(medium)*
**Problem.** A long, thin-walled cylindrical tank of radius r and wall thickness t has closed ends. With pressure p inside, a strain gauge on the outside surface, parallel to the axis, reads εa. Find p.

**Approach.** Wall stresses from Ch. 4 (σθ = pr/t, σa = pr/2t), then Hooke's law in the axial direction.

**Solution.**
1. $\epsilon_a = \dfrac1E(\sigma_a - \nu\sigma_\theta) = \dfrac{pr}{Et}\left(\dfrac12 - \nu\right)$.
2. Solve for p.

$$\boxed{p = \frac{2Et\,\epsilon_a}{r(1 - 2\nu)}}$$

**Check.** ν = 0.5 makes the axial gauge read zero whatever the pressure (the denominator vanishes): a hoop gauge would be needed ✓. For steel (ν = 0.3) the axial gauge reads only $0.2pr/Et$, a fifth of the hoop gauge's $0.85pr/Et$.

**Exam takeaway.** A hoop gauge is far more sensitive; mention it.

---

#### Q7 (Crandall Prob 5.20) — Tank just fitting between rigid walls: force on the walls *(medium)*
**Problem.** A long thin-walled cylindrical tank of length L just fits between two rigid end walls when it is unpressurised. Estimate the force on the walls when the pressure in the tank is p (Hooke's law material).

**Approach.** The walls prevent axial strain: εa = 0. Equilibrium of an end cap relates the axial wall stress to p and the wall force F.

**Solution.**
1. *End-cap equilibrium:* the pressure pushes the cap out with $p\pi r^2$; the wall pushes in with F; the tank wall carries the difference: $\sigma_a(2\pi rt) = p\pi r^2 - F$.
2. *Constraint:* $\epsilon_a = \frac1E(\sigma_a - \nu\sigma_\theta) = 0$, so $\sigma_a = \nu\sigma_\theta = \nu pr/t$.
3. *Combine:* $p\pi r^2 - F = 2\pi rt\cdot\nu pr/t = 2\nu p\pi r^2$.

$$\boxed{F = \pi r^2p\,(1 - 2\nu)}$$

**Check.** For ν = 0.3, F = 0.4πr²p. If ν were 0.5 the tank would not try to lengthen and F = 0 ✓.

**Exam takeaway.** Constraint problems always use "known strain → unknown stress".

---

#### Q8 (Crandall Prob 5.1) — Elastic block confined in a rigid cavity *(medium)*
**Problem.** An elastic material (E, ν) fills a square cavity of side 2a and height L in a rigid block. A rigid cap on top carries a force F, and the height decreases by δ. Find F.

**Approach.** Lateral strains are zero in both horizontal directions (εx = εy = 0); σz = −F/4a².

**Solution.**
1. By symmetry σx = σy. $\epsilon_x = \frac1E[\sigma_x - \nu(\sigma_x + \sigma_z)] = 0$, so $\sigma_x(1 - \nu) = \nu\sigma_z$ and $\sigma_x = \dfrac{\nu}{1 - \nu}\sigma_z$.
2. $\epsilon_z = \dfrac1E(\sigma_z - 2\nu\sigma_x) = \dfrac{\sigma_z}{E}\left(1 - \dfrac{2\nu^2}{1 - \nu}\right) = \dfrac{\sigma_z(1 + \nu)(1 - 2\nu)}{E(1 - \nu)}$.
3. With εz = −δ/L and σz = −F/4a²:

$$\boxed{F = \frac{4a^2E\,\delta}{L}\cdot\frac{(1 - \nu)}{(1 + \nu)(1 - 2\nu)}}$$

**Check.** ν = 0 gives the free result $4a^2E\delta/L$ ✓. For ν = 0.3 the confined block is 1.35× stiffer. As ν → 0.5 it becomes infinitely stiff, because an incompressible material cannot shorten if it cannot expand sideways ✓.

**Exam takeaway.** This is the "constrained modulus" used in soil mechanics. **Variation:** confinement in one direction only gives the factor $1/(1 - \nu^2)$ of Q2.

---

#### Q9 (PYQ 2023-24 Compre A Q3) — Plate in biaxial stress: γmax, Δt, ΔV *(easy–medium, 10 marks)*
**Problem.** A rectangular steel plate (400 × 550 × 20 mm) carries σx = 67 MPa (tension) and σy = −23 MPa (compression). E = 200 GPa (the paper's "200 MPa" is a typo), ν = 0.30. Find (a) the maximum in-plane shear strain, (b) the change in thickness Δt and (c) the change in volume ΔV.

**Solution.**
1. *(a)* No shear stress, so x and y are principal. $\gamma_{max} = \epsilon_x - \epsilon_y = \dfrac{(\sigma_x - \sigma_y)(1 + \nu)}{E} = \dfrac{90(1.3)}{200\,000} = 585\times10^{-6}$. (Or τmax = 45 MPa and G = 76.9 GPa give the same.)
2. *(b)* $\epsilon_z = -\dfrac{\nu}{E}(\sigma_x + \sigma_y) = -\dfrac{0.3(44)}{200\,000} = -66\times10^{-6}$, so $\Delta t = 20(-66\times10^{-6}) = -1.32\times10^{-3}$ mm.
3. *(c)* $\Delta V = V\dfrac{1 - 2\nu}{E}(\sigma_x + \sigma_y) = (4.4\times10^6)\dfrac{0.4(44)}{200\,000} = 387$ mm³.

$$\boxed{\gamma_{max} = 585\times10^{-6},\qquad \Delta t = -1.32\times10^{-3}\ \text{mm (thinner)},\qquad \Delta V = +387\ \text{mm}^3}$$

**Check by strains.** εx = (67 + 6.9)/2 × 10⁵ = 369.5μ and εy = (−23 − 20.1)/2 × 10⁵ = −215.5μ. Sum with εz: 369.5 − 215.5 − 66 = 88μ, and 88μ × 4.4 × 10⁶ mm³ = 387 mm³ ✓.

**Exam takeaway.** Three standard parts; the volume change uses the sum of the stresses, not their difference.

---

#### Q10 (PYQ 2024-25 Compre A Q2) — Etched circle on a brass plate *(easy–medium, 10 marks)*
**Problem.** A 200 mm circle is etched on a 400 × 400 × 20 mm brass plate. σx = 42 MPa and σy = 14 MPa. E = 100 GPa, ν = 0.34. Find the changes in length of diameter ac (along x) and bd (along y), the change in thickness and the change in volume.

**Solution.**
1. $\epsilon_x = \dfrac{42 - 0.34(14)}{100\,000} = 372.4\mu$; $\epsilon_y = \dfrac{14 - 0.34(42)}{100\,000} = -2.8\mu$; $\epsilon_z = -\dfrac{0.34(56)}{100\,000} = -190.4\mu$.
2. $\Delta_{ac} = 200\epsilon_x = 0.0745$ mm; $\Delta_{bd} = 200\epsilon_y = -5.6\times10^{-4}$ mm; $\Delta t = 20\epsilon_z = -3.81\times10^{-3}$ mm.
3. $\Delta V = (3.2\times10^6)(372.4 - 2.8 - 190.4)\times10^{-6} = 573$ mm³.

$$\boxed{\Delta_{ac} = 0.0745\ \text{mm},\quad \Delta_{bd} = -5.6\times10^{-4}\ \text{mm},\quad \Delta t = -3.81\times10^{-3}\ \text{mm},\quad \Delta V = 573\ \text{mm}^3}$$

**Check.** $\Delta V/V = 179.2\mu = (1 - 2\nu)(56)/E = 0.32(56)/100\,000$ ✓.

**Exam takeaway.** bd **shrinks** even though σy is tensile, because $\nu\sigma_x > \sigma_y$. Examiners set the numbers up for exactly this surprise.

---

## Concept 5.3 — Relations among E, G, ν and the bulk modulus K

### A. Concept explanation

**1. Intuition.** Shear and stretch are not independent. A square under pure shear is, viewed at 45°, a square stretched along one diagonal and squashed along the other. So the shear stiffness G must be fixed by E and ν. Likewise, squeezing equally from all sides (hydrostatic pressure) shrinks the volume by an amount set by E and ν.

**2. Why it matters.** Torsion problems give G, while axial problems give E; you often need to convert. The bulk modulus K governs how compressible a material is, and it explains why ν can never exceed ½.

**3. Formal treatment.** Only **two** of E, G, ν and K are independent for an isotropic material:
$$G = \frac{E}{2(1+\nu)},\qquad K = \frac{E}{3(1-2\nu)}\qquad(\text{bulk modulus } K = \frac{p}{-\Delta V/V})$$

**4. Derivations.**

*(a) E–G–ν (slides; Crandall §5.4).* Pure shear τ on the x–y element ⇔ principal stresses σ₁ = +τ and σ₂ = −τ on the 45° element.
- Strain along direction 1 from Hooke's law: $\epsilon_1 = \dfrac{\tau}{E} - \nu\dfrac{-\tau}{E} = \dfrac{\tau(1 + \nu)}{E}$.
- The same strain from the shear strain, by transformation (Ch. 4) with εx = εy = 0: $\epsilon_{45} = \gamma/2 = \tau/2G$.
- Equate: $\dfrac{\tau}{2G} = \dfrac{\tau(1 + \nu)}{E}$, so $G = \dfrac{E}{2(1 + \nu)}$. ∎

*(b) Bulk modulus (Crandall Prob 5.3).* Under hydrostatic pressure, σx = σy = σz = −p. Then $\Delta V/V = \frac{1 - 2\nu}{E}(-3p)$, so $K = \dfrac{p}{-\Delta V/V} = \dfrac{E}{3(1 - 2\nu)}$. ∎

**5. Picture.** A shear-distorted square with its 45° diagonals: one stretched by ε₁, one shortened by the same amount.

**6. Special cases.** ν = 0: G = E/2 and K = E/3. ν = 0.5: G = E/3 and K → ∞ (incompressible).

**7. Traps.** Using G = E/2(1 − ν) (wrong sign). Forgetting that the formulas need an isotropic material (not wood or composites).

**8. Summary.** $E = 2G(1 + \nu) = 3K(1 - 2\nu)$.

### B. Solved question

#### Q11 (Crandall Probs 5.3, 5.4) — Bulk modulus, and why ν cannot exceed ½ *(easy, conceptual)*
**Problem.** (5.3) Show that $\Delta V/V = (\sigma_x + \sigma_y + \sigma_z)(1 - 2\nu)/E$ and that the bulk modulus is $B = E/3(1 - 2\nu)$. (5.4) Discuss the stability under hydrostatic pressure of a hypothetical material with ν > ½.

**Solution.**
1. *(5.3)* Add the three Hooke's-law strains (no temperature change): $\epsilon_x + \epsilon_y + \epsilon_z = \frac{1}{E}(1 - 2\nu)(\sigma_x + \sigma_y + \sigma_z)$, which is ΔV/V (Prob 5.2). With all σ = −p: $B = E/3(1 - 2\nu)$.
2. *(5.4)* If ν > ½, then B < 0: hydrostatic **compression** would make the volume **increase**. Such a body would release energy as it expanded under pressure, so it would be unstable. Equivalently, the strain energy would not be positive for all deformations. Therefore $\nu \le \tfrac12$ for stable isotropic materials. (Positive G likewise needs ν > −1.)

$$\boxed{B = \frac{E}{3(1 - 2\nu)};\qquad -1 < \nu \le \tfrac12\ \text{for a stable material}}$$

**Exam takeaway.** ν > 0.5 is a red flag in any data you are given.

---

## Concept 5.4 — Thermal strain and thermal stresses

### A. Concept explanation

**1. Intuition.** Heat a rail and it wants to grow. If it is free, it grows and **no stress** develops. If it is clamped between walls, the walls must push it back to its original length, and that push is the thermal stress. A rail can buckle on a hot day for exactly this reason.

**2. Why it matters.** Rails, pipelines, bimetal strips, bolts in sleeves, shrink fits, aircraft skins, thermostats (the "thermo gate" PYQ). PYQ 2014 Compre A Q1 and Test-2 Q3 are thermal problems.

**3. Formal treatment (slides).**
$$\epsilon_T = \alpha(T - T_0) = \alpha\Delta T,\qquad \text{total strain } \epsilon = \frac{\sigma}{E} + \alpha\Delta T$$
For isotropic materials the thermal strain is the same in all directions and **produces no shear strain**.

**4. Derivation — bar fixed at both ends (slides, superposition).**
- Release B and let the bar expand freely: $\delta_T = \alpha\Delta TL$.
- Apply the redundant P to push it back: $\delta_P = PL/AE$.
- Compatibility: $\delta_T + \delta_P = 0$, so $P = -AE\alpha\Delta T$.
$$\boxed{\sigma = -E\alpha\Delta T}\quad(\text{compressive for heating; independent of L and A})$$
*With a gap Δ:* stress appears only after the gap closes; then $\alpha\Delta TL - \Delta = |P|L/AE$.

*General recipe (the three steps of Ch. 2):* (1) equilibrium of the member forces; (2) compatibility of **total** deformations, $\delta_i = \frac{F_iL_i}{A_iE_i} + \alpha_i\Delta TL_i$; (3) solve.

**5. Picture.** Three sketches (diagram below): (a) the free bar grows by αΔTL; (b) the force P pushes it back by PL/AE; (c) together the length is unchanged.

**6. Special cases.**
- A uniformly heated, unrestrained body of one material has no thermal stress, whatever its shape; even a hole simply grows (Q19).
- In composite systems (bolt + sleeve), the member with the **larger α** ends up in **compression**.
- A temperature **drop** in a fixed or pre-stressed member adds **tension**.

**7. Traps.**
- Using ΔT in °F with α in /°C.
- Forgetting the gap: close it first, then the stress builds.
- Forgetting the thermal term in **only one** of two members.
- Sign of ΔT for cooling problems.

**8. Summary.** $\epsilon = \sigma/E + \alpha\Delta T$; fixed ends: $\sigma = -E\alpha\Delta T$; composite: equilibrium + equal total deformation.

### B. Solved questions

#### Q12 (PYQ 2014-15 Compre A Q1) — Rod fixed at both ends, heated *(easy)*
**Problem.** A 20 mm diameter steel rod, 1.5 m long, is fixed at both ends. The temperature rises by 60°C. Find the reaction at the supports. E = 110 GPa, α = 1.2 × 10⁻⁵/°C.

**Solution.**
1. $\sigma = E\alpha\Delta T = 110\,000(1.2\times10^{-5})(60) = 79.2$ MPa (compression).
2. $R = \sigma A = 79.2\,\pi(10)^2 = 24\,880$ N.

$$\boxed{R = 24.9\ \text{kN}}$$

**Exam takeaway.** L does not matter. That is the classic trap.

---

#### Q13 (Slides Ch5, Gere) — Copper bar with a gap *(easy)*
**Problem.** A copper bar AB, 25 in long, is placed with a 0.008 in gap between end A and a rigid restraint. Find the axial compressive stress when the temperature rises by 50°F. α = 9.6 × 10⁻⁶/°F, E = 16 × 10⁶ psi.

**Solution.**
1. Free expansion $= 9.6\times10^{-6}(50)(25) = 0.012$ in, which exceeds the 0.008 in gap.
2. Excess suppressed: 0.004 in, so the strain is 0.004/25.
3. $\sigma_c = E(0.004/25) = 16\times10^6(1.6\times10^{-4})$.

$$\boxed{\sigma_c = 2560\ \text{psi (compression)}}$$

**Exam takeaway.** Always compare the free expansion with the gap first.

---

#### Q14 (Slides Ch5, Gere) — Pre-stressed steel wire *(easy)*
**Problem.** A steel wire stretched between rigid supports has a pre-stress of 42 MPa at 20°C. (a) What is the stress at 0°C? (b) At what temperature does the stress become zero? α = 14 × 10⁻⁶/°C, E = 200 GPa.

**Solution.**
1. *(a)* Cooling adds tension: $\Delta\sigma = E\alpha\Delta T = 200\,000(14\times10^{-6})(20) = 56$ MPa, so σ = 98 MPa.
2. *(b)* Zero stress when $E\alpha(T - 20) = 42$: $T - 20 = 42/2.8 = 15$, so T = 35°C.

$$\boxed{\sigma(0^\circ\text{C}) = 98\ \text{MPa},\qquad T_{\sigma=0} = 35^\circ\text{C}}$$

---

#### Q15 (Slides Ch5, Gere) — Three wires: when does steel carry everything? *(medium)*
**Problem.** A rigid bar weighing 750 lb hangs from three equally spaced wires (two steel, one aluminium in the middle), each 1/8 in diameter and initially of equal length. What temperature rise makes the entire load carried by the steel wires? $E_s = 30\times10^6$ psi, $\alpha_s = 6.5\times10^{-6}$/°F, $\alpha_a = 12\times10^{-6}$/°F.

**Approach.** Aluminium expands more. When its force drops to zero it is just slack; the bar stays level (symmetry), so all three wires have the same length change.

**Solution.**
1. *Equilibrium:* each steel wire carries W/2 = 375 lb; the aluminium carries 0.
2. *Compatibility:* $\alpha_s\Delta TL + \dfrac{(W/2)L}{A_sE_s} = \alpha_a\Delta TL$.
3. $\Delta T = \dfrac{W/2}{A_sE_s(\alpha_a - \alpha_s)}$, with $A_s = \frac{\pi}{4}(0.125)^2 = 0.01227$ in²:
$$\Delta T = \frac{375}{0.01227(30\times10^6)(5.5\times10^{-6})}$$

$$\boxed{\Delta T \approx 185^\circ\text{F}}$$

**Check.** The aluminium modulus is not needed, because its force is zero at this instant ✓.

**Exam takeaway.** "Entire load carried by X" means "force in the other member = 0". That kills one unknown.

---

#### Q16 (Slides Ch5, Gere) — Brass sleeve on a steel bolt *(medium)*
**Problem.** A brass sleeve S is fitted over a steel bolt B and the nut is tightened until just snug. Bolt: $d_B = 25$ mm, $E_B = 200$ GPa, $\alpha_B = 10\times10^{-6}$/°C. Sleeve: $d_1 = 26$ mm, $d_2 = 36$ mm, $E_S = 100$ GPa, $\alpha_S = 21\times10^{-6}$/°C. Find the temperature rise ΔT that produces a compressive stress of 25 MPa in the sleeve.

**Approach.** The sleeve (larger α) wants to grow more and is held back by the bolt. Equal forces, equal final lengths.

**Solution.**
1. *Equilibrium:* $P_S = P_B = P$ (sleeve in compression, bolt in tension).
2. *Compatibility:* $\alpha_S\Delta T - \dfrac{P}{E_SA_S} = \alpha_B\Delta T + \dfrac{P}{E_BA_B}$.
3. So $\sigma_S = \dfrac{P}{A_S} = \dfrac{(\alpha_S - \alpha_B)\Delta T\,E_S}{1 + \frac{E_SA_S}{E_BA_B}}$ and $\Delta T = \dfrac{\sigma_S}{E_S(\alpha_S - \alpha_B)}\left(1 + \dfrac{E_SA_S}{E_BA_B}\right)$.
4. $A_S = \frac\pi4(36^2 - 26^2) = 487$ mm² and $A_B = \frac\pi4(25)^2 = 491$ mm², so the bracket is $1 + \frac{100(487)}{200(491)} = 1.496$.
5. $\Delta T = \dfrac{25(1.496)}{100\,000(11\times10^{-6})}$.

$$\boxed{\Delta T \approx 34^\circ\text{C}}$$

**Exam takeaway.** The larger-α member always ends in compression. **Variation:** "find the bolt stress", $\sigma_B = 25(487/491) = 24.8$ MPa (T).

---

#### Q17 (Slides Ch5, Gere) — Rigid bar on two cables with a temperature rise: allowable P *(hard)*
**Problem.** A rigid bar ABCD is pinned at A and supported by cables at B (2b from A, $d_B = 12$ mm) and C (4b, $d_C = 20$ mm). A load P acts at D (5b). The temperature rises by 60°C. Each cable must have a factor of safety of at least 5 against its ultimate load ($(T_B)_{ult} = 102$ kN, $(T_C)_{ult} = 231$ kN). Find the allowable P. E = 140 GPa, α = 12 × 10⁻⁶/°C.

**Approach.** Equilibrium about A; compatibility from the rigid bar's rotation; each cable's deformation includes the thermal term.

**Solution.**
1. *Equilibrium:* $\sum M_A$: $2T_B + 4T_C = 5P$ … (1).
2. *Compatibility (rigid bar):* $\delta_C = 2\delta_B$ … (2).
3. *Force–displacement–temperature:* $\delta_B = \dfrac{T_BL}{EA_B} + \alpha\Delta TL$ and $\delta_C = \dfrac{T_CL}{EA_C} + \alpha\Delta TL$ … (3), (4).
4. *Substitute into (2):* $\dfrac{T_C}{EA_C} + \alpha\Delta T = \dfrac{2T_B}{EA_B} + 2\alpha\Delta T$, so $2T_BA_C - T_CA_B = -E\alpha\Delta TA_BA_C$ … (5).
5. *Numbers* (effective cable areas from the slide: $A_B = 76.7$ mm², $A_C = 173$ mm²): $T_B(346) - T_C(76.7) = -1\,338\,000$ … (6).
6. *Solve (1) and (6):* $T_B = 0.2494P - 3480$ and $T_C = 1.1253P + 1740$ (N).
7. *Allowables:* $(T_B)_{allow} = 20.4$ kN gives $P_B = 4.0096(20\,400) + 13\,953 = 95.7$ kN; $(T_C)_{allow} = 46.2$ kN gives $P_C = 0.8887(46\,200) - 1546 = 39.5$ kN.

$$\boxed{P_{allow} = 39.5\ \text{kN (cable C governs)}}$$

**Exam takeaway.** Heating *relieves* cable B (the −3480 term) and *loads* cable C, because compatibility forces C to stretch twice as much as B. Thermal terms appear in both cables, and examiners check that you include them in both.

---

#### Q18 (Crandall Prob 5.17) — Shrink fit: heat the pulley or cool the shaft? *(medium)*
**Problem.** A steel shaft (25.000 mm) is to be tight-fitted into a steel pulley (hole 24.950 mm). The pulley can be heated, or the shaft cooled, to give a clearance of 0.025 mm for easy assembly. Which is more effective, and what temperature change is needed in each case? (α = 12 × 10⁻⁶/°C.)

**Solution.**
1. *Heat the pulley:* the hole must grow from 24.950 to 25.025 mm (Δd = 0.075 mm). $\Delta T = \dfrac{0.075}{12\times10^{-6}(24.950)} = +250.5^\circ$C.
2. *Cool the shaft:* the shaft must shrink from 25.000 to 24.925 mm (Δd = −0.075 mm). $\Delta T = \dfrac{-0.075}{12\times10^{-6}(25.000)} = -250^\circ$C.

$$\boxed{\text{heat the pulley by } \approx 250^\circ\text{C, or cool the shaft by } \approx 250^\circ\text{C}}$$

The magnitudes are practically the same, but cooling by 250°C below room temperature (to about −230°C) is beyond even liquid nitrogen (−196°C). So **heating the pulley** (or combining a heated pulley with a cooled shaft) is the practical choice.

**Check.** A hole expands like the material around it, by α × diameter × ΔT ✓ (see Q19).

**Exam takeaway.** "Does a hole get bigger or smaller when heated?" Bigger, exactly as if it were filled with the same material.

---

#### Q19 (Crandall Prob 5.13) — A heated sheet with a hole *(easy, conceptual)*
**Problem.** A circular sheet of metal has a small circular hole cut out of it. If the sheet is initially stress-free, unrestrained and heated uniformly by T, what shape do the circular boundaries take?

**Solution.**
1. A uniform temperature rise in an unrestrained, homogeneous body produces uniform thermal strain αT in every direction and **no stress**.
2. Every length scales by (1 + αT): the outer circle and the hole both remain circles, and the hole **grows**.

$$\boxed{\text{Both boundaries stay circular; all radii (hole included) increase by the factor } (1 + \alpha T)}$$

**Exam takeaway.** Uniform heating is a pure "photographic enlargement". Stresses arise only from restraint or from temperature gradients.

---

#### Q20 (Crandall Prob 5.18) — Aircraft skin cooled relative to the ribs *(medium)*
**Problem.** An aircraft skin (2024-T4 aluminium) and its stringers are cooled 50°F below the ribs. The skin is free to contract longitudinally (x), but lateral contraction (y) may be constrained by the ribs. Find the stress and strain in the skin for (1) ribs heavy enough to prevent all lateral strain and (2) ribs so light they offer no constraint. Take E = 10.6 × 10⁶ psi, ν = 0.33, α = 12.6 × 10⁻⁶/°F.

**Approach.** Plane stress in the skin (σz = 0), σx = 0 (free longitudinally) and ΔT = −50°F. Case 1 adds εy = 0.

**Solution.**
1. *Case 1 (rigid ribs):* $\epsilon_y = \dfrac{\sigma_y}{E} + \alpha\Delta T = 0$, so $\sigma_y = -E\alpha\Delta T = 10.6\times10^6(12.6\times10^{-6})(50) = 6680$ psi (tension).
   - $\epsilon_x = -\dfrac{\nu\sigma_y}{E} + \alpha\Delta T = -\dfrac{0.33(6680)}{10.6\times10^6} - 630\times10^{-6} = -208\mu - 630\mu = -838\mu$
   - $\epsilon_z$ is the same, −838μ.
2. *Case 2 (no constraint):* no stress; $\epsilon_x = \epsilon_y = \epsilon_z = \alpha\Delta T = -630\mu$.

$$\boxed{\text{Case 1: } \sigma_y = 6.68\ \text{ksi (T)},\ \sigma_x = 0,\ \epsilon_x = -838\mu,\ \epsilon_y = 0;\qquad \text{Case 2: } \sigma = 0,\ \epsilon = -630\mu}$$

**Check.** The constrained skin is pulled sideways by the ribs, and its Poisson contraction adds to the thermal contraction along x ✓.

**Exam takeaway.** Bracketing a real problem between "fully constrained" and "free" limits is good engineering judgment, and Crandall asks for exactly that.

---

#### Q21 (PYQ 2014-15 Test-2 Q3) — Thermo-gate: aluminium and magnesium plates closing a gap *(medium, 20 marks)*
**Problem.** A thermo-gate consists of an aluminium plate AB (600 mm; $E_{al} = 68.9$ GPa, $\alpha_{al} = 24\times10^{-6}$/°C) and a magnesium plate CD (400 mm; $E_{am} = 44.7$ GPa, $\alpha_{am} = 26\times10^{-6}$/°C), each 15 mm wide and 10 mm thick, fixed at their outer ends. The gap between them is 1.5 mm at T₁ = 25°C. Find (a) the temperature that just closes the gap and (b) the axial force in each plate at T₂ = 100°C.

**Approach.** (a) Free expansions add up to the gap. (b) Beyond that, the excess expansion is suppressed by a common compressive force F (equilibrium: the same F in both plates).

**Solution.**
1. *(a)* $(24\times10^{-6}(600) + 26\times10^{-6}(400))\Delta T = 1.5$, so $0.0248\,\Delta T = 1.5$ and ΔT = 60.5°C. Hence T = 85.5°C.
2. *(b)* At ΔT = 75°C the free expansion is 0.0248(75) = 1.86 mm, an excess of 0.36 mm over the gap. With A = 150 mm²:
$$0.36 = F\left(\frac{600}{150(68\,900)} + \frac{400}{150(44\,700)}\right) = F(5.806 + 5.966)\times10^{-5}$$
so F = 3058 N.

$$\boxed{(a)\ T = 85.5^\circ\text{C};\qquad (b)\ F = 3.06\ \text{kN (compression in both plates)},\ \sigma = 20.4\ \text{MPa}}$$

**Check.** The two plates act as springs in series once the gap closes ✓.

**Exam takeaway.** Gap problems have two stages: free expansion until contact, then series springs. **Variation:** find T at which the stress reaches 50 MPa.

---

## Concept 5.5 — Complete equations of elasticity and strain energy

### A. Concept explanation

**1. Intuition.** Every elasticity problem, however complicated, is the three steps of Ch. 2 written for a continuum: forces balance at every point, the deformations fit together, and stress is tied to strain (and temperature) by the material law.

**2. Why it matters.** It shows that the course's methods are complete. The strain-energy density is the basis of Castigliano's theorem (Ch. 2) and of the von Mises criterion (Concept 5.6).

**3. Formal treatment (slides; Crandall §5.6, §5.8).**
- **Equilibrium:** $\dfrac{\partial\sigma_x}{\partial x} + \dfrac{\partial\tau_{xy}}{\partial y} + \dfrac{\partial\tau_{zx}}{\partial z} + X = 0$, and similarly for y and z (X, Y, Z are body forces per unit volume).
- **Geometric compatibility:** $\epsilon_x = \partial u/\partial x$, $\gamma_{xy} = \partial v/\partial x + \partial u/\partial y$, … (6 relations).
- **Stress–strain–temperature:** the generalized Hooke's law with α(T − T₀) (6 relations).

That is 15 equations for 15 unknowns (6 stresses, 6 strains, 3 displacements).

**4. Derivation — strain-energy density.** Work stored per unit volume, for each component $\tfrac12\sigma\epsilon$:
$$u = \tfrac12(\sigma_x\epsilon_x + \sigma_y\epsilon_y + \sigma_z\epsilon_z + \tau_{xy}\gamma_{xy} + \tau_{yz}\gamma_{yz} + \tau_{zx}\gamma_{zx})$$
In principal stresses, substituting Hooke's law:
$$u = \frac{1}{2E}\left[\sigma_1^2 + \sigma_2^2 + \sigma_3^2 - 2\nu(\sigma_1\sigma_2 + \sigma_2\sigma_3 + \sigma_3\sigma_1)\right]$$

**5. Picture.** u is the area under each stress–strain line, ½σε, added over the components.

**6. Special cases.** Uniaxial: $u = \sigma^2/2E$. Pure shear: $u = \tau^2/2G$. Integrating over a bar gives Ch. 2's $U = P^2L/2AE$; over a shaft, Ch. 6's $U = T^2L/2GJ$.

**7. Traps.** Forgetting the ½. Adding energies of separate loads (energy is quadratic: cross terms appear).

**8. Summary.** 15 equations, 15 unknowns; $u = \frac{1}{2E}[\sum\sigma_i^2 - 2\nu\sum\sigma_i\sigma_j]$.

---

## Concept 5.6 — Yield criteria: Tresca (maximum shear stress) and von Mises (distortion energy)

### A. Concept explanation

**1. Intuition.** A tensile test tells you when a material yields under *one* stress. Real parts feel combinations. A yield criterion is a rule that turns any combination into a single "equivalent" number you can compare with the tensile yield strength. Ductile metals yield by **slip** (shear), so both criteria are built on shear-like quantities, and hydrostatic pressure, which causes no slip, cannot cause yield.

**2. Why it matters.** Almost every compre has a "factor of safety by Tresca/von Mises" part (2019, 2021, 2024, 2014).

**3. Formal treatment (slides).**
*Fracture vs yield:* fracture is driven by normal stress (bonds break and cannot reform); yield is driven by shear stress (planes slide and bonds re-form).

**Tresca (maximum shear stress):** yield starts when τmax reaches its value at yield in the tension test, τY = σY/2:
$$\boxed{\sigma_{max} - \sigma_{min} = \sigma_Y}\quad(\text{all three principal stresses, including } \sigma_3 = 0 \text{ in plane stress})$$
Plane-stress cases (slides): σ₁ and σ₂ of **opposite** sign: |σ₁ − σ₂| = σY. **Same** sign: max(|σ₁|, |σ₂|) = σY. The yield surface in the σ₁–σ₂ plane is a **hexagon** (slides: "Tresca yield surface for plane stress problems").

**von Mises (distortion energy):** yield starts when the distortion part of the strain-energy density reaches its value at yield in simple tension:
$$\boxed{\sigma_{vm} = \sqrt{\frac{(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}{2}} \ge \sigma_Y}$$
Plane stress: $\sigma_{vm} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$, an **ellipse** circumscribing the Tresca hexagon (slides: "Von Mises yield surface"). In x–y components: $\sigma_{vm} = \sqrt{\sigma_x^2 - \sigma_x\sigma_y + \sigma_y^2 + 3\tau_{xy}^2}$. A shaft or beam point with only σ and τ: $\sigma_{vm} = \sqrt{\sigma^2 + 3\tau^2}$ and $\sigma_{Tresca} = \sqrt{\sigma^2 + 4\tau^2}$.

**Factor of safety:** $n = \sigma_Y/\sigma_{eq}$.

**4. Derivation of von Mises (slides).** Split each principal stress into a hydrostatic part $\sigma_{av} = (\sigma_1 + \sigma_2 + \sigma_3)/3$ and a distortional part $(\sigma_i - \sigma_{av})$.
- Total energy: $u = \frac{1}{2E}[\sum\sigma_i^2 - 2\nu\sum\sigma_i\sigma_j]$.
- Volume-change energy (replace each σᵢ by σav): $u_v = \frac{3\sigma_{av}^2}{2E}(1 - 2\nu) = \frac{1 - 2\nu}{6E}(\sigma_1 + \sigma_2 + \sigma_3)^2$.
- Distortion energy:
$$u_d = u - u_v = \frac{1 + \nu}{3E}\left[\frac{(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}{2}\right]\quad(1)$$
- In simple tension at yield (σ₁ = σY, σ₂ = σ₃ = 0): $u_{d,Y} = \frac{1 + \nu}{3E}\sigma_Y^2$ … (2).
- Setting (1) = (2) gives the criterion. ∎

*Tresca from Mohr's circle:* the tension-test circle at yield has diameter σY, so τY = σY/2.

**5. Picture.** In the σ₁–σ₂ plane the hexagon (Tresca) sits inside the ellipse (von Mises); they touch at the six points of uniaxial and equal-biaxial stress. The largest gap is in pure shear: Tresca predicts τY = 0.5σY and von Mises τY = σY/√3 = 0.577σY. Test data for steel, copper and nickel lie closer to von Mises.

**6. Special cases.** Tresca is **always conservative** (it predicts yield earlier or at the same point), so its FS ≤ the von Mises FS. If the question asks "will it yield?" and Tresca says no, von Mises says no too.

**7. Common traps.**
- Using the in-plane value (σ₁ − σ₂)/2 for Tresca when both principal stresses have the **same sign**. You must include σ₃ = 0.
- Plugging x–y stresses into $\sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$ without first finding principal stresses (or use the $3\tau^2$ form).
- Using σu instead of σY.

**8. Summary box**

| Criterion | Equivalent stress | Pure-shear yield |
|---|---|---|
| Tresca | σmax − σmin (including σ₃); $\sqrt{\sigma^2 + 4\tau^2}$ for a σ–τ state | 0.5σY |
| von Mises | $\sqrt{\sigma_x^2 - \sigma_x\sigma_y + \sigma_y^2 + 3\tau_{xy}^2}$; $\sqrt{\sigma^2 + 3\tau^2}$ for a σ–τ state | 0.577σY |

### B. Solved questions

#### Q22 (Slides Ch5) — Bolt diameter by Tresca and von Mises *(easy–medium)*
**Problem.** A bolt carries an axial pull of 15 kN together with a shear of 7.5 kN. The material yields at 95 N/mm² in uniaxial tension (ν = 0.3). Find the bolt diameter by (a) Tresca's criterion and (b) the von Mises criterion.

**Approach.** σ = P/A and τ = V/A (average shear), then the σ–τ forms of the criteria. ν is not needed for these two theories (it is for the maximum-principal-strain theory).

**Solution.**
1. *(a) Tresca:* $\dfrac{\sqrt{15^2 + 4(7.5)^2}\times10^3}{A} = \dfrac{21\,213}{A} = 95$, so A = 223.3 mm² and d = 16.9 mm.
2. *(b) von Mises:* $\dfrac{\sqrt{15^2 + 3(7.5)^2}\times10^3}{A} = \dfrac{19\,843}{A} = 95$, so A = 208.9 mm² and d = 16.3 mm.

$$\boxed{d_{Tresca} = 16.9\ \text{mm},\qquad d_{vM} = 16.3\ \text{mm}}$$

**Check.** Tresca is more conservative, so it gives the larger diameter ✓.

**Exam takeaway.** Always say which criterion is conservative. **Variation:** the maximum-principal-strain theory needs ν.

---

#### Q23 (PYQ 2014-15 Compre A Q3) — Tresca with σ₂ = −0.5σ₁ *(easy)*
**Problem.** A zirconium–magnesium alloy (σY = 120 MPa) is subjected to in-plane principal stresses σ₁ and σ₂ = −0.5σ₁. Find σ₁ at yield by Tresca.

**Solution.** The signs are opposite, so σmax − σmin = σ₁ − σ₂ = 1.5σ₁ = 120.

$$\boxed{\sigma_1 = 80\ \text{MPa}}$$

---

#### Q24 (PYQ 2014-15 Compre A Q4) — Does it yield by von Mises? *(easy)*
**Problem.** At a critical point, σx = 140, σy = −80 and τxy = 125 MPa. Yield stress 250 MPa. Does yielding occur (distortion-energy theory)?

**Solution.**
$$\sigma_{vm} = \sqrt{140^2 - (140)(-80) + 80^2 + 3(125)^2} = \sqrt{19\,600 + 11\,200 + 6\,400 + 46\,875} = \sqrt{84\,075} = 290\ \text{MPa}$$

$$\boxed{290 > 250\ \Rightarrow\ \text{yields (FS} = 0.86)}$$

---

#### Q25 (PYQ 2019-20 Compre A Q4) — Factor of safety by Tresca and von Mises *(medium, 7 marks)*
**Problem.** A critical point of a steel machine component carries σx = 60 MPa (T), σy = 35 MPa (T) and τxy = 30 MPa (downward on the right face). σY = 270 MPa. Find the factor of safety by (a) the maximum-shear-stress criterion and (b) the distortion-energy criterion.

**Solution.**
1. *Principal stresses:* centre 47.5, $R = \sqrt{12.5^2 + 30^2} = 32.5$, so σ₁ = 80, σ₂ = 15, σ₃ = 0 MPa.
2. *(a) Tresca:* same sign, so σmax − σmin = 80 − 0 = 80 and n = 270/80 = 3.38.
3. *(b) von Mises:* $\sqrt{80^2 - 80(15) + 15^2} = 73.7$ MPa, so n = 270/73.7 = 3.67.

$$\boxed{n_{Tresca} = 3.38,\qquad n_{vM} = 3.67}$$

**Check.** Using the in-plane value σ₁ − σ₂ = 65 would give n = 4.15. That is wrong (unsafe), because both principal stresses are tensile ✓. $n_{Tresca} < n_{vM}$ ✓.

**Exam takeaway.** The out-of-plane Mohr's circle (σ₁ to σ₃ = 0) is the largest one here.

---

#### PYQs on this concept solved in Ch. 6
- **2021-22 A-Q2(c):** does the axle yield by von Mises? (σ = 140 MPa, τ = 54.4 MPa, σY = 350 MPa): σvm = 169 MPa, so **no** (FS 2.07). See Ch. 6 Q25.
- **2024-25 B-Q2(d):** factor of safety at point B of the post by von Mises. See Ch. 6 Q27.

---

## Chapter 5 — Formula and convention sheet

| Item | Formula |
|---|---|
| Engineering stress/strain | $\sigma = P/A_0$, $\epsilon = \delta/L_0$; true strain $\ln(L/L_0)$; RA = $1 - e^{-\epsilon_t}$ |
| Hooke + Poisson | $\epsilon_x = \frac1E[\sigma_x - \nu(\sigma_y + \sigma_z)] + \alpha\Delta T$ (cyclic), $\gamma = \tau/G$ |
| Plane-stress inverse | $\sigma_x = \frac{E}{1 - \nu^2}(\epsilon_x + \nu\epsilon_y)$, $\epsilon_z = -\frac{\nu}{E}(\sigma_x + \sigma_y)$ |
| Lamé form | $\sigma_x = \lambda e + 2G\epsilon_x$, $\lambda = \frac{\nu E}{(1+\nu)(1-2\nu)}$ |
| Elastic constants | $G = \frac{E}{2(1 + \nu)}$, $K = \frac{E}{3(1 - 2\nu)}$; −1 < ν ≤ ½ |
| Volume change | $\Delta V/V = \epsilon_x + \epsilon_y + \epsilon_z = \frac{1 - 2\nu}{E}\sum\sigma$ |
| Lateral constraint | one direction: factor $1/(1 - \nu^2)$; two directions: $(1 - \nu)/[(1 + \nu)(1 - 2\nu)]$ |
| Thin tank from gauge | axial gauge: $p = 2Et\epsilon_a/[r(1 - 2\nu)]$; tank between walls: $F = \pi r^2p(1 - 2\nu)$ |
| Thermal (fixed ends) | $\sigma = -E\alpha\Delta T$; with a gap, stress only after it closes |
| Composite thermal | equilibrium + equal total deformation; larger α goes into compression |
| Shrink fit | $\Delta d = \alpha d\Delta T$ (holes grow like the material) |
| Energy density | $u = \frac{1}{2E}[\sum\sigma_i^2 - 2\nu\sum\sigma_i\sigma_j]$; uniaxial $\sigma^2/2E$; shear $\tau^2/2G$ |
| Tresca | σmax − σmin = σY (include σ₃ = 0); σ–τ: $\sqrt{\sigma^2 + 4\tau^2}$ |
| von Mises | $\sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$; x–y: $\sqrt{\sigma_x^2 - \sigma_x\sigma_y + \sigma_y^2 + 3\tau^2}$; σ–τ: $\sqrt{\sigma^2 + 3\tau^2}$ |
| Factor of safety | $n = \sigma_Y/\sigma_{eq}$; Tresca n ≤ von Mises n |

**Other Crandall Ch. 5 problems worth practising:** 5.2 (volume strain), 5.5–5.7 (isotropy proofs, inverting Hooke's law), 5.10 (principal strains → stresses, like PYQ 2019 A-Q2), 5.14 (bolted pressure vessel), 5.15–5.16 (rails, clad plates), 5.19 (bridge sun/shade).
