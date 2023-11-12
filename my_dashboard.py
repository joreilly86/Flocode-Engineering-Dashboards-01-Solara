import solara

@solara.component
def Page():
    length, set_length = solara.use_state(1.0)
    width, set_width = solara.use_state(1.0)
    slab_depth, set_slab_depth = solara.use_state(1.0)
    density_options = [2300, 2400, 2500, 2600]
    density, set_density = solara.use_state(2400)
    calculation_result, set_calculation_result = solara.use_state("")

    def update_calculation():
        weight = length * width * slab_depth * density
        set_calculation_result(f"The calculated weight is: {weight:.2f} kg")

    with solara.Column():
        solara.Title("Flocode - Solara Dashboard Example for Civil/Structural Engineering")

        with solara.Sidebar():
            solara.SliderFloat(label="Slab Depth (meters)", min=0, max=1.0, step=0.1, value=slab_depth, on_value=set_slab_depth)

        solara.Info("Welcome to Flocode's Solara Dashboard Example")

        with solara.Card():
            solara.Markdown(r'''
            # Concrete Slab Weight Calculator

            This very simple tool calculates the weight of a concrete slab based on its dimensions and the density of the concrete. Is this useful? Not really, but it is a good example of how to use Solara to create a simple dashboard. Once you can do this, you can create more complex dashboards specific to your needs.

            ## How to Use
            - **Length (meters):** Enter the length of the concrete slab.
            - **Width (meters):** Specify the width of the slab.
            - **Slab Depth (meters):** Use the slider on the left to specify the thickness of the slab.
            - **Density (kg/m^3):** Use the dropdown menu below to select the density of the concrete (typical density is around 2400 kg/m^3).

            Once all inputs are filled, the calculator will automatically compute and display the weight of the concrete slab.
                            
            ''')

        with solara.Card("Slab Weight Calculator"):
            solara.InputFloat(label="Length (meters)", value=length, on_value=set_length)
            solara.InputFloat(label="Width (meters)", value=width, on_value=set_width)
            solara.Select(label="Density (kg/m³)", values=density_options, value=density, on_value=set_density)
            solara.Markdown(calculation_result)

        # Automatically update the calculation whenever any input changes
        update_calculation()

        
        # This is just some random formatting to show how to use the Columns component
        with solara.Card("Use solara.Columns() to create a two column layout"):
            with solara.Columns([1, 2]):
                solara.Success("I'm in the first column")
                solara.Warning("I'm in the second column, I am twice as wide")
                solara.Info("I am like the first column")

