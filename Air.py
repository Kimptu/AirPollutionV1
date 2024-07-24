import streamlit as st  # type: ignore ## python -m streamlit run main.py ( This is the command to run our server)

home_page=st.Page(
    page="Views/Home.py", #we are orienting this program to find Home file in the folder called Views
    title="Home", #This is the name of the page
    
    default=True,
)
Contact_us=st.Page(
    page="Views/Contact.py",
    title="Contact_us",
    icon=":material/account_circle:", #This is material that can be found on google and you can add them accordingly
    
)
Data_view=st.Page(
    page="Views/Data.py",
    title="Data view",
    
)

prediction=st.Page(
    page="Views/Prediction.py",
    title="Prediction",
    
)
search=st.Page(
    page="Views/Search.py",
    title="Search",
    
)

chatbot=st.Page(
    page="Views/Chatbot.py",
    title="Chatbot",
    
)

## This is navigation set up without sections and that will show all pages 
#pg=st.navigation(pages=[home_page,Contact_us,Data_view,prediction,search])

## ------------ NAVIGATION SETUP WITH SECTIONS --------------
pg=st.navigation(
    {
        "Home":[home_page,Contact_us],
        "Project":[Data_view,prediction],
        "Search":[search,chatbot],
    }
)


## --- SHARED ON ALL PAGES ----------
st.logo("Assets/logo.jpg")
st.sidebar.text("Powered by Eric Kimptu")
st.write("<h1 style='text-align:center;'> AIR POLLUTION SPIKES MONITORING </h1>", unsafe_allow_html=True)

## This run the navigation 
pg.run()