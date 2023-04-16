
''' 
This is another streamlit app that uses some more advanced functionality such as:
1. multipages
2. session states
3. callback functions
4. caching
5. using custom components (made by community)

'''

import streamlit as st
import pandas as pd


## 1. Multipages

# It is very easy to set up multipages. No extra code needed. Just make a new folder called "pages"
# And create as many python files as the number of pages you'd like.
# Once you run this app, you will see on the sidebar that other pages are displayed



## 2/3. Session states and callback functions

# These two work together to remember a certain state of the application.
# They are a bit tricky to explain in writing.
# To learn about session states and callback functions in detail watch: https://www.youtube.com/watch?v=5l9COMQ3acc


# initialize a session state but using an if condition
if "count" not in st.session_state:
    st.session_state["count"] = 5

# this is a callback function that is called when it is time to update the state
def update_count():
    st.session_state["count"] = st.session_state.new_count

# and here is an example usage
# the function is called with the "on_change" parameter
data = pd.read_csv('JC-202103-citibike-tripdata.csv')
count = st.slider('How many rows would you like to see?', 1, data.shape[0], value=5, on_change=update_count, key="new_count")

data_subset = data.head(st.session_state["count"])
st.dataframe(data_subset)


## 4. Caching

# Streamlit apps run from beginning to end everytime something has changed or a new input is given
# But some functions will take a long time to run, so we wouldn't want them to run unless a new input is passed to them
# We achieve this by using caching.

# Streamlit used to do this with st.cache. Recently it has divided the functionality of this function.
# You can definitely read more about this in the documentation: https://docs.streamlit.io/library/api-reference/performance

# But for now, you should know that you can use the st.experimental_memo decorator for this purpose.


# decorate the function you'd like to cache
@st.experimental_memo
def get_station_rides(start_station):
    subset = data[data['start station name']==start_station]

    return subset

selected_station = st.selectbox(label="Select a start station to get the subset of the data",options=data["start station name"].tolist())

# use the function as you need it
subset = get_station_rides(selected_station)
st.dataframe(subset)



## 5. Using custom components made by the community

# Streamlit lets you build your own components
# and use components made by others
# each component is a bit different so for the easiest implementation, find the docs page of the component
# At the very least you will need to install and import the component
# and call it in your code based on the docs

# This is a custom toggle by CarlosSerrano: https://discuss.streamlit.io/t/streamlit-toggle-switch/32474


# import this new component like a library
import  streamlit_toggle as tog

# use it as shown in its docs
switch=tog.st_toggle_switch(label="On or off?", 
                    key="Key", 
                    default_value=False, 
                    label_after = False, 
                    inactive_color = '#D3D3D3', 
                    active_color="#11567f", 
                    track_color="#29B5E8"
                    )

if switch:
    st.write("It's on!")
else:
    st.write("It's off")

