from AFD import AFDNode, AFD
from Rule import Rule
from AFND import AFNDNode, AFND

inital_node = AFDNode('q0')
q1 = AFDNode('q1')
q2 = AFDNode('q2')
q3 = AFDNode('q3')

# Rule creation
rules_initial_node = [
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

inital_node.set_rules(rules_initial_node)
q1.set_rules(rules_q1)
q2.set_rules(rules_q2)
q3.set_rules(rules_q3)

automata = AFD('1010010101', inital_node, q3)
automata.run()
print(automata.is_final_state())

inital_node = AFNDNode('q0')
q1 = AFNDNode('q1')
q2 = AFNDNode('q2')
q3 = AFNDNode('q3')

# Rule creation
rules_initial_node = [
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

inital_node.set_rules(rules_initial_node)
q1.set_rules(rules_q1)
q2.set_rules(rules_q2)
q3.set_rules(rules_q3)

automata2 = AFND('1010010101', inital_node, [q3])
automata2.run()
print(automata2.is_final_state())