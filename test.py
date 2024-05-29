import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from sqlalchemy import create_engine
from ProjectFiles.e_menu.utils.queries import dataAnalysis as da
import urllib
import plotly.io as pio
# Initialize database connection
encoded_password = urllib.parse.quote_plus('mosatukba1')
engine = create_engine(f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu')

app = dash.Dash(__name__)

# SQL Queries mapping
queries = {
    "Gender Distribution": da.gender_distribution,
    "Age Distribution": da.age_distribution,
    "Favorite Cuisine Preferences": da.favorite_cuisine_preferences,
    "Visit Frequency": da.visit_frequency,
    "Spending Patterns": da.spending_patterns,
    "Best Selling Items": da.best_selling_items,
    "Category Performance": da.category_performance,
    "Yearly Sales": da.yearly_sales,
    "Monthly Sales": da.monthly_sales,
    "Peak Hours": da.peak_hours,
    "Popular Menu Items": da.popular_menu_items,
    "Rating Trends": da.rating_trends,
    "Food vs Service Ratings": da.food_vs_service_ratings,
    "Popular Payment Methods": da.popular_payment_methods,
    "Payment Trends": da.payment_trends
}

# App layout
app.layout = html.Div([
    html.H1("Restaurant Data Analysis Dashboard",
            style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'color': 'RebeccaPurple'}),

    dcc.Dropdown(
        id='analysis_type',
        options=[{'label': k, 'value': k} for k in queries.keys()],
        value='Gender Distribution',
        style={'width': '40%', 'margin': 'auto'}
    ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='plot')
])


# Callback to update the plot based on the selected analysis type
@app.callback(
    [Output('output_container', 'children'),
     Output('plot', 'figure')],
    [Input('analysis_type', 'value')]
)
def update_graph(selected_analysis):
    container = f"The selected analysis type is: {selected_analysis}"
    query = queries[selected_analysis]

    # Execute the SQL query
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)

    # Generate the plot based on the selected analysis
    if selected_analysis == 'Gender Distribution':
        fig = px.pie(result, names='gender', values='count', title='Gender Distribution')
    elif selected_analysis == 'Age Distribution':
        fig = px.histogram(result, x='age', y='count', nbins=10, title='Age Distribution')
    elif selected_analysis == 'Favorite Cuisine Preferences':
        fig = px.pie(result, names='favourite_cuisine', values='count', title='Favorite Cuisine Preferences')
    elif selected_analysis == 'Visit Frequency':
        fig = px.bar(result, x='name', y='visit_count', title='Visit Frequency')
    elif selected_analysis == 'Spending Patterns':
        fig = px.bar(result, x='name', y='total_spent', title='Spending Patterns')
    elif selected_analysis == 'Best Selling Items':
        fig = px.bar(result, x='name', y='count', title='Best Selling Items')
    elif selected_analysis == 'Category Performance':
        fig = px.bar(result, x='category', y='total', title='Category Performance')
    elif selected_analysis == 'Yearly Sales':
        fig = px.line(result, x='year', y='total', title='Yearly Sales')
    elif selected_analysis == 'Monthly Sales':
        fig = px.line(result, x='month', y='total', color='year', title='Monthly Sales')
    elif selected_analysis == 'Peak Hours':
        fig = px.bar(result, x='hour', y='avg_orders', title='Peak Hours')
    elif selected_analysis == 'Popular Menu Items':
        fig = px.bar(result, x='menu_item', y='order_count', title='Popular Menu Items')
    elif selected_analysis == 'Rating Trends':
        fig = px.line(result, x='rating_date', y='avg_rating', title='Rating Trends')
    elif selected_analysis == 'Food vs Service Ratings':
        fig = px.bar(result.melt(), x='variable', y='value', title='Food vs Service Ratings')
    elif selected_analysis == 'Popular Payment Methods':
        fig = px.pie(result, names='payment_method_id', values='method_count', title='Popular Payment Methods')
    elif selected_analysis == 'Payment Trends':
        fig = px.line(result, x='payment_date', y='method_count', color='payment_method_id', title='Payment Trends')

    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="RebeccaPurple"
        ),
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
        ),
        yaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
        ),
        margin=dict(l=40, r=40, t=40, b=40),
        showlegend=True,
    )

    # Save the Plotly figure as an HTML file
    pio.write_html(fig, file=f'{selected_analysis}.html', auto_open=False, config={'displayModeBar': False})

    return container, fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)