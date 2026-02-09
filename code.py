import sys

def build_suffix_automaton(s):
    states = [{'trans': {}, 'link': -1, 'len': 0}]
    last = 0
    for c in s:
        curr = len(states)
        states.append({'trans': {}, 'link': -1, 'len': states[last]['len'] + 1})
        p = last
        while p != -1 and c not in states[p]['trans']:
            states[p]['trans'][c] = curr
            p = states[p]['link']
        if p == -1:
            states[curr]['link'] = 0
        else:
            q = states[p]['trans'][c]
            i