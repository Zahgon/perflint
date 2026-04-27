from typing import Dict, List
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers import utils as checker_utils


class ListChecker(BaseChecker):
    """
    Check for inefficient list usage
    """

    name = 'list-checker'
    priority = -1
    msgs = {
        'W8301': (
            'Use tuple instead of list for a non-mutated sequence',
            'use-tuple-over-list',
            ''
        ),
    }

    def __init__(self, linter=None):
        super().__init__(linter)
        self._lists_to_watch: List[Dict[str, nodes.AssignName]] = []

    def visit_assign(self, node: nodes.Assign):
        pass

    def visit_module(self, node: nodes.Module):
        pass

    def _raise_for_scope(self):
        pass

    @checker_utils.only_required_for_messages("use-tuple-over-list")
    def leave_module(self, node: nodes.Module):
        pass

    def visit_functiondef(self, node: nodes.FunctionDef):
        pass

    @checker_utils.only_required_for_messages("use-tuple-over-list")
    def leave_functiondef(self, node: nodes.FunctionDef):
        pass

    def visit_call(self, node: nodes.Call) -> None:
        """Look for method calls to list nodes."""
        pass

    def _mark_mutated(self, _name: nodes.Name):
        pass

    def visit_subscript(self, node: nodes.Subscript):
        pass
