import solara
from pathlib import Path

# Remember to run the dashboard with the following command:
# solara run my_dashboard.py
# Then open the dashboard in your browser at http://localhost:8765

# If you run this in a docker container, you can access the dashboard at http://localhost:4000 

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
        volume = length * width * slab_depth
        set_calculation_result(f"The calculated weight is:<br> **{weight:.1f} kg ({(weight*0.00981):.1f} kN)**")

    with solara.Column():
        solara.Title("Flocode - Engineering Dashboards | 01. Solara - The Basics")

        with solara.Sidebar():
            # Add an image to the dashboard
            image_path = Path(__file__).parent / "KP_logo.png"
            solara.Image(image_path, width="400px")  # Set the desired width
            display("This is just an image")
            solara.Markdown(r'''
            ## Slab Depth Slider
            Adjust the slab depth using the slider below.
            ''')
            solara.SliderFloat(label="Slab Depth (meters)", min=0, max=1.0, step=0.1, value=slab_depth, on_value=set_slab_depth)


            solara.Markdown(r'''
            ## Sidebar Stuff Goes Here
                            
            ### 🔭 Explore Further

            - *You can add markdown text to describe something.*
            - Maybe even a list of **important things**.
            - Or a link to [flocode.dev](https://flocode.dev)
            - Or a table of contents for your dashboard documentation. 

            📘 For more information on Solara, check out the [Solara Documentation](https://solara.dev).

            🐍 And for learning more Python for engineering stuff, come and visit us at [flocode.dev](https://flocode.dev) 🌊.
                            
            ''')

        solara.Info("Welcome to Flocode's Solara Dashboard Example")


        with solara.Card():
            solara.Markdown(r'''
                # Concrete Slab Weight Calculator
                This simple tool, featured in [Flocode Newsletter's](https://flocode.substack.com) post **"Engineering Dashboards | 01. Solara - The Basics,"** demonstrates how to use Solara for creating dashboards.  
                
                ## How to Use
                To use the calculator, adjust the following inputs in the fields below:

                - **Length (meters):** Enter the slab's length.
                - **Width (meters):** Specify the slab's width.
                - **Slab Depth (meters):** Adjust using the sidebar slider.
                - **Density (kg/m³):** Select from the dropdown (commonly around 2400 kg/m³).

                The calculator dynamically displays the weight as inputs change.  
                Explore more Python for Engineering by subscribing to our newsletter [Flocode: Engineering Insights 🌊](https://flocode.substack.com).
            ''')

        with solara.Card("Slab Weight Calculator"):
            solara.InputFloat(label="Length (meters)", value=length, on_value=set_length)
            solara.InputFloat(label="Width (meters)", value=width, on_value=set_width)
            solara.Select(label="Density (kg/m³)", values=density_options, value=density, on_value=set_density)
            solara.Markdown(calculation_result)
            solara.Markdown(r'''
                            ### The columns and cards below are for Solara UI layout demonstration purposes. They are not part of the calculator.
                            ''')

        # Automatically update the calculation whenever any input changes
        update_calculation()

        
        # This is just some random formatting to show how to use the Columns component
        with solara.Card("Use solara.Columns([1, 2]) to create relatively sized columns, you can add whatever you want to them"):
            with solara.Columns([1, 2]):
                solara.Success("I'm in the first column")
                solara.Warning("I'm in the second column, I am twice as wide")
                solara.Info("I am like the first column")

        with solara.Card("Use solara.Column() to create a full width column"):
            with solara.Column():
                solara.Success("I'm first in this full with column")
                solara.Warning("I'm second in this full with column")
                solara.Error("I'm third in this full with column")

        with solara.Card("Use solara.ColumnsResponsive(6, large=4) to response to screen size"):
            with solara.ColumnsResponsive(6, large=4):
                for i in range(6):
                    solara.Info("two per column on small screens, three per column on large screens")

