import streamlit as st
import pandas as pd
import processing

Data_Base_Names = {
    "names": [
        'Bluewave Solutions Ltd',
        'SwiftPeak Technologies Inc',
        'Evergreen Ventures LLC',
        'CrystalEdge Innovations',
        'Lunar Horizon Enterprises',
        'Silverline Analytics',
        'Brightpath Consulting Group',
        'Vortex Dynamics Inc',
        'Aurora Nexus Holdings',
        'Ironclad Security Systems',
        'Crestline Developers Limited',
        'Nexon BioTech LLC',
        'VelvetStream Apparel Co',
        'UrbanOrbit Interiors',
        'Pioneer Energy Solutions',
        'StellarCore Technologies',
        'MapleCrest Foods LLC',
        'Quantum Ridge Consulting',
        'Oceanic Breeze Travel Co',
        'Timberland Industrial Supplies',
        'Zenith Health Partners',
        'AmberField Construction Group',
        'NextEra EcoWorks',
        'Fusion Point Media',
        'Skyline Horizons Inc',
        'Four Seasons'
    ],
}
Prohibited_Words = {
    "prohibited_words": ["bank", "police", "government", "unauthorized"],
}

df1 = pd.DataFrame(Data_Base_Names)
df2 = pd.DataFrame(Prohibited_Words)

# Streamlit application
st.header("NameSecure Pro")
st.markdown("### Problem Statement")
st.write("""
Organizations and businesses often struggle with validating and checking the availability of desired company names due to duplication, prohibited terms, or lack of contextually similar suggestions. This can lead to delays in registration, legal conflicts, and branding issues, especially when dealing with regulatory bodies.
""")

# Bold label for the input field
st.markdown("### Enter Company Name:")
st.caption("Check if your desired company name is unique, free of conflicts, and compliant with regulations in just a few seconds")
st.caption("Not sure where to start? Try these sample names: Four Seasons, Government of Technology, EcoWave Solutions")
user_input = st.text_input(
    "Enter company name",
    placeholder="Type the company name here",
    label_visibility="collapsed"
)
# Output field
st.markdown("### Result Section:")
if user_input.strip():
    result = processing.get_similarities(user_input, df1['names'].to_list())
    if "restricted word" in result:
        st.text_area(
            "Matching results",
            value=f"{result.split(".")[0]}. Could you please choose a different name?",
            label_visibility="collapsed"
        )
        st.markdown(f"<div style='color:red;'>{result.split(".")[1]} is prohibited word</div>", unsafe_allow_html=True)
    else:
        st.text_area(
            "Matching results",
            value=result,
            height=215,
            label_visibility="collapsed"
        )
else:
    st.warning("Please enter company name.")

st.markdown("#### Company Names Already in Use")
st.write("See the names our system has already identified as in use to ensure our system is functioning correctly and providing accurate results.")
# Display DataFrames side by side
col1, col2 = st.columns(2)
with col1:
    st.markdown("###### Here’s a list of company names already in use.")
    st.dataframe(df1, height=300)

with col2:
    st.markdown("###### Here’s a list of prohibited words.")
    st.dataframe(df2, height=300)
st.text("")
# Create two columns
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <p style="font-size: 20px; color: white;">Need Tailored Solution ?</p>
        <a href="https://clickchain.com" target="_blank" style="text-decoration: none;">
            <button style="background-color:  #1ebbeb; color: black; padding: 10px 20px; border: none; cursor: pointer; border-radius: 5px; font-size: 16px; font-weight:bold;">
                Connect with us
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)