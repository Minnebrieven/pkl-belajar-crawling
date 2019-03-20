import conf

def generatePlat():
    for a in conf.PLAT_KE_1:
        for b in conf.PLAT_KE_2:
            for c in conf.PLAT_KE_3:
                l = []
                l.append(a+b+c)
                e = ''.join(l)
                
                yield e