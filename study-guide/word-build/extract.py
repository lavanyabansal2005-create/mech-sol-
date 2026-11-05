import subprocess, os
S='/tmp/claude-0/-home-user-mech-sol-/5e236ef2-e171-5cb2-82aa-007544f55ba5/scratchpad'
R='/home/user/mech-sol-'
OUT=S+'/docx/img'
decks={'c1':'chapter 1 slides (1).pdf','c2':'Chapter 2 (1).pdf','c3':'Chapter 3 slides.pdf','c4a':'Chapter 4 part 1.pdf','c4b':'Ch 4 Part 2 (1).pdf','c5':'Chapter 5 slides.pdf','c6':'6.pdf'}
slides={'c1':[10,12,13,14,15,16,17,24,25,26,33,38,39,41,43,46,52,53,55,56,9,7],
 'c2':[3,11,12,14,15,19,25,26,27,28,29,30,31,32,33,13,10,16,22],
 'c3':[9,12,15,16,17,22,25,26,27,28,29,30,31,40,41,42,8],
 'c4a':[2,3,11,12,15,19,20,21,22,24,27,30,33,35,13],
 'c4b':[1,3,4,6,7,8,12,11,10,13],
 'c5':[5,9,14,16,25,26,29,39,45,46,47,48,49,50,53,58,19,21],
 'c6':[7,9,15,16,17,18,19,21,22,23,25,28,31,32,37,40,42,44,45,49,30]}
for d,pages in slides.items():
    for p in pages:
        o=f'{OUT}/src_{d}_p{p}'
        if os.path.exists(o+'.jpg'): continue
        subprocess.run(['pdftoppm','-r','110','-jpeg','-jpegopt','quality=82','-singlefile','-f',str(p),'-l',str(p),f'{R}/{decks[d]}',o],check=True)
# PYQ crops: (name, pdf, page, ytop_pt, ybot_pt)
pt=[('y23_A1','1157_ME_F211_20240212042616_Comprehensive_Exam_Question_Paper',1,100,412),
    ('y23_A3','1157_ME_F211_20240212042616_Comprehensive_Exam_Question_Paper',1,492,760),
    ('y23_B2','1157_ME_F211_20240212042616_Comprehensive_Exam_Question_Paper',2,342,494),
    ('y24_A2','1160_ME_F211_20241216111807_Comprehensive_Exam_Question_Paper',1,365,464),
    ('y24_B1','1160_ME_F211_20241216111807_Comprehensive_Exam_Question_Paper',2,133,386),
    ('y24_B2','1160_ME_F211_20241216111807_Comprehensive_Exam_Question_Paper',2,385,770),
    ('y19_A1','19-20_-_MechSol_-_Compre_1',1,222,496),
    ('y19_A2','19-20_-_MechSol_-_Compre_1',1,495,770),
    ('y19_A3','19-20_-_MechSol_-_Compre_1',2,50,343),
    ('y19_A4','19-20_-_MechSol_-_Compre_1',2,342,770),
    ('y19_B4','19-20_-_MechSol_-_Compre_1',4,347,770),
    ('y21_A1','21-22_-_MechSol_-_Compre_1',1,116,267),
    ('y21_A2','21-22_-_MechSol_-_Compre_1',1,266,543),
    ('y21_B1','21-22_-_MechSol_-_Compre_1',2,132,388)]
for n,pdf,p,a,b in pt:
    tmp=f'{S}/docx/tmp_{pdf[:8]}_{p}'
    if not os.path.exists(tmp+'.png'):
        subprocess.run(['pdftoppm','-r','150','-png','-singlefile','-f',str(p),'-l',str(p),f'{R}/{pdf}.pdf',tmp],check=True)
    k=150/72
    subprocess.run(['convert',tmp+'.png','-crop',f'1275x{int((b-a)*k)}+0+{int(a*k)}','+repage','-trim','-bordercolor','white','-border','12','-quality','85',f'{OUT}/{n}.jpg'],check=True)
# 2014 scan crops (pixel coords on 160dpi renders h14-N.png)
sc=[('y14_T1Q1',1,505,965),('y14_T1Q2',1,965,1467),('y14_T1Q3',2,55,690),('y14_T1Q4',2,685,1300),
    ('y14_T2Q1',3,470,1135),('y14_T2Q2',3,1135,1330),('y14_T2Q3',4,35,590),('y14_T2Q4',4,590,1500),
    ('y14_CA1to5',5,590,1135),('y14_CA8',5,1285,1400),('y14_CA11',5,1550,1640),
    ('y14_CA12_14',6,55,640),('y14_CA17_18',6,940,1295),('y14_CB1',7,480,1010),('y14_CB2',7,1010,1500)]
for n,p,a,b in sc:
    subprocess.run(['convert',f'{S}/pyq/h14-{p}.png','-crop',f'2000x{b-a}+0+{a}','+repage','-fuzz','12%','-trim','-bordercolor','white','-border','12','-quality','82',f'{OUT}/{n}.jpg'],check=True)
print(len(os.listdir(OUT)))
