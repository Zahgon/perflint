from typing import Dict, List, Set, Union
from astroid import nodes
from astroid.helpers import safe_infer
from pylint.checkers import BaseChecker
from pylint.checkers import utils as checker_utils
from pylint.interfaces import INFERENCE


iterable_types = (
    nodes.Tuple,
    nodes.List,
    nodes.Set,
)
iterable_type_names = (
    "tuple",
    "list",
    "set",
)


def get_children_recursive(node: nodes.NodeNG):
    """Get children of a node."""
    pass


def local_type(name: nodes.NodeNG) -> Union[None, nodes.Name]:
    pass


class ForLoopChecker(BaseChecker):
    """
    Check for poor for-loop usage.
    """

    name = "for-loop-checker"
    priority = -1
    msgs = {
        "W8101": (
            "Unnecessary using of list() on an already iterable type.",
            "unnecessary-list-cast",
            "Eager iteration of an iterable is inefficient.",
        ),
        "W8102": (
            "Incorrect iterator method for dictionary, use %s.",
            "incorrect-dictionary-iterator",
            "Incorrect use of .items() when not unpacking key and value.",
        ),
    }

    @checker_utils.only_required_for_messages(
        "unnecessary-list-cast", "incorrect-dictionary-iterator"
    )
    def visit_for(self, node: nodes.For) -> None:
        """Visit for loops."""
        pass


class LoopInvariantChecker(BaseChecker):
    """
    Check for poor for-loop usage.
    """

    name = "loop-invariant-checker"
    priority = -1
    msgs = {
        "W8201": (
            "Consider moving this expression outside of the loop.",
            "loop-invariant-statement",
            "None of the variables referred to in this expression change within the loop.",
        ),
        "W8202": (
            "Lookups of global names within a loop is inefficient, copy to a local variable outside of the loop first.",
            "loop-global-usage",
            "Global name lookups in Python are slower than local names.",
        ),
        "R8203": (
            "Try..except blocks have an overhead. Avoid using them inside a loop unless you're using them for control-flow. Rule only applies to Python < 3.11.",
            "loop-try-except-usage",
            "Avoid using try..except within a loop.",
        ),
        "W8204": (
            "Looped slicing of bytes objects is inefficient. Use a memoryview() instead",
            "memoryview-over-bytes",
            "Avoid using byte slicing in loops.",
        ),
        "W8205": (
            'Importing the "%s" name directly is more efficient in this loop.',
            "dotted-import-in-loop",
            "Dotted global names in loops are inefficient.",
        ),
    }

    def __init__(self, linter=None):
        super().__init__(linter)
        self._loop_level = 0
        self._loop_assignments: List[Set[str]] = []
        self._loop_names: List[List[nodes.Name]] = []
        self._loop_consts: List[List[nodes.Const]] = []
        self._ignore: List[nodes.NodeNG] = []

    @checker_utils.only_required_for_messages("loop-invariant-statement")
    def visit_for(self, node: nodes.For) -> None:
        """Visit for loop bodies."""
        pass

    @checker_utils.only_required_for_messages("loop-invariant-statement")
    def visit_while(self, node: nodes.While) -> None:
        """Visit while loop bodies."""
        pass

    def _visit_sequence(self, node: Union[nodes.List, nodes.Tuple]) -> None:
        pass

    def visit_list(self, node: nodes.List) -> None:
        pass

    def visit_tuple(self, node: nodes.Tuple) -> None:
        pass

    def visit_dict(self, node: nodes.Dict) -> None:
        pass

    @checker_utils.only_required_for_messages("loop-invariant-statement")
    def leave_for(self, node: nodes.For) -> None:
        pass

    @checker_utils.only_required_for_messages("loop-invariant-statement")
    def leave_while(self, node: nodes.While) -> None:
        pass

    def _leave_loop(self, node: Union[nodes.For, nodes.While]) -> None:
        """Drop loop level."""
        pass

    def visit_assign(self, node: nodes.Assign) -> None:
        """Track assignments in loops."""
        pass

    def visit_augassign(self, node: nodes.AugAssign) -> None:
        """Track assignments in loops."""
        pass

    @checker_utils.only_required_for_messages("loop-global-usage")
    def visit_name(self, node: nodes.Name) -> None:
        """Look for global names"""
        pass

    def visit_const(self, node: nodes.Const) -> None:
        pass

    def visit_call(self, node: nodes.Call) -> None:
        """Look for method calls."""
        pass

    @checker_utils.only_required_for_messages("loop-try-except-usage")
    def visit_tryexcept(self, node: nodes.Try) -> None:
        pass

    @checker_utils.only_required_for_messages("memoryview-over-bytes")
    def visit_subscript(self, node: nodes.Subscript) -> None:
        pass

    @checker_utils.only_required_for_messages("dotted-import-in-loop")
    def visit_attribute(self, node: nodes.Attribute) -> None:
        pass
