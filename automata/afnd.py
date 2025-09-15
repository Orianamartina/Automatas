from .finite_automata import FiniteAutomata

class AFND(FiniteAutomata):
    """Non-deterministic Finite Automaton (AFND)"""
    
    def __init__(self, initial_state, final_states, debug=False):
        self.debug = debug
        self.final_states = final_states
        self.current_states = [initial_state]

    def run(self, input):
        try:
            for character in input:
                if self.debug:
                    print(f"Character: {character}")
                new_states = []
                for state in self.current_states:
                    new_states += state.transition(character)
                self.current_states = new_states
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
