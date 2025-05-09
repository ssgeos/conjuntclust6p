from scipy.stats import binom

# Parameters
n = 6  # Number of trials
k = 6  # Number of successes
p = 0.306245  # Probability of success

# Compute the p-value for P(X >= 6), which is just P(X = 6)
p_value = binom.pmf(6, n, p)
print(f"P-value: {p_value}")
