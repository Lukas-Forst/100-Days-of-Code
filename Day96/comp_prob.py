from CoinProb import compute_event_probability

possible_children = ['Boy', 'Girl']
sample_space = set()
for child1 in possible_children:
    for child2 in possible_children:
                for child3 in possible_children:
                    for child4 in possible_children:
                        outcome = (child1, child2, child3, child4)
                        sample_space.add(outcome)

from itertools import product
all_combinations = product(*(4 * [possible_children]))
assert set(all_combinations) == sample_space

set(product(possible_children, repeat=4))
sample_space_efficient = set(product(possible_children, repeat=4))
assert sample_space == sample_space_efficient

def has_two_boys(outcome):
    return len([child for child in outcome if child == 'Boy']) == 2

prob = compute_event_probability(has_two_boys, sample_space)
print(f"Probability of 2 boys is {prob}")


possible_rolls = list(range(1, 7))
print(possible_rolls)

sample_space = set(product(possible_rolls, repeat=6))
def has_sum_of_21(outcome): return sum(outcome) == 21
prob = compute_event_probability(has_sum_of_21, sample_space)
print(f"6 rolls sum to 21 with a probability of {prob}")
prob = compute_event_probability(lambda x: sum(x) == 21, sample_space)
assert prob == compute_event_probability(has_sum_of_21, sample_space)

from collections import defaultdict
weighted_sample_space = defaultdict(int)
for outcome in sample_space:
    total = sum(outcome)
    weighted_sample_space[total] += 1