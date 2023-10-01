import plotly.graph_objects as go
import pandas as pd


def boxplot_results():

    results_dataset = pd.read_csv('../../dataset/results.csv', delimiter=';')
    fig = go.Figure()
    fig.add_trace(
        go.Box(
            y=results_dataset['vpl'],
            name='Valores VPL',
            marker_color='black', # noqa
        )
    )

    quantiles = results_dataset['vpl'].quantile([0, 0.25, 0.5, 0.75, 1])
    for y in zip(["MIN", "Q1", "MED", "Q3", "MAX"], quantiles.values.astype(int)):
        fig.add_annotation(
            x=0.3,
            y=y[1],
            text=f'<b>{str(y[0])} : {str(y[1])}</b>',
            showarrow=False
        )
    fig.update_layout(
        title_text='Valores VPL',
        title_x=0.5,
        plot_bgcolor='white',
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(xaxis=dict(showticklabels=False))
    fig.update_layout(yaxis=dict(showticklabels=False))
    fig.show()
    fig.write_html('graphics/vpl_boxplot.html')
