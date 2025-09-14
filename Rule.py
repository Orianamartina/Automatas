class Rule:
    def __init__(self, final_node, condition):
        self.final_node = final_node
        self.condition = condition
    
    def transition(self, input):
        if self.condition == input:
            return self.final_node
        return None
