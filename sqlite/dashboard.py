import dash
from dash import html,dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

#mental csv
mental_df = pd.read_csv("sqlite_db/mental_update_id_JDLT.csv")
mental_df = mental_df.drop(columns = "Unnamed: 0")
mental_df['PK'] = mental_df['city'].str.cat(mental_df['State_ab'],sep=", ")
mental_states = mental_df['State_name'].unique()
#mental figure
fig_mental = px.scatter(mental_df.loc[mental_df["State_name"]== "California"], x="PK", y=["Low_Confidence_Limit", "Data_Value", "High_Confidence_Limit"],title = "Mental Health Score per City")

#population csv
population_df = pd.read_csv("sqlite_db/city_update_id_JDLT.csv")
population_df['PK'] = population_df['city'].str.cat(population_df['state_id'],sep=", ")
population_df = population_df.drop(['Unnamed: 0'], axis = 1)
population_df = population_df[['PK', 'state_id', 'state_name', 'city', 'population', 'density']]
population_df = population_df.sort_values('population', ascending=False).drop_duplicates(subset=['population'])
population_states = population_df['state_name'].unique()
#population table
fig_population = px.histogram(population_df.loc[population_df["state_name"]== "California"].\
    sort_values(by='population', ascending = False).head(20), x='PK', y=['population','density'], barmode='group',\
        labels={
            "PK": "City, ST",
            "sum of value" : "Total"
        }, title = "Total Population with Calculated Density")

#income csv
income_df = pd.read_csv("sqlite_db/income_update_id_JDLT.csv")
income_df['PK'] = income_df['City'].str.cat(income_df['State_ab'],sep=", ")
income_df = income_df.drop(['Unnamed: 0', 'ALand', 'AWater'], axis=1)
income_df = income_df[income_df.Median != 300000]
income_df = income_df[['PK','id', 'State_ab', 'State_Name', 'City', 'Median', 'Stdev']]
income_states = income_df['State_Name'].unique()
#income figure
fig_income = px.scatter(income_df.loc[income_df["State_Name"]== "California"], x="Median", y="PK",
	         size="Stdev", color="State_Name",
                 hover_name="PK", log_x=True, title = "income figure")

#making the options for the dropdown menu
state_labels = [{'label':i, 'value':i} for i in mental_states]

app = dash.Dash()
app.layout = html.Div([html.Div('MHP'),
                       html.H1(children = 'Mental Health Predictor',
                       style={'textAlign':'center'}),
                       html.Div(dcc.Dropdown(id='dropdown', options = state_labels)),
                       dcc.Graph(id='fig1', figure=fig_mental),
                       dcc.Graph(id='fig2', figure=fig_population),
                       dcc.Graph(id='fig3', figure=fig_income)])

#UPDATING MENTAL FIGURE
@app.callback(Output('fig1', 'figure'),
              Input('dropdown', 'value'))
def update_mental(state):
    
    fig1 = px.scatter(mental_df.loc[mental_df["State_name"]== state].\
        sort_values('Data_Value'), x="PK", y=["Low_Confidence_Limit", "Data_Value", "High_Confidence_Limit"],
        labels = {"PK": "City, ST", "value":"Mental Health Score", "Low_Confidence_Limit":"Low Confidence Limit"})

    fig1.update_layout(title = {"text":"Mental Health Score per City","y":0.9,"x":0.5, "xanchor":"center", "yanchor":"top"})
    return fig1

# UPDATING POPULATION FIGURE
@app.callback(Output('fig2', 'figure'),
              Input('dropdown', 'value'))
def update_population(state):
    
    fig2 = px.histogram(population_df.loc[population_df["state_name"]== state].sort_values('population', ascending=False).\
        head(20), x='PK', y=['population','density'], barmode='group', labels = {"sum of value": "Total", "PK": "City, ST"},title = "Total Population with Calculated Density")
    fig2.update_layout(title = {"text":"Total Population with Calculated Density","y":0.9,"x":0.5, "xanchor":"center", "yanchor":"top"})

    return fig2

# UPDATING INCOME FIGURE
@app.callback(Output('fig3', 'figure'),
              Input('dropdown', 'value'))
def update_income(state):
    
    fig3 = px.scatter(income_df.loc[income_df["State_Name"]== state].sort_values('Stdev', ascending=True), x="Median", y="PK",
	         size="Stdev", color="State_Name",
                 hover_name="PK", log_x=True, labels = {"Median":"Median Income for City", "PK": "City, ST"},title = "City Median Income Tied to Standard Deviation")
    fig3.update_layout(title = {"text":"City Median Income Tied to Standard Deviation","y":0.9,"x":0.5, "xanchor":"center", "yanchor":"top"})
    
    
    return fig3

app.run_server(debug=True)
