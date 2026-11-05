# Chapter 1 — Fundamental Principles of Mechanics
### Force systems, free-body diagrams, equilibrium, dry friction, plane trusses

**Sources used:** Slides "chapter 1 slides" (Dr. Sharad Shrivastava); Crandall, Dahl & Lardner Ch. 1 (§1.1–1.8, Probs 1.7, 1.10, 1.13, 1.21, 1.31, 1.37, 1.39, 1.42, 1.45); PYQ 2014-15 Test-1 (Q1, Q3).

**How to read this chapter.** Every concept has a **Part A** with eight numbered items (intuition → why it matters → formal treatment → derivation → picture → special cases → traps → summary box). It is followed by **Part B**, the solved questions: slides first, then Crandall, then PYQs, each group running easy → hard. Every solved question uses the same template:

> **Problem** (restated) · **Given / Find** (with units) · **Approach** (which idea and why) · **FBD in words** · **Solution** (numbered steps, every substitution shown) · **Answer** (boxed) · **Check** (does it make sense? second method where possible) · **Exam takeaway** (what is really tested, plus a likely variation).

---

## Concept 1.1 — What mechanics of solids is, and how to attack any problem

### A. Concept explanation

**1. Intuition.** Put four books on a bookshelf. *Statics* tells you how hard each bracket must push up so that the shelf doesn't fall. *Mechanics of solids* asks the next questions. How much does the plank sag? How hard are the wood fibres being stretched at the bottom of the plank? Will it crack, and where first? The slides make the same point with a beam carrying four loads of $w/4$. Equilibrium gives the support reactions. But as those loads travel through the material to the supports, the material "develops resisting forces, generates stresses and undergoes deformation". That internal story is the subject of this course.

**2. Why it matters.** Every later chapter starts from correct external forces. Ch. 2 turns them into elongations, Ch. 3 into internal shear forces and bending moments, Ch. 4 into stresses, Ch. 5 into strains and failure checks, Ch. 6 into twist. If the free-body diagram (FBD) is wrong, every number after it is wrong. In the compre papers roughly a quarter of the marks on most long questions go to "draw the FBD and find the reactions".

**3. Formal treatment.**

*(a) The slides' five-step procedure (applied mechanics in general):*
1. Select the system of interest.
2. Idealize it (simplify: rigid bars, point loads, frictionless pins, weightless members …).
3. Apply the principles of mechanics to predict behaviour.
4. Compare the predictions with the real system (tests and experiments).
5. If they don't agree, construct a different idealized model and repeat.

The slides note that in research, steps 1 and 2 are the hardest.

*(b) Crandall's working version for a single problem (§1.8):*
1. Select the system and draw it (to scale where possible).
2. Isolate it: show every force the surroundings exert on it. Involve as many of the desired unknowns and given data as possible, and as few other quantities as possible.
3. Postulate the characteristics of the system, i.e. idealize it.
4. Apply the principles of mechanics. **Count unknowns against independent equations**; if there are too many unknowns, pick additional subsystems.
5. Reduce the result to **symbolic form first**. Check limiting cases and dimensional consistency.
6. Substitute numbers and **compare with intuition and order of magnitude**. Ask: "would a bar this size hold a mosquito, a mouse, a man, a car, a truck?"
7. Compare with the real system (test).
8. If anything is unsatisfactory, go back and reconsider the system choice or the idealization.

*(c) Two kinds of motion.* A body can (i) change position overall or (ii) change shape locally (deformation). This course deals with **static** situations and **small deformations**.

*(d) Rigid body.* The distance between any two points never changes. No real structure is rigid. But a lever carrying weights bends so little that the lever arm stays $L/2$, so for its **equilibrium** we may treat it as rigid. For its **strength** we must not, because the strength depends on the small deformation.

*(e) Principle of transmissibility.* A force may be slid along its own line of action without changing its effect on a **rigid** body. The slide's example: pushing a truck at the front bumper has the same effect as pulling it with the same force at the rear bumper.

**4. Derivation — why transmissibility works (and when it fails).** Slide a force $\mathbf F$ from point A to point B on the same line of action, so $\mathbf r_B = \mathbf r_A + \lambda\mathbf e$ with $\mathbf e \parallel \mathbf F$.
- The force sum is unchanged, because it is the same vector.
- The moment about any point O is $\mathbf r_B\times\mathbf F = \mathbf r_A\times\mathbf F + \lambda\,\mathbf e\times\mathbf F = \mathbf r_A\times\mathbf F$, since $\mathbf e\times\mathbf F = 0$.

So the **external** resultant force and moment, which are all a rigid body "feels", are unchanged. ∎

**Inside** a deformable body the story differs. Pulling a rubber band at its far end stretches the whole band. Pushing at its near end with the same force stretches nothing. The resultants are equal but the deformations differ.

**5. Picture.** Draw the truck twice: once with an arrow pushing on the rear bumper, once with the same arrow pulling on the front bumper, both on one horizontal line. The truck's motion is identical. Now draw a spring between the bumpers. In one case it is compressed and in the other stretched.

**6. Special / limiting cases.**
- Stiffness → ∞ is the rigid-body limit. It always gives the correct reactions for **statically determinate** systems.
- It cannot give the forces in **statically indeterminate** systems (more unknown reactions than equations). There, the way the members deform decides how the load is shared (Ch. 2).

**7. Common traps.**
- Using transmissibility to move a load along a beam before computing bending moment. **Never.** The moment diagram changes.
- Replacing a distributed load by its resultant *before* cutting the beam. This is fine for reactions, wrong for internal forces (Ch. 3).
- Plugging numbers in too early. You lose the chance to check limiting cases and dimensions (Crandall step 5).

**8. Summary box**

| Idea | Valid for | Not valid for |
|---|---|---|
| Rigid-body idealization | reactions of determinate structures | deformations; indeterminate structures |
| Transmissibility | external equilibrium of rigid bodies | internal forces, stresses, deformation |
| Deformable-body analysis | internal forces, stresses, deflections, indeterminate problems | — |

---

## Concept 1.2 — Forces, moments, couples and equivalent force systems

### A. Concept explanation

**1. Intuition.** Loosen a nut with a spanner. Pushing near the nut does almost nothing, and pushing at the end of the handle turns it easily. The *same* force has a different turning effect depending on how far its line of action is from the nut. That turning effect is the **moment**. If you turn a steering wheel with two hands, pushing up with one and down with the other, the wheel turns but is not pushed sideways. That pure turning effect is a **couple**.

**2. Why it matters.** Every equilibrium equation contains moments. Replacing a load by "a force plus a couple at another point" is exactly what we do at a cut in Ch. 3, where the force-couple system at the cut *is* the set of internal forces ($F, V, M_b, M_t$). Offset loads (brackets, cranks, arms welded to beams) appear in almost every PYQ and are handled this way.

**3. Formal treatment.**
- **Force:** a vector with magnitude, direction and line of action. In 2-D, $\mathbf F = F_x\mathbf i + F_y\mathbf j$.
- **Moment of a force about a point O:** $\mathbf M_O = \mathbf r\times\mathbf F$, where $\mathbf r$ runs from O to *any* point on the line of action. Its magnitude is $|\mathbf M_O| = F\,d$, with $d$ the **perpendicular** distance from O to the line of action. In 2-D, use $M_O = xF_y - yF_x$, counter-clockwise positive.
- **Moment about an axis** through O with unit vector $\mathbf n$: $M_n = \mathbf n\cdot(\mathbf r\times\mathbf F)$. This is what twists a shaft.
- **Couple:** two equal, opposite, non-collinear forces $F$ a distance $d$ apart. Its moment is $C = Fd$, the **same about every point**, so a couple can be moved anywhere on a rigid body (it is a "free vector"). The resultant force of a couple is zero.
- **Varignon's theorem:** the moment of a resultant equals the sum of the moments of its components, $\mathbf r\times(\mathbf F_1+\mathbf F_2) = \mathbf r\times\mathbf F_1+\mathbf r\times\mathbf F_2$ (Crandall Prob 1.3).
- **Equivalent force systems:** two systems have the same effect on a rigid body if and only if they have the same resultant force **and** the same resultant moment about one (hence every) point.
- **Force-couple system:** a force $\mathbf F$ acting at A is equivalent to the same $\mathbf F$ at O plus a couple $\mathbf M_O = \mathbf r_{OA}\times\mathbf F$.

**4. Derivations.**

*(a) A couple's moment is the same about every point.* Forces $\mathbf F$ at $\mathbf r_1$ and $-\mathbf F$ at $\mathbf r_2$:
$$\mathbf M_O = \mathbf r_1\times\mathbf F + \mathbf r_2\times(-\mathbf F) = (\mathbf r_1-\mathbf r_2)\times\mathbf F$$
This depends only on the separation $\mathbf r_1-\mathbf r_2$, not on O. ∎

*(b) Moving a force sideways.* Take $\mathbf F$ at A. Add $+\mathbf F$ and $-\mathbf F$ at O; adding zero changes nothing. The original $\mathbf F$ at A and the $-\mathbf F$ at O form a couple $\mathbf r_{OA}\times\mathbf F$. What remains is $\mathbf F$ at O plus that couple. ∎

*(c) The reverse (Crandall Prob 1.10).* A coplanar force $F$ and couple $M$ at the same point can be replaced by the single force $F$ moved sideways by
$$a = \frac{|M|}{|F|}$$
It is moved to the side that makes $F$'s new moment about the original point have the same sense as $M$. This is how an eccentric load is created: a column carrying a load $P$ off its axis feels $P$ on the axis plus a couple $Pe$ (PYQ 2023-24 A-Q2, post pulled by a sling).

**5. Picture / graphical method.** To get a 2-D moment quickly, resolve the force into $F_x$ and $F_y$ at a convenient point on its line of action. Then take each component times its own perpendicular arm, using a "which way would it spin the page?" sign. This is the same as $M_O = xF_y - yF_x$ and avoids hunting for the perpendicular distance.

**6. Special cases.**
- A force whose line of action passes through O has zero moment about O. Choose moment points so that unknown forces pass through them.
- A couple has no force sum, so it never appears in $\sum F_x$ or $\sum F_y$, only in $\sum M$.
- Parallel forces reduce to a single resultant at a definite point (Ch. 3: the resultant of a distributed load acts at its centroid).

**7. Common traps.**
- Using the slant distance instead of the **perpendicular** distance.
- Dropping an applied couple from $\sum M$, or adding it to $\sum F$.
- Sign slips: decide counter-clockwise positive once and stick to it.
- Unit slips: kN × mm = N·m, not kN·m.

**8. Summary box**
$$M_O = Fd = xF_y - yF_x,\qquad C = Fd\ \text{(couple; same about every point)},\qquad F@A \equiv F@O + \mathbf r_{OA}\times\mathbf F,\qquad a = |M|/|F|$$

### B. Solved questions

#### Q1 (Crandall Prob 1.10) — Replace a force and a couple by a single displaced force *(easy, derivation)*
**Problem.** A coplanar force $\mathbf F$ and a moment $M$ act at the same point O. Show that they may be replaced by an equal force displaced sideways a distance $a = |M|/|F|$, and decide which side it goes.

**Given:** $\mathbf F$ (magnitude $F$) at O and a couple $M$ (counter-clockwise, say). **Find:** the single equivalent force and its offset.

**Approach.** Equivalent systems must have the same resultant force and the same moment about one point (Concept 1.2, item 3).

**Solution.**
1. *Resultant force.* The couple contributes nothing to the force sum, so the replacement force must be $\mathbf F$ itself.
2. *Moment about O.* The original system has moment $M$ about O. A force $\mathbf F$ whose line of action is a perpendicular distance $a$ from O has moment $\pm Fa$ about O.
3. *Match the moments.* Set $Fa = |M|$, so $a = |M|/F$.
4. *Side.* With M counter-clockwise, put the line of action on the side where $\mathbf F$ spins the page counter-clockwise about O. For example, if $\mathbf F$ points in $+x$, shift it **down** by $a$, since a $+x$ force below O turns counter-clockwise about O.

$$\boxed{\ \mathbf F \text{ displaced by } a = \frac{|M|}{|F|},\ \text{on the side that reproduces the sense of } M\ }$$

**Check.** As $M\to 0$, $a\to 0$, so we recover the original force ✓. As $F\to 0$ with $M$ fixed, $a\to\infty$: a pure couple cannot be replaced by a single finite force ✓.

**Exam takeaway.** This is the eccentric-load idea. A load $P$ applied at offset $e$ equals $P$ on the axis plus $M = Pe$. **Variation:** "A 26 kN force acts on a bracket 75 mm off the beam axis. Replace it by a force and couple at the section centroid" (PYQ 2019-20 B-Q2 begins exactly like this).

---

## Concept 1.3 — Supports, free-body diagrams and equilibrium

### A. Concept explanation

**1. Intuition.** An FBD is like cutting the object out of a photograph with scissors. Everything that was touching it (the floor, a pin, a rope, a hand, gravity) is removed and replaced by an arrow showing the force it applied. If the object is not accelerating, those arrows must cancel exactly, both as pushes (force sums) and as twists (moment sums).

**2. Why it matters.** FBDs are step 1 of every problem in the course: trusses here, bars in Ch. 2, beams in Ch. 3, shafts in Ch. 6, columns later. A wrong or incomplete FBD is the single largest source of lost marks.

**3. Formal treatment.**

*Constraint:* any restriction on the free motion of a body. **Each prevented motion produces one reaction component.**

| Support (slides) | Prevents | Reactions in 2-D | Reactions in 3-D |
|---|---|---|---|
| Roller / rocker / smooth surface | motion ⟂ to the surface | 1 force ⟂ surface | 1 force |
| Hinge / pin | both translations | 2 forces $R_x, R_y$ | — |
| Ball-and-socket | all translations | — | 3 forces |
| Journal bearing (short) | translations ⟂ to the shaft | — | 2 forces (often treated as no moment) |
| Built-in / fixed / clamped | translations and rotation | $R_x, R_y$ and a moment $M$ | 3 forces and 3 moments |
| Cable / rope / link | stretching along itself | 1 tensile force along it | 1 force |

*Equations of equilibrium:*
$$\text{2-D: } \sum F_x = 0,\quad \sum F_y = 0,\quad \sum M_O = 0\qquad\qquad \text{3-D: }\ \sum\mathbf F = \mathbf 0,\quad \sum\mathbf M_O = \mathbf 0\ \ (6 \text{ scalar equations})$$
$\sum M_O$ includes the moments of all forces **plus** all applied couples.

*Equivalent sets of three equations in 2-D (Crandall Prob 1.7):* any of these is a complete set.
- (a) Two force sums in non-parallel directions plus one moment equation.
- (b) Moments about two points P and Q plus the force sum in any direction **not perpendicular** to PQ.
- (c) Moments about three **non-collinear** points.

Whichever set you choose, a 2-D body gives only **three independent** equations.

*Statical determinacy.* Count the unknown reaction components. More than 3 means the body is **statically indeterminate**. Fewer than 3, or 3 that are all parallel or all concurrent, means it is **improperly constrained**: it can move.

*Two-force member:* a body loaded at only two points, with no couples. Equilibrium requires the two forces to be **equal, opposite and collinear**, along the line joining the two points.

*Three-force member:* if three non-parallel forces keep a body in equilibrium, their lines of action **meet at a single point**.

**FBD procedure (use every time):**
1. Isolate the body and sketch it with its dimensions.
2. Draw every external force: applied loads, **self-weight at the centroid**, and every support reaction with the components from the table above.
3. Give each unknown an assumed direction and a name.
4. Choose axes, and moment points through which as many unknowns as possible pass.
5. Write the equations. Check that the number of unknowns ≤ 3 (2-D).
6. Solve. A negative answer means "opposite to the arrow drawn". State it in words.
7. Check with an equation you did not use.

**4. Derivations.**

*(a) Two-force member.* Forces $\mathbf F_A$ at A and $\mathbf F_B$ at B.
- $\sum\mathbf F = 0$ gives $\mathbf F_B = -\mathbf F_A$: equal and opposite.
- Moments about A: $\mathbf r_{AB}\times\mathbf F_B = 0$. A cross product vanishes only if the vectors are parallel, so $\mathbf F_B\parallel\mathbf r_{AB}$: the forces act **along AB**. ∎

*(b) Three-force concurrency.* Let the lines of action of two of the forces meet at a point K. Take moments about K: those two forces contribute nothing. So the third force's moment about K must be zero too, which means its line of action passes through K. ∎ (If two of the forces are parallel, the third must be parallel to them: the "point at infinity" version.)

*(c) Why a 2-D body has only three independent equations.* A rigid body in a plane has three independent ways to move: two translations and one rotation. Each equation of equilibrium forbids one of them. Any further equation, such as moments about a fourth point, is a combination of the first three and adds no information.

**5. Graphical interpretation.** For a three-force body, draw the two known lines of action and mark their intersection K. The third force must pass through K. This gives its direction immediately (lawn roller Q9, rod on a roller Q11). A **force triangle** drawn head-to-tail with the three forces must close. Its geometry gives magnitudes via the sine rule.

**6. Special cases.**
- **All forces parallel:** one force equation is trivially satisfied, so only 2 useful equations remain.
- **All forces concurrent:** the moment equation is trivially satisfied, again leaving 2.
- **A body hinged at one point with one other unknown:** take moments about the hinge first; it kills two unknowns at once.

**7. Common traps.**
- Forgetting self-weight ($mg$, with $g = 9.81$ m/s²) or putting it at the load point instead of the centroid.
- Giving a fixed support only forces and forgetting its **moment**.
- "Correcting" a reaction's assumed direction halfway through. Keep the arrow and let the sign speak.
- Drawing an internal force (such as the force between two parts of one body) on the FBD of the whole body. Internal forces cancel in pairs.
- kg is not N: multiply by 9.81.

**8. Summary box**
$$\boxed{\ \sum F_x=0,\ \ \sum F_y=0,\ \ \sum M_{\text{any pt}}=0\ }\qquad \text{pin} = 2,\ \text{roller} = 1,\ \text{fixed} = 3\ \text{unknowns}$$
Two-force member → force along the line joining its pins. Three-force member → lines of action concurrent. More than 3 unknowns → indeterminate (Ch. 2).

### B. Solved questions

#### Q2 (Slides Ch1, "Problem 3") — Simply supported beam with a central load *(easy)*
**Problem.** A 5000 N force acts at the centre C of a beam AB of length 5 m. A is a pin and B is a roller. Find the support reactions.

**Given:** $L = 5$ m, $P = 5000$ N at $x = 2.5$ m. **Find:** $A_x$, $A_y$, $B_y$.

**Approach.** Three unknowns and three equations (Concept 1.3), so the beam is statically determinate. Take moments about A first: two unknowns pass through it.

**FBD in words.** At A draw $A_x$ (→) and $A_y$ (↑). At B draw $B_y$ (↑); a roller gives no horizontal force. At C draw 5000 N ↓.

**Solution.**
1. $\sum F_x = 0$: $A_x = 0$, since no other horizontal force acts.
2. $\sum M_A = 0$ (counter-clockwise +): $B_y(5) - 5000(2.5) = 0$, so $B_y = 12\,500/5 = 2500$ N.
3. $\sum F_y = 0$: $A_y + B_y - 5000 = 0$, so $A_y = 2500$ N.

$$\boxed{A_x = 0,\qquad A_y = B_y = 2500\ \text{N}\ (\uparrow)}$$

**Check.** The load and supports are symmetric, so the reactions must be equal ✓. Moments about B as an independent check: $-A_y(5) + 5000(2.5) = 0$ gives 2500 ✓.

**Exam takeaway.** With $P$ at distance $a$ from A and $b$ from B, $A_y = Pb/L$ and $B_y = Pa/L$: the nearer support carries more. You will reuse this in every SFD/BMD question. **Variation:** two loads, or a load at $L/3$.

---

#### Q3 (Slides Ch1, "Problem 2") — Cantilever with self-weight *(easy)*
**Problem.** A uniform beam of mass 100 kg and length 6 m is built in at A. A 1200 N load acts 2 m from A. Draw the FBD and find the reactions.

**Given:** $m = 100$ kg, so $W = 100(9.81) = 981$ N acting at the centroid, 3 m from A; $P = 1200$ N at 2 m. **Find:** $A_x$, $A_y$, $M_A$.

**Approach.** A fixed support gives three unknowns, including a moment. Three equations solve it.

**FBD in words.** At A: $A_x$ (→), $A_y$ (↑) and a counter-clockwise moment $M_A$. Along the beam: 1200 N ↓ at 2 m and 981 N ↓ at 3 m.

**Solution.**
1. $\sum F_x = 0$: $A_x = 0$.
2. $\sum F_y = 0$: $A_y - 1200 - 981 = 0$, so $A_y = 2181$ N.
3. $\sum M_A = 0$: $M_A - 1200(2) - 981(3) = 0$, so $M_A = 2400 + 2943 = 5343$ N·m.

$$\boxed{A_x = 0,\quad A_y = 2181\ \text{N}\ (\uparrow),\quad M_A = 5.34\ \text{kN·m (counter-clockwise on the beam)}}$$

**Check.** The wall must hold the beam up (↑) and stop it drooping clockwise. A counter-clockwise wall moment does exactly that ✓. Magnitude: total load ≈ 2.2 kN at an average arm ≈ 2.45 m gives ≈ 5.3 kN·m ✓.

**Exam takeaway.** Two traps are planted: the self-weight (981 N) and its position (at $L/2$, not at the load). **Variation:** "the beam has a UDL of its own weight per metre" (same thing, treated in Ch. 3).

---

#### Q4 (Slides Ch1) — Bicycle hand brake *(easy)*
**Problem.** A rider applies $P = 70$ N to the brake lever. P is the resultant of a uniform hand pressure acting between 50 mm and 100 mm from pivot A. The lever pivots at A and the brake cable (460 mm long) is attached 37.5 mm from A, measured perpendicular to the cable. Find the cable tension $T$.

**Given:** $P = 70$ N, uniform pressure from 50 to 100 mm from A, so the resultant acts at the middle, 75 mm from A and perpendicular to the lever. Cable arm 37.5 mm. **Find:** $T$.

**Approach.** The lever is a body hinged at A. Moments about A eliminate the two unknown pin reactions.

**FBD in words.** Lever with pin reactions $A_x, A_y$ at A, $P$ at 75 mm from A, and $T$ along the cable at 37.5 mm perpendicular distance from A.

**Solution.**
1. Resultant of a uniform pressure acts at its centroid: $(50+100)/2 = 75$ mm from A.
2. $\sum M_A = 0$: $T(37.5) - 70(75) = 0$.
3. $T = 5250/37.5 = 140$ N.

$$\boxed{T = 140\ \text{N}}$$

**Check.** The cable arm is half the hand arm, so the cable force is twice the hand force ✓.

**Exam takeaway.** The 460 mm cable length is a **distractor**. It would matter only if you were asked how much the cable stretches: $\delta = TL/AE$ (Ch. 2). **Variation:** find the pin reaction at A, $\sqrt{A_x^2 + A_y^2}$, from the two force equations.

---

#### Q5 (Slides Ch1) — Diving board *(easy–medium)*
**Problem.** A person of mass 54 kg stands at the tip of a diving board of mass 36 kg. The board is pinned at A and rests on a roller at B, 1.2 m from A. The board's centroid is 2.4 m from A and the person stands 4.6 m from A. Draw the FBD and find the reactions at A and B.

**Given:** $W_D = 36(9.81) = 353.2$ N at 2.4 m; $W_P = 54(9.81) = 529.7$ N at 4.6 m; B at 1.2 m. **Find:** $A$ and $B$.

**Approach.** Two vertical unknowns, plus $A_x = 0$ since there are no horizontal loads. Moments about A give B directly.

**FBD in words.** Board with $A$ (↑ assumed) at $x = 0$, $B$ (↑) at 1.2 m, 353.2 N ↓ at 2.4 m and 529.7 N ↓ at 4.6 m.

**Solution.**
1. $\sum M_A = 0$: $B(1.2) - 353.2(2.4) - 529.7(4.6) = 0$.
2. $B = \dfrac{847.7 + 2436.6}{1.2} = \dfrac{3284.3}{1.2} = 2737$ N.
3. $\sum F_y = 0$: $A + 2737 - 353.2 - 529.7 = 0$, so $A = -1854$ N.

$$\boxed{B = 2737\ \text{N}\ (\uparrow),\qquad A = 1854\ \text{N}\ (\downarrow)}$$

**Check.** The board is a lever pivoting on B. The loads to the right of B try to lift end A, so the pin at A must pull **down** ✓. B carries more than the total weight (883 N), because A also pulls down ✓.

**Exam takeaway.** Supports that "pull the wrong way" are popular. Never flip a sign silently; write "the negative sign means A acts downward". **Variation:** where can the diver stand so that the pin force at A is zero? The board's own weight (right of B) turns it clockwise about B, so the diver must stand *between A and B* to balance it. Moments about B: $529.7(1.2 - x) = 353.2(2.4-1.2)$, so $1.2 - x = 0.800$ and $x = 0.40$ m.

---

#### Q6 (Slides Ch1) — Pliers *(medium)*
**Problem.** A person squeezes pliers with 20 N forces. In the FBD of one handle, the pin C joins the two halves. The bolt being gripped exerts a force $F_B$ perpendicular to the jaw, 25 mm to the left of C. The 20 N hand force acts at 45° (down and to the left) at a point 80 mm right of and 50 mm below C. Find $F_B$ and the pin reactions at C.

**Given:** C at the origin; $F_B$ acts vertically at (−25, 0) mm; hand force 20 N in direction $(-\cos45^\circ, -\sin45^\circ)$ at (80, −50) mm. **Find:** $F_B$, $C_x$, $C_y$.

**Approach.** One handle is a rigid body with three unknowns ($F_B$, $C_x$, $C_y$). Moments about C isolate $F_B$.

**FBD in words.** Handle with $C_x$ (→) and $C_y$ (↑) at C, $F_B$ ↓ at the jaw and the 20 N hand force.

**Solution.**
1. Components of the hand force: $F_x = -20\cos45^\circ = -14.14$ N and $F_y = -14.14$ N.
2. Moment of the hand force about C: $M = xF_y - yF_x = 80(-14.14) - (-50)(-14.14) = -1131.4 - 707.1 = -1838.5$ N·mm (clockwise).
3. Moment of $F_B$ (↓ at $x = -25$): $xF_y = (-25)(-F_B) = +25F_B$ (counter-clockwise).
4. $\sum M_C = 0$: $25F_B - 1838.5 = 0$, so $F_B = 73.5$ N.
5. $\sum F_x = 0$: $C_x - 14.14 = 0$, so $C_x = 14.1$ N.
6. $\sum F_y = 0$: $C_y - 73.5 - 14.14 = 0$, so $C_y = 87.7$ N.

$$\boxed{F_B = 73.5\ \text{N},\qquad C_x = 14.1\ \text{N},\qquad C_y = 87.7\ \text{N}\ (|C| = 88.8\ \text{N})}$$

**Check.** Mechanical advantage $73.5/20 \approx 3.7$, typical for pliers (handle arm ≈ 94 mm, jaw arm 25 mm, ratio ≈ 3.8) ✓.

**Exam takeaway.** The component method $M = xF_y - yF_x$ saves you from finding the perpendicular distance of a slanted force. **Variation:** "the jaw can bear at most 100 N; find the maximum hand force", giving $20 \times 100/73.5 = 27.2$ N.

---

#### Q7 (Slides Ch1) — Two cylinders in a box *(medium)*
**Problem.** Two identical cylinders P and Q, each 900 N, rest in a box. P touches the floor (B) and the left wall (A). Q rests on P and touches the right wall (C). The line of centres makes 45° with the horizontal. All surfaces are smooth. Draw FBDs of (a) both together, (b) P, (c) Q, and (d) find the reactions at A, B and C.

**Given:** $W = 900$ N each; angle of the line of centres 45°; smooth contacts (normal forces only). **Find:** $R_A$, $R_B$, $R_C$ and the contact force N between the cylinders.

**Approach.** Each cylinder is a concurrent force system (all forces pass through its centre, because contact forces on a smooth circle are radial). So each gives two useful equations. Start with Q, which has only two unknowns.

**FBD in words.**
- *Q:* weight 900 N ↓; $R_C$ horizontal ←; contact force N from P, acting along the line of centres, up and to the right at 45°.
- *P:* weight 900 N ↓; $R_A$ → from the left wall; $R_B$ ↑ from the floor; N from Q, down and to the left at 45° (Newton's third law).
- *Both together:* 1800 N ↓, $R_A$ →, $R_B$ ↑, $R_C$ ←. N is internal and does not appear.

**Solution.**
1. *Q, vertical:* $N\sin45^\circ = 900$, so $N = 1272.8$ N.
2. *Q, horizontal:* $R_C = N\cos45^\circ = 900$ N.
3. *P, horizontal:* $R_A = N\cos45^\circ = 900$ N.
4. *P, vertical:* $R_B = 900 + N\sin45^\circ = 1800$ N.

$$\boxed{R_A = 900\ \text{N},\quad R_B = 1800\ \text{N},\quad R_C = 900\ \text{N},\quad N = 1273\ \text{N}}$$

**Check (combined FBD).** $\sum F_y$: $R_B = 1800$ ✓ (total weight). $\sum F_x$: $R_A = R_C$ ✓. Moment balance of the combined body: the two wall forces form a couple $900 \times$ (vertical distance between contact points $= 2r\sin45^\circ$), which balances the weight couple $900 \times$ (horizontal offset of the centres $= 2r\cos45^\circ$). At 45° these are equal ✓.

**Exam takeaway.** For smooth spheres and cylinders, every contact force passes through the centre, so moment equations give nothing new. Variation: line of centres at angle θ gives $R_A = R_C = W\cot\theta$ and $N = W/\sin\theta$. As θ → 90° (Q directly above P), the wall forces vanish.

---

#### Q8 (Slides Ch1; Crandall Prob 1.13) — Lawn roller over a step: push vs pull *(medium)*
**Problem.** Compare the force F needed to just start a 900 N lawn roller (diameter 600 mm) over a 75 mm step when (a) the roller is **pushed** and (b) it is **pulled**. The handle is at 30° to the horizontal and its force acts through the axle.

**Given:** $W = 900$ N, $r = 300$ mm, $h = 75$ mm, handle at 30°. **Find:** $F_{push}$, $F_{pull}$.

**Approach.** "Just starting to roll over" means the roller is about to leave the ground, so the **ground reaction is zero**. Three forces then act: W, F and the corner reaction R. Take moments about the corner so that R drops out.

**FBD in words.** Roller centre O. W ↓ at O. F through O along the handle (pushed: down and toward the step at 30° below horizontal; pulled: up and toward the step at 30° above horizontal). R at the step corner K, directed toward O (smooth corner on a circle).

**Solution.**
1. *Geometry of the corner.* K is $r - h = 225$ mm below O. Its horizontal offset is $a = \sqrt{r^2-(r-h)^2} = \sqrt{300^2-225^2} = \sqrt{39\,375} = 198.4$ mm.
2. *Moment arms about K.* W (vertical) has arm $a = 198.4$ mm. The horizontal component of F has arm 225 mm; the vertical component has arm 198.4 mm.
3. *(a) Pushed* ($F\cos30^\circ$ toward the step, $F\sin30^\circ$ downward). The horizontal part tips the roller over; W and the downward part resist.
$$F\cos30^\circ(225) = W(198.4) + F\sin30^\circ(198.4)$$
$$F(194.86 - 99.20) = 900(198.4)\ \Rightarrow\ F = \frac{178\,560}{95.66} = 1867\ \text{N}$$
4. *(b) Pulled* (vertical part upward, now helping).
$$F\cos30^\circ(225) + F\sin30^\circ(198.4) = W(198.4)\ \Rightarrow\ F = \frac{178\,560}{294.06} = 607.2\ \text{N}$$

$$\boxed{F_{push} \approx 1867\ \text{N},\qquad F_{pull}\approx 607\ \text{N}}$$
(Slides: 1866.05 N and 607.28 N. The difference is rounding.)

**Check.** Three-force concurrency: W and F both pass through O, so R must too, which is consistent with a smooth corner pushing radially ✓. Pulling is about 3× easier because it partly lifts the roller, while pushing presses it into the ground ✓.

**Exam takeaway.** "Just about to" means a contact force becomes zero. **Variation:** find the minimum force and its direction. It is perpendicular to OK, so $F_{min} = W\,a/r = 900(198.4/300) = 595$ N, at angle $\cos^{-1}(225/300) = 41.4^\circ$ above the horizontal.

---

#### Q9 (Crandall Prob 1.42) — Forearm holding a weight; then elbow friction *(medium)*
**Problem.** A man holds an 80 N weight in his hand with the elbow at a right angle. The forearm and hand weigh 16 N with C.G. 105 mm from the elbow joint. The weight is 370 mm from the joint. The flexor muscle acts vertically, 40 mm from the joint. (i) Find the muscle force and the joint force from the humerus, neglecting friction. (ii) The elbow joint has radius 20 mm and friction coefficient 0.015. How does the muscle force change (a) to raise the load and (b) to just support it?

**Given:** loads 80 N at 370 mm and 16 N at 105 mm; muscle line at 40 mm; joint radius 20 mm; $\mu = 0.015$. **Find:** $F_m$, joint force $J$, and the friction corrections.

**Approach.** The forearm is a lever hinged at the elbow. Moments about the joint give the muscle force, and the vertical force sum gives the joint force. Friction adds a resisting moment $\mu J r$ that opposes the motion.

**FBD in words.** Forearm horizontal. Muscle force $F_m$ ↑ at 40 mm. Joint force $J$ ↓ at the joint (humerus pushing down on the ulna). Weights 16 N ↓ at 105 mm and 80 N ↓ at 370 mm.

**Solution.**
1. *(i) Moments about the joint:* $40F_m = 80(370) + 16(105) = 29\,600 + 1\,680 = 31\,280$ N·mm, so $F_m = 782$ N.
2. *(i) Vertical sum:* $F_m - J - 80 - 16 = 0$, so $J = 782 - 96 = 686$ N (↓ on the ulna).
3. *(ii) Friction moment.* At the joint surface the friction force is $\mu J$ with arm $r = 20$ mm, giving $M_f = \mu J r = 0.015(20)J = 0.3J$ N·mm. It always opposes the motion, and $J = F_m - 96$ still holds.
4. *(a) Raising* (friction resists the muscle): $40F_m = 31\,280 + 0.3(F_m - 96)$, so $39.7F_m = 31\,251.2$ and $F_m = 787.2$ N.
5. *(b) Just supporting* (the load tends to drop, friction helps): $40F_m = 31\,280 - 0.3(F_m - 96)$, so $40.3F_m = 31\,308.8$ and $F_m = 776.9$ N.

$$\boxed{F_m = 782\ \text{N},\ J = 686\ \text{N};\qquad \text{raise: } 787\ \text{N}\ (+5.2\ \text{N}),\quad \text{hold: } 777\ \text{N}\ (-5.1\ \text{N})}$$

**Check.** The muscle has a tiny lever arm (40 mm against 370 mm), so it must pull about 10× the load ✓. Joint friction changes the result by only 0.7%, as expected for a lubricated joint ✓.

**Exam takeaway.** Short-lever "biomechanics" FBDs test moment equations. The friction twist shows that friction always opposes the **impending** motion, so the answer depends on the direction. **Variation:** muscle inclined at 75° to the forearm. Use only its perpendicular component in the moment equation; the joint force then also has a horizontal component.

---

#### Q10 (Crandall Prob 1.7) — Alternative sets of equilibrium equations *(easy, conceptual)*
**Problem.** Show that, for coplanar forces, each of the following is a complete set of equilibrium conditions: (a) zero force sums in two non-parallel directions plus zero moment about any point; (b) zero moments about two points P and Q plus a zero force sum parallel to PQ; (c) zero moments about three non-collinear points.

**Approach.** Reduce any coplanar system to a single resultant force $\mathbf R$ through a chosen point plus a couple. Show that each set forces both to vanish.

**Solution.**
1. *(b)* $\sum M_P = 0$ means the resultant has no couple about P, so it is a single force $\mathbf R$ through P (or zero). $\sum M_Q = 0$ means that force also has zero moment about Q, so its line of action passes through Q too: **R lies along PQ**. Finally, $\sum F_{\parallel PQ} = 0$ says its component along PQ is zero, so $\mathbf R = 0$. ∎ (The force condition must not be perpendicular to PQ. A perpendicular component would be automatically zero and prove nothing.)
2. *(c)* Moments about P and Q being zero put R along PQ. A zero moment about a third point S, off line PQ, then requires $R\cdot(\text{distance from S to PQ}) = 0$, so $R = 0$. ∎ If S were on PQ the third equation would repeat the first two.
3. *(a)* Two independent force components zero gives $\mathbf R = 0$, and a zero moment then kills the couple. ∎

**Answer.** All three sets are equivalent. Each contains exactly three independent conditions, so a 2-D rigid body yields **at most three independent equations** however you choose them.

**Exam takeaway.** Use set (b) or (c) to write equations with **one unknown each**: take moments about points where other unknowns cross. That is the whole trick of the method of sections (Concept 1.5).

---

#### Q11 (Crandall Prob 1.21) — Rod on a roller against a smooth wall: where can the load sit? *(medium–hard, three-force member)*
**Problem.** A weightless rigid rod rests on a small roller A and bears against a smooth vertical wall at its end B. A load W can be placed at distance x from B along the rod. The roller is at horizontal distance b from the wall and the rod makes angle θ with the horizontal. Find x for equilibrium. Neglect friction.

**Given:** b, θ (rod angle from the horizontal, as drawn), smooth contacts. **Find:** x.

**Approach.** Exactly three forces act: W (vertical), the wall reaction at B (horizontal, since the wall is smooth) and the roller reaction at A (perpendicular to the rod). A three-force body needs **concurrent** lines of action (Concept 1.3).

**FBD in words.** B at the origin, rod going up and to the right at θ. $N_B$ → horizontal at B. $N_A$ at A, perpendicular to the rod. W ↓ at distance x along the rod.

**Solution.**
1. *Coordinates.* A is where the rod reaches $X = b$: $A = (b,\ b\tan\theta)$. The load is at $(x\cos\theta,\ x\sin\theta)$.
2. *Meeting point K.* The horizontal line through B ($Y = 0$) and the vertical line through W ($X = x\cos\theta$) meet at $K = (x\cos\theta,\ 0)$.
3. *Roller line through K.* $N_A$ acts along $(-\sin\theta, \cos\theta)$ from A. Points on that line: $(b - s\sin\theta,\ b\tan\theta + s\cos\theta)$. Setting $Y = 0$ gives $s = -b\tan\theta/\cos\theta$, so
$$X = b + \frac{b\tan\theta\sin\theta}{\cos\theta} = b\,(1 + \tan^2\theta) = \frac{b}{\cos^2\theta}$$
4. *Concurrency:* $x\cos\theta = \dfrac{b}{\cos^2\theta}$.

$$\boxed{x = \frac{b}{\cos^3\theta}}$$

**Check.** θ → 0: x → b, so the load sits directly over the roller and the wall carries nothing ✓. As θ grows, x grows, because a steeper rod pushes on the wall and the load must move outward to balance ✓.

**Second method (equations).** Moments about B: $N_A\,(b/\cos\theta) = W\,x\cos\theta$. Vertical sum: $N_A\cos\theta = W$. Combining gives $x = b/\cos^3\theta$ ✓.

**Exam takeaway.** When you see "three forces only", look for the concurrency point first; it often makes the problem one line long. **Variation:** if the load is at a fixed x and θ is unknown, $\cos\theta = (b/x)^{1/3}$.

---

## Concept 1.4 — Dry (Coulomb) friction, including belt friction

### A. Concept explanation

**1. Intuition.** Push a heavy box lightly and it doesn't move. The floor pushes back sideways *exactly as hard as you push*, up to a limit, and beyond that the box slides. The limit is larger for a heavier box (bigger normal force) but does **not** depend on how big its base is. A rope wrapped round a post is the same idea repeated around the curve. Each little bit of contact adds a little friction, and the effect multiplies, which is why a sailor can hold a ship with a few turns of rope.

**2. Why it matters.** Wedges, brakes, belts, bolts, ladders, vehicles on slopes. In the PYQs: the rope over a drum (2014 T1-Q3) combines belt friction with rope stretch (Ch. 2). In machine design, friction decides whether a joint slips.

**3. Formal treatment (slides).**
- No relative motion: **static** friction $f_s$. It takes *whatever value equilibrium needs*, from 0 up to $f_{s,max}$.
- Impending motion (the limiting case): $f_{s,max} = \mu_s N$.
- Sliding: **kinetic** friction $f_k = \mu_k N$. It is roughly constant and slightly less than $\mu_s N$.
- Friction is independent of the contact area (slides). Doubling the area at the same N halves the force per unit area.
- Friction always acts **opposite to the (impending) relative motion** of the contact surfaces.
- *Slide example:* if $f_{s,max} = 10$ N, an 8 N push gives $f = 8$ N and no motion; a 12 N push makes the block move. With no push, $f = 0$, **not** $\mu N$.

*Angle of friction:* $\tan\phi = \mu$. The total contact reaction (N and f combined) can lean from the normal by at most φ, the "friction cone".

**4. Derivations.**

*(a) Block on an incline of angle α, pulled up the slope by a force T parallel to it.* Resolve normal to the slope: $N = W\cos\alpha$.
- Impending motion **up** (friction acts down the slope): $T = W\sin\alpha + \mu W\cos\alpha$.
- Impending motion **down** (friction acts up the slope): $T = W\sin\alpha - \mu W\cos\alpha$.

Equilibrium holds for any T between these two values.

*(b) Angle of repose.* With no T, the block is about to slide when $W\sin\alpha = \mu W\cos\alpha$, i.e. $\tan\alpha = \mu$. Measuring the tilt angle at which a block just slides is a direct measurement of μ.

*(c) Belt (capstan) friction.* Take a rope element subtending $d\theta$ on a fixed drum, with tension T on one side and $T + dT$ on the other.
- Radial balance: the normal force is $dN = (T + dT)\sin\frac{d\theta}{2} + T\sin\frac{d\theta}{2} \approx T\,d\theta$, dropping second-order terms.
- Tangential balance at impending slip: $(T + dT) - T = \mu\,dN$, so $dT = \mu T\,d\theta$.
- Separate and integrate over the contact angle β:
$$\int_{T_1}^{T_2}\frac{dT}{T} = \mu\int_0^{\beta}d\theta\ \Rightarrow\ \ln\frac{T_2}{T_1} = \mu\beta\ \Rightarrow\ \boxed{\frac{T_2}{T_1} = e^{\mu\beta}}$$
Here $T_2$ is the tight side, $T_1$ the slack side, and β is in **radians** (each full turn is 2π). Along the contact the tension grows exponentially: $T(\theta) = T_1e^{\mu\theta}$.

**5. Graphical picture.** Draw the friction cone (half-angle φ) about the contact normal. The resultant of all the *other* forces on the body must fall inside the cone for no slip, and on its surface for impending slip. For a 3-D problem (block pushed sideways on a slope), friction opposes the **resultant** of the in-plane forces, not just the down-slope one (Q14).

**6. Special cases.**
- $\mu = 0$: a smooth surface; the reaction is purely normal.
- β = π (half wrap): $T_2/T_1 = e^{\mu\pi}$. Four full turns: $e^{8\pi\mu}$, which is huge even for μ = 0.3.
- Tipping versus sliding: a tall box may tip over before it slides. Check both.

**7. Common traps.**
- Writing $f = \mu N$ when the problem does **not** say motion is impending.
- Getting the friction direction wrong. Decide which way the body *would* move without friction.
- Forgetting that N changes when an applied force has a component normal to the surface.
- Degrees instead of radians in $e^{\mu\beta}$.
- In 3-D, balancing friction only against the down-slope weight component and ignoring a sideways push.

**8. Summary box**

| Situation | Equation |
|---|---|
| No slip | $f \le \mu_s N$; find f from equilibrium |
| Impending slip | $f = \mu_s N$, opposing the impending motion |
| Incline, impending up / down | $T = W(\sin\alpha \pm \mu\cos\alpha)$ |
| Angle of repose | $\tan\alpha = \mu$ |
| Rope on drum | $T_2/T_1 = e^{\mu\beta}$ (β in rad), $T(\theta) = T_1e^{\mu\theta}$ |

### B. Solved questions

#### Q12 (Slides Ch1) — Range of the hanging weight W for a block on an incline *(easy)*
**Problem.** A 500 N block rests on a 3-4-5 incline ($\sin\alpha = 0.6$, $\cos\alpha = 0.8$). A cable parallel to the incline runs over a frictionless pulley to a hanging weight W. $\mu_s = 0.5$. Find the range of W for equilibrium.

**Given:** block 500 N, α from a 3-4-5 triangle, μ = 0.5, weightless cable, frictionless pulley (so the tension is W). **Find:** $W_{min}$, $W_{max}$.

**Approach.** Two impending-motion cases: the block about to slide down (W smallest) and about to slide up (W largest). Friction flips direction between them.

**FBD in words.** Block with weight 500 N ↓, N normal to the incline, T = W up the slope, and friction f along the slope (direction depends on the case).

**Solution.**
1. Normal force: $N = 500(0.8) = 400$ N, so $f_{max} = 0.5(400) = 200$ N.
2. Weight component down the slope: $500(0.6) = 300$ N.
3. *Impending down* (friction up the slope): $W_{min} + 200 = 300$, so $W_{min} = 100$ N.
4. *Impending up* (friction down the slope): $W_{max} = 300 + 200 = 500$ N.

$$\boxed{100\ \text{N} \le W \le 500\ \text{N}}$$

**Check.** $\tan\alpha = 0.75 > \mu = 0.5$, so the block would slide down without the cable. That is why $W_{min} > 0$ ✓. When $W = 300$ N, friction is zero (the midpoint of the range) ✓.

**Exam takeaway.** "Range of values" always means two impending-motion cases with friction reversed. **Variation:** cable at angle β above the slope. Then $N = W_b\cos\alpha - T\sin\beta$ changes, and both limits shift.

---

#### Q13 (Slides Ch1; Crandall Prob 1.45) — Trunk on a ramp: find μ *(medium)*
**Problem.** A longshoreman can barely start pushing a trunk **up** a 30° ramp. With the same push (parallel to the ramp) he can barely hold it from sliding **back** when the slope is 60°. Find $\mu_s$.

**Given:** the same push P in both cases, parallel to the ramp. **Find:** μ.

**Approach.** Write impending-motion equations for both ramps and eliminate the unknown P and W ratio.

**FBD in words.** Trunk with W ↓, N normal to the ramp, P up the ramp, and friction μN down the ramp (30°, impending up) or up the ramp (60°, impending down).

**Solution.**
1. 30°, impending up: $P = W(\sin30^\circ + \mu\cos30^\circ) = W(0.5 + 0.866\mu)$.
2. 60°, impending down: $P = W(\sin60^\circ - \mu\cos60^\circ) = W(0.866 - 0.5\mu)$.
3. Equate: $0.5 + 0.866\mu = 0.866 - 0.5\mu$, so $1.366\mu = 0.366$.

$$\boxed{\mu_s = 0.268\ (= \tan15^\circ = 2-\sqrt3)}$$

**Check.** $\mu < \tan30^\circ = 0.577$, so on the 30° ramp the trunk would slide down unaided. That is consistent with him needing to push ✓. The push is $P = W(0.5 + 0.232) = 0.732W$ in both cases ✓.

**Exam takeaway.** "Barely start pushing" (impending up) and "barely hold" (impending down) are the two directions. **Variation:** a single slope with a range of pushes, as in Q12.

---

#### Q14 (Crandall Prob 1.39) — Block pushed sideways on an incline (3-D friction) *(medium)*
**Problem.** A block of weight W rests on a plane inclined at $\theta = \tan^{-1}(3/4)$. A horizontal force P, parallel to the x-axis (the horizontal edge of the incline, so in the plane of the incline and perpendicular to its slope), is applied and slowly increased from zero. The block starts to slide when $P = 0.4W$. Find μ.

**Given:** $\sin\theta = 0.6$, $\cos\theta = 0.8$; $P = 0.4W$ along x (in the incline plane, horizontal). **Find:** μ.

**Approach.** In the plane of the incline the block is pushed by two forces at right angles: the down-slope weight component and P. Friction must balance their **resultant**, and slip starts when that resultant reaches μN.

**FBD in words.** Normal $N = W\cos\theta$ out of the incline. In the incline plane: $W\sin\theta$ down the slope and P along x. Friction f, opposite to their resultant.

**Solution.**
1. Normal force: $N = W\cos\theta = 0.8W$.
2. In-plane driving forces: $W\sin\theta = 0.6W$ down the slope and $P = 0.4W$ along x, at right angles.
3. Resultant: $\sqrt{0.6^2 + 0.4^2}\,W = \sqrt{0.52}\,W = 0.7211W$.
4. Impending slip: $\mu N = 0.7211W$, so $\mu = 0.7211/0.8 = 0.901$.

$$\boxed{\mu = 0.90}$$

The block starts to move at $\tan^{-1}(0.4/0.6) = 33.7^\circ$ from the line of steepest descent, toward the direction of P.

**Check.** Even with P = 0, $\tan\theta = 0.75 < 0.90$, so the block rests unaided ✓. The answer exceeds 0.75 and P adds the extra drive ✓.

**Exam takeaway.** Friction resists the vector sum of the in-plane forces. Treating P and $W\sin\theta$ separately (for example $\mu = (0.6 + 0.4)/0.8 = 1.25$) is the classic wrong answer. **Variation:** given μ, find the largest P: $P = W\sqrt{\mu^2\cos^2\theta - \sin^2\theta}$.

---

#### Q15 (Slides Ch1; Crandall Prob 1.37) — Cylinder on two half-cylinders: maximum spacing *(hard)*
**Problem.** A cylinder A (weight W, radius r) rests on two half-cylinders B and C (each W/2, radius r). Their flat faces sit on a table with friction coefficient f. The cylinder-to-cylinder contacts are smooth. Find the maximum distance d between the centres of B and C for equilibrium.

**Given:** W, r, f; smooth curved contacts. **Find:** $d_{max}$.

**Approach.** Smooth contacts on circles act along the lines of centres. By symmetry, A pushes B and C equally. B tends to slide outward; table friction must stop it, and the limit is $F = fN$.

**FBD in words.**
- *A:* W ↓ and two contact forces N, one from each half-cylinder, along the lines of centres (each tilted θ from the vertical).
- *B:* W/2 ↓, N from A (down and outward along the line of centres), table normal $N_t$ ↑, and friction F ← (inward).

**Solution.**
1. *Geometry.* The centres of A and B are $2r$ apart. The horizontal offset is $d/2$, so $\sin\theta = \dfrac{d/2}{2r} = \dfrac{d}{4r}$, where θ is measured from the vertical.
2. *A, vertical:* $2N\cos\theta = W$, so $N = \dfrac{W}{2\cos\theta}$.
3. *B, vertical:* $N_t = \dfrac W2 + N\cos\theta = \dfrac W2 + \dfrac W2 = W$.
4. *B, horizontal:* $F = N\sin\theta = \dfrac W2\tan\theta$.
5. *No slip:* $F \le fN_t$, so $\dfrac W2\tan\theta \le fW$, i.e. $\tan\theta \le 2f$.
6. With $\tan\theta = 2f$: $\sin\theta = \dfrac{2f}{\sqrt{1+4f^2}}$, so $d_{max} = 4r\sin\theta$.

$$\boxed{d_{max} = \frac{8rf}{\sqrt{1+4f^2}}}$$

**Check.** f → 0 gives d → 0: with no friction the half-cylinders must touch ✓. f → ∞ gives d → 4r, the geometric limit at which A would fall between them ✓.

**Exam takeaway.** The table normal on B is **W**, not W/2: it carries half of A's weight as well as its own. **Variation:** with f = 0.3, $d_{max} = 8r(0.3)/\sqrt{1.36} = 2.06r$.

---

#### Q16 (PYQ 2014-15 Test-1 Q3) — Rope over a fixed drum: μ and the stretch of the wrapped part *(medium; combines Ch 1 and Ch 2)*
**Problem.** A steel rope (d = 10 mm, E = 200 GPa) hangs over a stationary drum of diameter 1.5 m, with 1 kN at one end (A) and 4 kN at the other (B), and 180° of contact. The rope is just about to slip. Find (a) the coefficient of friction and (b) the elongation of the rope segment AB in contact with the drum.

**Given:** $T_1 = 1$ kN, $T_2 = 4$ kN, β = π, r = 750 mm, $A = \frac{\pi}{4}(10)^2 = 78.54$ mm², E = 200 GPa. **Find:** μ and $\delta_{AB}$.

**Approach.** (a) Belt friction at impending slip. (b) The tension varies along the contact, so the elongation is $\int T\,ds/AE$ (Ch. 2, non-uniform bar).

**FBD in words.** Rope arc from θ = 0 (slack side, 1 kN) to θ = π (tight side, 4 kN). Normal pressure from the drum points radially outward, and friction acts along the rope toward the slack side.

**Solution.**
1. *(a)* $T_2/T_1 = e^{\mu\pi}$: $4 = e^{\mu\pi}$, so $\mu = \dfrac{\ln4}{\pi} = \dfrac{1.3863}{3.1416} = 0.441$.
2. *(b) Tension along the arc:* $T(\theta) = T_1e^{\mu\theta}$, with $ds = r\,d\theta$.
3. *Elongation:*
$$\delta = \int_0^{\pi}\frac{T(\theta)\,r\,d\theta}{AE} = \frac{rT_1}{AE}\int_0^\pi e^{\mu\theta}d\theta = \frac{rT_1}{AE\mu}\left(e^{\mu\pi}-1\right) = \frac{r(T_2 - T_1)}{AE\mu}$$
4. *Numbers:* $AE = 78.54(200\,000) = 1.571\times10^7$ N, so
$$\delta = \frac{750(4000-1000)}{1.571\times10^7(0.441)} = \frac{2.25\times10^6}{6.928\times10^6} = 0.325\ \text{mm}$$

$$\boxed{\mu = 0.441,\qquad \delta_{AB} \approx 0.325\ \text{mm}}$$

**Check.** If the whole arc carried the average tension of 2.5 kN: $\delta = 2500(\pi\times750)/1.571\times10^7 = 0.375$ mm. The exact answer is a little smaller because the exponential curve lies below the straight line joining 1 and 4 kN ✓.

**Exam takeaway.** This is how Test-1 mixes chapters: friction gives the force distribution, and Ch. 2 gives the stretch. **Variation:** "find the elongation of the free length below the drum" uses ordinary $PL/AE$ with the constant hanging load.

---

## Concept 1.5 — Plane trusses: method of joints, method of sections, zero-force members

### A. Concept explanation

**1. Intuition.** A truss is a skeleton of straight sticks pinned at their ends, like a Meccano bridge. If loads are applied only at the joints, each stick can only be pulled (tension) or squashed (compression) along its length. A pinned stick with no load along it cannot carry bending. Solving a truss means finding that single number for every stick.

**2. Why it matters.** Bridges, roof trusses, cranes, towers and space frames. Every member is a two-force member (Concept 1.3). In Ch. 2 the member forces give joint deflections through $\delta = FL/AE$ and Castigliano's theorem. PYQ 2014 Test-1 Q1 (15 marks) and Q2 (20 marks) are both truss questions.

**3. Formal treatment.**

*Ideal truss assumptions (slides):*
1. Members are connected only at their ends.
2. The connections are **frictionless pins**.
3. Loads are applied only at the joints.
4. Member weights are neglected (or lumped at the joints).

Under these assumptions every member is a two-force member, in pure tension or compression.

*Stability / determinacy (slides):* with m members, j joints and 3 support reactions:
- $m = 2j - 3$: rigid and statically determinate ("perfect").
- $m < 2j - 3$: unstable (a mechanism), collapsible.
- $m > 2j - 3$: over-rigid, statically indeterminate.

With r reactions in general, determinacy needs $m + r = 2j$, and the members must also be arranged sensibly (no collapsible panel).

*Zero-force members (slides):*
1. Two non-collinear members meet at a joint with no external load or support → **both** carry zero force.
2. Three members meet at an unloaded joint and two of them are collinear → the **third** carries zero force.

*Method of joints (slides):*
1. Find the support reactions from the whole truss (skip for a cantilever truss if you start at the free end).
2. Pick a joint with at most two unknown member forces. **Assume every unknown force is tensile** (arrow pointing away from the joint).
3. Apply $\sum F_x = 0$ and $\sum F_y = 0$ and move on joint by joint.
4. Tabulate: member, force, T or C. A negative result means compression.

*Method of sections (slides):* use it when only a few members are wanted.
1. Find the reactions if needed.
2. Pass a section that cuts **at most three** members, including the ones wanted, and splits the truss into two separate parts. It must pass through members, not joints.
3. Keep the part with fewer forces. Draw the cut members as tensile.
4. Apply the three equilibrium equations. Take moments about the point where two of the unknown forces intersect, so each equation has one unknown.

**4. Derivations.**

*(a) The counting rule.* Each pin joint gives 2 equations ($\sum F_x$, $\sum F_y$), so 2j equations in all. The unknowns are m member forces plus r reaction components. Unique solvability needs $m + r = 2j$, i.e. $m = 2j - 3$ when r = 3. For the slide example, $m = 13$ and $j = 8$: $13 = 2(8) - 3$ ✓.

*(b) Zero-force rule 2.* At an unloaded joint with members 1 and 2 collinear, sum forces **perpendicular** to that line. Only member 3 has a component in that direction, so $F_3\sin\alpha = 0$ and $F_3 = 0$. Rule 1 follows the same way: sum perpendicular to member 1, and only member 2 contributes.

*(c) Chord force = bending moment / depth.* Cut a parallel-chord truss through the top chord (force $F_1$), a diagonal ($F_3$) and the bottom chord ($F_2$). Take moments about the joint where $F_2$ and $F_3$ meet: only $F_1$ and the external loads on that side remain, so $F_1 h = M_{ext}$ and $F_1 = M/h$. The diagonal's vertical component equals the shear in that panel: $F_3\sin\theta = V$. A truss works like a beam whose flanges are the chords and whose web is the diagonals. This links directly to Ch. 3.

**5. Picture / geometric check.**
- A **cantilever** truss loaded downward hogs: top chord in tension, bottom chord in compression.
- A **simply supported** truss sags: top chord in compression, bottom chord in tension.
- Diagonals sloping down toward mid-span carry tension in a simply supported truss.

Sketch the deflected shape before calculating; it predicts every sign.

**6. Special cases.**
- A joint with only two collinear members and no load: equal forces.
- A load applied directly over a support goes straight into the reaction and causes no member forces (Ch. 2 Q13 bridge).
- Symmetric truss with symmetric load: solve half and mirror.

**7. Common mistakes.**
- Mixing up "assumed tension" and "answered compression". Keep the convention fixed throughout.
- Passing a section through a joint, or cutting four unknown members and expecting three equations to solve them.
- Wrong angles. Always compute $\tan\theta$ from the drawn dimensions; never guess 45° or 60°.
- Forgetting that a horizontal load at a pin support changes the horizontal reaction.

**8. Summary box**

| Tool | Use when |
|---|---|
| $m = 2j - 3$ | Check determinacy first |
| Zero-force rules | Spot them before starting: they save time and catch errors |
| Joints | All member forces wanted |
| Sections | One to three specific members wanted; take moments about the intersection of the other two |
| Chord = M/h, diagonal = V/sinθ | Quick checks of section results |

### B. Solved questions

#### Q17 (Slides Ch1) — Identify the zero-force members *(easy)*
**Problem.** Two trusses are shown. Identify all zero-force members.

**Approach.** Apply zero-force rule 2 at every unloaded, unsupported joint where two members are collinear. Then remove those members and re-check the neighbouring joints, because the rules cascade.

**Solution.**
1. *Upper truss:* the unloaded bottom joints F and G each join a straight bottom chord and one vertical, so the verticals FD and GE are zero (rule 2).
2. *Lower truss:* start at the unloaded joints on the free edges and work inward. Each removal of a zero member turns the next joint into a rule 1 or rule 2 case.

$$\boxed{\text{Upper: } F_{FD} = F_{GE} = 0.\qquad \text{Lower: } F_{BC},\ F_{FG},\ F_{FI},\ F_{HI},\ F_{HK},\ F_{JK} = 0}$$

**Check.** Each zero member is "unloaded" in the sense that, if it were removed, the truss would still carry the given loads (though it would become unstable for other loads).

**Exam takeaway.** Zero-force members often appear as a 2-mark part, and identifying them first shortens every later calculation. **Variation:** add a load at one of those joints; the member is then no longer zero.

---

#### Q18 (Slides Ch1) — A-frame truss by the method of joints *(easy–medium)*
**Problem.** A (pin) and B (roller) are 6 m apart. Apex C is 2.25 m above midpoint D. The members are AC, BC, CD, AD and BD. Loads: 10 kN down at D, and 20 kN at C acting down and to the right at 30° from the vertical. Find the reactions and all member forces.

**Given:** coordinates A(0,0), D(3,0), B(6,0), C(3,2.25) m. Load at C: $(+20\sin30^\circ, -20\cos30^\circ) = (10, -17.32)$ kN. **Find:** reactions and member forces.

**Approach.** Reactions from the whole truss, then joints D, A and B (each with at most two unknowns).

**Solution.**
1. *Geometry:* $AC = BC = \sqrt{3^2 + 2.25^2} = 3.75$ m, so for AC and BC $\sin\theta = 2.25/3.75 = 0.6$ and $\cos\theta = 0.8$.
2. *Reactions.* $\sum F_x$: $A_x + 10 = 0$, so $A_x = -10$ kN (10 kN ←). $\sum M_A$: $B_y(6) - 10(3) - [17.32(3) + 10(2.25)] = 0$. Here the second term is the 10 kN at D, and the 20 kN at C contributes $17.32(3)$ from its vertical part plus $10(2.25)$ from its horizontal part. So $B_y = (30 + 51.96 + 22.5)/6 = 17.41$ kN. $\sum F_y$: $A_y = 10 + 17.32 - 17.41 = 9.91$ kN.
3. *Joint D:* CD is the only member with a vertical component, so $F_{CD} - 10 = 0$ and $F_{CD} = 10$ kN (T). Horizontally, $F_{AD} = F_{BD}$.
4. *Joint A:* vertical: $0.6F_{AC} + 9.91 = 0$, so $F_{AC} = -16.52$ kN (C). Horizontal: $0.8(-16.52) + F_{AD} - 10 = 0$, so $F_{AD} = 23.21$ kN (T).
5. *Joint B:* vertical: $0.6F_{BC} + 17.41 = 0$, so $F_{BC} = -29.02$ kN (C). Horizontal: $-0.8F_{BC} - F_{BD} = 0$, so $F_{BD} = 23.21$ kN (T) ✓ (matches $F_{AD}$).

| Member | Force (kN) | Nature |
|---|---|---|
| AC | 16.52 | C |
| BC | 29.02 | C |
| CD | 10.00 | T |
| AD | 23.21 | T |
| BD | 23.21 | T |

**Check.** Joint C was not used. Horizontal at C: $0.8(16.52) - 0.8(29.02) + 10 = -10.0 + 10 \approx 0$ ✓. A full computer solve gives the same table ✓.

**Exam takeaway.** The slide table labels the first row "AB". It means AC, since there is no member AB. **Variation:** make the 20 kN vertical. Then $A_x = 0$ and the truss becomes symmetric apart from the load at D.

---

#### Q19 (Slides Ch1) — Warren truss with 2000 N and 4000 N *(medium)*
**Problem.** A Warren truss has equilateral panels of 3 m: bottom joints A (pin), B, C (roller) and top joints D (above x = 1.5 m) and E (above x = 4.5 m). 2000 N acts down at D and 4000 N down at E. Find all member forces.

**Given:** $h = 1.5\tan60^\circ = 2.598$ m; all members at 60°. **Find:** forces in AB, BC, AD, BD, BE, CE, DE.

**Approach.** Reactions, then joints A, C, D and E in turn.

**Solution.**
1. *Reactions:* $C_y = (2000\times1.5 + 4000\times4.5)/6 = 3500$ N and $A_y = 6000 - 3500 = 2500$ N.
2. *Joint A:* $F_{AD}\sin60^\circ + 2500 = 0$, so $F_{AD} = -2886.8$ N (C). $F_{AB} = -F_{AD}\cos60^\circ = 1443.4$ N (T).
3. *Joint C:* $F_{CE}\sin60^\circ + 3500 = 0$, so $F_{CE} = -4041.5$ N (C). $F_{BC} = 2020.7$ N (T).
4. *Joint D (vertical):* $-0.866F_{DA} - 0.866F_{DB} - 2000 = 0$, so $F_{DB} = \dfrac{-2000 + 0.866(2886.8)}{0.866} = 577.4$ N (T). *Horizontal:* $-0.5F_{DA} + 0.5F_{DB} + F_{DE} = 0$, so $F_{DE} = -1443.4 - 288.7 = -1732.1$ N (C).
5. *Joint E (vertical):* $-0.866F_{EB} - 0.866F_{EC} - 4000 = 0$, so $F_{EB} = \dfrac{-4000 + 3500}{0.866} = -577.4$ N (C).

| Member | AB | BC | AD | BD | BE | CE | DE |
|---|---|---|---|---|---|---|---|
| Force (N) | 1443.4 T | 2020.7 T | 2886.8 C | 577.4 T | **577.4 C** | 4041.5 C | 1732.1 C |

**Check.** The middle panel carries shear 2500 − 2000 = 500 N, and both diagonals have vertical component 500 N (577.4 × 0.866) ✓. The top chord is in compression and the bottom chord in tension, as for any simply supported truss ✓.

**Exam takeaway.** ⚠ **The slide table lists BE = 500 N (C). That is a slip.** 500 N is the diagonal's *vertical component*; the member force is $500/\sin60^\circ = 577.4$ N. **Variation:** equal loads at D and E make BD and BE zero (no panel shear).

---

#### Q20 (Slides Ch1) — Cantilever truss by joints *(medium)*
**Problem.** Wall joints A (top, y = 1.8 m) and E (bottom, y = 0). Top chord A–B–C with 2.4 m panels; bottom joint D below B. Members AB, BC, AD, BD, CD and ED. 30 kN acts down at B and at C. Find all member forces.

**Approach.** Start at the free joint C, which has only two unknowns. No reactions are needed until the end.

**Solution.**
1. *Geometry:* $\tan\theta = 1.8/2.4$, so θ = 36.87° ($\sin\theta = 0.6$, $\cos\theta = 0.8$) for AD and CD.
2. *Joint C:* vertical: $30 + F_{CD}(0.6) = 0$ with CD going down-left toward D, so $F_{CD} = -50$ kN (C). Horizontal: $F_{BC} = -F_{CD}(0.8) = 40$ kN (T).
3. *Joint B:* horizontal: $F_{BA} = F_{BC} = 40$ kN (T). Vertical: $F_{BD} + 30 = 0$ with BD pulling down on B when tensile, so $F_{BD} = -30$ kN (C).
4. *Joint D:* vertical: $0.6F_{DA} = 30 + 0.6(50)$, so $F_{DA} = 100$ kN (T). Horizontal: $F_{DE} = -120$ kN (C).

$$\boxed{BC = 40\,T,\ CD = 50\,C,\ BD = 30\,C,\ AB = 40\,T,\ AD = 100\,T,\ DE = 120\,C\ \ (\text{kN})}$$

**Check.** Moments about E for the whole truss: the wall reaction at A is $A_x$ along the top chord at height 1.8 m. $1.8A_x = 30(2.4) + 30(4.8) = 216$, so $A_x = 120$ kN of pull. That equals $F_{AB} + F_{AD}\cos\theta = 40 + 80 = 120$ ✓.

**Exam takeaway.** The slides show 40.01 and 50.01 because θ was rounded to 36.86°. Exact geometry gives round numbers. **Variation:** move both loads to C only (60 kN), then repeat.

---

#### Q21 (Slides Ch1) — Method of sections: GE, GC and BC *(medium)*
**Problem.** A pin at A and a roller at D, with 4 m panels and 3 m depth. 400 N acts horizontally at E and 1200 N downward at C. Find the forces in GE, GC and BC and state T or C.

**Given:** A(0,0), B(4,0), C(8,0), D(12,0), G(4,3), E(8,3). **Find:** $F_{GE}$, $F_{GC}$, $F_{BC}$.

**Approach.** Section a–a cuts GE, GC and BC. Keep the left part (A, B, G). Take moments about G and C so that each equation contains one unknown.

**Solution.**
1. *Reactions:* $A_x = 400$ N ←. $\sum M_A$: $D_y(12) - 1200(8) - 400(3) = 0$, so $D_y = 900$ N and $A_y = 300$ N.
2. *Moments about G (4, 3)* on the left part: $A_y$ (↑ at 4 m to the left) gives −1200 N·m. $A_x$ (← at 3 m below) gives −1200 N·m. $F_{BC}$ (assumed tensile, pointing →) at 3 m below G gives $+3F_{BC}$. So $-2400 + 3F_{BC} = 0$ and $F_{BC} = 800$ N (T).
3. *Moments about C (8, 0):* $A_y$ gives $-300(8) = -2400$. $A_x$ lies on the line through C, giving 0. $F_{GE}$ (→) at 3 m above C gives $-3F_{GE}$. So $F_{GE} = -800$ N (C).
4. *Vertical sum on the left part:* $300 - F_{GC}(3/5) = 0$, so $F_{GC} = 500$ N (T).

$$\boxed{F_{GE} = 800\ \text{N (C)},\qquad F_{GC} = 500\ \text{N (T)},\qquad F_{BC} = 800\ \text{N (T)}}$$

**Check.** These match the slide's answers. Horizontal sum on the left part: $-400 - 800 + 500(0.8) + 800 = 0$ ✓.

**Exam takeaway.** Moments about the intersection of two cut members give the third directly. That is the reason for choosing the section that way. **Variation:** ask for $F_{GB}$ instead, using a section through GE, GB and AB, or the joint B (where GB is then a zero-force check).

---

#### Q22 (Slides Ch1) — Sections with a horizontal load: CE, CF and FH *(medium)*
**Problem.** The top chord is B–C–E–G–I and the bottom chord A–D–F–H–J, with 3 m panels and 3 m depth. The diagonals are AC, CF, FG and GJ. A is a pin and J a roller. 20 kN acts horizontally (→) at B. Find $F_{CE}$, $F_{CF}$ and $F_{FH}$.

**Approach.** Reactions first, then two different sections.

**Solution.**
1. *Reactions:* $A_x = 20$ kN ←. $\sum M_A$: $J_y(12) = 20(3)$, so $J_y = 5$ kN ↑ and $A_y = 5$ kN ↓.
2. *Section through CE, CF and DF, left part.* Moments about F (6, 0): the 20 kN at B (3 m up) gives −60; $A_y$ = 5 ↓ at 6 m to the left gives +30; $F_{CE}$ (→) at 3 m above F gives −3$F_{CE}$. So $F_{CE} = -10$ kN (C).
3. *Same section, vertical sum:* $-5 - F_{CF}/\sqrt2 = 0$, so $F_{CF} = -7.07$ kN (C).
4. *Section through EG, FG and FH, right part.* Moments about G (9, 3): $J_y = 5$ ↑ at 3 m to the right gives +15; $F_{FH}$ (←, tensile on the right part) at 3 m below G gives −3$F_{FH}$. So $F_{FH} = 5$ kN (T).

$$\boxed{F_{CE} = 10\ \text{kN (C)},\quad F_{CF} = 7.07\ \text{kN (C)},\quad F_{FH} = 5\ \text{kN (T)}}$$

**Check.** These match the slide's answers ✓. A full solve also shows many zero-force verticals (see the diagram).

**Exam takeaway.** Horizontal loads create a couple of vertical reactions ($A_y$ down, $J_y$ up). Students who assume both reactions act upward get every sign wrong.

---

#### Q23 (Slides Ch1) — Zero-force members plus one joint: CE and CD *(medium)*
**Problem.** A cantilever truss has top chord B–C–E–G (3 m spacing) and a bottom chord A–D–F–G sloping at 40° near G, with verticals CD and EF and diagonal CF. 10 kN acts at G. Find $F_{CE}$ and $F_{CD}$.

**Approach.** Joint G first, then chain the zero-force rules.

**Solution.**
1. *Joint G:* vertical: $F_{GF}\sin40^\circ + 10 = 0$, so $F_{GF} = -15.56$ kN (C). Horizontal: $F_{GE} = -F_{GF}\cos40^\circ = 11.92$ kN (T).
2. *Joint E:* CE and EG are collinear and EF is the third member, with no load → $F_{EF} = 0$ (rule 2). So $F_{CE} = F_{EG} = 11.92$ kN (T).
3. *Joint F:* DF and FG are collinear and EF = 0, so CF is the odd one out → $F_{CF} = 0$.
4. *Joint C:* BC and CE are collinear and CF = 0, so the vertical CD is the odd one out → $F_{CD} = 0$.

$$\boxed{F_{CE} = 11.92\ \text{kN (T)},\qquad F_{CD} = 0}$$

**Check.** These match the slide's answers ✓.

**Exam takeaway.** Cascading zero-force members is fast and examiners love it. **Variation:** add a load at E; then EF is no longer zero and the cascade stops.

---

#### Q24 (Slides Ch1, "Question 2") — Find the load P that gives 3 kN in member AC *(medium, sections)*
**Problem.** A cantilever truss (60° triangles, height 2 m) carries loads P at C and E. Find P such that the force in AC is 3 kN.

**Approach.** Cut through AC, CD and the bottom member at D. Take moments about D, where CD and the bottom chord meet, so that only $F_{AC}$ and the loads appear.

**Solution.**
1. On the outer part, moments about D (horizontal arms 1.5 m to C and 4.5 m to E): $F_{AC}(2) - P(1.5) - P(4.5) = 0$.
2. So $F_{AC} = 6P/2 = 3P$.
3. Set $3P = 3$ kN.

$$\boxed{P = 1\ \text{kN}\ (AC \text{ in tension})}$$

**Check.** The top chord of a cantilever truss is in tension ✓.

**Exam takeaway.** "Find the load that gives force X in member Y" is a section question in disguise. **Variation:** the member has a maximum allowable force. Find the largest P for each member and take the smallest (just like Q25).

---

#### Q25 (Crandall Prob 1.31) — Six-member cantilever truss *(medium)*
**Problem.** Determine the forces in the six members of the truss. A (top) and E (bottom) are wall pins. B and C lie on the top line with AB = BC = L. D lies below B with BD = L. The members are AB, BC, ED, BD, EB and DC. A load W hangs at C.

**Given:** A(0,L), B(L,L), C(2L,L), E(0,0), D(L,0); load W ↓ at C. **Find:** all six member forces.

**Approach.** Joints, starting at the free end C (two unknowns), then D, then B.

**Solution.**
1. *Joint C* (members CB horizontal and CD diagonal at 45°): vertical: $F_{CD}\sin45^\circ + W = 0$ with CD pointing down-left toward D, so $F_{CD} = -\sqrt2W$ (C). Horizontal: $F_{CB} = -F_{CD}\cos45^\circ = W$ (T).
2. *Joint D* (members DE horizontal, DB vertical, DC diagonal): vertical: $F_{DB} + F_{DC}\sin45^\circ = 0$, so $F_{DB} = W$ (T). Horizontal: $-F_{DE} + F_{DC}\cos45^\circ = 0$, so $F_{DE} = -W$ (C).
3. *Joint B* (members BA, BC, BD, BE): vertical: $-F_{BD} - F_{BE}\sin45^\circ = 0$, so $F_{BE} = -\sqrt2W$ (C). Horizontal: $-F_{BA} + F_{BC} - F_{BE}\cos45^\circ = 0$, so $F_{BA} = W + W = 2W$ (T).

$$\boxed{AB = 2W\,(T),\ BC = W\,(T),\ BD = W\,(T),\ ED = W\,(C),\ EB = \sqrt2W\,(C),\ DC = \sqrt2W\,(C)}$$

Wall reactions: A pulls left with 2W. E pushes right with 2W and up with W.

**Check.** Moments about E for the whole truss: $W(2L) = 2W(L)$ ✓, where 2W is the horizontal force at A acting at height L.

**Exam takeaway.** This truss reappears in Ch. 2 (Crandall Prob 2.10), where its tip deflection is $12.66\,WL/AE$, found from these forces with Castigliano's theorem. **Variation:** load at B instead of C, which makes BC and CD zero.

---

#### Q26 (PYQ 2014-15 Test-1 Q1) — Cantilever truss: find W from $F_{BC}$ = 450 kN *(medium, 15 marks)*
**Problem.** The top chord is A–B–C–D and the bottom chord G–F–E, with AB = BC = CD = EF = FG = 6 m and BF = CE = 4 m. The diagonals are GB, FC and ED. Wall supports at A and G. Loads W at B, C and D. If the force in BC has magnitude 450 kN, find W.

**Approach.** Method of sections through BC, FC and FE. Keep the right part (C, D, E). Take moments about F, where FC and FE meet, so $F_{BC}$ is the only unknown.

**Solution.**
1. *Section:* cut BC (top), FC (diagonal) and FE (bottom). On the right part, the loads are W at C (6 m right of F) and W at D (12 m right of F).
2. *Moments about F:* $F_{BC}$ (assumed tensile, pointing ← toward B) acts 4 m above F. Equilibrium: $F_{BC}(4) - W(6) - W(12) = 0$.
3. So $F_{BC} = 18W/4 = 4.5W$.
4. $4.5W = 450$ kN gives W = 100 kN.

$$\boxed{W = 100\ \text{kN}\ (BC \text{ in tension})}$$

**Check.** A full joint-by-joint solve with W = 100 kN gives BC = 450 kN T, AB = 900 kN T and GF = 450 kN C. The top chord is in tension, as expected for a cantilever ✓.

**Exam takeaway.** A 15-mark question that takes three lines once you pick the right moment point. **Variation:** "find the force in GB". Cut AB, GB and GF, take moments about G for AB, then use the vertical sum for GB.

---

## Chapter 1 — Formula and convention sheet

| Topic | Key relation |
|---|---|
| Moment of a force | $M_O = Fd = xF_y - yF_x$ (counter-clockwise +) |
| Couple | $C = Fd$, same about every point; no force resultant |
| Force-couple equivalence | F at A ≡ F at O + $\mathbf r_{OA}\times\mathbf F$; F and M ≡ F displaced by $a = M/F$ |
| Equilibrium (2-D) | $\sum F_x=\sum F_y=\sum M_O=0$ (or 2 moments + 1 force, or 3 moments about non-collinear points) |
| Supports | roller 1, pin 2, fixed 3 (2-D); ball-and-socket 3, fixed 6 (3-D) |
| Two-force member | Equal, opposite, along the line joining the pins |
| Three-force member | Lines of action concurrent (or all parallel) |
| Static friction | $f\le\mu_s N$; at impending motion $f=\mu_s N$, opposing motion |
| Incline, impending up/down | $T=W(\sin\alpha\pm\mu\cos\alpha)$; angle of repose $\tan\alpha=\mu$ |
| 3-D friction on an incline | μN balances the **resultant** of the in-plane forces |
| Belt friction | $T_2/T_1=e^{\mu\beta}$ (β in rad); $T(\theta)=T_1e^{\mu\theta}$ |
| Truss determinacy | $m=2j-3$ (with 3 reactions) |
| Zero-force rules | 2 non-collinear unloaded → both 0; 3 with 2 collinear unloaded → third 0 |
| Sections | Cut ≤ 3 members; moments about the intersection of two unknowns |
| Chord/diagonal checks | chord = M/h; diagonal = V/sinθ |
| Sign convention | Assume tension; a negative answer means compression |

**Other Crandall Ch. 1 problems worth practising** (same patterns): 1.8, 1.9 (FBDs of beams and cylinders), 1.12–1.16 (brackets, pedals, welds), 1.22 (frames), 1.24–1.27 (friction, wedges), 1.36 (logs in a tilted truck), 1.43–1.44 (camp stool, rod angle).
