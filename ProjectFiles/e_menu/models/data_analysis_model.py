import pandas as pd
import plotly.express as px
from ProjectFiles.e_menu.utils.queries import dataAnalysis as da
import plotly.io as pio
from . import *
import plotly.graph_objects as go


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
    "Payment Trends": da.payment_trends,
    "Time Categorized Orders": da.time_categorized_orders,
    "Cohort Analysis": da.cohort_analysis,
    "Customer Life Time Value": da.customer_lifetime_value,
    "Table Location Ratings": da.table_location_ratings,
    "Most Profitable Items": da.most_profitable_items,
    "Payment Methods Impact": da.payment_methods_impact
}


def update_graph(selected_analysis):
    if selected_analysis is None:
        selected_analysis = 'Gender Distribution'

    query = queries[selected_analysis]

    # Execute the SQL query
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)

    # Generate the plot based on the selected analysis
    if selected_analysis == 'Gender Distribution':
        fig = px.pie(result, names='gender', values='count', title='Gender Distribution',
                     color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(template='plotly_white')
    elif selected_analysis == 'Age Distribution':
        fig = px.histogram(result, x='age', y='count', nbins=10, title='Age Distribution',
                           color_discrete_sequence=['indianred'])
        fig.update_layout(template='plotly_white')

    elif selected_analysis == 'Favorite Cuisine Preferences':
        top_5 = result.nlargest(5, 'count')

        # Calculate the count for 'Other' category
        other_count = result.nsmallest(len(result) - 5, 'count')['count'].sum()

        # Create a DataFrame for 'Other' category
        other = pd.DataFrame({'favourite_cuisine': ['Other'], 'count': [other_count]})

        # Concatenate the top 5 DataFrame with the 'Other' category DataFrame
        top_5 = pd.concat([top_5, other], ignore_index=True)

        # Create the pie chart
        fig = px.pie(top_5, names='favourite_cuisine', values='count', title='Favorite Cuisine Preferences',
                     color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(template='plotly_white')

    elif selected_analysis == 'Visit Frequency':
        fig = px.bar(result, x='name', y='visit_count', title='Visit Frequency',
                     color='visit_count', color_continuous_scale='Blues')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)

    elif selected_analysis == 'Spending Patterns':
        fig = px.bar(result, x='name', y='total_spent', title='Spending Patterns',
                     color='total_spent', color_continuous_scale='Greens')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)

    elif selected_analysis == 'Best Selling Items':
        fig = px.bar(result, x='name', y='count', title='Best Selling Items',
                     color='count', color_continuous_scale='Oranges')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)

    elif selected_analysis == 'Category Performance':
        fig = px.bar(result, x='category', y='total', title='Category Performance',
                     color='total', color_continuous_scale='Purples')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)

    elif selected_analysis == 'Yearly Sales':
        result = result.drop_duplicates(keep='first')
        fig = px.line(result, x='year', y='total', title='Yearly Sales',
                             markers=True, line_shape='spline')
        fig.update_traces(mode='lines+markers', marker=dict(size=10, symbol='circle'))

        # Customize layout
        fig.update_layout(
            title='Yearly Sales',
            xaxis_title='Year',
            yaxis_title='Total Sales',
            hovermode='x unified',
            template='plotly_white'
        )
    elif selected_analysis == 'Monthly Sales':
        fig = px.line(result, x='month', y='total', title='Monthly Sales',
                      markers=True)
        fig.update_traces(mode='lines+markers', marker=dict(size=8, symbol='circle'))

        # Customize layout
        fig.update_layout(
            title='Monthly Sales',
            xaxis_title='Month',
            yaxis_title='Total Sales',
            hovermode='x unified',
            template='plotly_white'
        )

    elif selected_analysis == 'Peak Hours':
        fig = px.bar(result, x='hour', y='avg_orders', title='Peak Hours',
                     color='avg_orders', color_continuous_scale='Viridis')
        fig.update_layout(template='plotly_white')

    elif selected_analysis == 'Popular Menu Items':
        fig = px.bar(result, x='name', y='order_count', title='Popular Menu Items',
                     color='order_count', color_continuous_scale='Cividis')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)

    elif selected_analysis == 'Rating Trends':
        fig = px.line(result, x='rating_date', y='avg_rating', title='Rating Trends',
                      markers=True, line_shape='linear', color_discrete_sequence=['firebrick'])
        fig.update_traces(mode='lines+markers', marker=dict(size=8, symbol='circle'))

        # Customize layout
        fig.update_layout(
            title='Rating Trends',
            xaxis_title='Date',
            yaxis_title='Average Rating',
            hovermode='x unified',
            template='plotly_white'
        )

    elif selected_analysis == 'Food vs Service Ratings':
        melted_result = result.melt(value_vars=['food_rating', 'service_rating'],
                                                 var_name='Rating Type', value_name='Rating')

        # Create the bar plot
        fig = px.bar(melted_result, x='Rating Type', y='Rating', color='Rating Type', title='Food vs Service Ratings')
        fig.update_layout(template='plotly_white')

    elif selected_analysis == 'Popular Payment Methods':
        fig = px.pie(result, names='payment_method_id', values='method_count', title='Popular Payment Methods',
                     color_discrete_sequence=px.colors.sequential.PuBu)
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(template='plotly_white')

    elif selected_analysis == 'Payment Trends':
        fig = px.line(result, x='payment_date', y='method_count', color='payment_method_id', title='Payment Trends',
                      markers=True)
        fig.update_traces(mode='lines+markers', marker=dict(size=8, symbol='circle'))

        # Customize layout
        fig.update_layout(
            title='Payment Trends',
            xaxis_title='Payment Date',
            yaxis_title='Method Count',
            hovermode='x unified',
            template='plotly_white'
        )

    elif selected_analysis == 'Time Categorized Orders':
        fig = px.bar(result, x='time_of_day', y='order_count', color='item_name',
                     title='Most Ordered Items by Time of Day')
        fig.update_layout(template='plotly_white')

    elif selected_analysis == 'Cohort Analysis':
        fig = go.Figure()

        # Add trace for customer count
        fig.add_trace(go.Scatter(x=result['cohort_month'], y=result['customer_count'], mode='lines+markers',
                                 name='Customer Count'))

        # Add trace for average order value
        fig.add_trace(go.Scatter(x=result['cohort_month'], y=result['average_order_value'], mode='lines+markers',
                                 name='Average Order Value'))

        # Add trace for average rating
        fig.add_trace(go.Scatter(x=result['cohort_month'], y=result['average_rating'], mode='lines+markers',
                                 name='Average Rating'))

        # Update layout
        fig.update_layout(title='Cohort Analysis',
                          xaxis_title='Cohort Month',
                          yaxis_title='Value',
                          legend_title='Metrics')
    elif selected_analysis == 'Customer Life Time Value':
        fig = px.bar(result, x='name', y='total_revenue', title='Customer Lifetime Value',
                     color='total_revenue', color_continuous_scale='Viridis')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)
    elif selected_analysis == 'Table Location Ratings':
        fig = px.bar(result, x='location', y='average_rating', title='Table Location Ratings',
                     color='average_rating', color_continuous_scale='Bluered')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)

    elif selected_analysis == 'Most Profitable Items':
        fig = px.bar(result, x='item_name', y='total_revenue', title='Most Profitable Items',
                     color='total_revenue', color_continuous_scale='Viridis')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)

    elif selected_analysis == 'Payment Methods Impact':
        fig = px.bar(result, x='payment_method', y='average_order_value', title='Payment Methods Impact',
                     color='average_order_value', color_continuous_scale='Teal')
        fig.update_layout(template='plotly_white', xaxis_tickangle=-45)
    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Arial, sans-serif",
            size=16,
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
                size=14,
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
                size=14,
                color='black',
            ),
        ),
        margin=dict(l=40, r=40, t=40, b=40),
        showlegend=True,
    )

    # Save the Plotly figure as an HTML file content
    plot_html = pio.to_html(fig, full_html=False, config={'displayModeBar': False})
    return plot_html
