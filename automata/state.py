from abc import ABC, abstractmethod

class State(ABC):
    """
    Abstract base class for automata states.
    Defines the common interface that all state implementations must follow.
    """
    
    def __init__(self, name):
        self.name = name

    def set_rules(self, rules):
        self.rules = rules
    
    @abstractmethod
    def transition(self, input):
        """
        Execute a transition based on the input.
        Must be implemented by subclasses.
        
        Args:
            input: The input character/symbol for the transition
            
        Returns:
            The next state after the transition, or None if no valid transition
            
        Raises:
            Exception: If no valid transition is found for the input
        """
        pass


class AFDState(State):
    """Deterministic Finite Automaton State"""
    
    def transition(self, input):
        for rule in self.rules:
            if rule.transition(input) is not None:
                return rule.transition(input)
        raise Exception('Missing rule for input: ' + input + ' in state: ' + self.name)


class AFNDState(State):
    """Non-deterministic Finite Automaton State"""
    
    def transition(self, input):
        new_states = []
        for rule in self.rules:
            if rule.transition(input) is not None:
                new_states.append(rule.transition(input))
        return new_states
        raise Exception('Transition failed, string not accepted')
