import math

C = 6409   # your fixed C

def square_from_r(r):
    """Return x such that x^2 = C^2 + r, or None if not a perfect square."""
    val = C*C + r
    if val < 0:
        return None
    x = int(math.isqrt(val))
    if x*x == val:
        return x
    return None

def build_variables(r_a, r_d, r_h):
    """
    Given r_a, r_d, r_h (with r_a+r_d also in the r-set),
    construct all nine variables a,b,c,d,e,f,g,h,i.
    Returns a dictionary or None if any square fails.
    """

    # Derived r-values
    r_b = -r_a
    r_e = -r_d
    r_f = -(r_a + r_d)
    r_g =  (r_a + r_d)
    r_i = -r_h
    r_c = 0   # because c^2 = C^2

    # Compute all variables
    a = square_from_r(r_a)
    b = square_from_r(r_b)
    c = C
    d = square_from_r(r_d)
    e = square_from_r(r_e)
    f = square_from_r(r_f)
    g = square_from_r(r_g)
    h = square_from_r(r_h)
    i = square_from_r(r_i)

    # If any failed, return None
    if None in (a,b,d,e,f,g,h,i):
        return None

    return {
        "a": a, "b": b, "c": c,
        "d": d, "e": e,
        "f": f, "g": g,
        "h": h, "i": i,
        "r-values": {
            "r_a": r_a, "r_b": r_b,
            "r_d": r_d, "r_e": r_e,
            "r_f": r_f, "r_g": r_g,
            "r_h": r_h, "r_i": r_i
        }
    }

result = build_variables(r_a, r_d, r_h)

if result:
    print(result)
else:
    print("This triple does not produce valid squares.")
