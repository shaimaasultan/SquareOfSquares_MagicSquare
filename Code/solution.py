import math

def find_unique_sets(S_target, num_sets_needed=5):
    used_numbers = set()
    found_sets = []
    
    # Iterate through possible values of 'a'
    # We start from 2 to avoid trivial cases and ensure S+3a^2 is even
    for a in range(2, 500):
        if a in used_numbers:
            continue
            
        # Rearranged: 2(b^2 + c^2 + d^2 + e^2) = S + 3a^2
        rhs = S_target + 3 * (a**2)
        if rhs % 2 != 0:
            continue
            
        target_sum_sq = rhs // 2
        limit = int(math.sqrt(target_sum_sq)) + 1
        found_current = False
        
        # Search for unique b, c, d, e
        for b in range(1, limit):
            if b in used_numbers or b == a: continue
            for c in range(b + 1, limit):
                if c in used_numbers or c == a: continue
                for d in range(c + 1, limit):
                    if d in used_numbers or d == a: continue
                    
                    e_sq = target_sum_sq - (b**2 + c**2 + d**2)
                    if e_sq <= 0: continue
                    
                    e = math.isqrt(e_sq)
                    # Check if e is a perfect square, unique, and positive
                    if e**2 == e_sq and e > d and e not in used_numbers and e != a:
                        current_set = [a, b, c, d, e]
                        found_sets.append({
                            "a": a, "b": b, "c": c, "d": d, "e": e,
                            "calc": f"2({b}²+{c}²+{d}²+{e}²)-3({a}²)"
                        })
                        used_numbers.update(current_set)
                        found_current = True
                        break
                if found_current: break
            if found_current: break
            
        if len(found_sets) >= num_sets_needed:
            break
            
    return found_sets

# Parameters
S_VAL = 442
sets = find_unique_sets(S_VAL, 100)

# Table Output
print(f"{'Set':<5} | {'a':<3} | {'b':<3} | {'c':<3} | {'d':<3} | {'e':<3} | {'Verification':<25} | {'S':<3}")
print("-" * 75)
for i, s in enumerate(sets, 1):
    print(f"{i:<5} | {s['a']:<3} | {s['b']:<3} | {s['c']:<3} | {s['d']:<3} | {s['e']:<3} | {s['calc']:<25} | {S_VAL}")