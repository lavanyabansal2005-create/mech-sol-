# ME F211 Mechanics of Solids — Exam Study Guide (Ch 1–6)

Built from the uploaded lecture slides (Ch 1–6), Crandall, Dahl & Lardner *An Introduction to the Mechanics of Solids* (2nd ed., SI), and six previous-year papers (2014-15 Test-1/Test-2/Compre, 2019-20, 2021-22, 2023-24 and 2024-25 Compre).

Each chapter file follows the same layout for every concept: **Part A** (intuition → why it matters → formal treatment and conventions → derivations → picture → special cases → traps → summary box), then **Part B** (solved questions: slides → Crandall → PYQs, easy → hard, with given/asked, approach, solution, boxed answer, sanity check and exam takeaway).

| File | Topics | Solved Qs |
|---|---|---|
| [ch1-equilibrium-friction-trusses.md](ch1-equilibrium-friction-trusses.md) | FBDs, equilibrium, 2- and 3-force members, Coulomb and belt friction, trusses (joints, sections, zero-force members) | 20 |
| [ch2-deformable-bodies-axial-energy.md](ch2-deformable-bodies-axial-energy.md) | 3-step method, δ = PL/AE, indeterminate bars, displacement diagrams, strain energy, Castigliano | 16 |
| [ch3-slender-members-sfd-bmd.md](ch3-slender-members-sfd-bmd.md) | Internal F/V/M, SFD and BMD, distributed loads, q–V–M relations, singularity functions, frames, curved and 3-D members | 19 |
| [ch4-stress-strain-mohr.md](ch4-stress-strain-mohr.md) | Stress tensor, transformation, Mohr's circle, principal and max-shear stresses, strain, strain Mohr's circle, rosettes | 16 |
| [ch5-stress-strain-temperature-yield.md](ch5-stress-strain-temperature-yield.md) | Tensile test, Hooke + Poisson, E–G–ν, ΔV, thermal stresses, strain energy, Tresca and von Mises | 15 |
| [ch6-torsion.md](ch6-torsion.md) | τ = Tr/J, twist, hollow vs solid, power, gears, indeterminate shafts, combined loading and yield | 26 |

**Word edition:** [ME_F211_Study_Guide_Ch1-6.docx](ME_F211_Study_Guide_Ch1-6.docx) (and a [PDF copy](ME_F211_Study_Guide_Ch1-6.pdf)) has all six chapters in one file, with the original problem figure under every question and worked diagrams (FBDs, truss force maps, SFD/BMD, torque diagrams, Mohr's circles, stress elements).

Math is in LaTeX (`$…$`). It renders on GitHub, in VS Code's Markdown preview, Obsidian and Typora.

> ⚠️ **Scope warning.** The compre papers cover the **whole course**. About **40% of PYQ marks** come from chapters **after** Ch 6 (bending stress σ = My/I, beam deflection and indeterminate beams, curved beams, Euler buckling). Those slides weren't uploaded, so those questions are listed below but not solved here.

---

## Part 1 — One-page formula and convention sheet (Ch 1–6)

### Conventions you must not mix up
| Item | Convention used in the slides/Crandall |
|---|---|
| Stress/force sign | + on a **positive face in a positive direction** (or −face, −direction). Tension +. |
| Shear force V (Ch 3) | Crandall: $V = -\Sigma(\text{up-forces left of cut})$, $dV/dx=-q$, $dM/dx=-V$. **Opposite sign to Gere/Hibbeler.** M is the same (sagging +). |
| Angle θ (Ch 4) | counter-clockwise from x to the **normal** of the face |
| Mohr's circle | σ to the right; **+τ_xy plotted downward at X**, upward at Y; rotating 2θ on the circle = rotating θ on the element, **same sense** |
| Strain circle | vertical axis = **γ/2** |
| Torque | right-hand rule; internal torque + if its vector points out of the cut face |

### Ch 1 — Statics
$\sum F_x=\sum F_y=\sum M=0$ · two-force member: forces collinear · three-force: concurrent · $f\le\mu N$ (= at impending) · incline: $T=W(\sin\alpha\pm\mu\cos\alpha)$ · belt: $T_2/T_1=e^{\mu\beta}$ · truss: $m=2j-3$; sections: cut ≤ 3 members, moments about the intersection of two.

### Ch 2 — Axial members and energy
$\delta=\sum\frac{P_iL_i}{A_iE_i}$ (internal P) · $k=AE/L$ · parallel: $k$ adds; series: $1/k$ adds · indeterminate: $\delta_{load}+\delta_{redundant}=0$ · displacement diagram: $\delta_{bar}=\mathbf u\cdot\mathbf e$ · $U=P^2L/2AE$ · Castigliano $\delta_i=\partial U/\partial F_i$; truss $\delta=\sum F\frac{\partial F}{\partial P}\frac{L}{AE}$; beam $\int\frac{M}{EI}\frac{\partial M}{\partial P}ds$ · thin ring $\sigma=pr/t$, $\delta_R=pr^2/Et$.

### Ch 3 — Internal forces
Resultant of distributed load = area at the centroid (**reactions only**) · $V'=-q$, $M'=-V$ · $M_{max}$ where V = 0 · contraflexure where M changes sign · clockwise couple: M jumps up · singularity: $\langle x-a\rangle^n$, point load $\langle\rangle_{-1}$, couple $\langle\rangle_{-2}$, no constants · standard: SS + W centre $WL/4$; SS + UDL $wL^2/8$; SS + W at a $Wab/L$; cantilever tip $PL$; cantilever UDL $wL^2/2$ · curved cantilever (tip P): $N=P\cos\theta$, $V=P\sin\theta$, $M=PR\cos\theta$.

### Ch 4 — Stress/strain transformation
$\sigma_{x'}=\frac{\sigma_x+\sigma_y}{2}+\frac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta$ · $\tau_{x'y'}=-\frac{\sigma_x-\sigma_y}{2}\sin2\theta+\tau_{xy}\cos2\theta$ · $\sigma_{x'}+\sigma_{y'}$ = const ·
$\sigma_{1,2}=\bar\sigma\pm R$, $R=\sqrt{(\frac{\sigma_x-\sigma_y}{2})^2+\tau_{xy}^2}$, $\tan2\theta_p=\frac{2\tau_{xy}}{\sigma_x-\sigma_y}$ (substitute back to identify σ₁) · $\tau_{max}=R$ at $\theta_p\pm45°$, with $\bar\sigma$ on those faces · **absolute** $\tau_{max}=(\sigma_{max}-\sigma_{min})/2$ including $\sigma_3=0$ ·
strain: replace σ→ε, τ→γ/2 · $\epsilon_x=\partial u/\partial x$, $\gamma_{xy}=\partial u/\partial y+\partial v/\partial x$ · 45° rosette $\gamma=2\epsilon_b-\epsilon_a-\epsilon_c$ · 60° rosette $\epsilon_y=\frac13(2\epsilon_b+2\epsilon_c-\epsilon_a)$, $\gamma=\frac{2}{\sqrt3}(\epsilon_b-\epsilon_c)$.

### Ch 5 — Constitutive law and yield
$\epsilon_x=\frac1E[\sigma_x-\nu(\sigma_y+\sigma_z)]+\alpha\Delta T$ · $\gamma=\tau/G$ · plane stress: $\sigma_x=\frac{E}{1-\nu^2}(\epsilon_x+\nu\epsilon_y)$, $\epsilon_z=-\frac{\nu}{E}(\sigma_x+\sigma_y)$ · $G=\frac{E}{2(1+\nu)}$, $K=\frac{E}{3(1-2\nu)}$ · $\Delta V/V=\frac{1-2\nu}{E}\sum\sigma$ · fixed bar heated: $\sigma=-E\alpha\Delta T$ · $u=\frac{1}{2E}[\sum\sigma_i^2-2\nu\sum\sigma_i\sigma_j]$ ·
**Tresca** $\sigma_{max}-\sigma_{min}=\sigma_Y$ (σ–τ: $\sqrt{\sigma^2+4\tau^2}$) · **von Mises** $\sqrt{\sigma_1^2-\sigma_1\sigma_2+\sigma_2^2}$ = $\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}$ (σ–τ: $\sqrt{\sigma^2+3\tau^2}$) · FS = $\sigma_Y/\sigma_{eq}$; Tresca is always more conservative.

### Ch 6 — Torsion
$\gamma=r\,d\phi/dz$ · $\frac TJ=\frac\tau r=\frac{G\phi}{L}$ · $J=\frac{\pi d^4}{32}$, $J_h=\frac{\pi(d_o^4-d_i^4)}{32}$ · $\tau_{max}=\frac{16T}{\pi d^3}$ · $\phi=\sum\frac{TL}{GJ}$ · $P=\frac{2\pi nT}{60}$ · gears: $T\propto r$, $r_B\phi_B=r_C\phi_C$ · fixed–fixed: $T_A=T_0b/L$ · $U=\sum\frac{T^2L}{2GJ}$ · pure shear: principal ±τ at 45° · combined: $\sigma=\frac FA\pm\frac{32M}{\pi d^3}$, $\tau=\frac{16T}{\pi d^3}\pm\frac{4V}{3A}$ (at the neutral axis).

### Units cheat
N, mm, MPa (= N/mm²) are consistent; GPa = 10³ MPa; kN·m = 10⁶ N·mm; angles in **radians** inside formulas; P = Tω needs ω in rad/s.

---

## Part 2 — PYQ question types ranked by frequency

Counted across the 7 papers supplied (2014-15 Test-1, Test-2, Compre; 2019-20, 2021-22, 2023-24, 2024-25 Compre). "Appearances" counts distinct questions, including sub-parts embedded in bigger questions.

| Rank | Question type | Appearances | Where | Solved in |
|---|---|---|---|---|
| 1 | **Euler buckling of columns** (often combined with a beam that loads the column) | 8 | 19 B1, 21 A3, 21 B3, 23 B1, 24 A3, 24 B3, 14 C-A20, 14 C-B4 | *not in Ch 1–6 slides* |
| 2 | **Torsion of circular shafts** (allowable T, twist, hollow vs solid, gears, fixed–fixed) | 7 | 14 T2-Q4, 14 C-A5, 14 C-B2, 19 B4, 21 A1, 23 A1, 24 B1 | Ch 6 Q12–Q14, Q17, Q18, Q20; Ch 4 Q13 |
| 3 | **Beam deflection / statically indeterminate beams** (integration, singularity functions, settlement, beam + rod) | 7 | 14 C-A9/10/15/16, 19 B3, 21 B2, 21 B3, 23 B3, 24 B3 | *not in Ch 1–6 slides* (SFD/BMD groundwork in Ch 3) |
| 4 | **Combined loading at a point** (find F, V, M, T at a section → σ, τ on a 2-D element → principal stresses → FS) | 6 | 14 T2-Q1, 19 B2, 21 A2, 21 B4, 23 B2, 24 B2 | Ch 6 Q23–Q26; Ch 4 Q8 |
| 5 | **Principal stresses / Mohr's circle / transformation** (stand-alone) | 5 | 14 C-A12, 14 C-A13, 14 C-B1, 19 A2, 14 T2-Q2 | Ch 4 Q6–Q9, Q14, Q16 |
| 5 | **Yield criteria and factor of safety** (Tresca, von Mises) | 5 | 14 C-A3, 14 C-A4, 19 A4, 21 A2c, 24 B2d | Ch 5 Q12–Q15; Ch 6 Q24, Q26 |
| 5 | **Bending stress / curved beams / eccentric loads** (σ = My/I, T-sections, chain link) | 5 | 14 C-A19, 14 C-B3, 19 A1b, 23 A2, 24 A1 | partly (Ch 3 Q18 uses σ = 32M/πd³); rest *not in slides* |
| 8 | **Generalized Hooke's law: Δ-dimensions, Δt, ΔV, circle → ellipse** | 4 | 14 C-A2, 21 B1, 23 A3, 24 A2 | Ch 5 Q1–Q3; Ch 4 Q15 |
| 8 | **SFD/BMD, contraflexure, singularity functions** | 4 papers (6 Qs) | 14 T1-Q4, 14 C-A6/7/14/17/18, 19 A1 | Ch 3 Q4, Q5, Q16–Q18 |
| 10 | **Strain energy / Castigliano** | 3 | 14 T1-Q2, 19 A3b, 24 B1c | Ch 2 Q11, Q12; Ch 6 Q20 |
| 11 | **Thermal stresses** | 2 | 14 T2-Q3, 14 C-A1 | Ch 5 Q5, Q11 |
| 12 | Trusses (sections) · friction + axial (rope on drum) · thin ring · strain gauge/rosette · axial stress ratio | 1 each | 14 T1-Q1, 14 T1-Q3, 14 C-A11, 21 A1, 14 C-A8 | Ch 1 Q20, Q11; Ch 2 Q16, PYQ A-Q8; Ch 4 Q13 |

**What this tells you for the compre:**
1. **Combined loading + Mohr + yield** shows up in every recent Part B (2019, 2021, 2023, 2024), worth 18–20 marks each time. Practise the 6-step procedure in Ch 6 Concept 6.5 until it's automatic.
2. **Torsion** appears in nearly every paper, usually as one clean 10–12 mark question (fixed–fixed shaft, gear pair, or allowable T + twist).
3. **Hooke's-law plate questions** (Δt, ΔV, etched circle) are a near-certain 10 marks in Part A (2021, 2023, 2024).
4. **Buckling and beam deflection** together are the biggest block, and they are **outside** these slides. Study them next.
5. Test-1 style (2014) puts trusses, friction, Castigliano and singularity SFD/BMD together, so Ch 1–3 matter most for the mid-sem.

---

## Part 3 — Errors found in the slides (double-check with your instructor)

| Location | Slide says | Correct value | Why |
|---|---|---|---|
| Ch 1, Warren truss (2000 N/4000 N) table | BE = 500 N (C) | **577.4 N (C)** | 500 N is the *vertical component*; member force = 500/sin 60° |
| Ch 1, A-frame truss table | member "AB" | **AC** | there is no member AB |
| Ch 2, brass bar 50/80/40/10 kN | δ = 0.2857 mm | **0.114 mm** | 0.2857 is the AB segment alone; BC (−30 kN) and CD (+10 kN) were dropped |
| Ch 2, member ABCD | 0.4903 **m** | 0.491 **mm** | units typo |
| Ch 4 Part 2, rosette example | ε₂ = **246** − 119.2 | **153** − 119.2 = 33.8 μ | 153 is the circle centre; final value is right |
| 2023-24 Compre A-Q3 | E = 200 **MPa** | E = 200 **GPa** | steel |

---

## Part 4 — PYQ questions not covered here (topics after Ch 6)

| Paper | Question | Topic needed |
|---|---|---|
| 2014-15 Compre A | Q9, Q10 (cantilever tip deflection/slope), Q15–16 (propped cantilever), Q19 (bending/shear ratio), Q20 (buckling) | Ch 7 (bending), Ch 8 (deflection), Ch 9 (buckling) |
| 2014-15 Compre B | Q3 (inverted-T beam stresses), Q4 (buckling from deflection data) | Ch 7, Ch 9 |
| 2019-20 | A-Q1(b) (partly done in Ch 3 Q18), B-Q1 (two columns), B-Q2 (box-beam combined loading needs I and Q of a box section), B-Q3 (beam + rod, 4th-order ODE) | Ch 7–9 |
| 2021-22 | A-Q3, B-Q2, B-Q3, B-Q4 | Ch 7–9 |
| 2023-24 | A-Q2 (eccentric pull on a post), B-Q1 (spreader buckling), B-Q3 (singularity deflection with settlement) | Ch 7–9 |
| 2024-25 | A-Q1 (curved chain link), A-Q3, B-Q3 | Ch 7–9 |

Say the word and the next session can cover Ch 7–9 (bending stresses, beam deflection, buckling) in the same format, starting with these questions.
