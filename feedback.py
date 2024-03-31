import streamlit as st

def app():
    st.title("Feedback Form")
    st.write("We appreciate your feedback on our application!")

    # Rating selection
    rating_label = "Rate your experience (1-5 stars):"
    rating = st.selectbox(rating_label, options=range(1, 6))

    # Feedback text area
    feedback_text = st.text_area("Please share your feedback:", height=100)

    # Checkbox for specific issue reporting
    issue_box_label = "Are you reporting a specific issue?"
    issue_box = st.checkbox(issue_box_label)

    # Text area for specific issue details (conditionally displayed)
    if issue_box:
        issue_details = st.text_area("Please describe the issue:", height=100)
    else:
        issue_details = None

    # Submit button
    submit_button = st.button("Submit Feedback")

    # Handle form submission (logic for processing feedback goes here)
    if submit_button:
        st.success("Thank you for your feedback!")