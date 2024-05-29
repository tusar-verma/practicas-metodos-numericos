import math

omegas = [0.8, 0.9, 1.0, 1.1, 1.2, 1.3]

for w in omegas:
    a = 1
    b = -math.pow(w*0.5, 2) + 2*(1-w)
    c = math.pow(1-w, 2)

    # solo hay una solución real
    if (math.pow(b,2) - 4*a*c < 0):
        lambda1 = -b/2
        print("omega: ", w, "Unico lambda: ", lambda1)
    else:
        gradient = math.sqrt(math.pow(b,2) - 4*a*c)
        lambda1 = (-b + gradient) / 2
        lambda2 = (-b - gradient) / 2
        print("omega: ", w, "Lambda1: ", lambda1, " lambda2: ", lambda2)