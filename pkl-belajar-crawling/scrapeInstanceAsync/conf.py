import string

MOTOR = list(range(3000, 7000))
MOBIL = list(range(1,3000))
BIS = list(range(7000,8000))
PENUMPANG = list(range(8000,9000))
BEBAN = list(range(9000,10000))
PLAT_AWAL = ['B']
PLAT_KE_1 = ['U','B','P','S','T','Z','E','N','C','V','K','F','W']
PLAT_KE_2 = ['A','W','E','R','Z','F','K','O','I','Y','V','P','M','G','J','L','T']
PLAT_KE_2_SPECIAL = ['HX','IX','QN']
PLAT_KE_2_PENUMPANG = ['UA','TX','UX']
PLAT_KE_2_BEBAN = ['B','U','Z','C','D']
PLAT_KE_2_BUS = ['F','K','O','Z','R','Y','I','B','V','P','M','G','Y','W','U']
PLAT_KE_3 = list(string.ascii_uppercase)
SetPLAT_KE_1 = {'U','B','P','S','T','Z','E','N','C','V','K','F','W'}
SetPLAT_KE_2 = {'A','W','E','R','Z','F','K','O','I','Y','V','P','M','G','J','L','T','HX','IX','QN','UA','TX','UX','B','U','Z','C','D','F','K','O','Z','R','Y','I','B','V','P','M','G','Y','W','U'}

base_link = 'https://samsat-pkb.jakarta.go.id/INFO_KBM'
headers_get = {'Host':'samsat-pkb.jakarta.go.id','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
headers_post = {'Host':'samsat-pkb.jakarta.go.id','Content-Lenght': '45','Origin':'https://samsat-pkb.jakarta.go.id','Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

storedData = []
total = 0