import helperfuncs
import distance_matrices
import time
import streamlit as st
st.set_page_config("Smart Pick", page_icon='IVIS_LABS logo.jpg')


st.title('Smart Pick')
st.sidebar.image('IVIS_LABS logo.jpg', width=200)
navbar = st.sidebar.radio('Go to', ['Best Match', 'All Products'], index=0)
st.sidebar.info(("Don't have time to compare prices? We have got you covered, hop on to \"Smart pick\" and compare hundreds of products to save your time and money!!!"))
li = []
if navbar == "Best Match":
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ29MFsduqCtJ24luTzQfTnAIzxwhQgVzny5g&usqp=CAU', width=400)
    ex = st.beta_expander("Search")
    serach_query = ex.text_input("Search")
    submit = ex.button("Search")


    if submit:
        distance_matrices.truncating()
        sq_formatter = helperfuncs.TextFormatting()
        KEYWORD = sq_formatter.SearchStringCompatibility(serach_query)
        li.append(KEYWORD)
        distance_matrices.GetData(KEYWORD, include_features=False)
        #SHAPE = int(input('Enter number of entries you want to compare '))
        matrix = distance_matrices.distance_calc(shape=distance_matrices.num_entries())
        info = st.beta_expander('View search results')
        distance_matrices.compare(matrix, info, confidence_score=0.5, omit=False)
        pog = st.progress(0)
        for i in range(100):
            time.sleep(0.001)
            pog.progress(i + 1)

    else:
        print(submit)
        #distance_matrices.db_disconnect()
        distance_matrices.truncating()
        submit.conjugate()
        serach_query.replace(serach_query, "")

else:
    try:
        distance_matrices.view_db('Search Query')

    except Exception as e:
        print(e)
