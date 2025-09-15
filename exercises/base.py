from abc import ABC, abstractmethod

class Exercise(ABC):
    """
    Abstract base class for automata exercises.
    All exercises should inherit from this class.
    """
    
    def __init__(self):
        self.automata = None
    
    def check(self, input_string):
        """
        Check if the input string is accepted by the automata.
        
        Args:
            input_string (str): The input string to test
            
        Returns:
            bool: True if the string is accepted, False otherwise
        """
        if self.automata is None:
            raise ValueError("Automata not initialized")
        
        self.automata.run(input_string)
        return self.automata.is_final_state()
    