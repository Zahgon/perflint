from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers import utils as checker_utils
from astroid.helpers import safe_infer


class ComprehensionChecker(BaseChecker):
    """
    Check for comprehension usage
    """

    name = "comprehension-checker"
    priority = -1
    msgs = {
        "W8401": (
            "Use a list comprehension instead of a for-loop",
            "use-list-comprehension",
            "",
        ),
        "W8402": (
            "Use a list copy instead of a for-loop",
            "use-list-copy",
            "",
        ),
        "W8403": (
            "Use a dictionary comprehension instead of a for-loop",
            "use-dict-comprehension",
            "",
        ),
    }

    def visit_for(self, node: nodes.For):
        pass

    @checker_utils.only_required_for_messages(
        "use-list-comprehension", "use-dict-comprehension", "use-list-copy"
    )
    def leave_for(self, node: nodes.For):
        pass
