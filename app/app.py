import solara as sol
from pathlib import Path
import calendar
from app.calculations import plot_hydrograph_for_year, daily_flows
import plotly.express as px

# Remember to run the dashboard with the following command:
# solara run my_dashboard.py
# Then open the dashboard in your browser at http://localhost:8765

# If you run this in a docker container, you can access the dashboard at http://localhost:4000 

@sol.component
def Page():
    
    # State hooks for user inputs
    design_flow, set_design_flow = sol.use_state(16.76)
    max_head, set_max_head = sol.use_state(335.8)
    reservoir_volume, set_reservoir_volume = sol.use_state(261804445.5)
    base_price, set_base_price = sol.use_state(100)
    # Generation months initially set to example months
    generation_months, set_generation_months = sol.use_state([1, 2, 3, 8, 9, 10, 11, 12])

    # Update calculations or plots based on user inputs
    def update_results():
        # Example function that might use the above states
        # result = calculate_something(design_flow, max_head, ...)
        # For demonstration, using a placeholder result
        result = "Results based on calculations."
        return result

    results = update_results()
    
    def HydrographPlotComponent():
        """
        Generates a hydrograph plot for a user-selectable year.

        Returns:
            A Solara component that renders the Plotly figure.
        """
        year, set_year = sol.use_state(2020)  # Example: user-selectable year state
        
        # Generate the Plotly figure using the specified year.
        # Ensure that calculations.daily_flows is correctly fetching or referencing your DataFrame.
        fig = plot_hydrograph_for_year(daily_flows, year)
        
        # Return a Solara component that renders the Plotly figure.
        return sol.FigurePlotly(fig)

    with sol.Column():
        sol.Title("Reservoir Flow and Revenue Analysis Tool")
        sol.Markdown(r'''
        ## Bridge River Energy Model

        This tool allows users to analyze reservoir inflows, outflows, power generation, and revenue based on various inout parameters. Hydrologic data is based on the Bridge River Energy Project in British Columbia, Canada and Streamflow data from 1978 to 2022.

        - **Data Source**: Hydrometric data from [Climate-Change Canada](https://climate-change.canada.ca/climate-data/#/water-quantity-data).
        - **Stream Gauges Analyzed**: 08ME023, 08ME028, 08ME029.
        - **Reservoir Volume**: Calculated based on the satellite imagery and topographic data provided by PhotoSat (February 2024).
        - **Price Data**: Based on assumed split of 5 hours peak and 19 hours off-peak pricing.
        ''')

        with sol.Sidebar():
            sol.Image(Path(__file__).parent / "KP_logo.png", width="100%")
            sol.Markdown(r'''
            ### User Inputs
            Enter baseline values below.
            ''')
            # create dropdown list for all years in the dataset
            sol.input
            sol.InputFloat("Design Flow (m³/s)", value=design_flow, on_value=set_design_flow)
            sol.InputFloat("Max Head (m)", value=max_head, on_value=set_max_head)
            sol.InputFloat("Reservoir Volume (m³)", value=reservoir_volume, on_value=set_reservoir_volume)
            sol.InputFloat("Base Price per MWh ($)", value=base_price, on_value=set_base_price)
            sol.Markdown("### Generation Months")
            # Generate checkboxes for each month
            for month in range(1, 13):
                sol.Checkbox(label=calendar.month_name[month], value=month in generation_months, on_value=lambda checked, month=month: set_generation_months(generation_months + [month] if checked else [m for m in generation_months if m != month]))

        # Main content area for plots and results
        with sol.Card():
            sol.Markdown("# Analysis Results")


            # For demonstration, using a placeholder text
            sol.Markdown("Graphs and detailed analysis will be displayed here based on the input parameters.")
            
            # Add a plot of the hydrograph for the selected year
            HydrographPlotComponent()

        # Additional UI elements as needed...

# Note: Don't forget to run your app using `solara run app.py`