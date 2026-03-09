from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Dict, Any, List, Optional
import ast


@dataclass
class PayrollLine:
    component_id: str
    component_name: str
    component_type: str
    calculation_type: str
    amount: Decimal
    display_order: int


def month_start_end(year: int, month: int) -> tuple[date, date]:
    start = date(year, month, 1)
    if month == 12:
        end = date(year + 1, 1, 1)
    else:
        end = date(year, month + 1, 1)
    return start, end


class SafeExprEvaluator:
    """
    Safe evaluator for expressions like: BASIC * 0.4 + HRA
    Only allows: numbers, + - * / ( ) and variable names.
    """
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div,
        ast.UnaryOp, ast.USub, ast.UAdd, ast.Constant, ast.Name, ast.Load,
        ast.Pow,  # optional (remove if you don't want **)
    )

    def eval(self, expr: str, variables: Dict[str, Decimal]) -> Decimal:
        tree = ast.parse(expr, mode="eval")
        for node in ast.walk(tree):
            if not isinstance(node, self.allowed_nodes):
                raise ValueError(f"Unsafe expression: {type(node).__name__}")

        def _eval(n):
            if isinstance(n, ast.Expression):
                return _eval(n.body)
            if isinstance(n, ast.Constant):
                return Decimal(str(n.value))
            if isinstance(n, ast.Name):
                if n.id not in variables:
                    raise ValueError(f"Unknown variable: {n.id}")
                return variables[n.id]
            if isinstance(n, ast.UnaryOp):
                v = _eval(n.operand)
                return -v if isinstance(n.op, ast.USub) else v
            if isinstance(n, ast.BinOp):
                left = _eval(n.left)
                right = _eval(n.right)
                if isinstance(n.op, ast.Add):
                    return left + right
                if isinstance(n.op, ast.Sub):
                    return left - right
                if isinstance(n.op, ast.Mult):
                    return left * right
                if isinstance(n.op, ast.Div):
                    return left / right
                if isinstance(n.op, ast.Pow):
                    return left ** right
            raise ValueError("Invalid expression")

        return _eval(tree)