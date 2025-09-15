from abc import ABC, abstractmethod

class FiniteAutomata(ABC):
    """
    Abstract base class for finite automata (AFD and AFND).
    Defines the common interface that all automata implementations must follow.
    """
    
    @abstractmethod
    def run(self, input):
        """
        Execute the automata on the input string.
        Must be implemented by subclasses.
        
        Args:
            input (str): The input string to process
            
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
    
    def get_current_state(self):
        """
        Get the current state(s).
        
        Returns:
            The current state(s)
        """
        return getattr(self, 'current_state', None) or getattr(self, 'current_states', None)
