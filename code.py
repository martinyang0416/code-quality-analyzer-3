def largestValsFromLabels(values, labels, num_wanted, use_limit):
    items = sorted(zip(values, labels), key=lambda x: -x[0])
    label_counts = {}
    total = 0
    taken = 0
    for value, label in items:
        if taken >= num_wanted:
            break
        current = label_counts.get(label, 0)
        if current < use_limit:
            total += value
            label_counts[label] = current + 1
            taken += 1
    return total