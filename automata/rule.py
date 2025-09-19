class Rule:
    """Represents a transition rule in a finite automaton"""
    
    def __init__(self, final_state, condition):
        self._final_state = final_state
        self._conditions =  condition.split(',')
    
    def transition(self, input):
        if input in self._conditions:
            return self._final_state
        return None

    def get_conditions(self):
        return self.conditions