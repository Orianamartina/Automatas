"""
Exercises module containing all automata exercises.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.base import Exercise
from exercises.practica3 import (
    TerminanCon010o101,
    CantidadParDe0s,
    CantidadParDe0sEImparDe1s,
    DosSimobolosConsecutivosIguales
)

__all__ = [
    'Exercise',
    'TerminanCon010o101',
    'CantidadParDe0s', 
    'CantidadParDe0sEImparDe1s',
    'DosSimobolosConsecutivosIguales'
]
