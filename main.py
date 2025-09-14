from AFD import AFDState, AFD
from Rule import Rule
from AFND import AFNDState, AFND
from DotParser import DotParser

inital_state = AFDState('q0')
q1 = AFDState('q1')
q2 = AFDState('q2')
q3 = AFDState('q3')

# Rule creation
rules_initial_state = [
    Rule(q1, '0')

]
rules_q1 = [
    Rule(q2, '1'),
]

rules_q2 = [
    Rule(q3, '0'),
]

rules_q3 = [
    Rule(q3, '1'),
    Rule(q3, '0'),
]

inital_state.set_rules(rules_initial_state)
q1.set_rules(rules_q1)
q2.set_rules(rules_q2)
q3.set_rules(rules_q3)

automata = AFD('1010010101', inital_state, q3)
automata.run()
print(automata.is_final_state())

inital_state = AFNDState('q0')
q1 = AFNDState('q1')
q2 = AFNDState('q2')
q3 = AFNDState('q3')

# Rule creation
rules_initial_state = [
    Rule(q1, '0')

]
rules_q1 = [
    Rule(q2, '1'),
]

rules_q2 = [
    Rule(q3, '0'),
]

rules_q3 = [
    Rule(q3, '1'),
    Rule(q3, '0'),
]

inital_state.set_rules(rules_initial_state)
q1.set_rules(rules_q1)
q2.set_rules(rules_q2)
q3.set_rules(rules_q3)

automata2 = AFND('01010010101', inital_state, [q3])
automata2.run()
print(automata2.is_final_state())

# Example using DOT parser
print("\n" + "="*50)
print("EXAMPLE: Using DOT Parser")
print("="*50)

# DOT notation for the same automata
dot_notation = """
0 -> 1 [label = "0"];
1 -> 2 [label = "1"];
2 -> 3 [label = "0"];
3 -> 3 [label = "0, 1"];
"""

# Create parser and automata from DOT notation
parser = DotParser()
parser.parse_dot_string(dot_notation, ["0"], ["3"])

print("Automata created from DOT notation:")
parser.print_automata_info()

# Create automata - let it handle success/failure
automata_from_dot = parser.create_automata(dot_notation, "0101", ["0"], ["3"])

print("\nTesting automata from DOT notation:")
result = automata_from_dot.run()
if result:
    print(f"Final state: {result.name}")
    print(f"Is final state: {automata_from_dot.is_final_state()}")
else:
    print("Automata failed to process input")