from dataclasses import dataclass


@dataclass
class Note:
    id: int = 0
    text: str = ""
    completed: bool = False
