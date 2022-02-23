import sys

with open(sys.argv[1],"r",encoding= "utf-8") as file:              # satir ['WPPWWW', 'WWPWPS', 'WWPWPW', 'PPPPPW', 'FWPWWW', 'WPPPPW']
    tüm = list()                                                       # [[w,p,p,w,w,w]......]
    satir = list()
    hepsi = list()
    for line in file:
        line = line.rstrip("''")
        arguman = line.split('\n')
        satir.append(arguman[0])
        uzun = len(arguman[0])
        for i in arguman[0]:
            hepsi.append(i)

    i = 0
    while i < len(satir):
        tek = list()
        for k in satir[i]:
            tek.append(k)
            tek = [w.replace('W', '0') for w in tek]
        tüm.append(tek)
        i += 1



sindex = hepsi.index('S')                                                                                                #hepsi'de S hangi indexte  11
htek = sindex//uzun                                                                                                      #hangi tekin içinde  1
ictek = sindex % uzun                                                                                                    #tekin içinde nerde   S'nin lokasyonu 1-5



pyer = list()
def degistirici(htek,ictek):

    if 1 <= htek <= (uzun-2) and 1 <= ictek <= (uzun-2):    #her tarafı kontrol
        if tüm[htek][ictek+1] == 'P' or tüm[htek][ictek+1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek+1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek+1)
        elif tüm[htek][ictek-1] == 'P' or tüm[htek][ictek-1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek-1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek-1)
        elif tüm[htek+1][ictek] == 'P' or tüm[htek+1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek+1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek+1,ictek)
        elif tüm[htek-1][ictek] == 'P' or tüm[htek-1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek-1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek-1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif htek == 0 and ictek == 0:            # 0,0 sağ ve aşağı kontrol
        if tüm[htek][ictek+1] == 'P' or tüm[htek][ictek+1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek+1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek+1)
        elif tüm[htek-1][ictek] == 'P' or tüm[htek-1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            pyer.append(yer)
            if tüm[htek-1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek-1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif htek == 0 and ictek == (uzun-1):           # 0,5 sol ve aşağı kontrol
        if tüm[htek][ictek-1] == 'P' or tüm[htek][ictek-1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek-1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek-1)
        elif tüm[htek-1][ictek] == 'P' or tüm[htek-1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek-1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek-1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif htek == (uzun-1) and ictek == 0:            # 5,0 sağ ve yukarı kontrol
        if tüm[htek][ictek+1] == 'P' or tüm[htek][ictek+1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek+1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek+1)
        elif tüm[htek+1][ictek] == 'P' or tüm[htek+1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek+1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek+1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif htek == (uzun-1) and ictek == (uzun-1):            # 5,5 sol ve yukarı kontrol
        if tüm[htek][ictek-1] == 'P' or tüm[htek][ictek-1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek-1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek-1)
        elif tüm[htek+1][ictek] == 'P' or tüm[htek+1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek+1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek+1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif 1 <= htek <= (uzun-2) and ictek == 0:              # sol kenar sağ yukarı aşağı kontrol
        if tüm[htek][ictek+1] == 'P' or tüm[htek][ictek+1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek+1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek+1)
        elif tüm[htek+1][ictek] == 'P' or tüm[htek+1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek+1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek+1,ictek)
        elif tüm[htek-1][ictek] == 'P' or tüm[htek-1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek-1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek-1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif 1 <= htek <= (uzun-2) and ictek == (uzun-1):       # sağ kenar   sol yukarı aşağı kontrol
        if tüm[htek][ictek-1] == 'P' or tüm[htek][ictek-1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek-1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek-1)
        elif tüm[htek+1][ictek] == 'P' or tüm[htek+1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek+1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek+1,ictek)
        elif tüm[htek-1][ictek] == 'P' or tüm[htek-1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek-1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek-1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif htek == 0 and 1 <= ictek <= (uzun-2):              # üst kenar  sağ sol aşağı kontrol
        if tüm[htek][ictek+1] == 'P' or tüm[htek][ictek+1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek+1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek+1)
        elif tüm[htek][ictek-1] == 'P' or tüm[htek][ictek-1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek-1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek-1)
        elif tüm[htek-1][ictek] == 'P' or tüm[htek-1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek-1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek-11,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek, ictek)
    elif htek == (uzun-1) and 1 <= ictek <= (uzun-2):       # alt kenar  sağ sol yukarı kontrol
        if tüm[htek][ictek+1] == 'P' or tüm[htek][ictek+1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek+1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek+1)
        elif tüm[htek][ictek-1] == 'P' or tüm[htek][ictek-1] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek][ictek-1] == 'F':
                return tüm
            else:
                degistirici(htek,ictek-1)
        elif tüm[htek+1][ictek] == 'P' or tüm[htek+1][ictek] == 'F':
            tüm[htek][ictek] = '1'
            yer = str(htek) + str(ictek)
            pyer.append(yer)
            if tüm[htek+1][ictek] == 'F':
                return tüm
            else:
                degistirici(htek+1,ictek)
        else:
            tüm[htek][ictek] = '0'
            htek = int(pyer[-1][0])
            ictek = int(pyer[-1][1])
            degistirici(htek,ictek)



degistirici(htek,ictek)
for i in range(len(tüm)):
    tüm[i]=[w.replace('P','0') for w in tüm[i]]

file2 = open(sys.argv[4], "w", encoding="utf-8")
for i in tüm:
    file2.write(' '.join(i))
    file2.write('\n')

print(tüm)
with open(sys.argv[2],"r",encoding= "utf-8") as file:              # satir ['WPPWWW', 'WWPWPS', 'WWPWPW', 'PPPPPW', 'FWPWWW', 'WPPPPW']
    tüm = list()                                                       # [[w,p,p,w,w,w]......]
    satir = list()
    hepsi = list()
    for line in file:
        line = line.rstrip("''")
        arguman = line.split('\n')
        satir.append(arguman[0])
        uzun = len(arguman[0])
        for i in arguman[0]:
            hepsi.append(i)

    i = 0
    while i < len(satir):
        tek = list()
        for k in satir[i]:
            tek.append(k)
            tek=[w.replace('W','0') for w in tek]
        tüm.append(tek)
        i += 1



sindex = hepsi.index('S')                                                                                                #hepsi'de S hangi indexte  11
htek = sindex//uzun                                                                                                      #hangi tekin içinde  1
ictek = sindex % uzun                                                                                                    #tekin içinde nerde   S'nin lokasyonu 1-5


pyer = list()

health =int(sys.argv[3])

def h_degistirici(htek,ictek,health):

    if 1 <= htek <= (uzun-2) and 1 <= ictek <= (uzun-2):                            #her tarafı kontrol
      if health != 0:
          if tüm[htek][ictek + 1] == 'P' or tüm[htek][ictek + 1] == 'F' or tüm[htek][ictek +1] == 'H':
              tüm[htek][ictek] = '1'
              yer = str(htek) + str(ictek)
              pyer.append(yer)
              if tüm[htek][ictek + 1] == 'F':
                  return tüm
              elif tüm[htek][ictek +1] == 'H':
                  health = int(sys.argv[3])
                  h_degistirici(htek,ictek+1,health-1)
              else:
                  h_degistirici(htek, ictek + 1,health-1)
          elif tüm[htek][ictek - 1] == 'P' or tüm[htek][ictek - 1] == 'F' or tüm[htek][ictek -1] == 'H':
              tüm[htek][ictek] = '1'
              yer = str(htek) + str(ictek)
              pyer.append(yer)
              if tüm[htek][ictek - 1] == 'F':
                  return tüm
              elif tüm[htek][ictek -1] == 'H':
                  health = int(sys.argv[3])
                  h_degistirici(htek,ictek-1,health-1)
              else:
                  h_degistirici(htek, ictek - 1,health-1)
          elif tüm[htek + 1][ictek] == 'P' or tüm[htek + 1][ictek] == 'F' or tüm[htek+1][ictek] == 'H':
              tüm[htek][ictek] = '1'
              yer = str(htek) + str(ictek)
              pyer.append(yer)
              if tüm[htek + 1][ictek] == 'F':
                  return tüm
              elif tüm[htek +1][ictek] == 'H':
                  health = int(sys.argv[3])
                  h_degistirici(htek+1,ictek,health-1)
              else:
                  h_degistirici(htek + 1, ictek,health-1)
          elif tüm[htek - 1][ictek] == 'P' or tüm[htek - 1][ictek] == 'F' or tüm[htek-1][ictek] == 'H':
              tüm[htek][ictek] = '1'
              yer = str(htek) + str(ictek)
              pyer.append(yer)
              if tüm[htek - 1][ictek] == 'F':
                  return tüm
              elif tüm[htek-1][ictek] == 'H':
                  health = int(sys.argv[3])
                  h_degistirici(htek-1,ictek,health-1)
              else:
                  h_degistirici(htek - 1, ictek,health-1)
          else:
              tüm[htek][ictek] = '0'
              htek = int(pyer[-1][0])
              ictek = int(pyer[-1][1])
              h_degistirici(htek, ictek,health-1)
      else:
          return 'Health time is over'

    elif htek == 0 and ictek == 0:            # 0,0 sağ ve aşağı kontrol
        if health !=0:
            if tüm[htek][ictek + 1] == 'P' or tüm[htek][ictek + 1] == 'F' or tüm[htek][ictek +1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek + 1] == 'F':
                    return tüm
                elif tüm[htek][ictek + 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek + 1, health - 1)
                else:
                    h_degistirici(htek, ictek + 1,health-1)
            elif tüm[htek - 1][ictek] == 'P' or tüm[htek - 1][ictek] == 'F' or tüm[htek-1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                pyer.append(yer)
                if tüm[htek - 1][ictek] == 'F':
                    return tüm
                elif tüm[htek -1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek-1, ictek , health - 1)
                else:
                    h_degistirici(htek - 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'
    elif htek == 0 and ictek == (uzun-1):           # 0,5 sol ve aşağı kontrol
        if health !=0:
            if tüm[htek][ictek - 1] == 'P' or tüm[htek][ictek - 1] == 'F' or tüm[htek][ictek -1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek - 1] == 'F':
                    return tüm
                elif tüm[htek][ictek -1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek - 1, health - 1)
                else:
                    h_degistirici(htek, ictek - 1,health-1)
            elif tüm[htek - 1][ictek] == 'P' or tüm[htek - 1][ictek] == 'F' or tüm[htek-1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek - 1][ictek] == 'F':
                    return tüm
                elif tüm[htek-1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek-1, ictek, health - 1)
                else:
                    h_degistirici(htek - 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'
    elif htek == (uzun-1) and ictek == 0:            # 5,0 sağ ve yukarı kontrol
        if health !=0:
            if tüm[htek][ictek + 1] == 'P' or tüm[htek][ictek + 1] == 'F' or tüm[htek][ictek +1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek + 1] == 'F':
                    return tüm
                elif tüm[htek][ictek + 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek + 1, health - 1)
                else:
                    h_degistirici(htek, ictek + 1,health-1)
            elif tüm[htek + 1][ictek] == 'P' or tüm[htek + 1][ictek] == 'F' or tüm[htek+1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek + 1][ictek] == 'F':
                    return tüm
                elif tüm[htek+1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek+1, ictek, health - 1)
                else:
                    h_degistirici(htek + 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'
    elif htek == (uzun-1) and ictek == (uzun-1):            # 5,5 sol ve yukarı kontrol
        if health !=0:
            if tüm[htek][ictek - 1] == 'P' or tüm[htek][ictek - 1] == 'F' or tüm[htek][ictek -1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek - 1] == 'F':
                    return tüm
                elif tüm[htek][ictek - 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek - 1, health - 1)
                else:
                    h_degistirici(htek, ictek - 1,health-1)
            elif tüm[htek + 1][ictek] == 'P' or tüm[htek + 1][ictek] == 'F' or tüm[htek+1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek + 1][ictek] == 'F':
                    return tüm
                elif tüm[htek+1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek+1, ictek, health - 1)
                else:
                    h_degistirici(htek + 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'
    elif 1 <= htek <= (uzun-2) and ictek == 0:              # sol kenar sağ yukarı aşağı kontrol
        if health !=0:
            if tüm[htek][ictek + 1] == 'P' or tüm[htek][ictek + 1] == 'F' or tüm[htek][ictek +1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek + 1] == 'F':
                    return tüm
                elif tüm[htek][ictek + 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek + 1, health - 1)
                else:
                    h_degistirici(htek, ictek + 1,health-1)
            elif tüm[htek + 1][ictek] == 'P' or tüm[htek + 1][ictek] == 'F' or tüm[htek+1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek + 1][ictek] == 'F':
                    return tüm
                elif tüm[htek+1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek+1, ictek, health - 1)
                else:
                    h_degistirici(htek + 1, ictek,health-1)
            elif tüm[htek - 1][ictek] == 'P' or tüm[htek - 1][ictek] == 'F' or tüm[htek-1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek - 1][ictek] == 'F':
                    return tüm
                elif tüm[htek-1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek-1, ictek, health - 1)
                else:
                    h_degistirici(htek - 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'
    elif 1 <= htek <= (uzun-2) and ictek == (uzun-1):       # sağ kenar   sol yukarı aşağı kontrol
        if health !=0:
            if tüm[htek][ictek - 1] == 'P' or tüm[htek][ictek - 1] == 'F' or tüm[htek][ictek -1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek - 1] == 'F':
                    return tüm
                elif tüm[htek][ictek -1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek -1, health - 1)
                else:
                    h_degistirici(htek, ictek - 1,health-1)
            elif tüm[htek + 1][ictek] == 'P' or tüm[htek + 1][ictek] == 'F'or tüm[htek+1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek + 1][ictek] == 'F':
                    return tüm
                elif tüm[htek+1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek+1, ictek, health - 1)
                else:
                    h_degistirici(htek + 1, ictek,health-1)
            elif tüm[htek - 1][ictek] == 'P' or tüm[htek - 1][ictek] == 'F' or tüm[htek -1][ictek == 'H']:
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek - 1][ictek] == 'F':
                    return tüm
                elif tüm[htek-1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek-1, ictek, health - 1)
                else:
                    h_degistirici(htek - 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'
    elif htek == 0 and 1 <= ictek <= (uzun-2):              # üst kenar  sağ sol aşağı kontrol
        if health !=0 :
            if tüm[htek][ictek + 1] == 'P' or tüm[htek][ictek + 1] == 'F' or tüm[htek][ictek +1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek + 1] == 'F':
                    return tüm
                elif tüm[htek][ictek + 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek + 1, health - 1)
                else:
                    h_degistirici(htek, ictek + 1,health-1)
            elif tüm[htek][ictek - 1] == 'P' or tüm[htek][ictek - 1] == 'F' or tüm[htek][ictek -1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek - 1] == 'F':
                    return tüm
                elif tüm[htek][ictek - 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek - 1, health - 1)
                else:
                    h_degistirici(htek, ictek - 1,health-1)
            elif tüm[htek - 1][ictek] == 'P' or tüm[htek - 1][ictek] == 'F' or tüm[htek-1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek - 1][ictek] == 'F':
                    return tüm
                elif tüm[htek-1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek-1, health - 1)
                else:
                    h_degistirici(htek - 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'
    elif htek == (uzun-1) and 1 <= ictek <= (uzun-2):       # alt kenar  sağ sol yukarı kontrol
        if health != 0:
            if tüm[htek][ictek + 1] == 'P' or tüm[htek][ictek + 1] == 'F' or tüm[htek][ictek +1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek + 1] == 'F':
                    return tüm
                elif tüm[htek][ictek + 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek + 1, health - 1)
                else:
                    h_degistirici(htek, ictek + 1,health-1)
            elif tüm[htek][ictek - 1] == 'P' or tüm[htek][ictek - 1] == 'F' or tüm[htek][ictek-1] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek][ictek - 1] == 'F':
                    return tüm
                elif tüm[htek][ictek - 1] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek, ictek - 1, health - 1)
                else:
                    h_degistirici(htek, ictek - 1,health-1)
            elif tüm[htek + 1][ictek] == 'P' or tüm[htek + 1][ictek] == 'F' or tüm[htek+1][ictek] == 'H':
                tüm[htek][ictek] = '1'
                yer = str(htek) + str(ictek)
                pyer.append(yer)
                if tüm[htek + 1][ictek] == 'F':
                    return tüm
                elif tüm[htek+1][ictek] == 'H':
                    health = int(sys.argv[3])
                    h_degistirici(htek+1, ictek, health - 1)
                else:
                    h_degistirici(htek + 1, ictek,health-1)
            else:
                tüm[htek][ictek] = '0'
                htek = int(pyer[-1][0])
                ictek = int(pyer[-1][1])
                h_degistirici(htek, ictek,health-1)
        else:
            return 'Health time is over'

h_degistirici(htek,ictek,health)
for i in range(len(tüm)):
    tüm[i]=[w.replace('P','0') for w in tüm[i]]


file2.write('\n')
for i in tüm:
    file2.write(' '.join(i))
    file2.write('\n')
file2.close()


