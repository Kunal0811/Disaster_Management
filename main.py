import streamlit as st
import time
from streamlit_option_menu import option_menu

import feedback,dailyalerts
import home, safety, account, CTA, about

hide_deploy_button_script = """
    <script>
        window.onload = function() {
            const deployButton = document.querySelector('.element-container .stButton');
            if (deployButton) {
                deployButton.remove();
            }
        }
    </script>
"""

# Add this line to remove the Streamlit menu, footer, and Deploy button
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_deploy_button_script, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def set_background_image(image_url):
    # Define the CSS styles
    styles = f"""
        <style>
            body {{
                background-image: url("{image_url}");
                background-size: cover;
            }}
        </style>
    """

    # Inject the CSS styles into the streamlit app
    st.markdown(styles, unsafe_allow_html=True)
    


# Main function to run the app

def run():
    set_background_image("bg69.jpg")
     # app = st.sidebar
    with st.sidebar:
        app = option_menu(
            menu_title='Contents ',
            options=['Home', 'Account', 'Safety Tips', 'Call to action', 'About','Feedback','Daily Alerts'],
            icons=['house-fill', 'person-circle', 'shield-fill', 'telephone-fill', 'info-circle-fill', 'chat-fill', 'bell-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"}, }

        )

    if app == "Home":
        home.app()
    if app == "Account":
        account.app()
    if app == "Safety Tips":
        safety.app()
    if app == 'Call to action':
        CTA.app()
    if app == 'About':
        about.app()
    if app == 'Feedback':
        feedback.app()
    if app == 'Daily Alerts':
        dailyalerts.app()


run()