class Node:
    def __init__(self, name):
        self.name = name

    def set_rules(self, rules):
        self.rules = rules
    
    def transition(self, input):
        for rule in self.rules:
            if rule.transition(input) is not None:
                return rule.transition(input)
        raise Exception('Missing rule for input: ' + input + ' in state: ' + self.name)