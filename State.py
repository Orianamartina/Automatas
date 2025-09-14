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
