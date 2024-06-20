import streamlit as st
import random
from PyDictionary import PyDictionary

dictionary = PyDictionary()

word_list = [
    "aberration", "catalyst", "eccentric", "facetious", "garrulous",
    "haphazard", "juxtapose", "luminous", "nefarious", "obfuscate",
    "pensive", "quintessential", "recalcitrant", "serendipity", "tenacious",
    "ubiquitous", "voracious", "winsome", "xenophobia", "zealous"
]

st.title("Random Words Generator")
st.header("Random Word")

placeholder = st.empty()
st.markdown('Click the **`Generate`** button to generate new word')

if st.button("Generate"):
    random_word = random.choice(word_list)
    meaning = dictionary.meaning(random_word)
    
    with placeholder.container():
        st.header(f"{random_word.capitalize()}")
        if meaning:
            for key, value in meaning.items():
                st.write(f"Meaning: ({key}) {', '.join(value)}")
        else:
            st.write("Meaning not found.")
#https://21520255-cau-1-3.streamlit.app/
