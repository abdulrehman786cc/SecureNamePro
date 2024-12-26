import streamlit as st
import pandas as pd
from networkx.generators.harary_graph import hkn_harary_graph

import processing

Data_Base_Names = {
    "Names": [
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
    "Prohibited Words": ["Bank", "Police", "Government", "Unauthorized"],
}

df1 = pd.DataFrame(Data_Base_Names)
df2 = pd.DataFrame(Prohibited_Words)

st.markdown("""
<h1 style="text-align: center;">NameSecure Pro</h1>
<hr style="border: 1px solid #ccc;">
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.text("")
    st.markdown("""
        <h5 font-family: 'Noto Sans', sans-serif;">
            An AI-driven search engine designed to help organizations validate, suggest and ensure the availability of company names.
        </h5>
        """, unsafe_allow_html=True)

with col2:
    st.image("logo.jpg",width=350)
st.markdown("""
<div style="text-align: justify;">
This showcases the capabilities of solving real-world problems with AI for legacy systems. Through this use case, we demonstrate:
<ul>
    <li><strong>AI Integration:</strong> How artificial intelligence can automate and enhance processes, such as validation and conflict detection, in your legacy systems.</li>
    <li><strong>Real-Time Insights:</strong> The ability to provide instant feedback and actionable suggestions based on data.</li>
    <li><strong>Scalable Solutions:</strong> Developing tailored AI-driven tools like NameSecure Pro to address specific business needs.</li>
</ul>
</div>
""", unsafe_allow_html=True)


st.markdown("### Problem Statement:")
st.markdown("""
<p style="text-align: justify;">Organizations and businesses often struggle with validating and checking the availability of desired company names due to duplication, prohibited terms, or lack of contextually similar suggestions. This can lead to delays in registration, legal conflicts, and branding issues, especially when dealing with regulatory bodies.</p>
""",unsafe_allow_html=True)
st.markdown("### Solution:")
st.markdown("""
<p style="text-align: justify;">NameSecure Pro is a solution designed to help organizations and businesses quickly validate and verify the availability of desired company names. 
It identifies conflicts, duplicates, prohibited terms, and contextual similarities in real time. 
Additionally, the system provides alternative name suggestions, ensuring regulatory compliance and uniqueness.</p>
""",unsafe_allow_html=True)

st.markdown("## Try It:")
st.image("workflow.png")
st.markdown("#### Enter Company Name:")
st.markdown(""" <p style="text-align: justify;">Check if your desired company name is unique, free of conflicts, and compliant with regulations in just a few seconds.</p>""",unsafe_allow_html=True)
st.write(""" <p style="text-align: justify;">Not sure where to start? Try these sample names: Four Seasons, Government of Technology, EcoWave Solutions.</p>""",unsafe_allow_html=True)
user_input = st.text_input(
    "Enter company name",
    placeholder="Type the company name here",
    label_visibility="collapsed"
)

st.markdown("#### Result Section:")
if user_input.strip():
    result = processing.get_similarities(user_input, df1['Names'].to_list())
    if "prohibited word" in result:
        st.text_area(
            "Matching results",
            value=f"{result.split(".")[0]}. Could you please choose a different name?",
            height=68,
            label_visibility="collapsed"
        )
        st.markdown(f"<div style='color:red;'>{result.split(".")[1]} is prohibited word</div>", unsafe_allow_html=True)
        st.write("")
    else:
        st.text_area(
            "Matching results",
            value=result,
            height=215,
            label_visibility="collapsed"
        )
else:
    st.warning("Please enter company name.")

st.markdown("##### Company Names Already in Use")
st.markdown(""" <p style="text-align: justify;">See the names our system has already identified as in use to ensure our system is functioning correctly and providing accurate results.</p>""",unsafe_allow_html=True)
# Display DataFrames side by side
col1, col2 = st.columns(2)
with col1:
    st.markdown("###### Here’s a list of company names already in use.")
    st.dataframe(df1, height=300, width=300)

with col2:
    st.markdown("###### Here’s a list of prohibited words.")
    st.dataframe(df2, height=300,width=300)

st.subheader("What Can We Do for You?")
st.markdown("""
We specialize in leveraging AI to modernize and optimize legacy systems. If you have specific pain points or challenges in integrating AI into your systems, we’d be happy to explore:
- How our expertise can help solve them.
- How to adapt solutions like NameSecure Pro to meet your needs.
""")
st.text("")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    st.write("Need Tailored Solution?")
    st.markdown(
        """
        <div>
            <a href="https://www.linkedin.com/company/clickchain/" target="_blank" style="text-decoration: none;">
                <button style="background-color:  #1ebbeb; color: black; padding: 10px 20px; border: none; cursor: pointer; border-radius: 5px; font-size: 16px; font-weight:bold;">
                    Connect with us
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.write("")
