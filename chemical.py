import streamlit as st

# Custom CSS for background image
background_style = """
    <style>
        body {
            background-color: #f0f2f6; /* Set background color */
        }
        .disaster-button {
            background-color: #4CAF50; /* Green background */
            border: none;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 30px;
            padding: 30px 60px;
            margin: 10px;
            cursor: pointer;
            border-radius: 10px;
            width: 300px;
            transition: all 0.4s;
        }
        .disaster-button:hover {
            background-color: #45a049; /* Darker green background on hover */
            transform: scale(1.1);
        }
    </style>
"""

# Display custom CSS
st.markdown(background_style, unsafe_allow_html=True)

# Title and description
st.title("Disaster Preparedness")
st.write("Explore information and safety measures for different types of disasters.")

# Dictionary mapping disaster names to image URLs
disaster_images = {
    "Earthquake": "earthquake.jpg",
    "Flood": "flood.jpg",
    "Hurricane": "https://example.com/hurricane_image.jpg",
    "Wildfire": "https://example.com/wildfire_image.jpg"
}

# Buttons for different types of disasters with images
for disaster, image_url in disaster_images.items():
    st.image(image_url, caption=disaster, width=300)