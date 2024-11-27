import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image


st.title("Image cropper")

image_file = st.sidebar.file_uploader(
    label="Envie uma imagem", type=["png", "jpg", "jpeg"]
)
realtime_update = st.sidebar.checkbox("Atualização em tempo real", value=True)
box_color = st.sidebar.color_picker(label="Grupo de cores", value="#0000FF")
aspect_choice = st.sidebar.radio(
    label="Proporção da tela", options=["1:1", "16:9", "4:3"]
)
aspect_dict = {"1:1": (1, 1), "16:9": (16, 9), "4:3": (4, 3)}
aspect_ratio = aspect_dict[aspect_choice]

if image_file:
    image = Image.open(image_file)

    if not realtime_update:
        st.write("Duplo clique para cortar a imagem")

    cropped_image = st_cropper(
        image,
        realtime_update=realtime_update,
        box_color=box_color,
        aspect_ratio=aspect_ratio,
    )

    cropped = cropped_image.thumbnail((350, 350))

    st.image(cropped_image)
