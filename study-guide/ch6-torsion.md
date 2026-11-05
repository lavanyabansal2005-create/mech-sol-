# Chapter 6 — Torsion
### Circular shafts: geometry of deformation, $\tau = Tr/J$, angle of twist, solid vs hollow, stepped shafts, power transmission, gears, statically indeterminate shafts, strain energy, combined torsion + axial/bending, yielding

**Sources used:** Slides "6.pdf" (Chapter 6, Torsion), Crandall Ch. 6 (§6.1–6.5, Figs 6.5–6.14), PYQs 2023-24 (A-Q1; B-Q2), 2024-25 (B-Q1; B-Q2), 2019-20 (B-Q4), 2021-22 (A-Q1; A-Q2), 2014-15 (Test-2 Q1, Q4; Compre A-Q5; Compre B-Q2).

---

## Concept 6.1 — Geometry of deformation of a twisted circular shaft

### A. Concept explanation

**1. Intuition.** Draw straight lines along a rubber hose, then twist it. The lines become helices, but each circular cross-section stays a flat circle and just rotates as a rigid disc, like a stack of coins each turned slightly more than the one below. Points far from the axis move farther, so the shear strain grows **linearly with radius**.

**2. Why it matters.** Drive shafts, axles, turbine–generator couplings, screwdrivers, torsion springs. Torsion appears in **every** compre (6 out of 6 papers in your set).

**3. Formal treatment (Crandall §6.2, slide figs 6.5–6.7).** Use cylindrical coordinates (r, θ, z). Crandall uses $M_t$ for torque, while the slides and Beer use T.
Crandall proves by **symmetry** (not by assumption) that:
1. Each cross-section originally normal to the axis **remains plane and normal**, and **does not distort in its own plane**. (Fig. 6.5: if the section warped, rotating the shaft 180° about a diameter X–X would give a different deformation under the same loading, which is impossible. Fig. 6.6: diameters must stay straight for the same reason.)
2. Radial lines stay straight and radial.

**No dilation** (slide): $\epsilon_r = \epsilon_\theta = \epsilon_z = \gamma_{r\theta} = \gamma_{rz} = 0$. The only deformation is the rotation of sections relative to each other.

**4. Derivation of shear strain (slides, Crandall Fig. 6.8).** Take two sections $\Delta z$ apart that rotate relative to each other by $\Delta\phi$. A surface element at radius r: point E₀ moves to E₁, through an arc $r\Delta\phi$.
$$\gamma_{\theta z} = \lim_{\Delta z\to0}\frac{E_0E_1}{H_1E_0} = \lim\frac{r\Delta\phi}{\Delta z}\ \Rightarrow\ \boxed{\gamma_{\theta z} = r\frac{d\phi}{dz}}$$
$d\phi/dz$ is the **rate of twist** (rad per unit length), the same for all r. So γ varies linearly from 0 at the centre to its maximum at the surface.

**5. Picture.** Draw a lengthwise line on the surface. After twisting it tilts by the angle $\gamma_{max} = r_o\,d\phi/dz$. This is the "helix angle" in slide Fig. 6.x.

**6. Special cases.** These results hold for solid **and** hollow circular sections. They do **not** hold for non-circular sections, which warp.

**7. Traps.** Using $\gamma = \phi$ (twist angle). It is $\gamma = r\phi/L$. γ is dimensionless (radians), φ is an angle of the whole bar.

---

## Concept 6.2 — The torsion formula and the angle of twist

### A. Concept explanation

**1. Intuition.** Material far from the axis is strained more and also has a longer lever arm, so it does most of the work. That is why hollow shafts are efficient: the material near the centre carries little and only adds weight.

**3. Formal treatment / 4. Derivation (slides, Crandall §6.3).**
*Step 1, stress–strain (Hooke in shear):*
$$\tau_{\theta z} = G\gamma_{\theta z} = Gr\frac{d\phi}{dz},\quad \text{all other stresses zero}$$
*Step 2, equilibrium:* the shear stresses on a cross-section must add up to the internal torque.
$$M_t = \int_A r\,(\tau_{\theta z}dA) = G\frac{d\phi}{dz}\int_A r^2dA = G\frac{d\phi}{dz}I_z$$
where $I_z = J = I_P$ is the **polar moment of inertia**:
$$\boxed{J_{solid} = \frac{\pi d^4}{32} = \frac{\pi r^4}{2},\qquad J_{hollow} = \frac{\pi(d_o^4-d_i^4)}{32}}$$
*Step 3, combine:*
$$\frac{d\phi}{dz} = \frac{M_t}{GJ}\qquad\text{and}\qquad \tau_{\theta z} = \frac{M_t\,r}{J}$$
*Step 4, integrate along the length:* $\phi = \int_0^L \frac{M_t}{GJ}dz = \frac{M_tL}{GJ}$ (uniform shaft).
$$\boxed{\frac{T}{J} = \frac{\tau}{r} = \frac{G\phi}{L}}$$
**Maximum (surface) stress for a solid shaft:** $\tau_{max} = \dfrac{Tc}{J} = \boxed{\dfrac{16T}{\pi d^3}}$.
**Hollow shaft:** $\tau_{max} = \dfrac{Td_o/2}{J}$ at the outer surface and $\tau_{min} = \dfrac{Td_i/2}{J}$ at the inner surface ($\tau_{min} = \tau_{max}\,d_i/d_o$).
**Torsional stiffness:** $k_T = T/\phi = GJ/L$. GJ is the torsional rigidity.

**Several segments or varying torque:**
$$\phi_{A/B} = \sum_i\frac{T_iL_i}{G_iJ_i}\quad\text{(with } T_i \text{ the internal torque in segment } i,\ \text{signed)}$$

**Sign convention (slides/Beer):** use the right-hand rule. An internal torque is positive if its vector points **away** from the cut face (outward normal). This is the same "positive face, positive direction" rule as in Ch. 3.

**5. Stress picture.** τ is linear in r on the cross-section (zero at the centre). By $\tau_{xy}=\tau_{yx}$, an equal shear acts on longitudinal planes too. This is why wooden shafts split lengthwise.

**6. Special cases.**
- Thin-walled tube (mean radius $r_m$, thickness t): $J \approx 2\pi r_m^3 t$ and $\tau\approx T/(2\pi r_m^2t)$.
- Same weight: a hollow shaft carries more torque and is stiffer than a solid shaft of the same area (see Q4).

**7. Common traps.**
- Using the radius r = d where it should be d/2.
- Units: T in N·mm with r in mm and J in mm⁴ gives MPa. φ comes out in **radians**; convert to degrees only at the end.
- Using the *external* torque instead of the *internal* torque of the segment. Draw a torque diagram just like an axial force diagram.
- For a hollow shaft, using $\pi d_o^4/32 - \pi d_i^4/32$ is right, but $\pi(d_o-d_i)^4/32$ is wrong.

**8. Summary box**
$$\tau = \frac{Tr}{J},\quad \tau_{max,solid} = \frac{16T}{\pi d^3},\quad \phi = \sum\frac{TL}{GJ},\quad J_s=\frac{\pi d^4}{32},\ J_h = \frac{\pi(d_o^4-d_i^4)}{32}$$

### B. Solved questions

#### Q1 (Slides Ch6, Gere 3.3-x) — Solid steel bar: τ_max, φ, and the allowable torque *(easy)*
**Given:** d = 40 mm, L = 1.3 m, G = 80 GPa. (a) T = 340 N·m. (b) $\tau_{allow} = 42$ MPa and $\phi_{allow} = 2.5^\circ$.
**(a)** $\tau_{max} = \frac{16(340\,000)}{\pi(40)^3} = \boxed{27.1\ \text{MPa}}$. $J = \pi(40)^4/32 = 251\,327$ mm⁴.
$$\phi = \frac{340\,000(1300)}{80\,000(251\,327)} = 0.0220\ \text{rad} = \boxed{1.26^\circ}$$
**(b)** Strength: $T = \tau\pi d^3/16 = 528$ N·m. Stiffness: $T = \phi GJ/L = 0.04363(80\,000)(251\,327)/1300 = 675$ N·m.
$$\boxed{T_{max} = 528\ \text{N·m (stress governs)}}$$
**Takeaway:** always check both strength and stiffness, and report the **smaller** value.

---

#### Q2 (Slides Ch6, Beer 3.x) — Hollow shaft, 40/60 mm *(easy)*
**Given:** L = 1.5 m, $d_i = 40$ mm, $d_o = 60$ mm, $\tau_{allow} = 120$ MPa, G = 77 GPa.
$J = \frac{\pi}{32}(60^4-40^4) = 1.021\times10^6$ mm⁴.
- (a) $T = \tau J/c = 120(1.021\times10^6)/30 = \boxed{4.08\ \text{kN·m}}$
- (b) $\tau_{min} = 120(20/30) = \boxed{80\ \text{MPa}}$
- For φ = 2°: $T = \phi GJ/L = 0.03491(77\,000)(1.021\times10^6)/1500 = \boxed{1.83\ \text{kN·m}}$
- For τ = 70 MPa on the inner surface: $\phi = \tau L/(Gr_i) = 70(1500)/(77\,000\cdot20) = 0.0682$ rad $= \boxed{3.91^\circ}$

---

#### Q3 (Slides Ch6, Gere) — Solid vs hollow tube (same outer R, inner 0.6R) *(medium, conceptual)*
**Given:** the same T, material and length. Compare τ, φ, weight, and strength-to-weight.
$J_h/J_s = 1-0.6^4 = 0.8704$ and $A_h/A_s = 1-0.36 = 0.64$.
- $\tau_h/\tau_s = \phi_h/\phi_s = 1/0.8704 = \boxed{1.15}$
- $W_h/W_s = \boxed{0.64}$
- Strength-to-weight (the torque each can carry at the same $\tau_{allow}$, divided by weight): hollow/solid $= 0.8704/0.64 = \boxed{1.36}$

The hollow shaft is 36% more efficient.

---

#### Q4 (Slides Ch6, Gere 3.x) — Design: solid vs hollow for 1200 N·m *(medium)*
**Given:** T = 1200 N·m, $\tau_{allow} = 40$ MPa, rate of twist ≤ 0.75°/m, G = 78 GPa. Hollow: $t = d_2/10$, so $d_1 = 0.8d_2$.
Rate limit: $\theta = 0.75^\circ/\text{m} = 1.309\times10^{-5}$ rad/mm.
- **(a) Solid.** Strength: $d^3 = 16T/(\pi\tau)$ gives $d = 53.5$ mm. Stiffness: $d^4 = 32T/(\pi G\theta)$ gives $d = 58.8$ mm. So $\boxed{d_0 = 58.8\ \text{mm}}$.
- **(b) Hollow** ($J = \frac{\pi d_2^4}{32}(0.5904)$). Strength gives 63.7 mm. Stiffness gives 67.1 mm. So $\boxed{d_2 = 67.1\ \text{mm}}$.
- **(c)** $d_2/d_0 = \boxed{1.14}$. Weight ratio $= \frac{d_2^2(1-0.64)}{d_0^2} = \boxed{0.47}$.

---

#### Q5 (Slides Ch6, Beer Sample 3.1) — Four-gear shaft: BC hollow, size AB and CD *(medium)*
**Given:** $T_A = 6$, $T_B = 14$, $T_C = 26$, $T_D = 6$ kN·m (balanced). BC: $d_i = 90$ mm, $d_o = 120$ mm. $\tau_{allow} = 65$ MPa in AB and CD.
Internal torques: $T_{AB} = 6$ kN·m and $T_{BC} = 6+14 = 20$ kN·m. $T_{CD} = 6$ kN·m (check: 20 − 26 = −6 ✓).
$J_{BC} = \frac{\pi}{32}(120^4-90^4) = 13.92\times10^6$ mm⁴.
$$\boxed{\tau_{max,BC} = \frac{20\times10^6(60)}{13.92\times10^6} = 86.2\ \text{MPa},\quad \tau_{min,BC} = 64.7\ \text{MPa}}$$
$$d = \left(\frac{16(6\times10^6)}{\pi(65)}\right)^{1/3} = \boxed{77.8\ \text{mm}}\ ✓\ \text{(slide)}$$

---

#### Q6 (Slides Ch6, Beer 3.x) — Hollow 4 in/6 in, 12 ksi; equal-weight comparisons *(medium)*
- (a) As designed: $J = \frac{\pi}{32}(6^4-4^4) = 102.1$ in⁴, so $T = 12(102.1)/3 = \boxed{408\ \text{kip·in}}$
- (b) Solid shaft of the same weight (same area $5\pi$ in²): $d = 4.47$ in, so $T = 12\pi d^3/16 = \boxed{211\ \text{kip·in}}$
- (c) Hollow shaft of the same weight with $d_o = 8$ in: $d_i^2 = 64-20 = 44$, so $d_i = 6.63$ in. $T = 12\frac{\pi(8^4-6.63^4)}{32}/4 = \boxed{636\ \text{kip·in}}$

**Lesson:** for the same material, moving it outward gives more torque capacity: 211 → 408 → 636.

---

#### Q7 (Slides Ch6, Beer 3.x) — Stepped hollow/solid shaft AD: twist at A *(medium)*
**Given:** fixed at D. AB solid, 30 mm, 0.4 m, with 250 N·m at A. BC solid, 60 mm, 0.2 m. CD is 60 mm with a 44 mm bore, 0.6 m. 2000 N·m at B. G = 77 GPa.
Internal: $T_{AB} = 250$ N·m and $T_{BC} = T_{CD} = 2250$ N·m (same sense).
$$\phi_A = \frac{1}{G}\left[\frac{250e3(400)}{\frac{\pi}{32}30^4} + \frac{2250e3(200)}{\frac{\pi}{32}60^4} + \frac{2250e3(600)}{\frac{\pi}{32}(60^4-44^4)}\right] = 0.0403\ \text{rad} = \boxed{2.31^\circ}$$
(The three terms are 0.0163, 0.00459 and 0.0194 rad.)

---

#### Q8 (Slides Ch6, Gere) — Two-segment solid shaft vs equivalent hollow shaft *(medium)*
**Given:** solid shaft with 80 mm × 1.2 m and 60 mm × 0.9 m. Hollow shaft 2.1 m long with $t = d/10$ ($d_i = 0.8d$). Equal torsional stiffness.
$$\phi_1 = \frac{32T}{\pi G}\left[\frac{1.2}{0.08^4}+\frac{0.9}{0.06^4}\right] = \frac{32T}{\pi G}(98\,741\ \text{m}^{-3}),\qquad \phi_2 = \frac{32T}{\pi G}\frac{2.1}{0.5904\,d^4}$$
Setting $\phi_1 = \phi_2$ gives $d^4 = 3.5569/98\,741$, so
$$\boxed{d = 77.5\ \text{mm}}$$

---

#### Q9 (Slides Ch6, Gere) — Truck drive shaft: power ↔ torque *(easy)*
$$\boxed{P = T\omega = \frac{2\pi nT}{60}}\quad(n\ \text{in rpm},\ P\ \text{in W},\ T\ \text{in N·m})$$
**Given:** $d_o = 60$ mm, $d_i = 40$ mm, n = 2500 rpm.
- (a) 150 kW: $T = 60(150\,000)/(2\pi\cdot2500) = 573$ N·m, so $\tau = 573\,000(30)/1.021\times10^6 = \boxed{16.8\ \text{MPa}}$
- (b) $\tau_{allow} = 30$ MPa: $P = 150(30/16.835) = \boxed{267\ \text{kW}}$

**Trap:** P = Tω needs ω in rad/s, **not** rpm.

---

#### Q10 (Slides Ch6, Gere) — Aluminium tube, shear strain at the inner surface *(easy)*
**Given:** $r_2 = 1.5r_1$, $\gamma_{max} = 400\times10^{-6}$. Since γ ∝ r:
$$\gamma_1 = \gamma_{max}\frac{r_1}{r_2} = \boxed{267\times10^{-6}}$$
(b) Rate of twist ≤ 0.125°/ft $= 1.818\times10^{-4}$ rad/in (as on the slide) and $\gamma = r\theta$, so $r_{2,min} = \gamma_{max}/\theta = \boxed{2.2\ \text{in}}$.

---

#### Q11 (Slides Ch6, Gere; also PYQ 2021-22 A Q1) — Strain gauge at 45° gives G *(easy)*
Slide: d = 50 mm, T = 500 N·m, ε = 339μ. So $\tau = 20.37$ MPa, $\gamma = 2\epsilon = 678\mu$, and $G = \boxed{30.0\ \text{GPa}}$.
PYQ 2021 (same bar, ε = 350μ): $\boxed{G = 29.1\ \text{GPa}}$. Full solution in Ch. 4 Q13.

---

#### Q12 (PYQ 2014-15 Compre A Q5) — Size a shaft *(easy)*
T = 205 N·m and $\tau_{allow} = 100$ MPa:
$$d = \left(\frac{16(205\,000)}{\pi(100)}\right)^{1/3} = \boxed{21.9\ \text{mm}}$$

---

#### Q13 (PYQ 2014-15 Test-2 Q4) — Axle of tubes + solid section *(easy–medium, 20 marks)*
**Given:** tubes AB and CD with $d_o = 30$ mm and $d_i = 20$ mm. Solid BC, 40 mm, 250 mm long. Gears at the ends carry 85 N·m. G = 75 GPa. Smooth bearings, so the internal torque is 85 N·m everywhere.
$J_{tube} = \frac{\pi}{32}(30^4-20^4) = 63\,814$ mm⁴.
$$\boxed{\tau_{max,tube} = \frac{85\,000(15)}{63\,814} = 20.0\ \text{MPa},\quad \tau_{min} = 13.3\ \text{MPa}}$$
$$\phi_{B/C} = \frac{85\,000(250)}{75\,000\cdot\frac{\pi}{32}(40)^4} = 1.13\times10^{-3}\ \text{rad} = \boxed{0.0646^\circ}$$

---

#### Q14 (PYQ 2023-24 A Q1) — Shaft with three disks: allowable T and twist A relative to C *(medium, 10 marks)*
**Given:** 60 mm solid aluminium shaft, $\tau_{allow} = 80$ MPa, G = 26 GPa. Disks: A carries $\tfrac23T$, B carries T (opposite sense), C carries $\tfrac13T$. AB = BC = 1.20 m. Smooth bearings.
**Internal torques:** $T_{AB} = \tfrac23T$ and $T_{BC} = \tfrac23T - T = -\tfrac13T$. The maximum is in AB.
**(a)** $\tfrac23T = \tau\pi d^3/16 = 80\pi(60)^3/16 = 3.393$ kN·m, so $\boxed{T = 5.09\ \text{kN·m}}$.
**(b)** $\boxed{T_{AB} = 3.39\ \text{kN·m},\quad T_{BC} = 1.70\ \text{kN·m (opposite sense)}}$
**(c)** $J = \pi(60)^4/32 = 1.272\times10^6$ mm⁴, $GJ = 3.308\times10^{10}$ N·mm².
$$\phi_{A/C} = \frac{(T_{AB}+T_{BC})L}{GJ} = \frac{(3.393-1.696)\times10^6(1200)}{3.308\times10^{10}} = 0.0615\ \text{rad} = \boxed{3.53^\circ}$$
**Takeaway:** opposite-signed segments partly cancel. Students who add magnitudes get 10.6°.

---

## Concept 6.3 — Gears and coupled shafts

### A. Concept explanation

**1. Intuition.** Two meshing gears share one tooth force F. The bigger gear gets a bigger torque ($T = Fr$) but turns through a smaller angle. The contact point moves the same arc length on both: $r_B\phi_B = r_C\phi_C$.

**3. Formal treatment (slides, Beer Sample 3.4).**
- **Statics:** $F = T_B/r_B = T_C/r_C$, so $T_C = T_B(r_C/r_B)$.
- **Kinematics:** $r_B\phi_B = r_C\phi_C$ (equal arc at the contact).
- **Twist of the free end:** $\phi_A = \phi_B + \phi_{A/B}$, where $\phi_B$ comes from the *other* shaft's twist through the gear ratio.

**7. Traps.** Using the gear ratio the wrong way (torque scales with r, rotation with 1/r). Forgetting that the free shaft's end rotation includes the gear's rotation, not just its own twist.

### B. Solved questions

#### Q15 (Slides Ch6, Beer Sample 3.4) — Two shafts with gears: largest $T_0$ and rotation of A *(medium)*
**Given:** AB: 0.75 in diameter, 24 in long, gear B $r_B = 0.875$ in. CD: 1 in diameter, 36 in long, fixed at D, gear C $r_C = 2.45$ in. G = 11.2 × 10⁶ psi, $\tau_{allow} = 8$ ksi.
**Statics:** $T_{CD} = 2.8T_0$. **Kinematics:** $\phi_B = 2.8\phi_C$.
- AB: $T_0 = 8000\cdot\frac{\pi}{2}(0.375)^3 = 663$ lb·in
- CD: $2.8T_0 = 8000\cdot\frac{\pi}{2}(0.5)^3$, so $T_0 = 561$ lb·in

$$\boxed{T_0 = 561\ \text{lb·in}}$$
Twists: $\phi_{A/B} = 2.22^\circ$, $\phi_C = 2.95^\circ$, $\phi_B = 2.8(2.95) = 8.26^\circ$.
$$\boxed{\phi_A = 8.26 + 2.22 = 10.48^\circ}$$

---

#### Q16 (Slides Ch6) — Find $\phi_E$ (gear-coupled shafts, symbolic) *(medium)*
Shaft AD is fixed at D and carries gear A ($r_A$). Shaft BE carries gear B ($r_B$) and torque T at E. Both have length L and rigidity GJ.
Statics: $T_{AD} = T\,r_A/r_B$. $\phi_A = \frac{T r_A L}{r_B GJ}$, so $\phi_B = \frac{r_A}{r_B}\phi_A = \frac{r_A^2}{r_B^2}\frac{TL}{GJ}$.
$$\boxed{\phi_E = \frac{TL}{GJ}\left(1 + \frac{r_A^2}{r_B^2}\right)}$$

---

#### Q17 (PYQ 2014-15 Compre B Q2) — Coupled shafts: twist of A relative to D *(medium, 15 marks)*
**Given:** T = 45 N·m at A. AB is 2 m long and free in bearings E, F, with gear B ($r_B = 150$ mm). DC is 1.5 m long, fixed at D, with gear C ($r_C = 75$ mm). Both shafts 20 mm diameter, G = 80 GPa.
$J = \pi(20)^4/32 = 15\,708$ mm⁴, $GJ = 1.2566\times10^9$ N·mm².
- Tooth force $F = 45\,000/150 = 300$ N, so $T_{DC} = 300(75) = 22.5$ N·m.
- $\phi_C = \frac{22\,500(1500)}{1.2566\times10^9} = 0.02686$ rad
- Kinematics: $\phi_B = \phi_C\frac{r_C}{r_B} = 0.01343$ rad
- $\phi_{A/B} = \frac{45\,000(2000)}{1.2566\times10^9} = 0.07162$ rad

$$\boxed{\phi_{A/D} = 0.01343 + 0.07162 = 0.0850\ \text{rad} = 4.87^\circ}$$

---

#### Q18 (PYQ 2019-20 B Q4) — Gear-coupled shafts: find $T_1$, $T_2$ for 0.05 rad at A and C *(hard, 12 marks)*
**Given:** ABC is 60 mm diameter on journal bearings, with gear B ($r_B = 75$ mm). AB = 600 mm and BC = 900 mm, with $T_2$ at A and $T_1$ at C (same sense). EH is 80 mm, fixed at E, with gear D ($r_D = 100$ mm) at 600 mm from E. G = 80 GPa. $\phi_A = \phi_C = 0.05$ rad.
$GJ_1 = 80\,000\cdot\frac{\pi}{32}(60)^4 = 1.018\times10^{11}$ and $GJ_2 = 80\,000\cdot\frac{\pi}{32}(80)^4 = 3.217\times10^{11}$ N·mm². Gear ratio $n = r_D/r_B = 4/3$.
- **Statics:** shaft ABC is in equilibrium, so gear B carries $T_B = T_1 + T_2$ and gear D gets $T_D = n(T_1+T_2)$.
- **Shaft EH:** $\phi_D = \frac{n(T_1+T_2)(600)}{GJ_2}$. **Gear kinematics:** $\phi_B = n\phi_D$.
- **Shaft ABC:** $\phi_A = \phi_B + \frac{T_2(600)}{GJ_1}$ and $\phi_C = \phi_B + \frac{T_1(900)}{GJ_1}$.

Setting $\phi_A = \phi_C$ gives $600T_2 = 900T_1$, so $T_2 = 1.5T_1$. Then
$$\frac{(16/9)(2.5T_1)(600)}{3.217\times10^{11}} + \frac{1.5T_1(600)}{1.018\times10^{11}} = 0.05 \Rightarrow T_1(8.29+8.84)\times10^{-9} = 0.05$$
$$\boxed{T_1 = 2.92\ \text{kN·m},\qquad T_2 = 4.38\ \text{kN·m}}$$
**Check:** $\phi_B = 0.0242$ rad. $\phi_A = 0.0242 + 4.38e6(600)/1.018e11 = 0.0500$ ✓.

---

## Concept 6.4 — Statically indeterminate shafts

### A. Concept explanation

**1. Intuition.** A shaft clamped at both ends with a torque in the middle: both walls resist, and statics gives only $T_A + T_D = T$. The extra fact is that **the total twist between the walls is zero**. It is the exact twin of the axially loaded bar fixed at both ends (Ch. 2).

**3–4. Method (the three steps of Ch. 2):**
1. Equilibrium: $T_A + T_D = \sum T_{applied}$.
2. Compatibility: $\phi_{A/D} = \sum\frac{T_iL_i}{GJ_i} = 0$.
3. Torque–twist: $\phi = TL/GJ$.

**Single torque $T_0$ at distance a from A (b from D), uniform GJ:**
$$\boxed{T_A = T_0\frac{b}{L},\qquad T_D = T_0\frac{a}{L}}$$
(The nearer wall carries more, as with axial bars.)
**Strain energy:** $U = \sum\frac{T_i^2L_i}{2GJ_i}$ (slide: $U = \int\frac{M_t^2}{2GI_z}dz$).

### B. Solved questions

#### Q19 (Slides Ch6, Crandall Example 6.x) — Fixed–fixed shaft: rotation of point O *(medium)*
**Given:** 25 mm aluminium, G = 26.5 GPa. A and C are built in. $M_B = 70$ N·m at B, with AB = 0.6 m and BC = 1.8 m. O is 1.2 m from C.
$T_A = 70(1.8/2.4) = 52.5$ N·m and $T_C = 17.5$ N·m. Segment OC carries 17.5 N·m.
$$\phi_O = \frac{17\,500(1200)}{26\,500\cdot\frac{\pi}{32}(25)^4} = 0.02066\ \text{rad} = \boxed{1.18^\circ}$$
**Check from the A side:** $\phi_B = 52\,500(600)/GJ = 0.0310$ rad. Then O, 0.6 m beyond B, is reduced by $17\,500(600)/GJ = 0.0103$, giving 0.0207 ✓.

---

#### Q20 (PYQ 2024-25 B Q1) — Fixed–fixed bar with two torques: reactions, max twist, strain energy *(medium, 12 marks)*
**Given:** d = 40 mm. A and D are fixed. $T_0 = 800$ N·m at B ($x = 0.3L$) and $2T_0$ at C ($x = 0.6L$), same sense. L = 1.2 m, G = 80 GPa.
$J = 251\,327$ mm⁴, $GJ = 2.0106\times10^{10}$ N·mm².
**(a) Reactions** (superposition of single-torque results):
$$T_A = T_0\frac{0.7L}{L} + 2T_0\frac{0.4L}{L} = 1.5T_0 = \boxed{1200\ \text{N·m}},\qquad T_D = 3T_0 - 1.5T_0 = \boxed{1200\ \text{N·m}}$$
(Both opposite to the applied torques.)
**Internal torques:** $T_{AB} = 1200$, $T_{BC} = 1200-800 = 400$ and $T_{CD} = 400-1600 = -1200$ N·m.
**Compatibility check:** $1200(360)+400(360)-1200(480) = 0$ ✓.
**(b) Twist:** $\phi_B = \frac{1200e3(360)}{2.0106e10} = 0.02149$ rad $= 1.23^\circ$ and $\phi_C = \phi_B + \frac{400e3(360)}{2.0106e10} = 0.02865$ rad.
$$\boxed{\phi_{max} = 1.64^\circ\ \text{at C}}$$
**(c) Strain energy:**
$$U = \frac{1}{2GJ}\left[1200^2(0.36)+400^2(0.36)+1200^2(0.48)\right]\times10^9\ \text{N·mm} = \boxed{31.5\ \text{J}}$$
**Takeaway:** the maximum twist is at a loading point where the internal torque changes sign, just as the maximum deflection in a beam occurs where the slope is zero.

---

## Concept 6.5 — Combined stresses: torsion + axial + bending; yielding of shafts

### A. Concept explanation

**1. Intuition.** Real shafts are rarely just twisted. A propeller shaft is twisted and pushed, and a crank is twisted and bent. At a point on the surface you get a normal stress σ (from axial force and bending) **plus** a shear stress τ (from torque and transverse shear). Put them on one small square element, then use Mohr's circle (Ch. 4) and a yield criterion (Ch. 5).

**2. Why it matters.** This is **the single most-repeated long question** in the compre papers (2019 B-Q2, 2021 A-Q2, 2023 B-Q2, 2024 B-Q2, 2021 B-Q4, 2014 Test-2 Q1), usually 15–20 marks.

**3. Formal treatment (slides, Crandall §6.5, Fig. 6.14).**
*Pure torsion:* the surface element is in **pure shear** τ. The principal stresses are ±τ, acting at **45°** to the axis. Brittle shafts (chalk!) break on a 45° helix (maximum tension), while ductile shafts shear off on a cross-section (maximum shear).
*Torsion + axial P:* $\sigma = P/A$ and $\tau = Tc/J$.
$$\sigma_{1,2} = \frac{\sigma}{2}\pm\sqrt{\left(\frac{\sigma}{2}\right)^2+\tau^2},\qquad \tau_{max} = \sqrt{\left(\frac{\sigma}{2}\right)^2+\tau^2}$$
*Yield (slides):* von Mises gives $\sqrt{\sigma^2+3\tau^2}=Y$ and Tresca gives $\sqrt{\sigma^2+4\tau^2} = Y$.
*Torsion + bending (solid shaft):* $\sigma_b = \frac{32M}{\pi d^3}$ and $\tau = \frac{16T}{\pi d^3}$.
$$\tau_{max} = \frac{16}{\pi d^3}\sqrt{M^2+T^2},\qquad \sigma_1 = \frac{16}{\pi d^3}\left(M+\sqrt{M^2+T^2}\right)$$
These are the "equivalent torque" and "equivalent moment" formulas.

**General procedure for combined-loading PYQs:**
1. FBD of the whole member, then reactions (Ch. 1).
2. Cut at the section and find $F$, $V$, $M_b$, $T$ (Ch. 3, 3-D vectors $\mathbf M = \mathbf r\times\mathbf F$).
3. At the requested surface point:
   - $\sigma = F/A \pm M_bc/I$ (bending stress is zero at the neutral axis; I = πd⁴/64)
   - $\tau = Tc/J \pm$ transverse shear ($\tau_V = \frac{4V}{3A}$ at the neutral axis of a solid circle, 0 at the extreme fibre)
4. Draw the 2-D element with correct directions.
5. Mohr's circle gives principal stresses and $\tau_{max}$ (Ch. 4).
6. Yield criterion gives the FS (Ch. 5).

**7. Traps.**
- Putting the maximum bending stress and the maximum transverse shear at the same point. They occur 90° apart.
- Using J where I is needed: $I = J/2$ for a circle.
- Forgetting that the transverse shear and torsion shear add on one side and subtract on the other.
- Using $\tau_{max}=R$ for Tresca when both principal stresses have the same sign. That can't happen here, because pure σ–τ states always have principal stresses of opposite sign. ✓

### B. Solved questions

#### Q21 (Slides Ch6, Beer 7.x) — Torque for yield by Tresca with P = 240 kN *(medium)*
**Given:** d = 38 mm, Y = 250 MPa, P = 240 kN.
$\sigma = 240\,000/1134.1 = 211.6$ MPa. Tresca: $\sqrt{\sigma^2+4\tau^2} = Y$, so $\tau = \tfrac12\sqrt{250^2-211.6^2} = 66.6$ MPa.
$$T = \frac{\tau\pi d^3}{16} = \boxed{717\ \text{N·m}}$$

---

#### Q22 (Slides Ch6, Hibbeler) — Helicopter rotor shaft *(easy)*
**Given:** d = 50 mm, T = 2.4 kN·m, P = 125 kN.
$\sigma = 63.66$ MPa and $\tau = 16(2.4e6)/(\pi\cdot50^3) = 97.78$ MPa.
$$\boxed{\sigma_1 = 134.7\ \text{MPa},\quad \sigma_2 = -71.0\ \text{MPa},\quad \tau_{max} = 102.8\ \text{MPa}}$$

---

#### Q23 (PYQ 2014-15 Test-2 Q1) — Axial + torque, principal stresses
Solved in Ch. 4 Q8: σ₁ = 76.8 MPa, σ₂ = −5.2 MPa, θₚ = 14.5° from the axis.

---

#### Q24 (PYQ 2021-22 A Q2) — Automobile axle: stress at H, principal stresses, von Mises *(medium, 10 marks)*
**Given:** solid axle d = 32 mm. At the wheel end: 3 kN ↑ and a 350 N·m torque. 3 kN ↓ at 0.15 m from the wheel. H is on top, 0.2 m beyond the 3 kN ↓ load. $\sigma_Y = 350$ MPa.
**Internal forces at H** (from the wheel side): $V = 3-3 = 0$ (no transverse shear), $M = 3(0.35)-3(0.20) = 0.45$ kN·m (the two 3 kN forces form a constant couple beyond the second load), T = 350 N·m.
**(a) Stresses at H (top fibre):**
$$\sigma = \frac{32M}{\pi d^3} = \frac{32(450\,000)}{\pi(32)^3} = 139.9\ \text{MPa (compression at the top: sagging)},\qquad \tau = \frac{16(350\,000)}{\pi(32)^3} = 54.4\ \text{MPa}$$
**(b) Principal:** centre −69.9 and R = 88.6, so
$$\boxed{\sigma_1 = 18.7\ \text{MPa},\quad \sigma_2 = -158.5\ \text{MPa},\quad \tau_{max} = 88.6\ \text{MPa}}$$
**(c) von Mises:**
$$\sigma_{vm} = \sqrt{139.9^2+3(54.4)^2} = 168.7\ \text{MPa} < 350\ \Rightarrow\ \boxed{\text{No yield (FS} = 2.07)}$$

---

#### Q25 (PYQ 2023-24 B Q2) — Crank on a 20 mm shaft: reactions, elements E₁ and E₂ *(hard, 20 marks)*
**Given (from the figure):** shaft AB, 20 mm diameter, 125 mm long along x from the wall at A. Crank arm BC is 100 mm long (6 mm × 30 mm section). The pin at C is parallel to x, and F = 2 kN acts downward (−y) at 38 mm along the pin. **Assumption:** the load point is at x = 125 + 38 = 163 mm from A and offset 100 mm in z.
**(a) Reactions at A:** $R_y = +2$ kN. Twisting moment $T = F(100) = 200$ N·m. Bending moment $M_z = F(163) = 326$ N·m (hogging: top in tension).
**(b) Stresses at A:**
- $\sigma_b = \frac{32(326\,000)}{\pi(20)^3} = 415$ MPa
- $\tau_T = \frac{16(200\,000)}{\pi(20)^3} = 127.3$ MPa
- $\tau_V = \frac{4(2000)}{3\pi(100)} = 8.5$ MPa

| Element | σ_x | τ |
|---|---|---|
| E₁ (top, on y-axis) | +415 MPa (tension) | 127.3 MPa (torsion only; transverse shear is 0 at the top) |
| E₂ (side, on z-axis = neutral axis) | 0 | 127.3 + 8.5 = 135.8 MPa (they add on this side; they subtract to 118.8 MPa on the opposite side) |

**(c) 2-D elements:** E₁ is viewed from +y, with σ along x and τ on the x-faces in the z direction. E₂ is viewed from +z, with τ on the x-faces in the y direction.
**(d) At E₁:** centre 207.5 and R = $\sqrt{207.5^2+127.3^2} = 243.5$, so
$$\boxed{\sigma_{max} = 451\ \text{MPa},\quad \sigma_{min} = -35.9\ \text{MPa},\quad \tau_{max} = 243.5\ \text{MPa}}$$
**Takeaway:** the examiner tests that you know *where* each stress is maximum. Bending peaks at E₁, transverse shear peaks at E₂, and torsion is the same at both.

---

#### Q26 (PYQ 2024-25 B Q2) — L-shaped post: F, V, M_b, T at z–z; stresses at B; principal stresses; von Mises FS *(hard, 18 marks)*
**Given:** 50 mm post, vertical axis x. A horizontal arm of 0.4 m (along z) is at the top. At the arm's free end, $P = 400\pi$ N (horizontal, along −y) and $R = 800\pi$ N (downward). Section z–z is 0.6 m below the free end. B is on the surface where the diameter along z meets it. $\sigma_Y = 140$ MPa.
**Interpretation:** this reads the figure with the arm along z and P along −y. If your figure differs, rerun the same steps.
**(a) Section forces** ($\mathbf M = \mathbf r\times\mathbf F$ with $\mathbf r = (0.6, 0, 0.4)$ m and $\mathbf F = (-800\pi, -400\pi, 0)$ N):
- Axial $F = -800\pi = -2513$ N (compression)
- Shear $V = 400\pi = 1257$ N (y-direction)
- $\mathbf M = (160\pi, -320\pi, -240\pi)$ N·m, so the twisting moment is $T = 160\pi = 502.7$ N·m, and the bending moments are $M_y = 320\pi = 1005$ N·m and $M_z = 240\pi = 754$ N·m (resultant $M_b = 400\pi = 1257$ N·m)

**(b) Stresses at B** (on the z-axis, so only $M_y$ bends B; B is on the neutral axis of $M_z$, where the y-shear peaks). $A = 625\pi$ mm² and $\frac{\pi d^3}{32} = 3906\pi$ mm³. The π's cancel, which is why they're in the data.
- $\sigma_{axial} = -\frac{800\pi}{625\pi} = -1.28$ MPa
- $\sigma_{bend} = -\frac{320\pi\times10^3}{3906\pi} = -81.92$ MPa (the downward R on the +z arm compresses the +z side)
- $\tau_{T} = \frac{160\pi\times10^3}{7812\pi} = 20.48$ MPa
- $\tau_{V} = \frac{4V}{3A} = 0.853$ MPa (adds to torsion at B)

$$\boxed{\sigma_x = -83.2\ \text{MPa},\quad \tau = 21.3\ \text{MPa}}$$
**(c) Principal:** centre −41.6 and R = 46.75, so
$$\boxed{\sigma_1 = 5.15\ \text{MPa},\quad \sigma_2 = -88.35\ \text{MPa},\quad \tau_{max} = 46.75\ \text{MPa}}$$
**(d) von Mises:**
$$\sigma_{vm} = \sqrt{83.2^2+3(21.3)^2} = 91.0\ \text{MPa}\ \Rightarrow\ \boxed{FS = 140/91.0 = 1.54}$$

---

## Chapter 6 — Formula and convention sheet

| Item | Formula |
|---|---|
| Kinematics | sections stay plane and undistorted; $\gamma = r\,d\phi/dz$ |
| Torsion formula | $T/J = \tau/r = G\phi/L$ |
| Solid | $J=\pi d^4/32$; $\tau_{max} = 16T/\pi d^3$ |
| Hollow | $J=\pi(d_o^4-d_i^4)/32$; $\tau_{min}=\tau_{max}d_i/d_o$ |
| Thin tube | $J\approx2\pi r_m^3t$ |
| Twist | $\phi = \sum T_iL_i/(G_iJ_i)$ with **internal** signed torques |
| Stiffness | $k_T = GJ/L$ |
| Power | $P = T\omega = 2\pi nT/60$ (n in rpm) |
| Gears | $T_C/T_B = r_C/r_B$; $r_B\phi_B = r_C\phi_C$ |
| Fixed–fixed, one torque | $T_A = T_0b/L$, $T_D = T_0a/L$ |
| Energy | $U = \sum T^2L/(2GJ)$ |
| Pure torsion element | principal ±τ at 45°; gauge at 45° reads γ/2 |
| Combined σ + τ | $\sigma_{1,2}=\sigma/2\pm\sqrt{(\sigma/2)^2+\tau^2}$; vM $\sqrt{\sigma^2+3\tau^2}$; Tresca $\sqrt{\sigma^2+4\tau^2}$ |
| Bending + torsion (solid) | $\tau_{max}=\frac{16}{\pi d^3}\sqrt{M^2+T^2}$, $\sigma_1=\frac{16}{\pi d^3}(M+\sqrt{M^2+T^2})$ |
| Transverse shear (solid circle) | $\tau_{V,max} = 4V/3A$ at the neutral axis |

**Other Crandall Ch. 6 problems worth practising:** 6.1–6.10 (basic shafts, power), 6.11–6.20 (indeterminate and composite shafts), 6.25+ (combined stresses, yield).
