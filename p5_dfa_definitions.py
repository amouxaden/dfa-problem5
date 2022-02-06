from automata.fa.dfa import DFA

id_A = DFA(
    states={'start', 's0'},
    input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
                   'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z'},
    transitions={
        'start': {'A': 's0', 'B': 's0', 'C': 's0', 'D': 's0', 'E': 's0', 'F': 's0',
                  'G': 's0', 'H': 's0', 'I': 's0', 'J': 's0', 'K': 's0', 'L': 's0',
                  'M': 's0', 'N': 's0', 'O': 's0', 'P': 's0', 'Q': 's0', 'R': 's0',
                  'S': 's0', 'T': 's0', 'U': 's0', 'V': 's0', 'W': 's0', 'X': 's0',
                  'Y': 's0', 'Z': 's0', 'a': 's0', 'b': 's0', 'c': 's0', 'd': 's0',
                  'e': 's0', 'f': 's0', 'g': 's0', 'h': 's0', 'i': 's0', 'j': 's0',
                  'k': 's0', 'l': 's0', 'm': 's0', 'n': 's0', 'o': 's0', 'p': 's0',
                  'q': 's0', 'r': 's0', 's': 's0', 't': 's0', 'u': 's0', 'v': 's0',
                  'w': 's0', 'x': 's0', 'y': 's0', 'z': 's0', },

        's0': {'0': 's0', '1': 's0', '2': 's0', '3': 's0', '4': 's0', '5': 's0',
               '6': 's0', '7': 's0', '8': 's0', '9': 's0', 'A': 's0', 'B': 's0',
               'C': 's0', 'D': 's0', 'E': 's0', 'F': 's0', 'G': 's0', 'H': 's0',
               'I': 's0', 'J': 's0', 'K': 's0', 'L': 's0', 'M': 's0', 'N': 's0',
               'O': 's0', 'P': 's0', 'Q': 's0', 'R': 's0', 'S': 's0', 'T': 's0',
               'U': 's0', 'V': 's0', 'W': 's0', 'X': 's0', 'Y': 's0', 'Z': 's0',
               'a': 's0', 'b': 's0', 'c': 's0', 'd': 's0', 'e': 's0', 'f': 's0',
               'g': 's0', 'h': 's0', 'i': 's0', 'j': 's0', 'k': 's0', 'l': 's0',
               'm': 's0', 'n': 's0', 'o': 's0', 'p': 's0', 'q': 's0', 'r': 's0',
               's': 's0', 't': 's0', 'u': 's0', 'v': 's0', 'w': 's0', 'x': 's0',
               'y': 's0', 'z': 's0', },
    },
    initial_state='start',
    final_states={'s0'},
    allow_partial=True
)
"""
id = {w | w is a string beginning with A … Z, a … z and followed by any character in the alphabet}.

The alphabet is  Σ={0 … 9, A … Z, a … z}
"""

num_B = DFA(
    states={'start', 's0'},
    input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    transitions={
        'start': {'0': 's0', '1': 's0', '2': 's0', '3': 's0', '4': 's0', '5': 's0',
                  '6': 's0', '7': 's0', '8': 's0', '9': 's0', },

        's0': {'0': 's0', '1': 's0', '2': 's0', '3': 's0', '4': 's0', '5': 's0',
               '6': 's0', '7': 's0', '8': 's0', '9': 's0', },
    },
    initial_state='start',
    final_states={'s0'},
    allow_partial=True
)
"""
num = {w | w contains 0 … 9}.

The alphabet is  Σ = {0, … ,9}.
"""

semicolon_C = DFA(
    states={'start', 's0', 's1'},
    input_symbols={';'},
    transitions={
        'start': {';': 's0'},
        's0': {';': 's1'},
        's1': {},
    },
    initial_state='start',
    final_states={'s0'},
    allow_partial=True
)
"""
semicolon = {w | w is the string ';'}.

The alphabet is  Σ = {;}.
"""

and_D = DFA(
    states={'start', 's0', 's1', 's2'},
    input_symbols={'&'},
    transitions={
        'start': {'&': 's0'},
        's0': {'&': 's1'},
        's1': {'&': 's2'},
        's2': {}
    },
    initial_state='start',
    final_states={'s1'},
    allow_partial=True
)
"""
and = {w | w is the string '&&'}.

The alphabet is Σ = {&}.
"""

# lol
while_E = DFA(
    states={'start', 's0', 's1', 's2', 's3', 's4', 's5'},
    input_symbols={'w', 'h', 'i', 'l', 'e'},
    transitions={
        'start': {'w': 's0'},
        's0': {'h': 's1'},
        's1': {'i': 's2'},
        's2': {'l': 's3'},
        's3': {'e': 's4'},
        's4': {'w': 's5', 'h': 's5', 'i': 's5', 'l': 's5', 'e': 's5'},
        's5': {},
    },
    initial_state='start',
    final_states={'s4'},
    allow_partial=True
)
"""
while = {w | w is the string 'while'}, 	

The alphabet is Σ = {w, h, i, l, e}.
"""