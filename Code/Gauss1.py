import math

C = 12209
target = 2 * C * C

r_values = set()

# search range: u^2 <= 2C^2  → |u| <= floor(sqrt(2)*C)
limit = int(math.isqrt(target))

for u in range(-limit, limit + 1):
    v2 = target - u*u
    if v2 < 0:
        continue
    v = int(math.isqrt(v2))
    if v*v == v2:
        # (u,v) is a valid representation
        r = u*u - C*C
        if r != 0:
            r_values.add(r)

# sort for readability
r_values = sorted(r_values)

print("Number of r-values:", len(r_values))
print("r-values:")
for r in r_values:
    print(r)



# r_values should already be a Python set of all r-values you generated
# Example: r_values = { ... }

pairs = []

# Convert to list for iteration
r_list = list(r_values)

# Search for all pairs (r_a, r_d) whose sum is also in the set
for i in range(len(r_list)):
    for j in range(i+1, len(r_list)):
        r_a = r_list[i]
        r_d = r_list[j]
        s = r_a + r_d
        if s in r_values:
            pairs.append((r_a, r_d, s))

# Display results
print("Number of valid (r_a, r_d, r_a+r_d) triples:", len(pairs))
for r_a, r_d, s in pairs:
    print(f"r_a = {r_a:>12},  r_d = {r_d:>12},  r_a + r_d = {s:>12}")
