import streamlit as st
from PIL import Image
import pickle

# Loading the model
with open('s_model.pkl', 'rb') as file:
   model = pickle.load(file)
img = Image.open('imag.png')
img = img.resize((156,145))
st.image(img,use_column_width=(100,40),output_format='GIF')
def predict():
   st.title("Bank Loan Approval Prediction")

   # File Upload for Image
   uploaded_image = st.file_uploader("Upload Your Photo", type=['png', 'jpg', 'jpeg'])

   if uploaded_image is not None:
       img = Image.open(uploaded_image)
       st.image(img, use_column_width=False)

   # Input Fields
   st.header("Loan Application Details")
   a_c = st.text_input("Account Number")
   name = st.text_input("Enter Name")

   gen_display = {'Male': 1, 'Female': 0}
   gen = st.selectbox("Gender", list(gen_display.keys()))
   selected_gender = gen_display[gen]

   mar_dis = {'No':0, 'Yes':1}
   mar_opt = st.selectbox("Married", list(mar_dis.keys()))
   mar = mar_dis[mar_opt]

   edu_dis = {'Not Graduate':0, 'Graduate':1}
   edu_opt = st.selectbox("Education", list(edu_dis.keys()))
   edu = edu_dis[edu_opt]

   emp_dis = {'Yes': 1.0, 'No':0.0}
   emp_opt = st.selectbox("Self-Employed", list(emp_dis.keys()))
   emp = emp_dis[emp_opt]

   app_income = st.number_input("Applicant's Income")
   c_app_income = st.number_input("Co-Applicant's Income")
   l_amt = st.number_input("Loan Amount")
   l_dr = st.number_input('Loan Amount Term')
   c_his = st.slider("Credit History", 0.0, 1.0, step=0.1)
   p_area = st.slider("Property Area", 0, 1000, step=1)

   # Prediction Button
   if st.button("Check Loan Eligibility"):
       features = [[selected_gender, mar, edu, emp, app_income, c_app_income, l_amt, l_dr, c_his, p_area]]
       prediction = model.predict(features)
       if prediction == 0:
           st.error(f"Hey {name}, your account number {a_c} is found to be non-eligible for the specified loan")
       else:
           st.success(f"Hey {name}, your account number {a_c} is found to be eligible for the specified loan\nFurther steps will be directed to receive the money")

predict()
