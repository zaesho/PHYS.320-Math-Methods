import sympy as sp


LA, RH, TD, RC, TR, ML, KN, PB, JE, UR, LW, CM, NG = sp.symbols('LA RH TD RC TR ML KN PB JE UR LW CM NG', real=True)
WI, NN, CO, EM, AY, SY, KY, CH, TH, HI, RY, KA, HR = sp.symbols('WI NN CO EM AY SY KY CH TH HI RY KA HR', real=True)

bygones_map = sp.Matrix([
    #LA
    [0 ,0 , CO, EM, AY, SY, KY, CH, TH, 0, 0, KA,0 ],
    #RH
    [0 ,0 , CO, 0, AY, SY, 0, 0, TH, HI, RY, KA, HR ],
    #TD
    [WI ,0 , 0, 0, 0, 0, KY, 0, 0, 0, RY, 0, HR ],
    #RC
    [WI ,0 , 0, EM, 0, SY, KY, CH, 0, 0, 0, 0, HR ],
    #TR
    [0 ,NN , 0, EM, AY, SY, 0, 0, TH, HI, RY, KA, HR ],
    #ML
    [0 ,NN , 0, EM, AY, SY, 0, CH, TH, 0, 0, KA, HR ],
    #KN
    [WI ,NN , CO, EM, AY, SY, 0, 0, 0, HI, 0, KA, 0 ],
    #PB
    [WI ,0 , CO, EM,0 ,0 , KY, CH, TH, 0, 0, KA, HR ],
    #JE
    [0 ,NN , CO, 0, AY, SY, 0, 0, TH, HI, RY, KA, 0 ],
    #UR
    [WI ,0 , CO, EM, AY, SY, KY, 0, TH, HI, 0, KA, HR ],
    #LW
    [0 ,0 , 0, EM, AY, SY, KY, CH, 0, 0, RY, KA, HR ],
    #CM
    [WI ,0 , CO, EM, AY, SY, KY, CH, TH, HI, 0, KA, HR ],
    #NG
    [WI ,NN , 0, EM, AY, SY, KY, CH, TH, HI, 0, KA, 0 ],
])


bygones_identity = sp.Matrix([
[LA ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
[0 ,RH ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
[0 ,0 ,TD, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
[0 ,0 ,0, RC, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
[0 ,0 ,0, 0, TR, 0, 0, 0, 0, 0, 0, 0, 0 ],
[0 ,0 ,0, 0, 0, ML, 0, 0, 0, 0, 0, 0, 0 ],
[0 ,0 ,0, 0, 0, 0, KN, 0, 0, 0, 0, 0, 0 ],
[0 ,0 ,0, 0, 0, 0, 0, PB, 0, 0, 0, 0, 0 ],
[0 ,0 ,0, 0, 0, 0, 0, 0, JE, 0, 0, 0, 0 ],
[0 ,0 ,0, 0, 0, 0, 0, 0, 0, UR, 0, 0, 0 ],
[0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, LW, 0, 0 ],
[0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, CM, 0 ],
[0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, NG ],


])

aug = bygones_map.row_join(bygones_identity)
sp.pprint(aug.rref())


soln = bygones_map.solve(bygones_map)

sp.pprint(soln)
