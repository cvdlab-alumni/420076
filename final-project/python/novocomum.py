from pyplasm import *

def NOVOCOMUM (r,h):
	shelf_1 = COLOR([0.396,0.267,0.129])(CYLINDER([r/1.216216,h/35.88])(60))
	shelf_2 = T([1])([r/(6.428571*2)])(COLOR([0.396,0.267,0.129])(CYLINDER([r/1.096761,h/35.88])(60)))
	shelf_3 = T([1])([r/(3.214285*2)])(COLOR([0.396,0.267,0.129])(CYLINDER([r,h/35.88])(60)))
	panel_1 = COLOR([0.396,0.267,0.129])(CUBOID([r/1.216216,h,h/35.88]))
	panel_2 = COLOR([0.396,0.267,0.129])(CUBOID([h/35.88,h,r/(1.216216/2)]))
	panel_3 = COLOR([0.396,0.267,0.129])(CUBOID([r/1.216216,h/4.357142,h/35.88]))
	panel_1_t = T([1])([-r/1.216216])(panel_1)
	panel_2_t = T([3])([-r/1.216216])(panel_2)
	panels = STRUCT([panel_1_t,panel_2_t,panel_3])
	panels_r = R([2,3])(PI/2)(panels)
	shelfs = STRUCT([T([3])([h])(shelf_1),T([3])([h/1.525])(shelf_2),T([3])([h/4.357])(shelf_3)])
	return STRUCT([shelfs,panels_r])


novocomum = S([1,2,3])([8,8,8])(NOVOCOMUM(0.45,0.61))
VIEW(novocomum)