from AFD import AFDState
from State import State
from Rule import Rule
from FiniteAutomata import FiniteAutomata


class AFNDState(State):
    def transition(self, input):
        for rule in self.rules:
            if rule.transition(input) is not None:
                return rule.transition(input)
        raise Exception('Transition failed, string not accepted')

class AFND(FiniteAutomata):
    def __init__(self, input, initial_state, final_states):
        self.final_states = final_states
        self.current_states = [initial_state]
        self.input = input

    def run(self):
        try:
            for character in self.input:
                new_states = []
                for state in self.current_states:
                    new_states.append(state.transition(character))
                self.current_states = new_states
            return self.current_states
        except Exception as e:
            print(f"Error: {e}")
            return None

    def is_final_state(self):
        for state in self.current_states:
            if state in self.final_states:
                return True
        return False
    