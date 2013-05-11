from pyplasm import *
import scipy
from scipy import *

Dom1D = INTERVALS(1)(60)


#prof_lat

p0 = [[-4,0,0],[4,0,0]]
c0 = BEZIER(S1)(p0)
l0 = MAP(c0)(Dom1D)

p1 = [[-4,0,0],[-4.3,1.5,0],[-5.7,1.5,0],[-6,0,0]]
c1 = BEZIER(S1)(p1)
l1 = MAP(c1)(Dom1D)

p2 = [[-6,0,0],[-6.4,-0.1,0],[-8.1,0.5,0]]
c2 = BEZIER(S1)(p2)
l2 = MAP(c2)(Dom1D)

p3 = [[-8.1,0.5,0],[-7.8,0.5,0]]
c3= BEZIER(S1)(p3)
l3 = MAP(c3)(Dom1D)

p4 = [[-7.8,0.5,0],[-6.5,1.6,0],[-5.8,1.5,0],[-5,1.8,0]]
c4 = BEZIER(S1)(p4)
l4 = MAP(c4)(Dom1D)

p5 = [[-5,1.8,0],[-2.3,3,0]]
c5 = BEZIER(S1)(p5)
l5 = MAP(c5)(Dom1D)

p6 = [[-2.3,3,0],[-2,3.3,0],[1,3.2,0],[3,2.8,0]]
c6 = BEZIER(S1)(p6)
l6 = MAP(c6)(Dom1D)

p7 = [[3,2.8,0],[6,1.5,0]]
c7 = BEZIER(S1)(p7)
l7 = MAP(c7)(Dom1D)

p8 = [[6,1.5,0],[7.5,1.5,0]]
c8 = BEZIER(S1)(p8)
l8 = MAP(c8)(Dom1D)

p9 = [[7.5,1.5,0],[7.6,1.4,0]]
c9 = BEZIER(S1)(p9)
l9 = MAP(c9)(Dom1D)

p10 = [[7.6,1.4,0],[7.6,1,0]]
c10 = BEZIER(S1)(p10)
l10 = MAP(c10)(Dom1D)

p11 = [[7.6,1,0],[7.8,1,0]]
c11 = BEZIER(S1)(p11)
l11 = MAP(c11)(Dom1D)

p12 = [[7.8,1,0],[7.7,0.8,0]]
c12 = BEZIER(S1)(p12)
l12 = MAP(c12)(Dom1D)

p13 = [[7.7,0.8,0],[7.6,0.8,0]]
c13 = BEZIER(S1)(p13)
l13 = MAP(c13)(Dom1D)

p14 = [[7.6,0.8,0],[7,0.5,0]]
c14 = BEZIER(S1)(p14)
l14 = MAP(c14)(Dom1D)

p15 = [[7,0.5,0],[6.7,0.6,0],[6.5,-0.5,0],[6,0,0]]
c15 = BEZIER(S1)(p15)
l15 = MAP(c15)(Dom1D)

p16 = [[4,0,0],[4.3,1.5,0],[5.7,1.5,0],[6,0,0]]
c16 = BEZIER(S1)(p16)
l16 = MAP(c16)(Dom1D)

lp=STRUCT([l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16])
lateral_prof = T([2])(-1.65)(lp)

#prof_sup
p17 = [[0,0,0],[-4,0,0]]
c17 = BEZIER(S1)(p17)
l17 = MAP(c17)(Dom1D)

p18 = [[-4,0,0],[-4.5,0,-0.2],[-5.5,0,-0.2],[-6,0,0]]
c18 = BEZIER(S1)(p18)
l18 = MAP(c18)(Dom1D)

p19 = [[-6,0,0],[-8,0,0.5]]
c19 = BEZIER(S1)(p19)
l19 = MAP(c19)(Dom1D)

p20 = [[-8,0,0.5],[-8.02,0,0.6],[-8.04,0,0.7],[-8.05,0,1]]
c20 = BEZIER(S1)(p20)
l20 = MAP(c20)(Dom1D)

p21 = [[-8.05,0,1],[-8.1,0,2.5]]
c21 = BEZIER(S1)(p21)
l21 = MAP(c21)(Dom1D)

p22 = [[0,0,0],[4,0,-0.2]]
c22 = BEZIER(S1)(p22)
l22 = MAP(c22)(Dom1D)

p23 = [[4,0,-0.2],[4.5,0,-0.2],[5.5,0,-0.2],[6,0,0]]
c23 = BEZIER(S1)(p23)
l23 = MAP(c23)(Dom1D)

p24 = [[6,0,0],[8,0,0.5]]
c24 = BEZIER(S1)(p24)
l24 = MAP(c24)(Dom1D)

p25 = [[8,0,0.5],[8.02,0,0.6],[8.04,0,0.7],[8.05,0,1]]
c25 = BEZIER(S1)(p25)
l25 = MAP(c25)(Dom1D)

p26 = [[8.05,0,1],[8.1,0,2.5]]
c26 = BEZIER(S1)(p26)
l26 = MAP(c26)(Dom1D)




pr = STRUCT([l17,l18,l19,l20,l21,l22,l23,l24,l25,l26])

pr_ok = T([3])(-2.5)(pr)

pr1 = R([2,3])(PI)(pr_ok)



superior_prof = S([1])([0.93])(STRUCT([pr_ok,pr1]))

#

p27 = [[0,0,0],[0,0,-2.2]]
c27 = BEZIER(S1)(p27)
l27 = MAP(c27)(Dom1D)

p28 = [[0,0,-2.2],[0,1,-2.5]]
c28 = BEZIER(S1)(p28)
l28 = MAP(c28)(Dom1D)

p29 = [[0,1,-2.5],[0,1.8,-2.5]]
c29 = BEZIER(S1)(p29)
l29 = MAP(c29)(Dom1D)

p30 = [[0,1.8,-2.5],[0,1.8,-2.2],[0,2,-2.2],[0,2,-2]]
c30 = BEZIER(S1)(p30)
l30 = MAP(c30)(Dom1D)

p31 = [[0,2,-2],[0,3.3,-1.7]]
c31 = BEZIER(S1)(p31)
l31 = MAP(c31)(Dom1D)

p32 = [[0,3.3,-1.7],[0,3.3,0]]
c32 = BEZIER(S1)(p32)
l32 = MAP(c32)(Dom1D)

pr_s = STRUCT([l27,l28,l29,l30,l31,l32])

pr_sez = T([2])(-1.65)(pr_s)

pr_sez2 = R([1,3])(PI)(pr_sez)

sez_prof =STRUCT([pr_sez,pr_sez2])

profiles = STRUCT([lateral_prof,superior_prof,sez_prof])

VIEW(profiles)

