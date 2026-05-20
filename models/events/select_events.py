from enum import Enum, auto

class EventSelectCell(Enum):
  SELECT_CELL = auto()
  DESELECT_CELL = auto()
  SWAPPED_CELLS = auto()