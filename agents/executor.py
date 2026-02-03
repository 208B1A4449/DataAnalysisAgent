import ast
import pandas as pd
from typing import Any


class UnsafeCodeError(Exception):
    pass


class PandasCodeExecutor:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def _validate_code(self, code: str):
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                raise UnsafeCodeError("Imports not allowed")

            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Lambda)):
                raise UnsafeCodeError("Function definitions not allowed")

            if isinstance(node, (ast.For, ast.While)):
                raise UnsafeCodeError("Loops not allowed")
            
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Lambda)):
                raise UnsafeCodeError(
                    "LLM generated a function definition. "
                    "Only single pandas expressions are allowed."
                )

            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    raise UnsafeCodeError(
                        f"Global call '{node.func.id}' not allowed"
                    )

    def execute(self, code: str):
        self._validate_code(code)

        safe_globals = {"__builtins__": {}}

        # 🔑 Automatically expose numeric_df
        numeric_df = self.df.select_dtypes(include="number")

        safe_locals = {
            "df": self.df,
            "numeric_df": numeric_df
        }

        try:
            return eval(code, safe_globals, safe_locals)
        except Exception as e:
            return f"Execution error: {str(e)}"

