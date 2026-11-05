# Chapter 6 — Torsion
### Circular shafts: geometry of deformation, $\tau = Tr/J$, angle of twist, solid vs hollow, power transmission, gears, statically indeterminate shafts, strain energy, combined torsion + axial/bending, yielding

**Sources used:** Slides "6.pdf" (Chapter 6, Torsion); Crandall Ch. 6 (§6.1–6.5, Figs 6.5–6.14; the uploaded textbook PDF ends before this chapter's problem set, so the solved problems here come from the slides and PYQs); PYQs 2023-24 (A-Q1; B-Q2), 2024-25 (B-Q1; B-Q2), 2019-20 (B-Q4), 2021-22 (A-Q1; A-Q2), 2014-15 (Test-2 Q1, Q4; Compre A-Q5; Compre B-Q2).

**Layout.** Part A (eight items) for each concept, then Part B: slides → PYQs, easy → hard. Each solution follows *Problem · Given/Find · Approach · Sketch · Steps · Answer · Check · Takeaway*.

---

## Concept 6.1 — Geometry of deformation of a twisted circular shaft

### A. Concept explanation

**1. Intuition.** Draw straight lines along a rubber hose, then twist it. The lines become helices, but each circular cross-section stays a flat circle and simply rotates as a rigid disc, like a stack of coins each turned slightly more than the one below. Points far from the axis move farther, so the shear strain grows **linearly with radius**.

**2. Why it matters.** Drive shafts, axles, turbine–generator couplings (slide: "turbine exerts torque T on the shaft; the shaft transmits it to the generator; the generator creates an equal and opposite torque T′"), screwdrivers, torsion bars. Torsion appears in **every** compre in your set. The slide's design aim: "we are interested primarily in the twisting moment which can be transmitted by the shaft without damage to the material".

**3. Formal treatment (Crandall §6.2; slide figures 6.5–6.7).** Use cylindrical coordinates (r, θ, z). Crandall uses $M_t$ for torque; the slides and Beer use T. Crandall proves by **symmetry** (not by assumption) that:
1. Each cross-section originally normal to the axis **remains plane and normal**, and **does not distort in its own plane**. (Fig. 6.5: if the section warped, rotating the shaft 180° about a diameter X–X would give a different deformation under the same loading, which is impossible. Fig. 6.6/6.7: diameters must stay straight for the same reason.)
2. Radial lines stay straight and radial.

**No dilation (slides):** $\epsilon_r = \epsilon_\theta = \epsilon_z = \gamma_{r\theta} = \gamma_{rz} = 0$. "The only remaining possible mode of deformation is one in which the cross sections of the shaft remain undeformed but rotate relative to each other."

**4. Derivation of the shear strain (slides; Crandall Fig. 6.8).** Two sections Δz apart rotate relative to each other by Δφ. On the surface element at radius r, point E₀ moves to E₁ through an arc rΔφ:
$$\gamma_{\theta z} = \lim_{\Delta z\to0}\frac{E_0E_1}{H_1E_0} = \lim_{\Delta z\to0}\frac{r\Delta\phi}{\Delta z}\ \Rightarrow\ \boxed{\gamma_{\theta z} = r\frac{d\phi}{dz}}$$
dφ/dz is the **rate of twist** (rad per unit length), the same for all r. So γ varies linearly from 0 at the centre to its maximum at the surface.

**5. Picture.** A line drawn along the surface tilts by $\gamma_{max} = r_o\,d\phi/dz$ after twisting: the "helix angle" in the slide figure. Section circles stay circles; radii stay straight.

**6. Special cases.** These results hold for solid **and** hollow circular sections. They do **not** hold for non-circular sections, which warp (outside this course).

**7. Traps.** Writing γ = φ (the twist angle). In fact γ = rφ/L. γ is the angle a surface line tilts through; φ is the rotation of one end of the bar relative to the other.

**8. Summary.** Sections stay plane and rigid; $\gamma_{\theta z} = r\,d\phi/dz$; all other strains are zero.

---

## Concept 6.2 — The torsion formula and the angle of twist

### A. Concept explanation

**1. Intuition.** Material far from the axis is strained more and also has a longer lever arm, so it does most of the work. That is why hollow shafts are efficient: material near the centre carries little and mostly adds weight.

**2. Why it matters.** The formula τ = Tr/J sizes every shaft, and φ = TL/GJ controls stiffness (gear alignment, vibration). Both appear in every torsion PYQ.

**3. Formal treatment / 4. Derivation (slides; Crandall §6.3).**
- *Step 1, stress–strain* (Hooke in shear; slide: "stresses obtained from stress–strain relations"): $\sigma_r = \sigma_\theta = \sigma_z = \tau_{r\theta} = \tau_{rz} = 0$ and
$$\tau_{\theta z} = G\gamma_{\theta z} = Gr\frac{d\phi}{dz}\quad(A)$$
- *Step 2, equilibrium* (slide: "equilibrium requirements"): the shear stresses on a section must add up to the internal torque:
$$M_t = \int_A r\,(\tau_{\theta z}\,dA) = G\frac{d\phi}{dz}\int_Ar^2dA = G\frac{d\phi}{dz}I_z\quad(1, 2)$$
where $I_z = J = I_P$ is the **polar moment of inertia**:
$$\boxed{J_{solid} = \frac{\pi r^4}{2} = \frac{\pi d^4}{32},\qquad J_{hollow} = \frac{\pi(d_o^4 - d_i^4)}{32}}\quad(3)$$
- *Step 3, combine:* $\dfrac{d\phi}{dz} = \dfrac{M_t}{GI_z}$ (4), and substituting (4) in (A): $\tau_{\theta z} = \dfrac{M_tr}{I_z}$ (6).
- *Step 4, integrate along the length:* $\phi = \displaystyle\int_0^L\frac{M_t}{GI_z}dz = \frac{M_tL}{GI_z}$ (5) for a uniform shaft.
$$\boxed{\frac{T}{J} = \frac{\tau}{r} = \frac{G\phi}{L}}$$
**Maximum (surface) stress, solid shaft:** $\tau_{max} = \dfrac{Tc}{J} = \boxed{\dfrac{16T}{\pi d^3}}$.
**Hollow shaft:** $\tau_{max} = \dfrac{T(d_o/2)}{J}$ at the outer surface and $\tau_{min} = \dfrac{T(d_i/2)}{J} = \tau_{max}\dfrac{d_i}{d_o}$ at the inner surface.
**Thin-walled tube** (mean radius $r_m$, thickness t): $J \approx 2\pi r_m^3t$ and $\tau \approx \dfrac{T}{2\pi r_m^2t}$.
**Torsional stiffness:** $k_T = T/\phi = GJ/L$; GJ is the torsional rigidity.

**Several segments or varying torque:**
$$\phi_{A/B} = \sum_i\frac{T_iL_i}{G_iJ_i}\quad(T_i = \text{internal torque in segment } i,\ \text{signed})$$
*Sign convention (slides/Beer):* right-hand rule. An internal torque is positive if its vector points **away** from the cut face (outward normal), the same "positive face, positive direction" rule as in Ch. 3. *Angle of twist (slides):* for a shaft fixed at one end it equals the rotation of the free end; in general it is the angle through which one end rotates relative to the other.

**5. Stress picture.** τ is linear in r on the cross-section, zero at the centre. By $\tau_{xy} = \tau_{yx}$, an equal shear acts on **longitudinal** planes too, which is why wooden shafts split lengthwise.

**6. Special cases.**
- Same weight (same area): a hollow shaft carries more torque and is stiffer than a solid one (Q3, Q6).
- Same strength requirement: the hollow shaft is lighter (Q4).

**7. Common traps.**
- Using r = d where it should be d/2.
- Units: T in N·mm with r in mm and J in mm⁴ gives MPa. φ comes out in **radians**; convert to degrees only at the end.
- Using the *external* torque instead of the *internal* torque of a segment. Draw a torque diagram, just like an axial-force diagram.
- $J_{hollow} = \frac{\pi}{32}(d_o^4 - d_i^4)$, **not** $\frac{\pi}{32}(d_o - d_i)^4$.

**8. Summary box**
$$\tau = \frac{Tr}{J},\quad \tau_{max,solid} = \frac{16T}{\pi d^3},\quad \phi = \sum\frac{TL}{GJ},\quad J_s = \frac{\pi d^4}{32},\quad J_h = \frac{\pi(d_o^4 - d_i^4)}{32},\quad k_T = \frac{GJ}{L}$$

### B. Solved questions

#### Q1 (Slides Ch6, Gere) — Solid steel bar: τmax, φ and the allowable torque *(easy)*
**Problem.** A solid steel bar has d = 40 mm, L = 1.3 m and G = 80 GPa. (a) With T = 340 N·m, find the maximum shear stress and the angle of twist between the ends. (b) If the allowable shear stress is 42 MPa and the allowable twist is 2.5°, find the maximum permissible torque.

**Solution.**
1. *(a) Stress:* $\tau_{max} = \dfrac{16(340\,000)}{\pi(40)^3} = 27.1$ MPa.
2. *(a) Twist:* $J = \pi(40)^4/32 = 251\,327$ mm⁴, so $\phi = \dfrac{340\,000(1300)}{80\,000(251\,327)} = 0.0220$ rad = 1.26°.
3. *(b) Strength:* $T = \tau\pi d^3/16 = 42\pi(40)^3/16 = 528$ N·m.
4. *(b) Stiffness:* $T = \phi GJ/L = 0.04363(80\,000)(251\,327)/1300 = 675$ N·m.

$$\boxed{(a)\ \tau_{max} = 27.1\ \text{MPa},\ \phi = 1.26^\circ;\qquad (b)\ T_{max} = 528\ \text{N·m (stress governs)}}$$

**Exam takeaway.** Always check both strength and stiffness and report the **smaller** torque.

---

#### Q2 (Slides Ch6, Beer) — Hollow shaft 40/60 mm *(easy)*
**Problem.** A hollow steel shaft (L = 1.5 m, $d_i = 40$ mm, $d_o = 60$ mm, G = 77 GPa). (a) Largest torque if τ ≤ 120 MPa? (b) The corresponding minimum shear stress? (c) Torque for a twist of 2°? (d) Angle of twist that creates 70 MPa on the inner surface?

**Solution.**
1. $J = \frac{\pi}{32}(60^4 - 40^4) = 1.021\times10^6$ mm⁴.
2. *(a)* $T = \tau J/c = 120(1.021\times10^6)/30 = 4.08$ kN·m.
3. *(b)* $\tau_{min} = 120(20/30) = 80$ MPa.
4. *(c)* $T = \phi GJ/L = 0.03491(77\,000)(1.021\times10^6)/1500 = 1.83$ kN·m.
5. *(d)* From $\tau = Gr\phi/L$: $\phi = \tau L/(Gr_i) = 70(1500)/(77\,000\times20) = 0.0682$ rad = 3.91°.

$$\boxed{(a)\ 4.08\ \text{kN·m};\quad (b)\ 80\ \text{MPa};\quad (c)\ 1.83\ \text{kN·m};\quad (d)\ 3.91^\circ}$$

**Exam takeaway.** τ ∝ r: the inner surface always has the smaller stress, $\tau_{min} = \tau_{max}d_i/d_o$.

---

#### Q3 (Slides Ch6, Gere) — Hollow vs solid shaft of the same outer radius *(medium, conceptual)*
**Problem.** A hollow shaft (outer radius R, inner radius 0.6R) and a solid shaft (radius R) of the same material and length carry the same torque. Compare their shear stresses, angles of twist and weights, and their strength-to-weight ratios.

**Solution.**
1. $J_h/J_s = 1 - 0.6^4 = 0.8704$ and $A_h/A_s = 1 - 0.36 = 0.64$.
2. Stresses and twists scale as 1/J: $\tau_h/\tau_s = \phi_h/\phi_s = 1/0.8704 = 1.15$.
3. Weight ratio: $W_h/W_s = 0.64$.
4. Strength-to-weight (torque each can carry at the same τallow, per unit weight): $0.8704/0.64 = 1.36$.

$$\boxed{\tau_h/\tau_s = \phi_h/\phi_s = 1.15,\qquad W_h/W_s = 0.64,\qquad \text{strength/weight (hollow/solid)} = 1.36}$$

**Exam takeaway.** Removing the inner 60% of the radius costs only 13% of J but saves 36% of the weight.

---

#### Q4 (Slides Ch6, Gere) — Design a solid vs a hollow shaft for 1200 N·m *(medium)*
**Problem.** A steel shaft must transmit 1200 N·m without exceeding τallow = 40 MPa or a rate of twist of 0.75°/m (G = 78 GPa). (a) Find the diameter d₀ of a solid shaft. (b) Find the outer diameter d₂ of a hollow shaft with wall thickness t = d₂/10. (c) Find d₂/d₀ and the weight ratio.

**Solution.**
1. Rate limit: θ = 0.75°/m = 1.309 × 10⁻⁵ rad/mm.
2. *(a) Solid:* strength gives $d^3 = 16T/(\pi\tau)$, so d = 53.5 mm. Stiffness gives $d^4 = 32T/(\pi G\theta)$, so d = 58.8 mm. Take d₀ = 58.8 mm.
3. *(b) Hollow* ($d_1 = 0.8d_2$, so $J = \frac{\pi d_2^4}{32}(1 - 0.8^4) = 0.5904\frac{\pi d_2^4}{32}$): strength gives 63.7 mm; stiffness gives 67.1 mm. Take d₂ = 67.1 mm.
4. *(c)* $d_2/d_0 = 1.14$. Weight ratio $= \dfrac{d_2^2(1 - 0.64)}{d_0^2} = 0.47$.

$$\boxed{d_0 = 58.8\ \text{mm},\quad d_2 = 67.1\ \text{mm},\quad d_2/d_0 = 1.14,\quad W_h/W_s = 0.47}$$

**Exam takeaway.** Here stiffness governs both designs; the hollow shaft is 14% larger in diameter but weighs less than half.

---

#### Q5 (Slides Ch6, Beer Sample 3.1) — Four-gear shaft: hollow BC, size AB and CD *(medium)*
**Problem.** Torques $T_A = 6$, $T_B = 14$, $T_C = 26$ and $T_D = 6$ kN·m act on shaft ABCD (balanced). BC is hollow ($d_i = 90$, $d_o = 120$ mm). AB and CD are solid with diameter d. Find (a) the maximum and minimum shear stress in BC and (b) d for τallow = 65 MPa.

**Approach.** Internal torques from free bodies (slides: "T_AB" and "T_BC" sketches), then τ = Tr/J.

**Solution.**
1. *Internal torques:* $T_{AB} = 6$ kN·m; $T_{BC} = 6 + 14 = 20$ kN·m; $T_{CD} = 20 - 26 = -6$ kN·m (magnitude 6).
2. $J_{BC} = \frac\pi{32}(120^4 - 90^4) = 13.92\times10^6$ mm⁴.
3. *(a)* $\tau_{max} = \dfrac{20\times10^6(60)}{13.92\times10^6} = 86.2$ MPa and $\tau_{min} = 86.2(45/60) = 64.7$ MPa.
4. *(b)* $d = \left(\dfrac{16(6\times10^6)}{\pi(65)}\right)^{1/3} = 77.8$ mm.

$$\boxed{(a)\ \tau_{max} = 86.2\ \text{MPa},\ \tau_{min} = 64.7\ \text{MPa};\qquad (b)\ d = 77.8\ \text{mm}}$$

**Check.** Matches the slide (d = 77.8 mm) ✓.

**Exam takeaway.** The torque diagram decides which segment is critical.

---

#### Q6 (Slides Ch6, Beer) — Hollow 4 in/6 in shaft vs equal-weight alternatives *(medium)*
**Problem.** A motor–generator shaft is hollow, 4 in inner and 6 in outer diameter, with τallow = 12 ksi. Find the maximum torque (a) for the shaft as designed, (b) for a solid shaft of the same weight and (c) for a hollow shaft of the same weight with an 8 in outer diameter.

**Solution.**
1. *(a)* $J = \frac\pi{32}(6^4 - 4^4) = 102.1$ in⁴, so $T = 12(102.1)/3 = 408$ kip·in.
2. *(b)* Same area 5π in², so d = 4.47 in and $T = 12\pi d^3/16 = 211$ kip·in.
3. *(c)* Same area with $d_o = 8$: $d_i^2 = 64 - 20 = 44$, so $d_i = 6.63$ in and $T = 12\cdot\frac{\pi(8^4 - 6.63^4)}{32}/4 = 636$ kip·in.

$$\boxed{(a)\ 408;\quad (b)\ 211;\quad (c)\ 636\ \text{kip·in}}$$

**Exam takeaway.** For the same material, moving it outward raises the torque capacity: 211 → 408 → 636.

---

#### Q7 (Slides Ch6, Beer) — Stepped shaft AD with a bored section: twist at A *(medium)*
**Problem.** Shaft AD is fixed at D. AB is solid, 30 mm, 0.4 m long, with 250 N·m at A. BC is solid, 60 mm, 0.2 m, with 2000 N·m at B. CD is 60 mm with a 44 mm bore, 0.6 m long. G = 77 GPa. Find the angle of twist at A.

**Solution.**
1. *Internal torques:* $T_{AB} = 250$ N·m; $T_{BC} = T_{CD} = 2250$ N·m (same sense).
2. *Twists:*
$$\phi_A = \frac1G\left[\frac{250\times10^3(400)}{\frac\pi{32}30^4} + \frac{2250\times10^3(200)}{\frac\pi{32}60^4} + \frac{2250\times10^3(600)}{\frac\pi{32}(60^4 - 44^4)}\right] = 0.0163 + 0.0046 + 0.0194$$

$$\boxed{\phi_A = 0.0403\ \text{rad} = 2.31^\circ}$$

**Check.** The bored section CD, longest and with the largest torque, contributes most (48%) ✓.

**Exam takeaway.** Write one term per segment with its own T, L and J.

---

#### Q8 (Slides Ch6, Gere) — Two-segment solid shaft vs an equivalent hollow shaft *(medium)*
**Problem.** A solid shaft has segments of 80 mm × 1.2 m and 60 mm × 0.9 m. A hollow shaft of the same material is 2.1 m long with t = d/10 (so $d_i = 0.8d$). For equal torsional stiffness, find the hollow shaft's outer diameter d.

**Solution.**
1. $\phi_1 = \dfrac{32T}{\pi G}\left[\dfrac{1.2}{0.08^4} + \dfrac{0.9}{0.06^4}\right] = \dfrac{32T}{\pi G}(29\,297 + 69\,444) = \dfrac{32T}{\pi G}(98\,741\ \text{m}^{-3})$.
2. $\phi_2 = \dfrac{32T}{\pi G}\cdot\dfrac{2.1}{0.5904\,d^4} = \dfrac{32T}{\pi G}\cdot\dfrac{3.5569}{d^4}$.
3. Equal stiffness means $\phi_1 = \phi_2$, so $d^4 = 3.5569/98\,741 = 36.02\times10^{-6}$ m⁴.

$$\boxed{d = 77.5\ \text{mm}}$$

**Exam takeaway.** "Same torsional stiffness" means the same T/φ, i.e. the same φ under the same T.

---

#### Q9 (Slides Ch6, Gere) — Aluminium tube: shear strain at the inner surface; minimum outer radius *(easy)*
**Problem.** An aluminium tube in pure torsion has $r_2 = 1.5r_1$. (a) If the maximum shear strain is 400 × 10⁻⁶ rad, what is the shear strain at the inner surface? (b) If the allowable rate of twist is 0.125°/ft and the maximum shear strain is kept at 400 × 10⁻⁶ by adjusting T, find the minimum outer radius.

**Solution.**
1. *(a)* γ ∝ r: $\gamma_1 = \gamma_{max}(r_1/r_2) = 400/1.5 = 267\times10^{-6}$ rad.
2. *(b)* θ = 0.125(π/180)/12 = 1.818 × 10⁻⁴ rad/in, and γmax = r₂θ, so $r_{2,min} = \gamma_{max}/\theta = 400\times10^{-6}/1.818\times10^{-4}$.

$$\boxed{(a)\ \gamma_1 = 267\times10^{-6}\ \text{rad};\qquad (b)\ r_{2,min} = 2.2\ \text{in}}$$

**Exam takeaway.** Strain problems in torsion need no G: γ = rθ is pure geometry.

---

#### Q10 (Slides Ch6, Gere) — Strain gauge at 45° gives G *(easy)*
**Problem.** A solid 50 mm bar is twisted to T = 500 N·m; a gauge at 45° to the axis reads ε = 339 × 10⁻⁶. Find G.

**Solution.**
1. $\tau_{max} = 16(500)/\pi(0.05)^3 = 20.37$ MPa.
2. Pure shear: $\gamma_{max} = 2\epsilon_{45} = 678\times10^{-6}$.
3. $G = \tau/\gamma$.

$$\boxed{G = 30.0\ \text{GPa}}$$

**Exam takeaway.** PYQ 2021-22 A-Q1 is the same bar with ε = 350μ, giving G = 29.1 GPa (Ch. 4 Q30).

---

#### Q11 (PYQ 2014-15 Compre A Q5) — Size a shaft for 205 N·m *(easy)*
**Problem.** A solid steel shaft transmits 205 N·m; τallow = 100 MPa. Find the required diameter.

**Solution.** $d = \left(\dfrac{16(205\,000)}{\pi(100)}\right)^{1/3}$.

$$\boxed{d = 21.9\ \text{mm}}$$

---

#### Q12 (PYQ 2014-15 Test-2 Q4) — Axle of tubes plus a solid section *(easy–medium, 20 marks)*
**Problem.** An A-36 steel axle has tubes AB and CD (outer 30 mm, inner 20 mm) and a solid section BC (40 mm, 250 mm long), on smooth bearings. G = 75 GPa. 85 N·m torques act on the end gears. Find (a) the maximum and minimum shear stress in the tubes and (b) the twist of B relative to C.

**Solution.**
1. Smooth bearings, so the internal torque is 85 N·m everywhere.
2. $J_{tube} = \frac\pi{32}(30^4 - 20^4) = 63\,814$ mm⁴; $J_{BC} = \frac\pi{32}(40)^4 = 251\,327$ mm⁴.
3. *(a)* $\tau_{max} = \dfrac{85\,000(15)}{63\,814} = 20.0$ MPa and $\tau_{min} = 20.0(10/15) = 13.3$ MPa.
4. *(b)* $\phi_{B/C} = \dfrac{85\,000(250)}{75\,000(251\,327)} = 1.13\times10^{-3}$ rad = 0.0646°.

$$\boxed{(a)\ \tau_{max} = 20.0\ \text{MPa},\ \tau_{min} = 13.3\ \text{MPa};\qquad (b)\ \phi_{B/C} = 0.0646^\circ}$$

---

#### Q13 (PYQ 2023-24 Compre A Q1) — Shaft with three disks: allowable T and twist A relative to C *(medium, 10 marks)*
**Problem.** A 60 mm solid 6061-T6 aluminium shaft (τallow = 80 MPa, G = 26 GPa) carries disks A (⅔T), B (T, opposite sense) and C (⅓T); AB = BC = 1.20 m. Find (a) the maximum allowable T, (b) the internal torques in AB and BC and (c) the twist of disk A relative to disk C.

**Solution.**
1. *Internal torques:* $T_{AB} = \tfrac23T$ and $T_{BC} = \tfrac23T - T = -\tfrac13T$. The maximum is in AB.
2. *(a)* $\tfrac23T = \tau\pi d^3/16 = 80\pi(60)^3/16 = 3.393$ kN·m, so T = 5.09 kN·m.
3. *(b)* $T_{AB} = 3.39$ kN·m; $T_{BC} = 1.70$ kN·m in the opposite sense.
4. *(c)* $J = \pi(60)^4/32 = 1.272\times10^6$ mm⁴ and $GJ = 3.308\times10^{10}$ N·mm²:
$$\phi_{A/C} = \frac{(T_{AB} + T_{BC})L}{GJ} = \frac{(3.393 - 1.696)\times10^6(1200)}{3.308\times10^{10}} = 0.0615\ \text{rad}$$

$$\boxed{(a)\ T = 5.09\ \text{kN·m};\quad (b)\ 3.39\ \text{and}\ 1.70\ \text{kN·m (opposite)};\quad (c)\ \phi_{A/C} = 3.53^\circ}$$

**Exam takeaway.** Opposite-signed segments partly cancel; students who add magnitudes get 10.6°.

---

## Concept 6.3 — Power transmission

### A. Concept explanation

**1. Intuition.** A shaft spinning fast can carry a lot of power with a small torque, which is why high-speed shafts are thin. Power = torque × angular speed.

**2. Why it matters.** Drive shafts, motors and generators are specified by power and speed; the designer has to convert to torque first.

**3. Formal treatment.**
$$\boxed{P = T\omega = \frac{2\pi nT}{60}}\quad(P\ \text{in W},\ T\ \text{in N·m},\ \omega\ \text{in rad/s},\ n\ \text{in rpm}),\qquad T = \frac{60P}{2\pi n}$$
With frequency f (Hz): $P = 2\pi fT$.

**4. Derivation.** Work done by a torque turning through dφ is T dφ; power is its rate, $T\,d\phi/dt = T\omega$; and one revolution per minute is 2π/60 rad/s.

**5–6. Picture / special cases.** At constant power, T ∝ 1/n: halving the speed doubles the torque and needs a shaft of $2^{1/3} = 1.26$ times the diameter.

**7. Traps.** Using rpm directly in P = Tω; kW vs W.

**8. Summary.** $T = 60P/(2\pi n)$, then the torsion formula.

### B. Solved question

#### Q14 (Slides Ch6, Gere) — Truck drive shaft *(easy)*
**Problem.** A truck drive shaft (outer diameter 60 mm, inner 40 mm) runs at 2500 rpm. (a) If it transmits 150 kW, what is the maximum shear stress? (b) If τallow = 30 MPa, what is the maximum power?

**Solution.**
1. $J = \frac\pi{32}(60^4 - 40^4) = 1.021\times10^{-6}$ m⁴.
2. *(a)* $T = \dfrac{60(150\,000)}{2\pi(2500)} = 573$ N·m, so $\tau_{max} = \dfrac{Td_2}{2J} = \dfrac{573(0.060)}{2(1.021\times10^{-6})} = 16.8$ MPa.
3. *(b)* τ ∝ P, so $P_{max} = 150(30/16.835) = 267$ kW.

$$\boxed{(a)\ \tau_{max} = 16.8\ \text{MPa};\qquad (b)\ P_{max} = 267\ \text{kW}}$$

**Exam takeaway.** P = Tω needs ω in rad/s, **not** rpm.

---

## Concept 6.4 — Gears and coupled shafts

### A. Concept explanation

**1. Intuition.** Two meshing gears share one tooth force F. The bigger gear gets the bigger torque (T = Fr) but turns through a smaller angle. The contact point moves the same arc length on both: $r_B\phi_B = r_C\phi_C$.

**2. Why it matters.** Gearboxes, coupled shafts, PYQs 2014 Compre B Q2 and 2019 B Q4.

**3. Formal treatment (slides, Beer Sample 3.4).**
- **Statics** (slide): $F = T_B/r_B = T_C/r_C$, so $T_C = T_B(r_C/r_B)$.
- **Kinematics** (slide: "peripheral motions of the gears are equal"): $r_B\phi_B = r_C\phi_C$.
- **Twist of the free end:** $\phi_A = \phi_B + \phi_{A/B}$, where φB comes from the *other* shaft's twist through the gear ratio.

**4. Derivation.** Tooth contact: equal and opposite tangential forces F on the two gears (Newton's third law). The arc length rolled out at the pitch circles must be the same, otherwise the teeth would separate or interpenetrate.

**5. Picture.** Slide: two gears with F acting down on A and up on B at the contact point; arcs $r_A\phi_A = r_B\phi_B$.

**6. Special cases.** Gear ratio n = r_large/r_small: torque multiplies by n, rotation divides by n. The stiffness of the far shaft, seen through the gears, scales by n².

**7. Traps.** Using the ratio the wrong way (torque scales with r, rotation with 1/r). Forgetting that the free shaft's end rotation includes the gear's own rotation, not just its twist.

**8. Summary.** $T_C/T_B = r_C/r_B$; $\phi_B/\phi_C = r_C/r_B$; total rotation = gear rotation + own twist.

### B. Solved questions

#### Q15 (Slides Ch6, Beer Sample 3.4) — Two shafts connected by gears: largest $T_0$ and rotation of A *(medium)*
**Problem.** Shaft AB (0.75 in diameter, 24 in long, gear B with $r_B = 0.875$ in) meshes with shaft CD (1 in diameter, 36 in long, fixed at D, gear C with $r_C = 2.45$ in). G = 11.2 × 10⁶ psi and τallow = 8 ksi. Find (a) the largest torque T₀ that may be applied at A and (b) the corresponding rotation of A.

**Solution.**
1. *Statics:* $F(0.875) = T_0$ and $F(2.45) = T_{CD}$, so $T_{CD} = 2.8T_0$ (1).
2. *Kinematics:* $r_B\phi_B = r_C\phi_C$, so $\phi_B = 2.8\phi_C$ (2).
3. *(a)* AB: $T_0 = 8000\cdot\frac\pi2(0.375)^3 = 663$ lb·in. CD: $2.8T_0 = 8000\cdot\frac\pi2(0.5)^3$, so $T_0 = 561$ lb·in. The smaller governs: T₀ = 561 lb·in.
4. *(b)* $\phi_{A/B} = \dfrac{561(24)}{\frac\pi2(0.375)^4(11.2\times10^6)} = 0.0387$ rad = 2.22°. $\phi_C = \dfrac{2.8(561)(36)}{\frac\pi2(0.5)^4(11.2\times10^6)} = 0.0514$ rad = 2.95°. So $\phi_B = 2.8(2.95^\circ) = 8.26^\circ$.

$$\boxed{T_0 = 561\ \text{lb·in},\qquad \phi_A = 8.26^\circ + 2.22^\circ = 10.48^\circ}$$

**Exam takeaway.** The slide's four steps (statics, kinematics, allowable torque in each shaft, twist) are the marking scheme.

---

#### Q16 (Slides Ch6) — Find φE for gear-coupled shafts (symbolic) *(medium)*
**Problem.** Shaft AD (fixed at D) carries gear A of radius $r_A$. Shaft BE carries gear B ($r_B$) and torque T at E. Both have length L and rigidity GJ. Find φE.

**Solution.**
1. *Statics:* tooth force $F = T/r_B$, so $T_{AD} = Fr_A = T\,r_A/r_B$.
2. *Twist of AD:* $\phi_A = \dfrac{Tr_AL}{r_BGJ}$.
3. *Gear B:* $\phi_B = \dfrac{r_A}{r_B}\phi_A = \dfrac{r_A^2}{r_B^2}\dfrac{TL}{GJ}$.
4. *E:* $\phi_E = \phi_B + \dfrac{TL}{GJ}$.

$$\boxed{\phi_E = \frac{TL}{GJ}\left(1 + \frac{r_A^2}{r_B^2}\right)}$$

**Exam takeaway.** The far shaft appears $(r_A/r_B)^2$ times as flexible: torque and rotation each bring one factor of the gear ratio.

---

#### Q17 (PYQ 2014-15 Compre B Q2) — Coupled shafts: twist of end A relative to D *(medium, 15 marks)*
**Problem.** Solid shafts, each 20 mm diameter, are coupled by meshed gears. T = 45 N·m acts at A. AB (2 m) turns freely in bearings E and F, with gear B ($r_B = 150$ mm). DC (1.5 m) is fixed at D, with gear C ($r_C = 75$ mm). G = 80 GPa. Find the twist of A relative to D.

**Solution.**
1. $J = \pi(20)^4/32 = 15\,708$ mm⁴, so $GJ = 1.2566\times10^9$ N·mm².
2. *Tooth force:* $F = 45\,000/150 = 300$ N, so $T_{DC} = 300(75) = 22.5$ N·m.
3. $\phi_C = \dfrac{22\,500(1500)}{1.2566\times10^9} = 0.02686$ rad.
4. *Kinematics:* $\phi_B = \phi_C(r_C/r_B) = 0.01343$ rad.
5. $\phi_{A/B} = \dfrac{45\,000(2000)}{1.2566\times10^9} = 0.07162$ rad.

$$\boxed{\phi_{A/D} = 0.01343 + 0.07162 = 0.0850\ \text{rad} = 4.87^\circ}$$

**Exam takeaway.** Here the larger gear is on the driven shaft, so DC sees *half* the torque but turns gear B only half as far.

---

#### Q18 (PYQ 2019-20 Compre B Q4) — Gear-coupled shafts: find T₁ and T₂ for 0.05 rad at A and C *(hard, 12 marks)*
**Problem.** Shaft ABC (60 mm, on journal bearings) carries gear B ($r_B = 75$ mm), with AB = 600 mm and BC = 900 mm; torques T₂ at A and T₁ at C act in the same sense. Shaft EH (80 mm) is fixed at E and carries gear D ($r_D = 100$ mm) at 600 mm from E. G = 80 GPa. Find T₁ and T₂ so that the twists at gears A and C are both 0.05 rad.

**Solution.**
1. $GJ_1 = 80\,000\cdot\frac\pi{32}(60)^4 = 1.018\times10^{11}$ and $GJ_2 = 80\,000\cdot\frac\pi{32}(80)^4 = 3.217\times10^{11}$ N·mm². Gear ratio $n = r_D/r_B = 4/3$.
2. *Statics:* shaft ABC is in equilibrium, so gear B carries $T_B = T_1 + T_2$, and gear D gets $T_D = n(T_1 + T_2)$.
3. *Shaft EH:* $\phi_D = \dfrac{n(T_1 + T_2)(600)}{GJ_2}$. *Gears:* $\phi_B = n\phi_D$.
4. *Shaft ABC:* $\phi_A = \phi_B + \dfrac{T_2(600)}{GJ_1}$ and $\phi_C = \phi_B + \dfrac{T_1(900)}{GJ_1}$.
5. $\phi_A = \phi_C$ gives $600T_2 = 900T_1$, so $T_2 = 1.5T_1$.
6. Then $\dfrac{(16/9)(2.5T_1)(600)}{3.217\times10^{11}} + \dfrac{1.5T_1(600)}{1.018\times10^{11}} = 0.05$, i.e. $T_1(8.29 + 8.84)\times10^{-9} = 0.05$.

$$\boxed{T_1 = 2.92\ \text{kN·m},\qquad T_2 = 4.38\ \text{kN·m}}$$

**Check.** $\phi_B = 0.0242$ rad; $\phi_A = 0.0242 + 4.38\times10^6(600)/1.018\times10^{11} = 0.0500$ ✓.

**Exam takeaway.** Write φA and φC each as "gear rotation + own twist", then the equal-twist condition gives T₂/T₁ at once.

---

## Concept 6.5 — Statically indeterminate shafts and torsional strain energy

### A. Concept explanation

**1. Intuition.** A shaft clamped at both ends with a torque in the middle: both walls resist, but statics gives only $T_A + T_D = T$. The extra fact: **the total twist between the walls is zero**. It is the exact twin of the axially loaded bar fixed at both ends (Ch. 2).

**2. Why it matters.** Fixed–fixed shafts, composite (tube + core) shafts and gear trains with locked ends. PYQ 2024 B-Q1 (12 marks) is a fixed–fixed shaft with strain energy.

**3. Formal treatment (the three steps of Ch. 2):**
1. Equilibrium: $T_A + T_D = \sum T_{applied}$.
2. Compatibility: $\phi_{A/D} = \sum\frac{T_iL_i}{GJ_i} = 0$.
3. Torque–twist: φ = TL/GJ.

*Strain energy (slides):* $U = \displaystyle\int\frac{M_t^2}{2GI_z}dz = \sum\frac{T_i^2L_i}{2G_iJ_i}$.

**4. Derivations.**
*(a) Single torque T₀ at distance a from A (b from D), uniform GJ.* Release D: φD = T₀a/GJ. The redundant $T_D$ alone gives $-T_DL/GJ$. Compatibility gives
$$\boxed{T_D = T_0\frac{a}{L},\qquad T_A = T_0\frac{b}{L}}$$
As for axial bars, the nearer wall carries more.
*(b) Composite shaft (core + tube, bonded).* Both twist equally, so $T_i = T\dfrac{(GJ)_i}{\sum(GJ)}$.

**5. Picture.** The internal-torque diagram changes sign at a loading point; the twist diagram is piecewise linear and peaks there (Q20).

**6. Special cases.** Several torques: superpose the single-torque results.

**7. Traps.** Signs of internal torques; forgetting that the twists of all segments must add to zero, not just two.

**8. Summary.** $T_A = T_0b/L$; $\sum TL/GJ = 0$; $U = \sum T^2L/2GJ$.

### B. Solved questions

#### Q19 (Slides Ch6, Crandall example) — Fixed–fixed shaft: rotation of point O *(medium)*
**Problem.** A 25 mm aluminium-alloy shaft (G = 26.5 GPa) has both ends A and C built in. A 70 N·m torque acts at B, 0.6 m from A; BC = 1.8 m. Find the rotation of point O, 1.2 m from C.

**Solution.**
1. *Reactions:* $T_A = 70(1.8/2.4) = 52.5$ N·m and $T_C = 70(0.6/2.4) = 17.5$ N·m.
2. Segment OC carries 17.5 N·m, so
$$\phi_O = \frac{17\,500(1200)}{26\,500\cdot\frac\pi{32}(25)^4} = 0.02066\ \text{rad}$$

$$\boxed{\phi_O = 1.18^\circ}$$

**Check (from the A side).** $\phi_B = 52\,500(600)/GJ = 0.0310$ rad, then O (0.6 m beyond B) comes back by $17\,500(600)/GJ = 0.0103$, giving 0.0207 ✓.

**Exam takeaway.** Rotations measured from either fixed end must agree; that is the check.

---

#### Q20 (PYQ 2024-25 Compre B Q1) — Fixed–fixed bar with two torques: reactions, maximum twist, strain energy *(medium, 12 marks)*
**Problem.** A solid 40 mm bar ABCD is fixed at A and D. Torques T₀ = 800 N·m at B (x = 0.3L) and 2T₀ at C (x = 0.6L) act in the same sense. L = 1.2 m, G = 80 GPa. Find (a) the reactions at A and D, (b) the maximum angle of twist (degrees) and (c) the total strain energy (J).

**Solution.**
1. $J = 251\,327$ mm⁴ and $GJ = 2.0106\times10^{10}$ N·mm².
2. *(a) Superposition of the single-torque result:* $T_A = T_0(0.7) + 2T_0(0.4) = 1.5T_0 = 1200$ N·m and $T_D = 3T_0 - 1.5T_0 = 1200$ N·m, both opposite to the applied torques.
3. *Internal torques:* $T_{AB} = 1200$, $T_{BC} = 1200 - 800 = 400$, $T_{CD} = 400 - 1600 = -1200$ N·m. Compatibility check: $1200(360) + 400(360) - 1200(480) = 0$ ✓.
4. *(b) Twists:* $\phi_B = \dfrac{1200\times10^3(360)}{2.0106\times10^{10}} = 0.02149$ rad = 1.23°; $\phi_C = \phi_B + \dfrac{400\times10^3(360)}{2.0106\times10^{10}} = 0.02865$ rad = 1.64°.
5. *(c) Energy:* $U = \dfrac{1}{2GJ}\left[1200^2(0.36) + 400^2(0.36) + 1200^2(0.48)\right]\times10^9$ N·mm.

$$\boxed{(a)\ T_A = T_D = 1200\ \text{N·m};\quad (b)\ \phi_{max} = 1.64^\circ\ \text{at C};\quad (c)\ U = 31.5\ \text{J}}$$

**Exam takeaway.** The maximum twist occurs at a loading point where the internal torque changes sign, just as a beam's maximum deflection occurs where its slope is zero.

---

## Concept 6.6 — Combined stresses: torsion + axial + bending; yielding of shafts

### A. Concept explanation

**1. Intuition.** Real shafts are rarely just twisted. A propeller shaft is twisted and pushed; a crank is twisted and bent. At a surface point you get a normal stress σ (from the axial force and bending) **plus** a shear stress τ (from the torque and the transverse shear). Put them on one small square element, then use Mohr's circle (Ch. 4) and a yield criterion (Ch. 5).

**2. Why it matters.** This is **the most-repeated long question** in the compre papers (2019 B-Q2, 2021 A-Q2, 2023 B-Q2, 2024 B-Q2, 2021 B-Q4, 2014 Test-2 Q1), usually 15–20 marks.

**3. Formal treatment (slides; Crandall §6.5, Fig. 6.14).**
- *Pure torsion:* the surface element is in **pure shear** τ. The principal stresses are ±τ, acting at **45°** to the axis (slide: "the principal stresses in torsion are equal tension and compression acting on faces inclined at 45° to the axis of the shaft"). Brittle shafts (chalk!) break on a 45° helix (maximum tension); ductile shafts shear off on a cross-section (maximum shear).
- *Torsion + axial P* (slide: "combined state of stress"): $\sigma = P/A$ and $\tau = Tc/J$, so
$$\sigma_{1,2} = \frac\sigma2 \pm \sqrt{\left(\frac\sigma2\right)^2 + \tau^2},\qquad \tau_{max} = \sqrt{\left(\frac\sigma2\right)^2 + \tau^2}$$
- *Yield (slides):* von Mises $\sqrt{\sigma^2 + 3\tau^2} = Y$; Tresca $\sqrt{\sigma^2 + 4\tau^2} = Y$.
- *Torsion + bending (solid shaft):* $\sigma_b = \dfrac{32M}{\pi d^3}$ and $\tau = \dfrac{16T}{\pi d^3}$, so
$$\tau_{max} = \frac{16}{\pi d^3}\sqrt{M^2 + T^2},\qquad \sigma_1 = \frac{16}{\pi d^3}\left(M + \sqrt{M^2 + T^2}\right)$$
These are the "equivalent torque" and "equivalent moment" formulas.

**4. General procedure for combined-loading PYQs:**
1. FBD of the whole member, then reactions (Ch. 1).
2. Cut at the section and find F, V, $M_b$ and T (Ch. 3, 3-D vectors $\mathbf M = \mathbf r\times\mathbf F$).
3. At the requested surface point: $\sigma = F/A \pm M_bc/I$ (bending stress is zero at the neutral axis; I = πd⁴/64 = J/2), and $\tau = Tc/J \pm$ transverse shear (for a solid circle $\tau_V = 4V/3A$ at the neutral axis, 0 at the extreme fibre).
4. Draw the 2-D element with the correct directions.
5. Mohr's circle → principal stresses and τmax (Ch. 4).
6. Yield criterion → factor of safety (Ch. 5).

**5. Picture.** Around the cross-section: bending σ is largest at the top and bottom fibres and zero at the sides (neutral axis); torsional τ is the same all round; transverse-shear τ is largest at the sides and zero at the top and bottom. The critical point is usually where bending σ peaks.

**6. Special cases.** For a σ–τ state (one normal stress, one shear), the principal stresses always have opposite signs, so in-plane τmax = R is also the absolute maximum.

**7. Traps.**
- Putting the maximum bending stress and the maximum transverse shear at the same point. They occur 90° apart.
- Using J where I is needed: for a circle I = J/2.
- Forgetting that transverse shear and torsion shear add on one side and subtract on the other.

**8. Summary.** σ from F and M, τ from T and V, at the same point; then Mohr; then Tresca/von Mises.

### B. Solved questions

#### Q21 (Slides Ch6, Beer) — Torque for yield by Tresca with an axial load of 240 kN *(medium)*
**Problem.** A 38 mm shaft AB of steel (Y = 250 MPa) carries P = 240 kN. Using the maximum-shear-stress criterion, find the torque T at which yield occurs.

**Solution.**
1. $A = \frac\pi4(38)^2 = 1134.1$ mm², so σ = 240 000/1134.1 = 211.6 MPa.
2. Tresca: $2R = \sqrt{\sigma^2 + 4\tau^2} = Y$, so $\tau = \tfrac12\sqrt{250^2 - 211.6^2} = 66.6$ MPa.
3. $T = \tau J/c = \tau\pi d^3/16 = 66.6\pi(38)^3/16$.

$$\boxed{T = 717\ \text{N·m}}$$

**Exam takeaway.** A large axial stress leaves little room for torsion: here σ alone uses 85% of Y.

---

#### Q22 (Slides Ch6, Hibbeler) — Helicopter rotor shaft *(easy)*
**Problem.** A 50 mm rotor shaft transmits T = 2.4 kN·m with a tensile force P = 125 kN. Find the maximum tensile stress, maximum compressive stress and maximum shear stress.

**Solution.**
1. $\sigma = \dfrac{125\,000}{\frac\pi4(50)^2} = 63.66$ MPa and $\tau = \dfrac{16(2.4\times10^6)}{\pi(50)^3} = 97.78$ MPa.
2. $R = \sqrt{31.83^2 + 97.78^2} = 102.8$ MPa.

$$\boxed{\sigma_1 = 134.7\ \text{MPa},\quad \sigma_2 = -71.0\ \text{MPa},\quad \tau_{max} = 102.8\ \text{MPa}}$$

**Check.** Matches the slide (135 and −71 MPa) ✓.

---

#### Q23 (PYQ 2014-15 Test-2 Q1) — Axial force + torque: principal stresses
Solved in Ch. 4 Q15: σ₁ = 76.8 MPa and σ₂ = −5.2 MPa, with θp = 14.5° from the axis.

---

#### Q24 (PYQ 2021-22 Compre A Q1) — Strain gauge at 45°: find G
Solved in Ch. 4 Q30: G = 29.1 GPa.

---

#### Q25 (PYQ 2021-22 Compre A Q2) — Automobile axle: stress at H, principal stresses, von Mises *(medium, 10 marks)*
**Problem.** A solid 32 mm axle carries, at the wheel end, 3 kN ↑ and a 350 N·m torque, and 3 kN ↓ at 0.15 m from the wheel. H is on top of the axle, 0.2 m beyond the 3 kN ↓ load. σY = 350 MPa. Find (a) the state of stress at H, (b) the principal stresses and (c) whether the axle yields by von Mises.

**Solution.**
1. *Internal forces at H* (from the wheel side): V = 3 − 3 = 0 (no transverse shear). M = 3(0.35) − 3(0.20) = 0.45 kN·m (the two 3 kN forces form a constant couple beyond the second load). T = 350 N·m.
2. *(a) Stresses at H (top fibre):* $\sigma = \dfrac{32(450\,000)}{\pi(32)^3} = 139.9$ MPa, compression at the top (sagging), and $\tau = \dfrac{16(350\,000)}{\pi(32)^3} = 54.4$ MPa.
3. *(b)* Centre −69.9, R = 88.6, so σ₁ = 18.7 MPa, σ₂ = −158.5 MPa and τmax = 88.6 MPa.
4. *(c)* $\sigma_{vm} = \sqrt{139.9^2 + 3(54.4)^2} = 168.7$ MPa < 350.

$$\boxed{(a)\ \sigma = -139.9\ \text{MPa},\ \tau = 54.4\ \text{MPa};\quad (b)\ 18.7,\ -158.5\ \text{MPa};\quad (c)\ \text{no yield (FS} = 2.07)}$$

**Exam takeaway.** Two equal and opposite forces make a constant bending moment between them, so V = 0 at H.

---

#### Q26 (PYQ 2023-24 Compre B Q2) — Crank on a 20 mm shaft: reactions and elements E₁ and E₂ *(hard, 20 marks)*
**Problem.** A crank loaded by F = 2 kN twists and bends a 20 mm shaft fixed at the origin A. The shaft AB runs 125 mm along x from the wall; a crank arm BC (6 × 30 mm) is 100 mm long; at C a pin parallel to x carries F (downward, −y) at 38 mm along the pin. (a) Draw the FBD of AB and find the reactions at A. (b) Find the stresses on elements E₁ (on the y-axis) and E₂ (on the z-axis) at A. (c) Show them on 2-D elements. (d) Find the maximum and minimum normal stresses and the maximum shear at E₁.

**Approach.** The load point is at x = 125 + 38 = 163 mm from A and offset 100 mm in z (reading of the figure).

**Solution.**
1. *(a) Reactions at A:* $R_y = +2$ kN. Twisting moment T = F(100) = 200 N·m. Bending moment $M_z = F(163) = 326$ N·m (hogging: top in tension).
2. *(b) Stresses at A:* $\sigma_b = \dfrac{32(326\,000)}{\pi(20)^3} = 415$ MPa; $\tau_T = \dfrac{16(200\,000)}{\pi(20)^3} = 127.3$ MPa; $\tau_V = \dfrac{4(2000)}{3\pi(100)} = 8.5$ MPa.

| Element | σx | τ |
|---|---|---|
| E₁ (top, on y-axis) | +415 MPa (tension) | 127.3 MPa (torsion only; transverse shear is 0 at the top) |
| E₂ (side, on z-axis = neutral axis) | 0 | 127.3 + 8.5 = 135.8 MPa (they add on this side; 118.8 MPa on the opposite side) |

3. *(c)* E₁ is viewed from +y, with σ along x and τ on the x-faces in the z direction. E₂ is viewed from +z, with τ on the x-faces in the y direction.
4. *(d) At E₁:* centre 207.5, $R = \sqrt{207.5^2 + 127.3^2} = 243.5$, so σmax = 451 MPa, σmin = −35.9 MPa and τmax = 243.5 MPa.

$$\boxed{E_1:\ \sigma_{max} = 451\ \text{MPa},\ \sigma_{min} = -35.9\ \text{MPa},\ \tau_{max} = 243.5\ \text{MPa};\qquad E_2:\ \tau = 135.8\ \text{MPa}}$$

**Exam takeaway.** The examiner tests *where* each stress peaks: bending at E₁, transverse shear at E₂, torsion equal at both.

---

#### Q27 (PYQ 2024-25 Compre B Q2) — L-shaped post: F, V, M and T at z–z; stresses at B; principal stresses; von Mises FS *(hard, 18 marks)*
**Problem.** Loads P = 400π N and R = 800π N act at the free end of a 50 mm diameter post, which has a vertical stem (axis x) and a 0.4 m horizontal arm at the top. Section z–z is 0.6 m below the free end. Point B is on the outer surface, on the diametral line z–z. σY = 140 MPa. Find (a) F, V, Mb and T at z–z, (b) the stresses at B on a 2-D element, (c) the principal stresses and τmax at B and (d) the von Mises factor of safety.

**Approach.** Reading of the figure: the arm runs along z, P acts along −y and R downward (−x). If your figure differs, rerun the same steps.

**Solution.**
1. *(a) Section forces* ($\mathbf M = \mathbf r\times\mathbf F$, with $\mathbf r = (0.6, 0, 0.4)$ m and $\mathbf F = (-800\pi, -400\pi, 0)$ N): axial F = −800π = −2513 N (compression); shear V = 400π = 1257 N (y-direction); $\mathbf M = (160\pi, -320\pi, -240\pi)$ N·m, so T = 160π = 502.7 N·m, $M_y = 320\pi = 1005$ N·m and $M_z = 240\pi = 754$ N·m (resultant $M_b = 400\pi = 1257$ N·m).
2. *(b) Stresses at B* (on the z-axis, so only My bends B, and B is on the neutral axis of Mz, where the y-shear peaks). With A = 625π mm² and πd³/32 = 3906π mm³ (the π's cancel, which is why they are in the data):
   - $\sigma_{axial} = -800\pi/625\pi = -1.28$ MPa
   - $\sigma_{bend} = -320\pi\times10^3/3906\pi = -81.92$ MPa (the downward R on the +z arm compresses the +z side)
   - $\tau_T = 160\pi\times10^3/7812\pi = 20.48$ MPa
   - $\tau_V = 4V/3A = 0.853$ MPa (adds to torsion at B)
   
   So σx = −83.2 MPa and τ = 21.3 MPa.
3. *(c)* Centre −41.6, R = 46.75, so σ₁ = 5.15 MPa, σ₂ = −88.35 MPa and τmax = 46.75 MPa.
4. *(d)* $\sigma_{vm} = \sqrt{83.2^2 + 3(21.3)^2} = 91.0$ MPa, so FS = 140/91.0 = 1.54.

$$\boxed{\sigma_x = -83.2\ \text{MPa},\ \tau = 21.3\ \text{MPa};\quad \sigma_{1,2} = 5.15,\ -88.35\ \text{MPa};\quad \tau_{max} = 46.8\ \text{MPa};\quad FS = 1.54}$$

**Exam takeaway.** π-multiples in the data are a hint that the areas and moduli will cancel nicely; it is also a check that you used the right formula.

---

## Chapter 6 — Formula and convention sheet

| Item | Formula |
|---|---|
| Kinematics | sections stay plane and undistorted; $\gamma = r\,d\phi/dz$ |
| Torsion formula | $T/J = \tau/r = G\phi/L$ |
| Solid | $J = \pi d^4/32$; $\tau_{max} = 16T/\pi d^3$ |
| Hollow | $J = \pi(d_o^4 - d_i^4)/32$; $\tau_{min} = \tau_{max}d_i/d_o$ |
| Thin tube | $J \approx 2\pi r_m^3t$, $\tau \approx T/(2\pi r_m^2t)$ |
| Twist | $\phi = \sum T_iL_i/(G_iJ_i)$ with **internal**, signed torques |
| Stiffness | $k_T = GJ/L$ |
| Power | $P = T\omega = 2\pi nT/60$ (n in rpm) |
| Gears | $T_C/T_B = r_C/r_B$; $r_B\phi_B = r_C\phi_C$; far shaft flexibility × (gear ratio)² |
| Fixed–fixed, one torque | $T_A = T_0b/L$, $T_D = T_0a/L$ |
| Composite shaft | $T_i = T(GJ)_i/\sum(GJ)$ |
| Energy | $U = \sum T^2L/(2GJ)$ |
| Pure-torsion element | principal ±τ at 45°; gauge at 45° reads γ/2 |
| Combined σ + τ | $\sigma_{1,2} = \sigma/2 \pm \sqrt{(\sigma/2)^2 + \tau^2}$; vM $\sqrt{\sigma^2 + 3\tau^2}$; Tresca $\sqrt{\sigma^2 + 4\tau^2}$ |
| Bending + torsion (solid) | $\tau_{max} = \frac{16}{\pi d^3}\sqrt{M^2 + T^2}$, $\sigma_1 = \frac{16}{\pi d^3}(M + \sqrt{M^2 + T^2})$ |
| Transverse shear (solid circle) | $\tau_{V,max} = 4V/3A$ at the neutral axis |
