import streamlit as st
import requests

st.title("Image Caption Generator (Moondream)")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Caption"):
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
        }

        try:
            response = requests.post(
                "http://localhost:8000/caption/",
                files=files
            )

            st.write("Status code:", response.status_code)
            st.write("Raw response:", response.text)

            if response.ok:
                caption = response.json().get("caption", "No caption returned.")
            else:
                caption = f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            caption = f"Request failed: {e}"

        st.subheader("Caption:")
        st.write(caption)