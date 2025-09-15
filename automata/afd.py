from .finite_automata import FiniteAutomata

class AFD(FiniteAutomata):
    """Deterministic Finite Automaton (AFD)"""
    
    def __init__(self, initial_state, final_state, debug=False):
        self.debug = debug
        self.final_state = final_state
        self.current_state = initial_state
    
    def run(self, input):
        try:
            for character in input:
                if self.debug:
                    print(f"Character: {character}")
                self.current_state = self.current_state.transition(character)
                if self.debug:
                    print(f"Current state: {self.current_state.name}")
            return self.current_state
        except Exception as e:
            print(f"Error: {e}")
            self.final_state = None
            return None

    def is_final_state(self):
        return self.current_state == self.final_state and self.final_state is not None
