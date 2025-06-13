import streamlit as st
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Staff Age Difference Guessing Game",
    page_icon="🎂",
    layout="centered"
)

# Title and description
st.title("Staff Age Difference Guessing Game")
st.markdown("""
Guess the age difference between staff members! Fill out the form below to submit your guess.
""")

# Initialize session state for storing submissions if it doesn't exist
if 'submissions' not in st.session_state:
    st.session_state.submissions = []

staff_list = """
Aaron
Aditi
Alexey
Amy
Christina
Clara
Corrina
Daniel
Didde
Duncan
Ellie
John
Julian
Katelin
Lizette
Macy
Madison
Maureen
Nicola
Palak
Paz
Sarah
Tim
Vincent
Vishal"""
staff_list = staff_list.split("\n")

# Create the form
with st.form("age_difference_form"):
    # Staff member selection
    col1, col2 = st.columns(2)
    with col1:
        person_a = st.selectbox("Older Staff Member", staff_list)
    with col2:
        person_b = st.selectbox("Younger Staff Member", staff_list)
    
    # Age difference input
    age_difference = st.number_input(
        "Age Difference (in years)",
        min_value=0,
        max_value=10,
        help="Enter how many years older is the older person"
    )
    
    # Submit button
    submitted = st.form_submit_button("Submit Guess")
    
    if submitted:
        if person_a and person_b:
            # Create submission entry
            submission = {
                'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Older Staff Member': person_a,
                'Younger Staff Member': person_b,
                'Age Difference': age_difference
            }
            
            # Add to session state
            st.session_state.submissions.append(submission)
            
            # Show success message
            st.success("Your guess has been submitted!")
        else:
            st.error("Please enter both staff members' names!")

# Display submissions in a table
if st.session_state.submissions:
    st.subheader("Previous Submissions")
    df = pd.DataFrame(st.session_state.submissions)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Add download button for submissions
    df.rename(columns={'Timestamp':'timestamp',
                       'Older Staff Member':'older_staff_member',
                       'Younger Staff Member':'younger_staff_member',
                       'Age Difference':'age_difference'}, inplace=True)
    csv = df[['older_staff_member', 'younger_staff_member', 'age_difference']].to_csv(index=False)
    st.download_button(
        label="Download Submissions as CSV",
        data=csv,
        file_name="age_difference_guesses.csv",
        mime="text/csv"
    ) 