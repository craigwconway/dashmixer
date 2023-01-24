from dash import Dash, html, dcc, Input, Output

colors = ("red", "green", "blue")

sliders = [
    html.Div(
        [
            html.Span(color),
            dcc.Slider(
                min=0,
                max=255,
                step=1,
                value=int(255 / 2),
                marks=None,
                id=f"{color}-slider",
            ),
        ]
    )
    for color in colors
]

renders = [html.Span("-", id=f"{color}-render", className="box") for color in colors]

result = html.Div("-", "result", className="box")

app = Dash(__name__)

app.layout = html.Div(
    children=[
        *sliders,
        *renders,
        result,
    ]
)


@app.callback(
    Output("result", "style"),
    Input("red-slider", "drag_value"),
    Input("green-slider", "drag_value"),
    Input("blue-slider", "drag_value"),
)
def mixer(r, g, b):
    style = {"background-color": f"rgb({r},{g},{b})"}
    return style


@app.callback(
    Output("red-render", "style"),
    Input("red-slider", "drag_value"),
)
def red(r):
    style = {"background-color": f"rgb({r}, 0, 0)"}
    return style


@app.callback(
    Output("green-render", "style"),
    Input("green-slider", "drag_value"),
)
def green(g):
    style = {"background-color": f"rgb(0, {g}, 0)"}
    return style


@app.callback(
    Output("blue-render", "style"),
    Input("blue-slider", "drag_value"),
)
def blue(b):
    style = {"background-color": f"rgb(0, 0, {b})"}
    return style


@app.callback(
    Output("result", "children"),
    Input("red-slider", "drag_value"),
    Input("green-slider", "drag_value"),
    Input("blue-slider", "drag_value"),
)
def white(r, g, b):
    return "white" if r == g == b == 255 else "-"


if __name__ == "__main__":
    app.run_server(debug=True)
