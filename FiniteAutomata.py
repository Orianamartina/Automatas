from abc import ABC, abstractmethod

class FiniteAutomata(ABC):
    """
    Abstract base class for finite automata (AFD and AFND).
    Defines the common interface that all automata implementations must follow.
    """
    
    @abstractmethod
    def run(self):
        """
        Execute the automata on the input string.
        Must be implemented by subclasses.
        
        Returns:
            The final state(s) after processing the input, or None if error occurs
        """
        pass
    
    @abstractmethod
    def is_final_state(self):
        """
        Check if the current state(s) is/are final state(s).
        Must be implemented by subclasses.
        
        Returns:
            bool: True if in final state, False otherwise
        """
        pass
    
    def get_input(self):
        """
        Get the input string.
        
        Returns:
            str: The input string
        """
        return self.input
    
    def get_current_state(self):
        """
        Get the current state(s).
        
        Returns:
            The current state(s)
        """
        return self.current_state