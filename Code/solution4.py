import math

def find_complex_magic_sets(num_sets=5):
    used_numbers = set()
    results = []
    
    # We search for k and a that allow for two distinct offsets x1 and x2
    for k in range(5, 100):
        for a in range(1, 50):
            if a in used_numbers: continue
            
            S = 2 * (k**2) + a**2
            
            # The two values that satisfy (a ± x)^2 = k^2
            x1 = abs(k - a)
            x2 = k + a
            
            # Filter out zeros and numbers already used
            candidates = [x for x in [x1, x2] if x > 0 and x != a and x not in used_numbers]
            
            # To have variety, we need both x1 and x2 to be available
            if len(candidates) >= 2:
                b, c = candidates[0], candidates[1]
                # We can assign d and e from these same candidates to satisfy the symmetry
                # while keeping the set's 'a, b, c' unique
                res = {
                    "a": a, "b": b, "c": c, "d": b, "e": c, 
                    "S": S, "k": k,
                    "nums": {a, b, c}
                }
                
                results.append(res)
                used_numbers.update(res["nums"])
                
            if len(results) >= num_sets:
                return results
    return results

# Generate and Print
magic_sets = find_complex_magic_sets(15)

print(f"{'Set':<5} | {'a':<3} | {'b':<3} | {'c':<3} | {'d':<3} | {'e':<3} | {'S':<6} | {'k':<3}")
print("-" * 55)
for i, r in enumerate(magic_sets, 1):
    print(f"{i:<5} | {r['a']:<3} | {r['b']:<3} | {r['c']:<3} | {r['d']:<3} | {r['e']:<3} | {r['S']:<6} | {r['k']:<3}")