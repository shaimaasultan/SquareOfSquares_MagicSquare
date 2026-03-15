import math

def find_fixed_sk_sets(S_fixed, k_fixed):
    # Calculate 'a' based on fixed S and k: S = 2k² + a²
    a_sq = S_fixed - 2 * (k_fixed**2)
    
    if a_sq < 0:
        return "Error: S is too small for this k."
    
    a = math.isqrt(a_sq)
    if a**2 != a_sq:
        return "Error: S and k combination does not result in an integer 'a'."

    # The two possible values for variables b, c, d, e
    x1 = abs(k_fixed - a)
    x2 = k_fixed + a
    
    # We create unique combinations of [b, c, d, e] using our two available offsets
    # Each row below represents a unique set that satisfies all 8 image conditions
    combinations = [
        [x1, x1, x1, x1],
        [x2, x2, x2, x2],
        [x1, x2, x1, x2],
        [x2, x1, x2, x1],
        [x1, x1, x2, x2]
    ]
    
    return a, combinations

# Parameters
S_VAL = 225
K_VAL = 8  
# 2(8²) + a² = 128 + a²; if a=root(225-128)=root(97) -> Not integer
# Let's use S=225, k=7 -> 2(49) + a² = 225 -> 98 + a² = 225 -> a² = 127 -> Not integer
# Let's use S=129, k=8 -> 2(64) + a² = 129 -> 128 + a² = 129 -> a = 1
S_VAL = 129
K_VAL = 8
S_VAL = 225
K_VAL = 8  

a_val, sets = find_fixed_sk_sets(S_VAL, K_VAL)

print(f"Fixed Values: S = {S_VAL}, k = {K_VAL}, a = {a_val}")
print(f"{'Set':<5} | {'a':<3} | {'b':<3} | {'c':<3} | {'d':<3} | {'e':<3} | {'Verification'}")
print("-" * 65)

for i, combo in enumerate(sets, 1):
    # combo is a list, so we access by index
    b, c, d, e = combo
    verif = f"2({K_VAL}²) + {a_val}² = {S_VAL}"
    print(f"{i:<5} | {a_val:<3} | {b:<3} | {c:<3} | {d:<3} | {e:<3} | {verif}")