import subprocess
S='/tmp/claude-0/-home-user-mech-sol-/5e236ef2-e171-5cb2-82aa-007544f55ba5/scratchpad'
OUT=S+'/docx/img'
# (name, source image, x0, y0, x1, y1)
boxes = [
 ('bk_1_21', 'bookimg/s-033.png', 990, 620, 1520, 915),
 ('bk_1_31', 'bookimg/s-036.png', 1005, 262, 1510, 512),
 ('bk_1_39', 'bookimg/s-038.png', 1015, 258, 1515, 640),
 ('bk_1_42', 'bookimg/s-039.png', 1015, 275, 1345, 452),
 ('bk_2_10', 'bookimg/s-067.png', 120, 580, 650, 875),
 ('bk_2_11', 'bookimg/s-067.png', 1015, 325, 1330, 530),
 ('bk_2_12', 'bookimg/s-067.png', 1005, 540, 1525, 840),
 ('bk_2_14', 'bookimg/s-068.png', 372, 290, 690, 475),
 ('bk_2_17', 'bookimg/s-068.png', 1005, 600, 1525, 905),
 ('bk_2_20', 'bookimg/s-069.png', 25, 690, 705, 910),
 ('bk_3_1', 'bookimg/s-097.png', 330, 445, 650, 745),
 ('bk_3_4', 'bookimg/s-097.png', 1005, 255, 1330, 575),
 ('bk_3_6', 'bookimg/s-097.png', 1005, 585, 1260, 690),
 ('bk_3_9', 'bookimg/s-098.png', 440, 245, 660, 385),
 ('bk_3_10', 'bookimg/s-098.png', 25, 395, 660, 618),
 ('bk_3_12', 'bookimg/s-098.png', 25, 812, 660, 965),
 ('bk_3_14', 'bookimg/s-098.png', 1005, 505, 1510, 695),
 ('bk_4_7', 'bk/s133_1.png', 60, 545, 680, 925),
 ('bk_4_15', 'bk/s135_0.png', 390, 275, 705, 565),
 ('bk_4_27', 'bk/s137_0.png', 330, 245, 690, 400),
 ('bk_4_28', 'bk/s137_0.png', 60, 440, 700, 665),
 ('bk_4_25', 'bk/s136_1.png', 80, 230, 700, 430),
 ('bk_4_32', 'bk/s137_1.png', 60, 235, 700, 450),
 ('bk_5_9', 'bk/s181_0.png', 60, 735, 720, 965),
 ('bk_5_12', 'bk/s181_1.png', 60, 640, 720, 830),
 ('bk_5_18', 'bk/s182_1.png', 60, 240, 720, 655),
]
for n, src, x0, y0, x1, y1 in boxes:
    subprocess.run(['convert', f'{S}/{src}', '-crop', f'{x1-x0}x{y1-y0}+{x0}+{y0}', '+repage', '-fuzz', '8%', '-trim',
                    '-bordercolor', 'white', '-border', '10', '-quality', '85', f'{OUT}/{n}.jpg'], check=True)
print(len(boxes))
