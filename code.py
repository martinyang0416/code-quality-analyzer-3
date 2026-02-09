def generate_states(quests):
    states = {(0, 0): (0, [])}
    for li, mi, wi in quests:
        new_states = {}
        for (d_ab, d_bc), (sum_total, path) in states.items():
            # Option LM
            new_d_ab_lm = d_ab + (li - mi)
            new_d_bc_lm = d_bc + mi
            new_sum_lm = sum_total + li + mi
            new_path_lm = path + ['LM']
            key_lm = (new_d_ab_lm, new_d_bc_lm)
            if key_lm not in new_states or new_sum_lm > new_states[key_lm][0]:
        