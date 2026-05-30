import streamlit as st
import pandas as pd


#st.write("Hello Boss! Testing 123...")

st.set_page_config(page_title="Realistic CG Calculator", page_icon="🎓")

if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'courses' not in st.session_state:
    st.session_state.courses = []
if 'show_input' not in st.session_state:
    st.session_state.show_input = False


if st.session_state.page == 'landing':
    st.markdown("<h1 style='text-align: center;'>🎓 Welcome to Realistic CG Calculator</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='text-align: center;'>Calculate your semester GPA easily and accurately.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start Calculation", use_container_width=True):
            st.session_state.page = 'calculator'
            st.rerun()


elif st.session_state.page == 'calculator':
    st.title("📊 Semester CGPA Calculator")
    st.write("---")

    if st.session_state.courses:
        st.subheader("Added Courses")
        df = pd.DataFrame(st.session_state.courses)
        df.index = df.index + 1
        st.table(df)

    if st.session_state.show_input:
        st.markdown("### 📝 Enter Course Details")
        with st.container(border=True): 
            c_name = st.text_input("Course Name (e.g., CSE 103)")
            c_title = st.text_input("Course Title (e.g., Discrete Mathematics)")
            
            col1, col2 = st.columns(2)
            with col1:
                c_gpa = st.number_input("Achieved GPA", min_value=0.0, max_value=4.0, step=0.01, format="%.2f")
            with col2:
                c_credit = st.number_input("Credit", min_value=0.5, step=0.5)
            
            if st.button("Done", type="primary"):
                if c_name and c_title: 
                
                    st.session_state.courses.append({
                        "Course Name": c_name,
                        "Course Title": c_title,
                        "GPA": c_gpa,
                        "Credit": c_credit
                    })
                    st.session_state.show_input = False
                    st.rerun()
                else:
                    st.error("Please fill in both Course Name and Course Title!")


    else:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Add Course", use_container_width=True):
                st.session_state.show_input = True
                st.rerun()
                
        with col2:

            if st.session_state.courses:
                if st.button("🧮 Calculate Result", use_container_width=True, type="primary"):
                    total_credits = sum(course["Credit"] for course in st.session_state.courses)
                    total_points = sum(course["Credit"] * course["GPA"] for course in st.session_state.courses)
                    
                    if total_credits > 0:
                        cgpa = total_points / total_credits
                        st.success(f" Your Semester CGPA is: **{cgpa:.2f}**")
                        st.balloons() 