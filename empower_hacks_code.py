import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random 
import time
import sqlite3
import os
# database creation to store username and password sign in information (along with additional user details) 
path_desktop = os.path.expanduser("~/Desktop") # determine where you want to store data table results (change this to desktop or any other place)
path_database = os.path.join(path_desktop, "data_v.db")
connection = sqlite3.connect(path_database) # create .db (database) file with any name. To access files with stored username and password, search for same file name on the device and opens on db browser for sqlite
con = connection.cursor() # to execute 

def usertable_creation(): 
	con.execute('CREATE TABLE IF NOT EXISTS table_user(username TEXT,password TEXT, uni_or_school TEXT, f_q1 TEXT, f_q2 TEXT, f_q3 TEXT, school_uni_name TEXT, grade_level TEXT, major_name TEXT)')

def adding_userdata(username,password, uni_or_school, f_q1, f_q2, f_q3, school_uni_name, grade_level, major_name): 
	con.execute('INSERT INTO table_user(username,password, uni_or_school, f_q1, f_q2, f_q3, school_uni_name, grade_level, major_name) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)',(username,password, uni_or_school, f_q1, f_q2, f_q3, school_uni_name, grade_level, major_name)) # con.execute inserts  a new row into the "userstable" with provided username and password values (inside columns)
	connection.commit() #  commit changes to the database 

def user_login(username,password):
	con.execute('SELECT * FROM table_user WHERE username =? AND password = ?',(username,password)) 
	final_data = con.fetchall() 
	return final_data #  function returns the retrieved data (matching rows)

def select_textbook_user_background(username_loggedin, password_loggedin):
     con.execute('SELECT uni_or_school, major_name FROM table_user WHERE username=? AND password = ?', (username_loggedin, password_loggedin))
     background_data = con.fetchall()
     return background_data 

def main():

    st.title("RESALE REVOLUTION")
    st.write("Acquire Knowledge, Not Wallets")
    
    options = ["Home", "Sign Up", "Login", "Gift Card", "About Us"]
    chosen_option = st.sidebar.selectbox("Main", options)

    if chosen_option == "Home":
        st.subheader("What is Resale Revolution (RR)? ")
        st.image("https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=aaron-burden-QJDzYT_K8Xg-unsplash.jpg", use_column_width=True, caption="Image of Books (Unsplash)")
        st.markdown("#### An issue that's often overlooked but significant is the additional cost of university and school supplies, which place a huge financial burden on students, particularly those from low-income backgrounds.")
        st.markdown("This project focuses on one of those supplies - textbooks.")
        st.markdown("##### **Resale Revolution or RR** is a web application that facilitates lending or borrowing & selling or purchasing of course textbooks, with some unique elements, to promote:")
        st.markdown("- Learning for **academic success**, unburdened by financial concerns")
        st.markdown("- A sense of **belonging** and community amongst low income students")
        st.markdown("- Resource **sharing** ")
        st.markdown("- Initiative to help by creating **incentives** such as an opportunity for senior low income students to receive gift cards to purchase food, clothes and supplies by increasing their 'rank' ")
        st.markdown("- Reduction in the **opportunity and time costs** of finding cost-effective and budget-friendly books in libraries or platforms")
        st.markdown("- And most importantly, help low income students feel **valued** in the community and have the ability to contribute")
        st.markdown("- **Reusing** textbooks and **reducing** waste (also lowering printing costs)")
        st.write("")
        st.write("Find out about current features on the signup page.")

    elif chosen_option == "Sign Up":
        st.subheader("Sign Up Here")
        st.image("https://media.giphy.com/media/SpopD7IQN2gK3qN4jS/giphy.gif", caption="GIF by Silgoweb (Giphy)")
        st.write("#### By clicking the button below to :blue[sign up] after inputting details, you can access many features, some of which currently include: ")
        with st.expander("##### Analytics"): 
             st.markdown("""
<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">
    Sellers: track how many books loaned/sold (that you do not require or use) and receive badges and ranks for good communication with borrower/buyer, good condition of books, generous lending periods, affordability ranks, increase your overall rank to improve your chances of receiving a gift card and most importantly, find out how many lives you impacted based on the number of books sold/lent!
</div>
""", unsafe_allow_html=True) 
             
             st.markdown("""
<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">
    Buyers: track how many gift cards sent (optional based on your financial situation), how much potential money saved by purchasing a textbook at a lower second-hand price or borrowing, and how many lives impacted through your gift cards. Additionally, purchase significantly low-priced and affordable textbooks or make use of flexible and generous lending periods for borrowing. Be part of a community of students from similar backgrounds and learn from senior students. 
</div>
""", unsafe_allow_html=True)
             st.write("") 
             st.write("Find out more about what gift cards are and their benefits on the gift card page.")

        with st.expander("##### Other Features"): 
             st.markdown("""
<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">
   ➟ Select Textbook: Find textbook matches based on users' backgrounds (eg: university or school and major). Obtain images and features of the selected textbook (including textbook condition) and then make a choice to either buy or borrow it. Option to also send virtual gift cards to sellers/lenders. <br>
   ➟ Message: Message other users about receiving books, meeting times, locations and more. Connect with senior university or school students for support and general help to create a sense of inclusivity. <br>
   ➟ Payment: Ability to connect to personal bank accounts, gift card providers and more. <br>
   ➟ Profile Settings: Find profile details such as financial information and questions answered during signup. <br> 
   ➟ Ratings & Reviews: Leave ratings and constructive feedback on the seller's services, contributing to the seller's overall rank.  
</div>
""", unsafe_allow_html=True)
             st.write("") 

        user_name = st.sidebar.text_input("Please input a user name")
        password = st.sidebar.text_input("Please input a password", type='password')
        uni_or_school = st.sidebar.text_input("Input 'u' if in university, or 's' if in school", type='password') 
        if uni_or_school.lower() == "u":
            university_name = st.sidebar.text_input("Name of university (choose a/b)")
            study_year = st.sidebar.text_input("Which year are you in? (choose either 1, 2 or 3)")
            major_u = st.sidebar.text_input("What is your major (choose either 'stem' or 'humanities')")
        elif uni_or_school.lower() == "s":
            school_name = st.sidebar.text_input("Name of school (choose a/b)")
            study_grade = st.sidebar.text_input("What grade are you in? (choose either 10, 11 or 12)")
            major_s = st.sidebar.text_input("What class are you currently taking (choose either 'ap physics' or 'ap literature')")
        
        st.sidebar.text("Financial status: ")
        f_q1 = st.sidebar.text_input("Are either of your parents earning an income higher than U.S $14850 anually? (y/n)") 
        f_q2 = st.sidebar.text_input("Have either of your parents obtained an education beyond high school (y/n)? ")
        f_q3 = st.sidebar.text_input("My parents or I am able to set aside a specific amount monthly after university, utility, medical and other essential payments that goes into savings (y/n)? ")
        # more questions can be added if needed 
        
        st.write("") 

        if st.button("Sign Up"): 
            usertable_creation() # create table once user clicks sign up
            if uni_or_school.lower() == "u":
                 adding_userdata(user_name, password, uni_or_school, f_q1, f_q2, f_q3, university_name, study_year, major_u) 
            elif uni_or_school.lower() == "s": 
                 adding_userdata(user_name, password, uni_or_school, f_q1, f_q2, f_q3, school_name, study_grade, major_s)
            st.success(f"You signed up as {user_name} successfully!")
            st.info("Select the 'Login' option in the main tab to login.")

    elif chosen_option == "Login":
        st.subheader("Login Here")
        user_name_log = st.sidebar.text_input("Please input a user name")
        password_log = st.sidebar.text_input("Please input a password", type='password')

        if st.sidebar.checkbox("Login"): 
            usertable_creation()
            login_results = user_login(user_name_log, password_log)  
            
            if login_results: 
                st.success(f"You logged in as {user_name_log} successfully!")
                log_options = ["Profile Settings", "Select Textbook", "Message", "Payment", "Analytics", "Ratings & Reviews"]
                login_options = st.selectbox("Login Options", log_options)
            
                if login_options == "Profile Settings":
                    signup_profile_results = user_login(user_name_log, password_log)
                    
                    columns_from_sql = ["Username", "Password", "Uni/School", "FinanceQ1", "FinanceQ2", "FinanceQ3", "Uni/School Name", "Year of Study", "Major"]
                    change_to_df = pd.DataFrame(signup_profile_results, columns=columns_from_sql)
                    
                    st.markdown("<hr>", unsafe_allow_html=True)
                    st.image("https://images.unsplash.com/photo-1542042179-de5cdc0cf242?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=nathan-dumlao-lot-86rAZZk-unsplash.jpg", use_column_width=True, caption="Person (Unsplash)")

                    finance_columns = ["FinanceQ1", "FinanceQ2", "FinanceQ3"]
                    w_f_columns = ["Username", "Password"]
                    uni_columns = ["Uni/School", "Uni/School Name", "Year of Study", "Major"]
                    for col in w_f_columns:
                         with st.expander(f":arrow_forward: **{col}**"):
                              st.write(f"{change_to_df[col].item()}")
                    
                    with st.expander(f":arrow_forward: **University or School Related**"):
                         st.write("**University ('u'), School ('s')**") 
                         st.write("**University or School Names ('a' or 'b')**") 
                         for colu in uni_columns:
                              st.write(f"For the question related to **'{colu}'**, your response was **'{change_to_df[colu].item()}'**") 
                         
                    with st.expander(f":arrow_forward: **Finance**"):
                         st.write("**No ('n'), Yes ('y')**")
                         for i, cols in enumerate(finance_columns):
                              st.write(f"For finance **question {i+1}**, your response was **'{change_to_df[cols].item()}'**") 
                         
                    # st.dataframe(change_to_df) - if needed to print as a dataframe 

                elif login_options == "Select Textbook":
                    st.subheader("Select a Textbook")
                    
                    st.write("These are the books that our current users are lending/selling (either select the top right of the table to expand, or scroll the table columns horizontally): ")
                    textbooks_list = {"Book Number": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], 
                                      "Textbook Name": ["Introductory Econometrics", "Engineering Mathematics", "AP English Literature and Composition", "College Physics for AP Courses", "Principles of Biochemistry", "Multivariable Calculus with Mathematica", "History of the World", "Introduction to Formal Philosophy", "AP Physics 1", "AP Physics C Prep", "The Great Gatsby", "High School English Grammar and Composition"],
                                      "Image Link": ["https://m.media-amazon.com/images/I/410qHCkvOrL._SX393_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51GtO94mqlL._SX382_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51CpuQDnQ5L._SY264_BO1,204,203,200_QL40_ML2_.jpg", "https://m.media-amazon.com/images/I/41mLeGRMz1L._SX384_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51S8Bgm9FmL._SX388_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51Q6SYmearL._SX323_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/416jy4tPEaL._SX329_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51aO1ppCGrL._SX331_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51GpHS+kz7L._SX258_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51OOxWobxuL._SX198_BO1,204,203,200_QL40_ML2_.jpg", "https://m.media-amazon.com/images/I/41EYmJwqnIL._SY264_BO1,204,203,200_QL40_ML2_.jpg", "https://m.media-amazon.com/images/I/41OjKBKlLCL._SX353_BO1,204,203,200_.jpg"],
                                      "Buy/Borrow": ["bu", "bo", "bu", "bo", "bo", "bu", "bo", "bu", "bo", "bu", "bo", "bu"],
                                      "Texbook Condition": ["New", "Average", "Best", "Average", "New", "Average", "Best", "Best", "New", "New", "Average", "Average"],
                                      "Username": ["abbie", "jackie1", "matt76", "03julie", "02hollie4", "john", "susanna", "bethany4", "ger", "finneas", "ed", "eddie"],
                                      "Uni/School Level": ["u", "u", "s", "s", "u", "u", "u", "u", "s", "s", "s", "s"],
                                      "Uni/School Name": ["a", "b", "b", "a", "a", "b", "a", "a", "b", "a","b", "b"], 
                                      "Main Subject": ["humanities", "stem", "ap literature", "ap physics", "stem", "stem", "humanities", "humanities", "ap physics", "ap physics", "ap literature", "ap literature"], 
                                      "Year Level": ["Year 2", "Year 1", "Grade 11", "Grade 11", "Year 1", "Year 1", "Year 1", "Year 2", "Grade 11", "Grade 12", "Grade 10", "Grade 11"],
                                      "Cost U.S$": ["35", "NA", "20", "NA", "NA", "10", "NA", "81", "NA", "14", "NA", "23"],
                                      "Borrowing period in days": ["NA", "15", "NA", "60", "75", "NA", "45", "NA", "56", "NA", "29", "NA"]}
                    
                    textbooks_df = pd.DataFrame(textbooks_list)      
                    columns_to_display_df = textbooks_df.drop(columns=["Image Link"]) 
                    st.dataframe(columns_to_display_df) # display a new dataframe without the image link column only
                    
                    # get logged in user information to match with dataframe seller's university or school level book and main subject/major
                    user_info = select_textbook_user_background(user_name_log, password_log) 
                    buyer_uni = user_info[0][0]
                    buyer_major = user_info[0][1]

                    background_of_buyer = st.text_input(":sparkles: Enter :blue['y' and select 'FIND MATCHES'] to receive book recommendations that match your background and profile (whether you are in university/school and what major/subject you're studying): ")
                    search_button_buyer = st.button("Find Matches")
                    textbooks_df_filtered = textbooks_df[(textbooks_df["Uni/School Level"] == buyer_uni) & (textbooks_df["Main Subject"] == buyer_major)] 
                    
                    if background_of_buyer == "y" and search_button_buyer:
                         st.write("Sellers are selling the following books that match your background and profile: ")
                         display_textbooks_df_filtered = textbooks_df_filtered.drop(columns=["Image Link"]) 
                         st.dataframe(display_textbooks_df_filtered)

                    else:
                         st.write("Sorry, please enter 'y' and then select 'FIND MATCHES'.") 
                    
                    buy_or_borrow = st.text_input(":sparkles: Enter :blue['bo'] if you would like to borrow (bo) or :blue['bu'] to buy a book")
                    
                    if buy_or_borrow == "bo": 
                              # display only bo books: 
                              bo_textbooks_df_filtered = textbooks_df_filtered[textbooks_df_filtered["Buy/Borrow"] == "bo"] 
                              # sorting data from most to least number of borrowing days:
                              st.write("Final books list sorted from most to least lending period in days: ")
                              sorted_bo_textbooks_df_filtered = bo_textbooks_df_filtered.sort_values(by="Borrowing period in days", ascending=False)
                              display_sorted_bo_textbooks_df_filtered = sorted_bo_textbooks_df_filtered.drop(columns=["Image Link"])
                              st.dataframe(display_sorted_bo_textbooks_df_filtered)
                              
                              # ask for chosen book: 
                              bo_book_numbers = sorted_bo_textbooks_df_filtered["Book Number"].tolist() 
                              bo_chosen_book = st.text_input("From the above, please choose the book number you would like to purchase")
                              if bo_chosen_book: 
                                   if bo_chosen_book in bo_book_numbers and bo_chosen_book.isnumeric():  
                                        bo_chosen_row_index = sorted_bo_textbooks_df_filtered.index[sorted_bo_textbooks_df_filtered['Book Number'] == bo_chosen_book]

                                        image_reference_link = sorted_bo_textbooks_df_filtered.loc[bo_chosen_row_index, 'Image Link'].item()
                                        image_reference_link = str(image_reference_link) 

                                        with st.expander(f"Details of '{sorted_bo_textbooks_df_filtered.loc[bo_chosen_row_index, 'Textbook Name'].item()}'"): 
                                             st.image(image_reference_link, use_column_width = True, caption = "Textbook Image") 
                                             st.markdown("**FEATURES**")
                                             st.markdown(f"""
                                        <div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;"> 
                                        Textbook condition: {sorted_bo_textbooks_df_filtered.loc[bo_chosen_row_index, 'Texbook Condition'].item()} <br> 
                                        Lender: {sorted_bo_textbooks_df_filtered.loc[bo_chosen_row_index, 'Username'].item().title()} <br> 
                                        Return by: {sorted_bo_textbooks_df_filtered.loc[bo_chosen_row_index, 'Borrowing period in days'].item()} days <br> 
                                        Year level: {sorted_bo_textbooks_df_filtered.loc[bo_chosen_row_index, 'Year Level'].item()} <br>
                                        </div>
                                        """, unsafe_allow_html=True)  
                                             st.write("")
                                             if st.button("Borrow"): 
                                                  st.success("Thanks for borrowing!")
                                   else:
                                        st.write("Sorry, please input a valid number in the above books list.") 
                                             
                    elif buy_or_borrow == "bu": 
                         # display only bu books
                         bu_textbooks_df_filtered = textbooks_df_filtered[textbooks_df_filtered["Buy/Borrow"] == "bu"] 
                         # sorting data from most to least number of borrowing days:
                         st.write("Final books list sorted from least to highest prices: ")
                         sorted_bu_textbooks_df_filtered = bu_textbooks_df_filtered.sort_values(by="Cost U.S$")
                         display_sorted_bu_textbooks_df_filtered = sorted_bu_textbooks_df_filtered.drop(columns=["Image Link"])
                         st.dataframe(display_sorted_bu_textbooks_df_filtered)
                         
                         # ask for chosen book: 
                         bu_book_numbers = sorted_bu_textbooks_df_filtered["Book Number"].tolist() 
                         bu_chosen_book = st.text_input("From the above, please choose the book number you would like to purchase")
                         if bu_chosen_book:
                              if bu_chosen_book in bu_book_numbers and bu_chosen_book.isnumeric(): 
                                   bu_chosen_row_index = sorted_bu_textbooks_df_filtered.index[sorted_bu_textbooks_df_filtered['Book Number'] == bu_chosen_book]
                                   bu_image_reference_link = sorted_bu_textbooks_df_filtered.loc[bu_chosen_row_index, 'Image Link'].item()
                                   bu_image_reference_link = str(bu_image_reference_link) 
                              
                                   with st.expander(f"Details of '{sorted_bu_textbooks_df_filtered.loc[bu_chosen_row_index, 'Textbook Name'].item()}'"): 
                                    st.image(bu_image_reference_link, use_column_width = True, caption = "Textbook Image") 
                                    st.markdown("**FEATURES**")
                                    st.markdown(f"""
                                        <div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;"> 
                                        Textbook condition: {sorted_bu_textbooks_df_filtered.loc[bu_chosen_row_index, 'Texbook Condition'].item()} <br> 
                                        Lender: {sorted_bu_textbooks_df_filtered.loc[bu_chosen_row_index, 'Username'].item().title()} <br> 
                                        Cost: U.S$ {sorted_bu_textbooks_df_filtered.loc[bu_chosen_row_index, 'Cost U.S$'].item()} <br> 
                                        Year level: {sorted_bu_textbooks_df_filtered.loc[bu_chosen_row_index, 'Year Level'].item()} <br>   
                                        </div>
                                        """, unsafe_allow_html=True)  
                                    st.write("")
                                    if st.button("Purchase"): 
                                        st.success("Thanks for purchasing!")
                                    st.write("Include this option: Would you like to send a gift card? (y/n)")
                                    st.markdown("Based on users' response, insert a slider to choose the dollar amount for the gift card: ")
                                    output_slider_bu = st.slider("Choose an amount (U.S$):", min_value=5, max_value=100, value=25) 
                                    st.write(f"Great, you chose U.S$ {output_slider_bu}.")
                                    st.markdown("Include feature to connect to Paypal/banking accounts and add giftcard value and book price value as applicable.") 
                              else:
                                   st.write("Sorry, please input a valid number in the above books list.")
                    else:
                        st.write("Sorry, please enter either 'bu' or 'bo'.")  
                    st.write("")

                elif login_options == "Message":
                    st.subheader("Message other students (sellers/lenders)")
                    st.write("This page can include user profiles of lenders/sellers")
                    st.image("https://media.giphy.com/media/fKqBFh5pebTrycP2wo/giphy.gif")
                    st.write(":arrow_forward: Message other users on receiving books, meeting times, locations and more") 
                    st.write(":arrow_forward: Connect with other university students and mentors for support and help") 
                    st.write(":arrow_forward: Creating of a sense of inclusivity") 

                elif login_options == "Payment":
                    st.subheader("Payment")
                    st.write("This page is not fully developed yet. However, potential ideas for this section could include: ")
                    st.write(":arrow_forward: Ability to connect to multiple bank accounts, Paypal and others")
                    st.write(":arrow_forward: Connection to personal accounts for gift card providers such as Simon")
                    st.write(":arrow_forward: Link from 'Select Textbook' page to this page after selecting 'Purchase'")
                    st.write(":arrow_forward: And much more!")

                elif login_options == "Analytics":
                    months_list = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

                    st.subheader("Gift Cards")
                    random_no = random.randint(2,12) 
                    st.write(f"You sent :blue[{random_no}] gift cards! :sparkles:") 
                
                    st.subheader("Money Saved")
                    st.write("Here are your savings over the months (comparison made to current same textbook costs) [using arbitrary values currently]: ") 

                    data_values = {'Months': months_list,
                                   'Savings': [50,30,20,70,90,100,23,43,23,11,10,9]}
                    
                    numerical_months = [np.arange(1,13,1)] # numerical version of month names (jan = 1 and so on)
                    data_df = pd.DataFrame(data_values, index=numerical_months)
                    specific_slider_value = st.select_slider("Choose a month: ", options = months_list) 
                    savings_index_corresp_to_slidervalue = data_df.index[data_df['Months'] == str(specific_slider_value)]
                    st.write(f"You saved U.S$:blue[{data_df.loc[savings_index_corresp_to_slidervalue, 'Savings'].item()}]!") 

                    # display line graph:
                    plt.style.use('ggplot') 
                    plt.figure(figsize=(8,6))
                    plt.plot(data_df["Months"], data_df["Savings"])
                    plt.xlabel('Months (January to December)')
                    plt.ylabel('Savings')
                    plt.title('Money Saved Over Time')
                    plt.scatter(specific_slider_value, data_df.loc[savings_index_corresp_to_slidervalue, 'Savings'], color='black', marker='o', label='Selected Point')
                    plt.legend()
                    st.pyplot(plt)

                    st.subheader("Accomplishment Showcase - Badges & Honours :trophy:") 
                    badges_data = {"ACCOMPLISHMENTS": ["Gift Card Streak", "Jan. Month Money Saver"], 
                                   "BADGES": ["🎖️", "📛"]} 
                    badges_df = pd.DataFrame(badges_data, index=[1,2])
                    st.dataframe(badges_df)

                    st.subheader(f"Lives Impacted: :blue[{random_no}]") 
                    link_of_pic = "https://images.unsplash.com/photo-1454923634634-bd1614719a7b?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=timon-studler-ABGaVhJxwDQ-unsplash.jpg"
                    st.image(link_of_pic, use_column_width = True, caption = "People Walking (Unsplash)")

                    st.markdown("Note: Analytics would look different if the user is a lender/seller.")

                elif login_options == "Ratings & Reviews":
                     textbooks_list_r = {"Book Number": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], 
                                      "Textbook Name": ["Introductory Econometrics", "Engineering Mathematics", "AP English Literature and Composition", "College Physics for AP Courses", "Principles of Biochemistry", "Multivariable Calculus with Mathematica", "History of the World", "Introduction to Formal Philosophy", "AP Physics 1", "AP Physics C Prep", "The Great Gatsby", "High School English Grammar and Composition"],
                                      "Image Link": ["https://m.media-amazon.com/images/I/410qHCkvOrL._SX393_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51GtO94mqlL._SX382_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51CpuQDnQ5L._SY264_BO1,204,203,200_QL40_ML2_.jpg", "https://m.media-amazon.com/images/I/41mLeGRMz1L._SX384_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51S8Bgm9FmL._SX388_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51Q6SYmearL._SX323_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/416jy4tPEaL._SX329_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51aO1ppCGrL._SX331_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51GpHS+kz7L._SX258_BO1,204,203,200_.jpg", "https://m.media-amazon.com/images/I/51OOxWobxuL._SX198_BO1,204,203,200_QL40_ML2_.jpg", "https://m.media-amazon.com/images/I/41EYmJwqnIL._SY264_BO1,204,203,200_QL40_ML2_.jpg", "https://m.media-amazon.com/images/I/41OjKBKlLCL._SX353_BO1,204,203,200_.jpg"],
                                      "Buy/Borrow": ["bu", "bo", "bu", "bo", "bo", "bu", "bo", "bu", "bo", "bu", "bo", "bu"],
                                      "Texbook Condition": ["New", "Average", "Best", "Average", "New", "Average", "Best", "Best", "New", "New", "Average", "Average"],
                                      "Username": ["abbie", "jackie1", "matt76", "03julie", "02hollie4", "john", "susanna", "bethany4", "ger", "finneas", "ed", "eddie"],
                                      "Uni/School Level": ["u", "u", "s", "s", "u", "u", "u", "u", "s", "s", "s", "s"],
                                      "Uni/School Name": ["a", "b", "b", "a", "a", "b", "a", "a", "b", "a","b", "b"], 
                                      "Main Subject": ["humanities", "stem", "ap literature", "ap physics", "stem", "stem", "humanities", "humanities", "ap physics", "ap physics", "ap literature", "ap literature"], 
                                      "Year Level": ["Year 2", "Year 1", "Grade 11", "Grade 11", "Year 1", "Year 1", "Year 1", "Year 2", "Grade 11", "Grade 12", "Grade 10", "Grade 11"],
                                      "Cost U.S$": ["35", "NA", "20", "NA", "NA", "10", "NA", "81", "NA", "14", "NA", "23"],
                                      "Borrowing period in days": ["NA", "15", "NA", "60", "75", "NA", "45", "NA", "56", "NA", "29", "NA"]}
                    
                     textbooks_df_ratings = pd.DataFrame(textbooks_list_r)
                     st.subheader("Rate your lender and provide constructive feedback! ")
                     user_rate = st.text_input("Who would you like to rate from users under 'Select Textbook'?")
                     usernames_list = textbooks_df_ratings["Username"].tolist()
                     if user_rate: # once user inputs username 
                          if user_rate.lower() in usernames_list: 
                               rating_no = st.text_input(f"Please rate {user_rate.title()} on a scale of 1 (Below Average) to 5 (Excellent)")
                               if rating_no.isnumeric(): 
                                    if 1 <= int(rating_no) <= 5:
                                         rating_feedback = st.text_input(f"Please provide constructive feedback for {user_rate.title()}")
                                         if rating_feedback: 
                                              time.sleep(1)
                                              st.success(f"{user_rate.title()} just received a rating of {rating_no} with feedback!")
                                    else:
                                         st.write("Sorry, please input a valid rating.")   
                               else:
                                    st.write("Please input a numeric value")                  

                          else:
                               st.warning("Sorry, please input a valid user.")
                    
                     st.markdown("All ratings are anonymous.")
                     st.markdown("Based on ratings, sellers/lenders increase their chances of receiving a gift card and increasing profile rank.")
                     st.markdown("Extensions: store ratings and provide recommendations for users of highly-ranked sellers/lenders.")
                          
            else:
                st.warning("Sorry, incorrect username or password.")

    elif chosen_option == "Gift Card":
         st.subheader("Gift Card")
         st.image("https://adc3ef35f321fe6e725a-fb8aac3b3bf42afe824f73b606f0aa4c.ssl.cf1.rackcdn.com/giftcard/hero-images/Multicard_Slider_MC_Desktop.jpg", use_column_width=True, caption="Simon Mall Gift Cards (simon.com website img)")
         st.write("A unique feature of this project is the introduction of gift cards.")
         st.write("When (and if) a buyer or borrower from a low income background is in a financially able position after using the web app to save costs, they have an option to send virtual gift cards (of any value) to high-ranked senior (higher grade/university year) low income (and some higher income) lenders.")
         st.write("The process is as follows: ")
         st.write(":arrow_forward: Users declare their financial status when signing up (this is confidential)")
         st.write(":arrow_forward: When low income buyers/borrowers purchase or borrow a book, they are matched with highly-ranked senior sellers of similar or higher economic status (particularly low income) selling/lending the same book")
         st.write(":arrow_forward: Buyers have the option to not only pay for or borrow the second-hand book but also send an optional virtual gift card to the seller/lender")
         st.write(":arrow_forward: This gift card can be used by the senior low income seller/lender to purchase food, supplies and more at select stores")
         st.write("")
         st.write("An example of a very useful gift card that borrowers or buyers can send is the Simon gift card, which will allow other low income students (sellers or lenders) to purchase clothes, food, back-to-school supplies, and more. Any alternative local provider can also be used.")

    elif chosen_option == "About Us":
        st.subheader("About Us")
        st.write("Please see the 'Home' and 'Sign Up' pages for information on what this project is about and what features are present.")
        st.write("#### The prompt for this project held by Empower Hacks is: ")
        st.write("Create software that addresses an issue in first generation low income students such as: financial planning, career opportunities, mental health, community building, or an issue found in your community.")

if __name__ == '__main__':
    main()

