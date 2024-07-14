import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Portfolio - Computer Vision Student", layout="wide")

# Header section
st.title("Welcome to My Portfolio")
st.subheader("A Journey in Computer Vision")

# Sidebar with navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home section
if options == "Home":
    st.write("""
    ## Home
    Welcome to my portfolio website. Here you will find information about my background, 
    skills, and projects in the field of computer vision. Use the navigation bar to explore more!
    """)

# About Me section
elif options == "About Me":
    st.write("""
    ## About Me
    I am a Computer Vision enthusiast with a passion for developing and applying machine learning models to solve real-world problems. 
    I have completed coursework in various aspects of computer vision and have hands-on experience with several projects.
    """)
    st.image(["img1.jpg","img2.jpg","img3.jpg"], width=325)
   
# Projects section
elif options == "Projects":
    st.write("""
    ## Projects
    Here are some of the projects I have worked on:
    """)

    st.write("""
    ### Project 1: Image Classification
    - Developed a convolutional neural network (CNN) model to classify images into various categories.
    - Achieved an accuracy of 90% on the validation dataset.
    - [GitHub Repository](https://github.com/yourusername/project1)
    """)

    st.write("""
    ### Project 2: Object Detection
    - Built an object detection model using YOLOv3 to detect and classify objects in images.
    - Implemented real-time detection using OpenCV.
    - [GitHub Repository](https://github.com/yourusername/project2)
    """)

# Contact section
elif options == "Contact":
    st.write("""
    ## Contact
    Feel free to reach out to me through any of the following platforms:
    """)
    st.write("[LinkedIn](https://www.linkedin.com/in/yourusername)")
    st.write("[GitHub](https://github.com/yourusername)")
    st.write("[Email](mailto:your.email@example.com)")

# Footer
st.markdown("---")
st.markdown("© Avirash Badgainyan")
