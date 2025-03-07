import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Streamlit UI setup
st.set_page_config(page_title="JD Generator", page_icon="📄", layout="centered")

st.title("📄 AI Job Description Generator")
st.markdown("### ✨ Generate a professional job description effortlessly!")

# Model initialization
llm = ChatOpenAI(model="o3-mini")

company_name = st.text_input("🏢 Company Name", placeholder="BuildFastWithAI")
# Job Title Input
st.subheader("Job Details")
job_title = st.text_input("🔹 Job Title", placeholder="e.g., Software Engineer")

# Required Skills Input
skills = st.text_area("🛠 Required Skills", placeholder="e.g., Python, TensorFlow, SQL")

# Experience Level Selection
experience = st.selectbox("🎓 Experience Level", ["Entry-level", "Mid-level", "Senior"], index=0)

# Responsibilities Input
responsibilities = st.text_area(
    "📌 Responsibilities", placeholder="e.g., Develop and maintain machine learning models"
)

# Preferred Qualifications Input
qualifications = st.text_area(
    "🎓 Preferred Qualifications", placeholder="e.g., Bachelor’s degree in Computer Science"
)

# Additional Details (Location & Salary)
st.subheader("Additional Details")
col1, col2 = st.columns(2)
with col1:
    location = st.text_input("📍 Location", placeholder="e.g., New York, Remote")
with col2:
    salary = st.text_input("💰 Salary (Optional)", placeholder="e.g., $80,000 - $120,000")



def generate_response(llm,title,skills,experience,responsibilites,qualification,location,salary,company_name):
    template="""You are a HR of a well reputated company . You have to prepare job description for the requirements of job profile for the {company_name} given below
                - The title of the job is {title} be sure to include relevent details from the title itself
                - The skills required for the job are {skills} so make a job description in such a way that applicants with these skills should apply
                - The experience level of the job should be {experience} years 
                - The responsibilities of the job are {responsibilites} so make sure to include these all these responsibilites in job profile
                - The qualification required for the job is {qualification} and it is located in {location} 
                - The expected salary for the applicant is {salary}
                also provide link to google form to submit application the link is www.googleform.com


    """
    output_parser = StrOutputParser()
    prompt=ChatPromptTemplate.from_messages([
           ("system", template)
       ])
    
    chain= prompt | llm | output_parser
    
    response = chain.invoke({"skills":skills,"title":title,"experience":experience,"responsibilites":responsibilites,"qualification":qualifications,"location":location,"salary":salary,"company_name":company_name})
    st.write(response)
# Submit button
if st.button("Generate Job Description 🚀"):
    if job_title and skills and experience and responsibilities:
        generate_response(llm,job_title,skills,experience,responsibilities,qualifications,location,salary,company_name)  # You will implement this function
    else:
        st.warning("Please fill in all required fields.")

# Footer
st.markdown("---")
st.markdown("🔹 *Powered by BuildFastWithAI❤️*")
