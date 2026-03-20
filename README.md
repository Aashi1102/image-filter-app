**🖼️** Image Filter App****

A simple and interactive Image Processing Web App built using Streamlit and Pillow (PIL).
This app allows users to upload an image and apply different filters like grayscale, blur, and contour in real-time.

**🚀 Features**

Upload images (.jpg, .png, .jpeg)

Apply filters:

🖤 Grayscale

🌫️ Blur

✏️ Contour

**🖼️ Original view**

Instant preview of processed image

Simple and user-friendly interface

**🛠️ Tech Stack**

Python

Streamlit

Pillow (PIL)

**📂 Project Structure**

├──image_filter.py

├── README.md

**📜 Code Overview**

The app uses Streamlit for UI and Pillow for image processing.
Example snippet:

img = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

if img:
    img = Image.open(img)
    option = st.selectbox("Select Filter", ["ORIGINAL","GRAYSCALE","BLUR","CONTOUR"])

Full code available here: image_filter.py

**⚙️ Installation & Setup**

1. Clone the repository
git clone 
cd image-filter-app
2. Install dependencies
pip install streamlit pillow
3. Run the app
streamlit run day5.py

**📸 How It Works**

Upload an image

Select a filter from dropdown

View the processed image instantly

**🌟 Future Improvements**

Add more filters (Sepia, Edge Detection, Sharpen)

Download processed image option

Drag & drop upload support

Image comparison view (before/after)

**🤝 Contributing**

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

**📄 License**

This project is open-source and available under the MIT License.

**🙌 Author**

Aashi Tomar
