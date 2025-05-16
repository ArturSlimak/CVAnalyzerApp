from dataclasses import dataclass
from typing import Optional

@dataclass
class GrammarIssue:
    message: str
    context: str
    offset: int
    length: int
    replacement: Optional[str] = None