from .finite_automata import FiniteAutomata

class AFNDEpsilon(FiniteAutomata):
    """AFND con transiciones epsilon (ε)"""
    def __init__(self, initial_state, final_states, debug=False):
        self.debug = debug
        self.initial_state = initial_state
        self.final_states = final_states
        self.current_states = [initial_state]

    def epsilon_closure(self, states):
        """Devuelve la clausura epsilon de un conjunto de estados."""
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            for next_state in state.transition('ε'):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return list(closure)

    def run(self, input):
        try:
            self.current_states = self.epsilon_closure([self.initial_state])
            for character in input:
                if self.debug:
                    print(f"Character: {character}")
                new_states = []
                for state in self.current_states:
                    new_states += state.transition(character)
                self.current_states = self.epsilon_closure(new_states)
                if not self.current_states:
                    raise Exception('No valid transitions, string not accepted')
                if self.debug:
                    print(f"Current states: {[state.name for state in self.current_states]}")
            return self.current_states
        except Exception as e:
            print(f"Error: {e}")
            return None

    def is_final_state(self):
        for state in self.current_states:
            if state in self.final_states:
                return True
        return False
