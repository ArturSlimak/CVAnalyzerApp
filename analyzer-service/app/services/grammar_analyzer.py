import language_tool_python
from models.grammar_issue import GrammarIssue

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text: str) -> list[GrammarIssue]:
    matches = tool.check(text)
    issues = []

    for match in matches:
        issue = GrammarIssue(
            message= match.message,
            context= match.context,
            offset=match.offsetInContext,
            length= match.errorLength,
            replacement= match.replacements
        )
        issues.append(issue)

    return issues