import re
from State import State
from Rule import Rule
from AFD import AFDState

class DotParser:
    """
    Parser for DOT notation (Graphviz format) to convert automata definitions
    into States and Rules for finite automata.
    """
    
    def __init__(self):
        self.states = {}
        self.rules = []
    
    def parse_dot_string(self, dot_string, initial_state_names, final_state_names):
        """
        Parse a DOT notation string and create States and Rules.
        
        Args:
            dot_string (str): DOT notation string containing transitions
            initial_state_names (list): List of initial state names/IDs
            final_state_names (list): List of final state names/IDs
            
        Returns:
            dict: Dictionary of parsed states
        """
        # Clean the input string
        dot_string = dot_string.strip()
        
        # Store initial and final state names
        self.initial_state_names = initial_state_names
        self.final_state_names = final_state_names
        
        # Split into lines and process each transition
        lines = [line.strip() for line in dot_string.split('\n') if line.strip()]
        
        for line in lines:
            self._parse_transition_line(line)
        
        return self.states
    
    def _parse_transition_line(self, line):
        """
        Parse a single transition line in DOT format.
        Format: "source -> target [label = \"input\"];"
        """
        # Remove semicolon if present
        line = line.rstrip(';')
        
        # Extract source and target states
        arrow_match = re.search(r'(\d+)\s*->\s*(\d+)', line)
        if not arrow_match:
            raise ValueError(f"Invalid transition format: {line}")
        
        source_id = arrow_match.group(1)
        target_id = arrow_match.group(2)
        
        # Extract label (input symbols)
        label_match = re.search(r'label\s*=\s*"([^"]+)"', line)
        if not label_match:
            raise ValueError(f"Missing label in transition: {line}")
        
        label = label_match.group(1)
        
        # Create states if they don't exist
        if source_id not in self.states:
            self.states[source_id] = AFDState(f'q{source_id}')
        if target_id not in self.states:
            self.states[target_id] = AFDState(f'q{target_id}')
        
        # Parse input symbols (handle comma-separated values)
        input_symbols = [symbol.strip() for symbol in label.split(',')]
        
        # Create rules for each input symbol
        for symbol in input_symbols:
            rule = Rule(self.states[target_id], symbol)
            if not hasattr(self.states[source_id], 'rules'):
                self.states[source_id].rules = []
            self.states[source_id].rules.append(rule)
    
    def get_initial_state(self):
        """
        Get the initial state from the provided initial state names.
        """
        if hasattr(self, 'initial_state_names') and self.initial_state_names:
            # Return the first initial state that exists
            for state_name in self.initial_state_names:
                if state_name in self.states:
                    return self.states[state_name]
        
        # Fallback to state 0 if no initial states specified
        if '0' in self.states:
            return self.states['0']
        elif self.states:
            # If no state 0, return the first state
            return list(self.states.values())[0]
        return None
    
    def get_final_states(self):
        """
        Get the final states from the provided final state names.
        """
        final_states = []
        if hasattr(self, 'final_state_names') and self.final_state_names:
            for state_name in self.final_state_names:
                if state_name in self.states:
                    final_states.append(self.states[state_name])
        
        # If no final states specified, return empty list
        return final_states
    
    def get_all_states(self):
        """
        Get all parsed states.
        
        Returns:
            dict: Dictionary of state_id -> State objects
        """
        return self.states
    
    def create_automata(self, dot_string, input_string, initial_state_names, final_state_names):
        """
        Create an AFD automata from DOT notation and input string.
        
        Args:
            dot_string (str): DOT notation string
            input_string (str): Input string to process
            initial_state_names (list): List of initial state names/IDs
            final_state_names (list): List of final state names/IDs
            
        Returns:
            AFD: Configured AFD automata
        """
        from AFD import AFD
        
        self.parse_dot_string(dot_string, initial_state_names, final_state_names)
        
        # Get initial state
        initial_state = self.get_initial_state()
        if not initial_state:
            raise ValueError("No initial state found")
        
        # Get final states (use first one for AFD)
        final_states = self.get_final_states()
        if not final_states:
            raise ValueError("No final states found")
        
        final_state = final_states[0]  # AFD uses single final state
        
        return AFD(input_string, initial_state, final_state)
    
    def print_automata_info(self):
        """
        Print information about the parsed automata.
        """
        print("=== Parsed Automata Information ===")
        print(f"States: {len(self.states)}")
        for state_id, state in self.states.items():
            print(f"  State {state_id}: {state.name}")
            if hasattr(state, 'rules') and state.rules:
                for rule in state.rules:
                    print(f"    -> {rule.final_state.name} on '{rule.condition}'")
        
        initial_state = self.get_initial_state()
        final_states = self.get_final_states()
        print(f"\nInitial State: {initial_state.name if initial_state else 'None'}")
        print(f"Final States: {[state.name for state in final_states]}")
        print("=" * 35)
