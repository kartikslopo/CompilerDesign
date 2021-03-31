from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an even number of '1's
dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q2'}
)
input_str = input('string =')
if dfa.accepts_input(input_str):
    print('accepted')
else:
    print('rejected')

dfa.read_input('011')

