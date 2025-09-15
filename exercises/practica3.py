from automata import AFDState, AFD, AFNDState, AFND, Rule
from exercises.base import Exercise

class TerminanCon010o101(Exercise):
    def __init__(self):
        super().__init__()
        # Inicializar estados
        initial_state = AFNDState('q0')
        q1a = AFNDState('q1a')
        q1b = AFNDState('q1b')
        q2a = AFNDState('q2a')
        q2b = AFNDState('q2b')
        q3a = AFNDState('q3a')
        q3b = AFNDState('q3b')

        # Transiciones
        rules_initial_state = [
            Rule(q1a, '0'),
            Rule(q1b, '1'),
        ]

        # Transiciones para final en '010'
        rules_q1a = [
            Rule(q2a, '1'),
            Rule(q1a, '0'),
        ]

        rules_q2a = [
            Rule(q3a, '0'),
            Rule(q2a, '1'),
        ]
        
        # Transiciones para final en 101
        rules_q1b = [
            Rule(q2b, '0'),
            Rule(q1b, '1'),
        ]

        rules_q2b = [
            Rule(q3b, '1'),
            Rule(q2b, '0'),
        ]

        # Estados finales
        rules_q3a = [
            Rule(q3b, '1'),
            Rule(q1a, '0'),
        ]

        rules_q3b = [
            Rule(q3a, '0'),
            Rule(q1b, '1'),
        ]

        initial_state.set_rules(rules_initial_state)
        q1a.set_rules(rules_q1a)
        q1b.set_rules(rules_q1b)
        q2a.set_rules(rules_q2a)
        q2b.set_rules(rules_q2b)
        q3a.set_rules(rules_q3a)
        q3b.set_rules(rules_q3b)

        self.automata = AFND(initial_state, [q3a, q3b])

class CantidadParDe0s(Exercise):

    def __init__(self):
        super().__init__()
        # Inicializar estados
        initial_state = AFDState('q0')
        q1 = AFDState('q1')
        q2 = AFDState('q2')

        # Transiciones
        rules_initial_state = [
            # Q1 -> cantidad impar de 0s
            Rule(q1, '0'),
            Rule(initial_state, '1'),
        ]

        rules_q1 = [
            # Q2 -> cantidad par de 0s
            Rule(q2, '0'),
            Rule(q1, '1'),
        ]

        rules_q2 = [
            # Q1 -> cantidad impar de 0s
            Rule(q1, '0'),
            Rule(q2, '1'),
        ]

        initial_state.set_rules(rules_initial_state)
        q1.set_rules(rules_q1)
        q2.set_rules(rules_q2)

        self.automata = AFD(initial_state, q2, debug=True)

class CantidadParDe0sEImparDe1s(Exercise):

    def __init__(self):
        super().__init__()
        # Inicializar estados
        initial_state = AFDState('q0')
        #  q1 ->  Cantidad par de 0s, cantidad par de 1s
        q1 = AFDState('q1')
        #  q2 ->  Cantidad par de 0s, cantidad impar de 1s
        q2 = AFDState('q2')
        #  q3 ->  Cantidad impar de 0s, cantidad par de 1s
        q3 = AFDState('q3')
        #  q4 ->  Cantidad impar de 0s, cantidad impar de 1s
        q4 = AFDState('q4')

        # Transiciones
        rules_initial_state = [
            Rule(q3, '0'),
            Rule(q2, '1'),
        ]
        rules_q1 = [
            Rule(q3, '0'),
            Rule(q2, '1'),
        ]
        rules_q2 = [
            Rule(q4, '0'),
            Rule(q1, '1'),
        ]
        rules_q3 = [
            Rule(q1, '0'),
            Rule(q4, '1'),
        ]
        rules_q4 = [
            Rule(q2, '0'),
            Rule(q3, '1'),
        ]

        initial_state.set_rules(rules_initial_state)
        q1.set_rules(rules_q1)
        q2.set_rules(rules_q2)
        q3.set_rules(rules_q3)
        q4.set_rules(rules_q4)

        self.automata = AFD(initial_state, q2, debug=True)

class DosSimobolosConsecutivosIguales(Exercise):

    def __init__(self):
        super().__init__()
        # Inicializar estados
        initial_state = AFDState('q0')
        q1 = AFDState('q1')
        q2 = AFDState('q2')
        q3 = AFDState('q3')
        
        rules_initial_state = [
            Rule(q1, '0'),
            Rule(q2, '1'),
        ]
        rules_q1 = [
            Rule(q3, '0'),
            Rule(q2, '1'),
        ]
        rules_q2 = [
            Rule(q1, '0'),
            Rule(q3, '1'),
        ]
        rules_q3 = [
            Rule(q3, '0'),
            Rule(q3, '1'),
        ]

        initial_state.set_rules(rules_initial_state)
        q1.set_rules(rules_q1)
        q2.set_rules(rules_q2)
        q3.set_rules(rules_q3)

        self.automata = AFD(initial_state, q3, debug=True)
