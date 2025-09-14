from Node import Node
from Rule import Rule
from FiniteAutomata import FiniteAutomata

class AFDNode(Node):
    def transition(self, input):
        for rule in self.rules:
            if rule.transition(input) is not None:
                return rule.transition(input)
        raise Exception('Missing rule for input: ' + input + ' in state: ' + self.name)

class AFD(FiniteAutomata):
    def __init__(self, input, initial_state, final_state):
        self.final_state = final_state
        self.current_state = initial_state
        self.input = input
    

    def run(self):
        try:
            for character in self.input:
                self.current_state = self.current_state.transition(character)
            return self.current_state
        except Exception as e:
            print(f"Error: {e}")
            self.final_state = None
            return None

    def is_final_state(self):
        return self.current_state == self.final_state and self.final_state is not None