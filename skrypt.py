import streamlit as st
import transformers as tf

# tytuł
st.title('Zadanie 2 - tłumacz')

# podtytuł
st.subheader('Witaj w translatorze z angielskiego na niemiecki')

# komunikat
st.write('Poniżej znajduje się okolicznościowy mem')

# mem
st.image('https://d-art.ppstatic.pl/kadry/k/r/1/00/77/66603b31e4127_o_large.jpg')

# przycisk
if st.button('Kliknij mnie'):
    st.write('Ta aplikacja została stworzona przez s25238')

translation_options = {
    'en-de': 'Tlumaczenie z angielskiego na niemiecki',
    'default': 'Opcja której jeszcze nie ma'
}

# lista rozwijana
translation_options_selectbox = st.selectbox(
    'Wynierz opcję tłumaczenia',
    translation_options.values()
)


# metoda pomocnicza do mapowania czytelnego tekstu opcji na klucz slownika
def extract_key(val, d):
    for key, value in d.items():
        if value == val:
            return key

# warunek
if extract_key(translation_options_selectbox, translation_options) == 'en-de':

    to_translate = st.text_area('Podaj tekst po angielsku')

    if to_translate:
        translator = tf.pipeline(task='translation', model='Helsinki-NLP/opus-mt-en-de')

        translated = translator(to_translate)

        st.write(translated[0]['translation_text'])

elif extract_key(translation_options_selectbox, translation_options) == 'default':
    st.write('Ta opcja jeszcze nie została dodana')
