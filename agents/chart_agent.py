import matplotlib.pyplot as plt

def chart_agent(context: dict):
    if "histogram" in context:
        fig, ax = plt.subplots()
        for label, series in context["histogram"]:
            ax.hist(series.dropna(), alpha=0.5, label=str(label))
        ax.legend()
        return fig
    return None
