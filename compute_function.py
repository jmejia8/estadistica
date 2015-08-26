import numpy as np
from downhill import downhill
from gmpy2 import log, exp
from random import random

if __name__ == '__main__':
    x_data = []
    y_data = []

    with open('filtered.data', 'r') as datafile:
        for line in datafile:
            y, x = line.strip().split(' ')

            y_data.append(bool(y))
            x_data.append(np.array([1] + list(map(float, x.split(',')))))

    def makeloglike(x_data, y_data):
        def loglike(ß):
            def term(x, y):
                dot = ß.dot(x)
                if y:
                    return dot - log(1 + exp(dot))
                else:
                    return -log(1 + exp(dot))
            return sum(
                map(term, x_data, y_data)
            )

        return loglike

    loglike = makeloglike(x_data, y_data)

    ß = [
        -0.1304872044,
        0.0044359242,
        -0.0073997135,
        0.0049064469,
        0.0136753262,
        0.0053199764,
        0.0030747525,
        0.0058595307,
        0.0065312279,
        0.0027749817,
        0.0119486008,
        0.0084906961,
        -0.0071369348,
        0.0111621659,
        0.0107097929,
        0.0095900680,
        0.0100376958,
        0.0078948492,
        0.0101152806,
        -0.1137999010,
        0.0025213808,
        -0.0248121621,
        0.0102444762,
        0.0130512402,
        0.0225180184,
        0.0027041271,
        0.0038154447,
        -0.0019889984,
        0.0040718530,
        -0.0043652449,
        0.0035052964,
        0.0115125718,
        0.0108878716,
        0.0059364008,
        0.0106850746,
        0.0096340528,
        0.0019104727,
        0.0073117573,
        0.0067469463,
        0.0048177387,
        0.0114278735,
        0.0085407650,
        0.0029670354,
        0.0084244794,
        0.0080599022,
        0.0006081326,
        0.0059236393,
        0.0079667724,
        0.0081770204,
        0.0078493733,
        0.0052903681,
        0.0081219285,
        0.0150988575,
        0.0164040146,
        0.0023174244,
        -0.0032760498,
        -0.0011112326,
        -0.0002531620,
        0.0090297403,
    ]

    print(loglike(np.array(ß)))
    print(loglike(np.array([0]*59)))

    # print(downhill(
    #     loglike,
    #     np.array([random()*10]*59),
    # ))
