import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from processamento import processar_dados

# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Carregando os dados processados
df = processar_dados()

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='Análise de Big Data com PySpark e Hadoop'),

    dcc.Dropdown(
        id='coluna-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0],
        clearable=False,
    ),

    dcc.Graph(id='grafico-dados'),

    dcc.Slider(
        id='limite-slider',
        min=df['coluna'].min(),
        max=df['coluna'].max(),
        value=df['coluna'].min(),
        marks={int(i): str(int(i)) for i in range(int(df['coluna'].min()), int(df['coluna'].max()), 100)},
        step=None,
    )
])

# Callback para atualizar o gráfico
@app.callback(
    Output('grafico-dados', 'figure'),
    [Input('coluna-dropdown', 'value'), Input('limite-slider', 'value')]
)
def atualizar_grafico(coluna_selecionada, limite):
    # Filtrar os dados com base na seleção do usuário
    df_filtrado = df[df['coluna'] > limite]

    # Criar o gráfico
    fig = px.histogram(df_filtrado, x=coluna_selecionada)

    return fig

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
