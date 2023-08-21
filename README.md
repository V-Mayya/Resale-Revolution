# Resale-Revolution
**Empower Hacks Hackathon Submission** 

--- 
<img src="Images/thumbnail.png" width="500" height="270" />

‣ **Main Idea**: Web application that facilitates lending/borrowing & selling/purchasing of course textbooks, with some unique elements (involving gift cards, tracking analytics and more), to promote: 
- Learning for academic success, unburdened by financial concerns <br>
- A sense of belonging and community among low income students <br>
- Resource sharing <br>
- Initiative to help by creating incentives such as an opportunity for senior low income students to receive gift cards to purchase food, clothes and supplies by increasing their 'rank' <br>
- Reduction in the opportunity and time costs of finding cost-effective and budget-friendly books and lack of availability in libraries or platforms <br>
- And most importantly, help low income students feel valued in the community and have the ability to contribute <br>
- Reusing textbooks and reducing waste (also lowering printing costs) <br>

‣ See **Devpost project** [page](https://devpost.com/software/resale-revolution) for more details (including future implications, user guide, inspiration and more)

‣ The prompt was
> "Create software that addresses an issue in first generation low income students such as: financial planning, career opportunities, mental health, community building, or an issue found in your community." 

‣ **Video Demo and Pitch**: Click on the image below to find a pitch and video demo of the project: 

[![Image of Video Demo and Pitch](Images/videodempitch.png)](https://youtu.be/M8Gl508-fq4) 

‣ To run the application on your device:  
- Install [DB Browser for SQLite](https://sqlitebrowser.org/) to find saved user signup information (rename the database file in the code as you please) 
- Input the following commands on your terminal (once you create a directory [mkdir] at a location of your choice and are in your newly created directory [cd new_directory_name])

```
git clone https://github.com/V-Mayya/Resale-Revolution
```
Once you are in the repository folder ("Resale Revolution"): 
```
streamlit run empower_hacks_code.py 
```

**Note**: Due to the time-constrained nature under which the software was built, there are several ways to improve the code structure, security, resolution of errors, and exception handling. I will be working to improve these features in the future.

‣ Find the code **[here](empower_hacks_code.py)**. 

‣ Further questions on project background: <br/> 

<details close>
<summary><b>What was this project built with?</b></summary>
<br>
- Coded from scratch and primarily used Python and Streamlit. 
<br>
- Some packages used include numpy, pandas, matplotlib (and others such as time and random). Used SQLite to build a database to store user signup information and use it on other pages in the web app. 
<br>
- Also used the os module as part of this. Incorporated a bit of HTML to make a few changes to the default structure. 
<br>
- Started with a basic web app structure and then added further details. Coded in Visual Code.  
</details>

<details close>
<summary><b>Features and structure of web app</b></summary>
<br>
- Analytics: Buyers track the number of gift cards sent, their monthly savings by purchasing/borrowing textbooks on the web app, gain accomplishments/badges. Sellers/lenders track the number of books loaned/sold, receive badges and ranks (eg: for affordability, lending periods, textbook condition). Both can find out how many they lives were impacted (based on books sold/lent or gift cards sent). Sellers analytics page will be developed. <br>
<br> 
- Select Textbook: (buyer/borrower account) Find textbook matches based on users' backgrounds (eg: university or school and major). Specific seller/lender match after finding appropriate textbooks (textbook match) can be based on similar economic status of a seller/lender and buyer/borrower (the latter will be developed). Obtain images and features of the selected textbook (including textbook condition) and then make a choice to either buy or borrow it. Option to also send virtual gift cards to sellers/lenders. <br>
<br> 
- Ratings & Reviews: Leave ratings and constructive feedback on the seller's services, contributing to the seller's overall rank. <br>
<br> 
- Message: Message other users about receiving books, meeting times, locations and more. Connect with senior university or school students for support and general help. Create a sense of inclusivity - page will be developed. <br>
<br> 
- Profile Settings & Payments: Find profile details such as financial information and questions answered during signup.  The payments page can include the ability to connect to personal bank accounts, gift card providers and more - payments page will be developed. 
</details>

--- 

