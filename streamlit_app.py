import streamlit as st
import pandas as pd

# Load the dataset for Page 2
file_path = "tab3_importance.csv"
df = pd.read_csv(file_path)

# Sidebar navigation for multi-page functionality
page = st.sidebar.radio("Navigate to:", ["Questionnaire", "Interactive Table"])

# ---------------------------- PAGE 1: Questionnaire ----------------------------
if page == "Questionnaire":
    # Page title
    st.title("Questionnaire")

    # Gender Selection
    st.header("Gender")
    gender = st.radio("Select your gender:", ["Male", "Female"])

    # Teaching Context
    st.header("Teaching Context")
    teaching_levels = ["University", "Secondary school","Elementary school", "Language school", "Private practice"]
    selected_levels = [level for level in teaching_levels if st.checkbox(level)]

    # Teaching Experience
    st.header("Teaching Experience")
    experience = st.radio("Select your teaching experience:", 
                          ["Less than 1 year", "1 to 4 years", "5 to 9 years", "More than 10 years"])

    st.markdown("<hr>", unsafe_allow_html=True)

    # Rating Instructions
    st.subheader("Please rate each strategy on a 7-point scale:")
    st.markdown(
    """
    <p style='font-size:32px; background-color: yellow; padding: 10px; border-radius: 5px;'>
    <b>1</b> = not important<br>
    <b>2</b> = slightly important<br>
    <b>3</b> = somewhat important<br>
    <b>4</b> = moderately important<br>
    <b>5</b> = important<br>
    <b>6</b> = quite important<br>
    <b>7</b> = very important
    </p>
    """,
    unsafe_allow_html=True
)

    # Rating Table
    strategies = [
        "Prepare for the lessons properly.",
        "Show a good example by being committed and motivated.",
        "Try to behave naturally and be yourself in class.",
        "Be as sensitive and accepting as you can.",
        "Create a pleasant atmosphere in the classroom.",
        "Bring in humor, laughter, and smiles.",
        "Have games and fun in class.",
        "Give clear instructions.",
        "Provide guidance about how to do the task.",
        "Give positive feedback and appraisal.",
        "Constantly encourage your students.",
        "Make tasks challenging to involve your students.",
    ]

    # Initialize the ratings dictionary
    ratings = {}

    for i, strategy in enumerate(strategies):
        st.markdown(f"<p style='font-size: 24px; font-weight: bold;'>{strategy}</p>", unsafe_allow_html=True)
        ratings[strategy] = st.radio(
            "",  # Empty label removes duplicate text
            options=[1, 2, 3, 4, 5, 6, 7],
            index=3,  # Default to Moderately Important (index 3 = value 4)
            horizontal=True,
            key=f"rating_{i}"  # Unique key for each radio button
        )

    # Display the results when the user submits
    if st.button("Submit"):
        st.subheader("Your Responses:")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Teaching Context:** {', '.join(selected_levels) if selected_levels else 'None'}")
        st.write(f"**Teaching Experience:** {experience}")
        st.subheader("Ratings:")
        for strategy, rating in ratings.items():
            st.write(f"- {strategy}: **{rating}**")

# ---------------------------- PAGE 2: Interactive Table ----------------------------
elif page == "Interactive Table":
    st.title("Interactive Importance Table")

    # Filter by Scale
    unique_scales = df["Scale"].unique()
    selected_scale = st.multiselect("Filter by Scale:", unique_scales, default=unique_scales)

    # Apply filter
    filtered_df = df[df["Scale"].isin(selected_scale)]

    # Display filtered table
    st.dataframe(filtered_df, use_container_width=True)
