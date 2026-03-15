import math
from itertools import product

def check_conditions(a, b, c, d, e, S):
    # The 8 conditions from the image
    # Format: (variable1, variable2, variable3) where 0 represents 'a' itself
    conditions = [
        (e, b, d), # (a±e)² + (a±b)² + (a±d)² = S
        (c, 0, c), # (a±c)² + (a)² + (a±c)² = S
        (d, b, e), # (a±d)² + (a±b)² + (a±e)² = S
        (e, c, d), # (a±e)² + (a±c)² + (a±d)² = S
        (b, 0, b), # (a±b)² + (a)² + (a±b)² = S
        (d, c, e), # (a±d)² + (a±c)² + (a±e)² = S
        (e, 0, e), # (a±e)² + (a)² + (a±e)² = S
        (d, 0, d)  # (a±d)² + (a)² + (a±d)² = S
    ]
    
    for cond in conditions:
        found_valid_sign_combo = False
        # Test all combinations of + and - for the variables in the condition
        for signs in product([1, -1], repeat=3):
            term1 = (a + signs[0] * cond[0])**2
            term2 = a**2 if cond[1] == 0 else (a + signs[1] * cond[1])**2
            term3 = (a + signs[2] * cond[2])**2
            
            if term1 + term2 + term3 == S:
                found_valid_sign_combo = True
                break
        
        if not found_valid_sign_combo:
            return False
    return True

def find_magic_sets(S_target, num_sets=3):
    used_numbers = set()
    results = []
    
    # Range of 'a' should be small enough so (a-x) doesn't always go negative 
    # but large enough to find squares.
    for a in range(1, 500):
        if a in used_numbers: continue
        
        # Optimization: From image conditions like (a±e)² + a² + (a±e)² = S
        # We know 2(a±e)² = S - a²
        # This gives us a very specific range for valid 'a'
        if S_target - a**2 <= 0 or (S_target - a**2) % 2 != 0:
            continue
            
        # Try to find b, c, d, e that satisfy the most restrictive conditions first
        # e.g., 2(a±e)² + a² = S  => (a±e) = sqrt((S-a²)/2)
        val_sq = (S_target - a**2) // 2
        val = math.isqrt(val_sq)
        if val**2 != val_sq: continue
        
        # Potential values for e, b, c, d are those where (a ± x) = val
        # So x = |val - a| or x = | -val - a |
        possible_x = {abs(val - a), abs(-val - a)}
        possible_x.discard(0) # Natural numbers only
        
        for e in possible_x:
            if e in used_numbers or e == a: continue
            for b in possible_x: # Similar constraints apply to b, c, d
                if b in used_numbers or b == a or b == e: continue
                for c in possible_x:
                    if c in used_numbers or c == a or c == e or c == b: continue
                    for d in possible_x:
                        if d in used_numbers or d == a or d == e or d == b or d == c: continue
                        
                        if check_conditions(a, b, c, d, e, S_target):
                            current_set = [a, b, c, d, e]
                            results.append({"a":a, "b":b, "c":c, "d":d, "e":e})
                            used_numbers.update(current_set)
                            if len(results) >= num_sets: return results
    return results

# Example run
S_VALUE = 442 # Example S that works well with squares
final_sets = find_magic_sets(S_VALUE, 10)

print(f"{'Set':<5} | {'a':<3} | {'b':<3} | {'c':<3} | {'d':<3} | {'e':<3} | {'S':<3}")
print("-" * 40)
for i, s in enumerate(final_sets, 1):
    print(f"{i:<5} | {s['a']:<3} | {s['b']:<3} | {s['c']:<3} | {s['d']:<3} | {s['e']:<3} | {S_VALUE}")