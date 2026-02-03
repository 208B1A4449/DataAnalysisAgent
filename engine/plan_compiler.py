import pandas as pd

class PlanCompiler:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.context = {}

    def run(self, plan: dict):
        for step in plan["steps"]:
            action = step["action"]

            if action == "compute_quantile":
                self.context[step["output"]] = (
                    self.df[step["column"]].quantile(step["q"])
                )

            elif action == "filter":
                threshold = self.context[step["condition"].split()[-1]]
                col = step["condition"].split()[0]
                op = step["condition"].split()[1]

                if op == ">=":
                    self.context[step["output"]] = self.df[self.df[col] >= threshold]
                elif op == "<=":
                    self.context[step["output"]] = self.df[self.df[col] <= threshold]

            elif action == "mean":
                df_src = self.context[step["source"]]
                self.context[step["output"]] = df_src[step["column"]].mean()

            elif action == "group_mean":
                self.context[step["output"]] = (
                    self.df.groupby(step["group_by"])[step["column"]].mean()
                )

            elif action == "histogram_compare":
                self.context[step["output"]] = (
                    self.df.groupby(step["group_by"])[step["column"]]
                )

            elif action == "compare_values":
                a = self.context[step["left"]]
                b = self.context[step["right"]]
                self.context[step["output"]] = {
                    "left": a,
                    "right": b,
                    "difference": a - b
                }

        return self.context
