class Rule:
    def __init__(self, final_state, condition):
        self.final_state = final_state
        self.condition = condition
    
    def transition(self, input):
        if self.condition == input:
            return self.final_state
        return None
