import re, os, subprocess
D = "/tmp/claude-0/-home-user-mech-sol-/5e236ef2-e171-5cb2-82aa-007544f55ba5/scratchpad/docx"
G = "/home/user/mech-sol-/study-guide"
IMG = D + "/img"

def S(deck, p):  # slide page
    names = {"c1": "Slides Ch 1", "c2": "Slides Ch 2", "c3": "Slides Ch 3", "c4a": "Slides Ch 4 Part 1", "c4b": "Slides Ch 4 Part 2",
             "c5": "Slides Ch 5", "c6": "Slides Ch 6"}
    return (f"src_{deck}_p{p}.jpg", f"Original: {names[deck]}, slide {p}", 4.6)

def Y(name, label):
    return (f"{name}.jpg", f"Original question: {label}", 6.2)

def F(name, cap, w=6.0):
    return (f"{name}.png", cap, w)

PB = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'

# (anchor regex, sub-anchor regex or None, mode, [images])
# mode: 'after' = after the anchor paragraph; 'end' = before the next ---/####/## line
plan = {
 "ch1-equilibrium-friction-trusses.md": [
  (r"^## Concept 1\.2", r"^\| Support \(slides\)", "aftertable", [S("c1", 8)]),
  (r"^#### Q1 ", None, "after", [S("c1", 12)]),
  (r"^#### Q2 ", None, "after", [S("c1", 10)]),
  (r"^#### Q3 ", None, "after", [S("c1", 15)]),
  (r"^#### Q4 ", None, "after", [S("c1", 13)]),
  (r"^#### Q4 ", None, "end", [F("c1_cyl", "Worked FBDs: system, cylinder Q, cylinder P", 6.4)]),
  (r"^#### Q5 ", None, "after", [S("c1", 14)]),
  (r"^#### Q5 ", None, "end", [F("c1_roller", "Geometry and three-force FBD at lift-off (pushed case)", 5.6)]),
  (r"^#### Q6 ", None, "after", [S("c1", 16)]),
  (r"^#### Q7 ", None, "after", [S("c1", 17)]),
  (r"^#### Q8 ", None, "after", [S("c1", 24)]),
  (r"^#### Q8 ", None, "end", [F("c1_incline", "Worked FBD of the block", 5.2)]),
  (r"^#### Q9 ", None, "after", [S("c1", 25)]),
  (r"^#### Q10 ", None, "after", [S("c1", 26)]),
  (r"^#### Q11 ", None, "after", [Y("y14_T1Q3", "PYQ 2014-15 Test-1 Q3")]),
  (r"^#### Q11 ", None, "end", [F("c1_drum", "Rope tension varies exponentially along the drum", 6.2)]),
  (r"^## Concept 1\.4", r"^\*\*Stability / determinacy", "after", [S("c1", 33)]),
  (r"^#### Q12 ", None, "after", [S("c1", 41)]),
  (r"^#### Q12 ", None, "end", [F("c1_q12", "Solution: member forces (blue = tension, red = compression)", 5.6)]),
  (r"^#### Q13 ", None, "after", [S("c1", 39)]),
  (r"^#### Q13 ", None, "end", [F("c1_q13", "Solution: member forces; note BE = 577 N (C), not 500 N", 5.6)]),
  (r"^#### Q14 ", None, "after", [S("c1", 43)]),
  (r"^#### Q14 ", None, "end", [F("c1_q14", "Solution: member forces", 5.6)]),
  (r"^#### Q15 ", None, "after", [S("c1", 53)]),
  (r"^#### Q16 ", None, "after", [S("c1", 52)]),
  (r"^#### Q16 ", None, "end", [F("c1_q16", "Full joint-by-joint solution, used to check the section answers", 5.6)]),
  (r"^#### Q17 ", None, "after", [S("c1", 55)]),
  (r"^#### Q17 ", None, "end", [F("c1_q17", "Full solution (zero-force members dashed)", 6.2)]),
  (r"^#### Q18 ", None, "after", [S("c1", 56)]),
  (r"^#### Q19 ", None, "after", [S("c1", 38)]),
  (r"^#### Q20 ", None, "after", [Y("y14_T1Q1", "PYQ 2014-15 Test-1 Q1")]),
  (r"^#### Q20 ", None, "end", [F("c1_q20", "Check: full solve with W = 100 kN", 6.2)]),
 ],
 "ch2-deformable-bodies-axial-energy.md": [
  (r"^## Concept 2\.1", r"^\*\*4\. Derivation", "after", [S("c2", 3), F("c2_springs", "Parallel springs share the deflection", 4.6)]),
  (r"^## Concept 2\.2", r"^\*\*3\. Formal treatment", "after", [S("c2", 10)]),
  (r"^#### Q1 ", None, "after", [S("c2", 11)]),
  (r"^#### Q1 ", None, "end", [F("c2_q1", "Axial force diagram (tension +)", 5.6)]),
  (r"^#### Q2 ", None, "after", [S("c2", 12)]),
  (r"^#### Q2 ", None, "end", [F("c2_q2", "Axial force diagram (bar width shows the area)", 5.6)]),
  (r"^#### Q3 ", None, "after", [S("c2", 15)]),
  (r"^#### Q4 ", None, "after", [S("c2", 30)]),
  (r"^#### PYQs on this concept", None, "after", [Y("y14_CA8", "PYQ 2014-15 Compre A Q8")]),
  (r"^## Concept 2\.3", r"^\*\*5\. Picture", "after", [S("c2", 13)]),
  (r"^#### Q5 ", None, "after", [S("c2", 14)]),
  (r"^#### Q5 ", None, "end", [F("c2_q5", "Final axial forces: upper part in tension, lower part in compression", 5.6)]),
  (r"^#### Q6 ", None, "after", [S("c2", 31)]),
  (r"^## Concept 2\.4", r"^\*\*5\. Graphical construction", "after", [S("c2", 16)]),
  (r"^#### Q7 ", None, "after", [S("c2", 19)]),
  (r"^#### Q7 ", None, "end", [F("c2_q7", "Williot (displacement) diagram for joint D", 6.2)]),
  (r"^#### Q8 ", None, "after", [S("c2", 27)]),
  (r"^## Concept 2\.5", r"^\*\*3\. Formal treatment", "after", [S("c2", 22)]),
  (r"^#### Q9 ", None, "after", [S("c2", 26)]),
  (r"^#### Q10 ", None, "after", [S("c2", 24)]),
  (r"^#### Q11 ", None, "after", [Y("y14_T1Q2", "PYQ 2014-15 Test-1 Q2")]),
  (r"^#### Q11 ", None, "end", [F("c2_q11", "Castigliano set-up with fictitious load Q", 5.6)]),
  (r"^#### Q12 ", None, "after", [Y("y19_A3", "PYQ 2019-20 Compre A Q3")]),
  (r"^#### Q13 ", None, "after", [S("c2", 25)]),
  (r"^#### Q13 ", None, "end", [F("c2_q13", "Member forces from the 180 kN and 270 kN loads", 6.2)]),
  (r"^#### Q14 ", None, "after", [S("c2", 29)]),
  (r"^#### Q15 ", None, "after", [S("c2", 28)]),
  (r"^#### Q16 ", None, "after", [S("c2", 32), S("c2", 33)]),
  (r"^\*\*PYQ 2014-15 Compre A Q11", None, "after", [Y("y14_CA11", "PYQ 2014-15 Compre A Q11")]),
 ],
 "ch3-slender-members-sfd-bmd.md": [
  (r"^## ⚠️ Read first", r"^Quick rule", "after", [S("c3", 9), F("c3_sign", "Positive shear and positive bending moment (Crandall)", 5.0)]),
  (r"^## Concept 3\.1", r"^\*\*4\. Derivation", "after", [S("c3", 15)]),
  (r"^#### Q1 ", None, "after", [S("c3", 16)]),
  (r"^#### Q1 ", None, "end", [F("c3_q1", "Solution: loading, SFD, BMD")]),
  (r"^#### Q2 ", None, "after", [S("c3", 17)]),
  (r"^#### Q2 ", None, "end", [F("c3_q2", "Solution with P = 10 kN, L = 4 m (M jumps up at B because of the clockwise couple)")]),
  (r"^#### Q3 ", None, "after", [S("c3", 28)]),
  (r"^#### Q3 ", None, "end", [F("c3_q3", "Vertical-load SFD/BMD for ABCD (M at C = 50.4 kN·m)")]),
  (r"^#### Q4 ", None, "after", [Y("y14_CA12_14", "PYQ 2014-15 Compre A Q12–Q14")]),
  (r"^## Concept 3\.2", r"^\*Slide illustration", "after", [S("c3", 22)]),
  (r"^#### Q6 ", None, "after", [S("c3", 29)]),
  (r"^#### Q6 ", None, "end", [F("c3_q6", "Solution")]),
  (r"^#### Q7 ", None, "after", [S("c3", 26)]),
  (r"^#### Q7 ", None, "end", [F("c3_q7", "Solution with W = 12 kN, L = 6 m")]),
  (r"^#### Q8 ", None, "after", [S("c3", 27)]),
  (r"^#### Q8 ", None, "end", [F("c3_q8", "Solution with w₀ = 10 kN/m, a = 3 m, L = 5 m")]),
  (r"^#### Q9 ", None, "after", [S("c3", 42)]),
  (r"^#### Q9 ", None, "end", [F("c3_q9", "Solution")]),
  (r"^## Concept 3\.3", r"^\*\*3\. Formal treatment / 4\. Derivation", "after", [S("c3", 31)]),
  (r"^#### Q10 ", None, "after", [S("c3", 30)]),
  (r"^#### Q10 ", None, "end", [F("c3_q10", "Solution")]),
  (r"^#### Q11 ", None, "after", [S("c3", 41)]),
  (r"^#### Q11 ", None, "end", [F("c3_q11", "Solution")]),
  (r"^#### Q12 ", None, "after", [S("c3", 25)]),
  (r"^#### Q12 ", None, "end", [F("c3_q12", "Solution: the arm forces become a 20 kN·m clockwise couple at D")]),
  (r"^#### Q13 ", None, "after", [S("c3", 40)]),
  (r"^#### Q13 ", None, "end", [F("c3_q13", "Solution for the optimum overhang a = 0.414L")]),
  (r"^#### Q14 ", None, "after", [S("c3", 40)]),
  (r"^#### Q14 ", None, "end", [F("c3_q14", "Solution")]),
  (r"^#### Q15 ", None, "end", [F("c3_q15", "Solution: sawhorse at 4.62 m, M = 0 at the cut (x = 4.2 m)")]),
  (r"^## Concept 3\.4", r"^\*Loading representation", "after", [S("c3", 35)]),
  (r"^#### Q16 ", None, "after", [Y("y14_T1Q4", "PYQ 2014-15 Test-1 Q4")]),
  (r"^#### Q16 ", None, "end", [F("c3_q16", "Solution: SFD and BMD from the singularity equations")]),
  (r"^#### Q17 ", None, "after", [Y("y14_CA17_18", "PYQ 2014-15 Compre A Q17–Q18")]),
  (r"^#### Q17 ", None, "end", [F("c3_q17", "Solution")]),
  (r"^#### Q18 ", None, "after", [Y("y19_A1", "PYQ 2019-20 Compre A Q1")]),
  (r"^#### Q18 ", None, "end", [F("c3_q18", "Bending moment along the bracket (units of Pb)", 6.4)]),
  (r"^#### Q19 ", None, "after", [Y("y19_A3", "PYQ 2019-20 Compre A Q3")]),
  (r"^#### Q19 ", None, "end", [F("c3_q19", "Internal forces vs θ", 4.8)]),
 ],
 "ch4-stress-strain-mohr.md": [
  (r"^## ⚠️ Read first", r"^4\. \*\*Strain Mohr", "after", [F("c4_posshear", "A positive τxy element", 2.8)]),
  (r"^## Concept 4\.1", r"^\*\*2\. Why it matters", "after", [S("c4a", 3)]),
  (r"^## Concept 4\.1", r"^\*\*4\. Derivation", "after", [S("c4a", 11)]),
  (r"^## Concept 4\.2", r"^\*\*4\. Derivation", "after", [S("c4a", 15)]),
  (r"^## Concept 4\.3", r"^\*\*5\. Graphical construction", "after", [F("c4_mohr_construct", "Mohr's circle construction (Crandall convention)", 5.6)]),
  (r"^## Concept 4\.3", r"^\*\*6\. Special cases", "after", [F("c4_signature", "Signature circles: uniaxial tension, uniaxial compression, pure shear, equal biaxial", 6.2)]),
  (r"^#### Q1 ", None, "after", [S("c4a", 21)]),
  (r"^#### Q1 ", None, "end", [F("c4_q1", "Mohr's circle: diameter XY rotated 90° to X′Y′", 5.2)]),
  (r"^#### Q2 ", None, "after", [S("c4a", 35)]),
  (r"^#### Q2 ", None, "end", [F("c4_q2", "Mohr's circle check", 5.2)]),
  (r"^#### Q3 ", None, "after", [S("c4a", 33)]),
  (r"^#### Q3 ", None, "end", [F("c4_q3", "Uniaxial circle with the weld plane marked", 5.2)]),
  (r"^#### Q4 ", None, "after", [S("c4a", 24)]),
  (r"^#### Q4 ", None, "end", [F("c4_q4", "Mohr's circle", 5.2), F("c4_q4e", "Stress elements: given, principal, maximum shear", 6.4)]),
  (r"^#### Q5 ", None, "after", [S("c4a", 30)]),
  (r"^#### Q5 ", None, "end", [F("c4_q5", "Mohr's circle with the rotated diameter X′Y′", 5.2), F("c4_q5e", "Stress elements", 6.4)]),
  (r"^#### Q6 ", None, "after", [Y("y14_CA12_14", "PYQ 2014-15 Compre A Q12–Q13")]),
  (r"^#### Q8 ", None, "after", [Y("y14_T2Q1", "PYQ 2014-15 Test-2 Q1")]),
  (r"^#### Q8 ", None, "end", [F("c4_q8", "Mohr's circle", 5.2)]),
  (r"^#### Q9 ", None, "after", [Y("y14_CB1", "PYQ 2014-15 Compre B Q1")]),
  (r"^#### Q9 ", None, "end", [F("c4_q9", "Mohr's circle, with the σ3 = 0 circles dashed", 5.2), F("c4_q9e", "Resultant x–y element and principal element", 6.4)]),
  (r"^## Concept 4\.4", r"^\*\*3\. Formal treatment", "after", [S("c4b", 1), S("c4b", 3)]),
  (r"^## Concept 4\.5", r"^\*\*3–4\. Derivation", "after", [S("c4b", 4)]),
  (r"^#### Q10 ", None, "after", [S("c4b", 6), S("c4b", 7)]),
  (r"^#### Q10 ", None, "end", [F("c4_q10", "Strain Mohr's circle (vertical axis γ/2)", 5.2)]),
  (r"^#### Q11 ", None, "after", [S("c4b", 8)]),
  (r"^#### Q11 ", None, "end", [F("c4_q11", "Strain Mohr's circle", 5.2)]),
  (r"^## Concept 4\.6", r"^\*\*3\. Formal treatment", "after", [S("c4b", 10), S("c4b", 11)]),
  (r"^#### Q12 ", None, "after", [S("c4b", 12)]),
  (r"^#### Q12 ", None, "end", [F("c4_q12", "Strain Mohr's circle", 5.2)]),
  (r"^#### Q13 ", None, "after", [Y("y21_A1", "PYQ 2021-22 Compre A Q1")]),
  (r"^#### Q14 ", None, "after", [Y("y19_A2", "PYQ 2019-20 Compre A Q2")]),
  (r"^#### Q14 ", None, "end", [F("c4_q14", "Stress Mohr's circle used to return to x–y", 5.2)]),
  (r"^#### Q15 ", None, "after", [Y("y21_B1", "PYQ 2021-22 Compre B Q1")]),
  (r"^#### Q15 ", None, "end", [F("c4_q15", "The deformed circle (strains exaggerated ×300)", 4.2)]),
  (r"^#### Q16 ", None, "after", [Y("y14_T2Q2", "PYQ 2014-15 Test-2 Q2")]),
  (r"^#### Q16 ", None, "end", [F("c4_q16", "Strain circle for the uniaxial bar", 4.8)]),
 ],
 "ch5-stress-strain-temperature-yield.md": [
  (r"^## Concept 5\.1", r"^\*\*3\. Formal treatment", "after", [S("c5", 5), S("c5", 9)]),
  (r"^## Concept 5\.1", r"^\*\*Idealized curves", "after", [F("c5_ideal", "Idealized stress–strain curves", 6.2)]),
  (r"^## Concept 5\.2", r"^\*\*3\. Formal treatment", "after", [S("c5", 16)]),
  (r"^## Concept 5\.2", r"^\*\*Isotropy arguments", "after", [S("c5", 19), S("c5", 21)]),
  (r"^#### Q1 ", None, "after", [Y("y14_CA1to5", "PYQ 2014-15 Compre A Q1–Q5")]),
  (r"^#### Q2 ", None, "after", [Y("y23_A3", "PYQ 2023-24 Compre A Q3")]),
  (r"^#### Q3 ", None, "after", [Y("y24_A2", "PYQ 2024-25 Compre A Q2")]),
  (r"^#### Q4 ", None, "after", [S("c5", 29)]),
  (r"^## Concept 5\.3", r"^\*\*4\. Derivation", "after", [S("c5", 25)]),
  (r"^## Concept 5\.4", r"^\*\*4\. Derivation", "after", [S("c5", 26), F("c5_thermal", "Thermal stress by superposition", 5.6)]),
  (r"^#### Q6 ", None, "after", [S("c5", 48)]),
  (r"^#### Q7 ", None, "after", [S("c5", 49)]),
  (r"^#### Q8 ", None, "after", [S("c5", 47)]),
  (r"^#### Q9 ", None, "after", [S("c5", 50)]),
  (r"^#### Q10 ", None, "after", [S("c5", 53)]),
  (r"^#### Q11 ", None, "after", [Y("y14_T2Q3", "PYQ 2014-15 Test-2 Q3")]),
  (r"^## Concept 5\.5", r"^\*Uniaxial:", "after", [S("c5", 30)]),
  (r"^## Concept 5\.6", r"^\*\*5\. Picture", "after", [S("c5", 39), S("c5", 45), F("c5_yield", "Tresca hexagon inside the von Mises ellipse", 4.6)]),
  (r"^#### Q14 ", None, "after", [Y("y19_A4", "PYQ 2019-20 Compre A Q4")]),
  (r"^#### Q14 ", None, "end", [F("c5_q14", "Mohr's circles including σ3 = 0", 5.2)]),
  (r"^#### Q15 ", None, "after", [S("c5", 58)]),
 ],
 "ch6-torsion.md": [
  (r"^## Concept 6\.1", r"^\*\*3\. Formal treatment", "after", [S("c6", 7)]),
  (r"^## Concept 6\.1", r"^\*\*4\. Derivation of shear strain", "after", [S("c6", 9)]),
  (r"^## Concept 6\.2", r"^\*\*5\. Stress picture", "after", [S("c6", 12), F("c6_dist", "Shear stress varies linearly with radius", 5.4)]),
  (r"^#### Q1 ", None, "after", [S("c6", 15)]),
  (r"^#### Q2 ", None, "after", [S("c6", 18)]),
  (r"^#### Q3 ", None, "after", [S("c6", 16)]),
  (r"^#### Q4 ", None, "after", [S("c6", 17)]),
  (r"^#### Q5 ", None, "after", [S("c6", 25)]),
  (r"^#### Q5 ", None, "end", [F("c6_q5", "Internal torque diagram", 5.6)]),
  (r"^#### Q6 ", None, "after", [S("c6", 28)]),
  (r"^#### Q7 ", None, "after", [S("c6", 19)]),
  (r"^#### Q7 ", None, "end", [F("c6_q7", "Internal torque diagram", 5.6)]),
  (r"^#### Q8 ", None, "after", [S("c6", 45)]),
  (r"^#### Q9 ", None, "after", [S("c6", 42)]),
  (r"^#### Q10 ", None, "after", [S("c6", 44)]),
  (r"^#### Q11 ", None, "after", [S("c6", 49)]),
  (r"^#### Q12 ", None, "after", [Y("y14_CA1to5", "PYQ 2014-15 Compre A Q5")]),
  (r"^#### Q13 ", None, "after", [Y("y14_T2Q4", "PYQ 2014-15 Test-2 Q4")]),
  (r"^#### Q14 ", None, "after", [Y("y23_A1", "PYQ 2023-24 Compre A Q1")]),
  (r"^#### Q14 ", None, "end", [F("c6_q14", "Internal torque diagram", 5.6)]),
  (r"^## Concept 6\.3", r"^\*\*3\. Formal treatment", "after", [S("c6", 30)]),
  (r"^#### Q15 ", None, "after", [S("c6", 32)]),
  (r"^#### Q16 ", None, "after", [S("c6", 31)]),
  (r"^#### Q17 ", None, "after", [Y("y14_CB2", "PYQ 2014-15 Compre B Q2")]),
  (r"^#### Q18 ", None, "after", [Y("y19_B4", "PYQ 2019-20 Compre B Q4")]),
  (r"^#### Q19 ", None, "after", [S("c6", 21)]),
  (r"^#### Q19 ", None, "end", [F("c6_q19", "Internal torque diagram", 5.6)]),
  (r"^#### Q20 ", None, "after", [Y("y24_B1", "PYQ 2024-25 Compre B Q1")]),
  (r"^#### Q20 ", None, "end", [F("c6_q20", "Internal torque and angle of twist along the bar", 5.6)]),
  (r"^## Concept 6\.5", r"^\*\*3\. Formal treatment", "after", [S("c6", 22), S("c6", 23)]),
  (r"^#### Q21 ", None, "after", [S("c6", 37)]),
  (r"^#### Q22 ", None, "after", [S("c6", 40)]),
  (r"^#### Q22 ", None, "end", [F("c6_q22", "Mohr's circle", 5.0)]),
  (r"^#### Q24 ", None, "after", [Y("y21_A2", "PYQ 2021-22 Compre A Q2")]),
  (r"^#### Q24 ", None, "end", [F("c6_q24", "Mohr's circle at H", 5.0), F("c6_q24e", "Stress elements at H", 6.4)]),
  (r"^#### Q25 ", None, "after", [Y("y23_B2", "PYQ 2023-24 Compre B Q2")]),
  (r"^#### Q25 ", None, "end", [F("c6_q25", "Mohr's circle at element E₁", 5.0)]),
  (r"^#### Q26 ", None, "after", [Y("y24_B2", "PYQ 2024-25 Compre B Q2")]),
  (r"^#### Q26 ", None, "end", [F("c6_q26", "Mohr's circle at B", 5.0), F("c6_q26e", "Stress elements at B", 6.4)]),
 ],
}


def img_md(imgs):
    out = []
    for fn, cap, w in imgs:
        assert os.path.exists(f"{IMG}/{fn}"), fn
        out += ["", f"![{cap}]({IMG}/{fn}){{width={w}in}}", ""]
    return out


def para_end(lines, i):
    j = i + 1
    while j < len(lines) and lines[j].strip() != "":
        j += 1
    return j


def apply(fname, items):
    lines = open(f"{G}/{fname}").read().split("\n")
    inserts = []  # (index, lines)
    for anchor, sub, mode, imgs in items:
        ia = next(k for k, l in enumerate(lines) if re.search(anchor, l))
        if mode == "after" and sub is None:
            inserts.append((ia + 1, img_md(imgs)))
        elif mode in ("after", "aftertable"):
            ib = next(k for k in range(ia, len(lines)) if re.search(sub, lines[k]))
            inserts.append((para_end(lines, ib), img_md(imgs)))
        elif mode == "end":
            k = ia + 1
            while k < len(lines) and not re.match(r"^(---\s*$|#### |## |### )", lines[k]):
                k += 1
            inserts.append((k, img_md(imgs)))
    for idx, ins in sorted(inserts, key=lambda t: t[0], reverse=True):
        lines[idx:idx] = ins
    return "\n".join(lines)


def fix_blocks(md):
    """pandoc needs a blank line before lists and tables."""
    out = []
    lines = md.split("\n")
    for i, l in enumerate(lines):
        st = l.lstrip()
        is_item = bool(re.match(r"^([-*+] |\d+\. |\|)", st)) and not st.startswith("**")
        if is_item and out and out[-1].strip() != "":
            prev = out[-1].lstrip()
            prev_item = bool(re.match(r"^([-*+] |\d+\. |\|)", prev))
            prev_cont = out[-1].startswith("   ") and not st.startswith("|")
            if not prev_item and not prev_cont:
                out.append("")
        out.append(l)
    return "\n".join(out)


def clean(md):
    md = fix_blocks(md)
    md = md.replace("⚠️", "⚠").replace("✓", "✓")
    md = re.sub(r"\n---\n", "\n\n", md)   # horizontal rules -> nothing (headings carry structure)
    # demote: chapter title "# " stays H1, "### subtitle" right after title -> italic line
    md = re.sub(r"^(# .*)\n### (.*)$", r"\1\n\n*\2*", md, count=1, flags=re.M)
    md = md.replace("> Math is written in LaTeX (`$...$`). It renders on GitHub, in VS Code's Markdown preview, and in Obsidian/Typora.\n", "")
    return md


parts = []
readme = open(f"{G}/README.md").read()
readme = readme.split("## Part 1")[0], "## Part 1" + readme.split("## Part 1")[1]
intro = readme[0]
intro = re.sub(r"\| File \| Topics \| Solved Qs \|.*?\n\n", "", intro, flags=re.S)
intro = intro.replace("Math is in LaTeX (`$…$`). It renders on GitHub, in VS Code's Markdown preview, Obsidian and Typora.\n", "")
intro = intro.replace("# ME F211 Mechanics of Solids — Exam Study Guide (Ch 1–6)", "# How to use this guide")
intro += ("\n**What's new in this Word edition:** every solved question now shows the **original problem figure** "
          "(cropped from the lecture slides or the question paper) directly under its heading, and most solutions end with a "
          "**worked diagram** drawn from the solution itself: free-body diagrams, truss member-force maps (blue = tension, "
          "red = compression), shear-force and bending-moment diagrams (Crandall sign convention), axial-force and torque "
          "diagrams, Mohr's circles (+τ plotted down at X) and rotated stress elements.\n")
parts.append(clean(intro))
for f in plan:
    parts.append(PB + clean(apply(f, plan[f])))
parts.append(PB + clean(readme[1].replace("## Part 1", "# Course summary\n\n## Part 1", 1)))
full = "\n\n".join(parts)
open(f"{D}/combined.md", "w").write(full)
print(len(full), full.count("!["))
