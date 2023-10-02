# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install streamlit
RUN pip install joblib
RUN pip install pefile
#RUN pip install pandas
#RUN pip install numpy
RUN pip install scikit-learn~=1.1.2
RUN pip install Pillow


# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]
