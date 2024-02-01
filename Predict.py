import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np

def show_predict_page():
    st.title("Show Predict Page")

    st.write("This page displays random graphs.")

    # Number of random graphs to display
    num_graphs = st.number_input("Number of Graphs to Display", min_value=1, step=1, value=5)

    for i in range(num_graphs):
        st.subheader(f"Random Graph {i + 1}")

        # Generate random data for the graph
        x = np.linspace(0, 10, 100)
        y = np.random.rand(100)

        # Create a plot using matplotlib
        fig, ax = plt.subplots()
        ax.plot(x, y)

        # Display the plot using Streamlit
        st.pyplot(fig)
