import graphviz

class NFA:
    # ... (previous implementation)

    def visualize(self):
        dot = graphviz.Digraph(comment='NFA Visualization', format='png')
        self._add_states_to_graph(dot, self.start_state)
        dot.render('nfa', format='png', cleanup=True)
        dot.view()

    def _add_states_to_graph(self, dot, state):
        if state not in dot.node:
            dot.node(state.label, label=state.label, shape='circle')

        for next_state, _ in state.transitions.items():
            self._add_states_to_graph(dot, next_state)
            dot.edge(state.label, next_state.label)

class DFA(NFA):
    # ... (previous implementation)

    def visualize(self):
        dot = graphviz.Digraph(comment='DFA Visualization', format='png')
        states = self._subset_construct(self.start_state)

        for state_set in states:
            state_label = ', '.join(state.label for state in state_set)
            dot.node(state_label, label=state_label, shape='doublecircle' if self.accept_state in state_set else 'circle')

        for state_set in states:
            for char, next_state_set in state_set.transitions.items():
                next_state_label = ', '.join(state.label for state in next_state_set)
                dot.edge(', '.join(state.label for state in state_set), next_state_label, label=char)

        dot.render('dfa', format='png', cleanup=True)
        dot.view()

# Example usage:
nfa_regex = 'a*b'
nfa_engine = NFA(nfa_regex)
nfa_engine.visualize()

dfa_engine = DFA(nfa_regex)
dfa_engine.visualize()


import re

def grep(pattern, filename):
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if re.search(pattern, line):
                print(f"{filename}:{line_number}:{line.strip()}")

# Example usage:
grep("regex", "sample.txt")
