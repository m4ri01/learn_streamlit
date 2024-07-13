import streamlit as st
import pandas as pd

st.title("Hello, world! :sunglasses: :wave:")

st.write("halo namaku melki mario gulo")

nama = "yono"

st.write(f"halo {nama}")

st.text("Ini adalah text")
st.write("ini adalah text")

st.markdown("#  __Ini__ adalah markdown")

st.header("ini adalah header")
st.subheader("ini adalah subheader")

df = pd.DataFrame({
    "Nama": ["Melki", "Mario", "Gulo"],
    "Umur": [21, 22, 23]
})

# st.dataframe(df)

# st.table(df)

# st.write(df)

data_dict = {
    "nama": ["melki", "mario", "gulo"],
    "umur": [21, 22, 23]
}
st.json(data_dict)

st.write(data_dict)

# st.image("https://pics.craiyon.com/2023-10-26/1e3aa464d65d4bbc953c3a9ebffc25c8.webp")

# st.video("https://www.youtube.com/watch?v=Rp5vd34d-z4")

tab1,tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Ini adalah tab 1")

with tab2:
    st.write("Ini adalah tab 2")




# st.bar_chart(df.set_index("Nama"), width=1000, height=500)

# df2 = pd.DataFrame({
#     "Nama": ["Melki", "Mario", "Gulo"],
#     "Umur": [21, 22, 23],
#     "Berat": [70, 80, 90]
# })

# st.bar_chart(df2.set_index("Nama"), width=1000, height=500)

# st.bar_chart(df2, x="Nama",y="Berat", width=1000, height=500)



button1 = st.button("Click Me!")

if button1:
    st.write("halo aku sudah di click")

select = st.selectbox("Pilih nama", ["Melki", "Mario", "Gulo"])
st.write(f"Nama yang dipilih adalah {select}")