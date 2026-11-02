import numpy as np
def polytic(ps, pw:int, show = False):
    size = len(ps)
    alphabet = 'abcdefghigklmnopqrstuvwxyz'
    d= dict()
    for i in range(pw+1):
        for j in range(i, pw+1):
            d.update({alphabet[i]+alphabet[j]: 0})
        d.update({alphabet[i]: 0})

    addends = []
    for i in range(size):
        addends.append([])
        for j in range(pw, 0, -1):
            addends[i].append(ps[i][0]**j)
        addends[i].append(1)
        addends[i].append(ps[i][1])
    for k in range(size):
        for i in range(pw+1):
            for j in range(i, pw+2):
                if i==j and i!=pw+1:
                    d[alphabet[i]*2] += addends[k][i]**2
                elif i != j and (i != pw+1 and j != pw+1):
                    d[alphabet[i]+alphabet[j]] += 2*addends[k][i]*addends[k][j]
                else:
                    d[alphabet[i]] += 2*addends[k][i]*addends[k][j]
    a = [[] for i in range(pw+1)]
    b = [[] for i in range(pw+1)]
    for i in range(pw+1):
        for key in d:
            if alphabet[i] in key:
                if key == alphabet[i]*2:
                    a[i].append(alphabet[i] + str(d[key]*2))
                elif len(key) == 2:
                    a[i].append(key.replace(alphabet[i], '') + str(d[key]))
                else:
                    b[i].append(d[key])

    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = float(a[i][j][1:])
    a = np.array(a)
    b = np.array(b)
    c = np.linalg.pinv(a) @ b
    ans = [float(i[0]) for i in c]

    if show:
        s = ''
        for i in range(len(ans)):
            s += '(' + str(f"{ans[i]:.16f}") +')x^' + str(pw) +' + '
            pw-=1
        print(s[:-3])

    return ans