from sympy import *

# # some sympy tutorial
# x = Symbol('x')
# y = diff(sin(x)**2)
# print(x,', ', y)


# u, v = symbols('u v')
# f_uv = u**2 *v
# df_du = diff(f_uv, u)
# df_dv = diff(f_uv, v)
# print(df_du, '\n', df_dv)

# z = sin(2*x)
# a = simplify(y)
# print(y)
# print(a)
# print(z==a)


def flip_metric(metric_lower):
    # returns the inverse of the given metric
    # i.e. if input is lower metric, then returns the upper metric
    return metric_lower ** (-1)


def connection(metric_lower, metric_symbols, t, m, n):
    # returns Gamma^t_mn from a given metric
    accum = 0
    temp = 0

    metric_upper = flip_metric(metric_lower)
    dim = sqrt(len(metric_upper))

    # metric is symmetric, so only need to loop through the first row
    for s in range(0, dim, 1):
        this_g_up = metric_upper[t * dim + s]
        temp += diff(metric_lower[s * dim + n], metric_symbols[m])
        temp += diff(metric_lower[s * dim + m], metric_symbols[n])
        temp -= diff(metric_lower[m * dim + n], metric_symbols[s])
        accum += this_g_up * temp
        temp = 0
    return accum / 2


if __name__ == "__main__":
    t, x, y, r, theta, phi, G, M = symbols("t x y r theta phi G M")
    init_printing(use_unicode=True)
    # define the metric
    # note: sympy store matrices in row major order

    # sample metric: Eulidean R2, Cartesian metric
    g_cart2_symbols = [x, y]
    g_cart2_lower = Matrix([[1, 0], [0, 1]])

    # sample metric: Eulidean R2, polar metric
    g_pol2_symbols = [r, theta]
    g_pol2_lower = Matrix([[1, 0], [0, r**2]])

    # sample metric: Euclidean R3, spherical metric
    g_sph3_symbols = [r, theta, phi]
    g_sph3_lower = Matrix([[1, 0, 0], [0, r**2, 0], [0, 0, (r**2) * sin(theta) ** 2]])

    # sample metric: Schwarzschild
    g_sch_symbols = [t, r, theta, phi]
    g_sch_lower = Matrix(
        [
            [-(1 - 2 * G * M / r), 0, 0, 0],
            [0, 1 / (1 - 2 * G * M / r), 0, 0],
            [0, 0, r**2, 0],
            [0, 0, 0, (r**2) * sin(theta) ** 2],
        ]
    )

    # choose a metric and compute
    metric_lower = g_sph3_lower
    metric_symbols = g_sph3_symbols
    dim = len(metric_symbols)
    print("Connections Gamma^t_mn: \n")
    for t in range(0, dim, 1):
        for m in range(0, dim, 1):
            for n in range(0, dim, 1):
                print(
                    f"Gamma^{str(metric_symbols[t])}_({str(metric_symbols[m])}, {str(metric_symbols[n])}) = ",
                    simplify(connection(metric_lower, metric_symbols, t, m, n)),
                )


# output for Schwarzschild connections:
# Gamma^t_(t, t) =  0
# Gamma^t_(t, r) =  G*M/(r*(-2*G*M + r))
# Gamma^t_(t, theta) =  0
# Gamma^t_(t, phi) =  0
# Gamma^t_(r, t) =  G*M/(r*(-2*G*M + r))
# Gamma^t_(r, r) =  0
# Gamma^t_(r, theta) =  0
# Gamma^t_(r, phi) =  0
# Gamma^t_(theta, t) =  0
# Gamma^t_(theta, r) =  0
# Gamma^t_(theta, theta) =  0
# Gamma^t_(theta, phi) =  0
# Gamma^t_(phi, t) =  0
# Gamma^t_(phi, r) =  0
# Gamma^t_(phi, theta) =  0
# Gamma^t_(phi, phi) =  0
# Gamma^r_(t, t) =  G*M*(-2*G*M + r)/r**3
# Gamma^r_(t, r) =  0
# Gamma^r_(t, theta) =  0
# Gamma^r_(t, phi) =  0
# Gamma^r_(r, t) =  0
# Gamma^r_(r, r) =  G*M/(r*(2*G*M - r))
# Gamma^r_(r, theta) =  0
# Gamma^r_(r, phi) =  0
# Gamma^r_(theta, t) =  0
# Gamma^r_(theta, r) =  0
# Gamma^r_(theta, theta) =  2*G*M - r
# Gamma^r_(theta, phi) =  0
# Gamma^r_(phi, t) =  0
# Gamma^r_(phi, r) =  0
# Gamma^r_(phi, theta) =  0
# Gamma^r_(phi, phi) =  (2*G*M - r)*sin(theta)**2
# Gamma^theta_(t, t) =  0
# Gamma^theta_(t, r) =  0
# Gamma^theta_(t, theta) =  0
# Gamma^theta_(t, phi) =  0
# Gamma^theta_(r, t) =  0
# Gamma^theta_(r, r) =  0
# Gamma^theta_(r, theta) =  1/r
# Gamma^theta_(r, phi) =  0
# Gamma^theta_(theta, t) =  0
# Gamma^theta_(theta, r) =  1/r
# Gamma^theta_(theta, theta) =  0
# Gamma^theta_(theta, phi) =  0
# Gamma^theta_(phi, t) =  0
# Gamma^theta_(phi, r) =  0
# Gamma^theta_(phi, theta) =  0
# Gamma^theta_(phi, phi) =  -sin(2*theta)/2
# Gamma^phi_(t, t) =  0
# Gamma^phi_(t, r) =  0
# Gamma^phi_(t, theta) =  0
# Gamma^phi_(t, phi) =  0
# Gamma^phi_(r, t) =  0
# Gamma^phi_(r, r) =  0
# Gamma^phi_(r, theta) =  0
# Gamma^phi_(r, phi) =  1/r
# Gamma^phi_(theta, t) =  0
# Gamma^phi_(theta, r) =  0
# Gamma^phi_(theta, theta) =  0
# Gamma^phi_(theta, phi) =  1/tan(theta)
# Gamma^phi_(phi, t) =  0
# Gamma^phi_(phi, r) =  1/r
# Gamma^phi_(phi, theta) =  1/tan(theta)
# Gamma^phi_(phi, phi) =  0
