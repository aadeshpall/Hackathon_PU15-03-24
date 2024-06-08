<h1 align="center">Food Recommendation System</h1>


## :bookmark_tabs:Table of contents
* [Team info](#Team-info)
* [Project info](#Project-info)
* [Technologies](#Technologies)
* [Setup](#setup)

## Team info
### Team Name : ideal bits
Team members : 
* Niranjan Pal
* Pratham Gautam
* Aditya Das
* Divyajeet Parmar

Team No : PU111



## Project info

### What is a food recommendation engine?
Food recommendation systems revolutionize dining experiences by seamlessly blending technology with culinary exploration. These systems harness intricate algorithms and user data to curate personalized suggestions for recipes, restaurants, and dietary plans. From catering to dietary restrictions and cultural preferences to facilitating serendipitous discoveries, they streamline decision-making while enhancing satisfaction. By analyzing past interactions and leveraging cutting-edge machine learning techniques, food recommendation systems empower users to embark on gastronomic journeys tailored to their unique tastes and preferences. With every recommendation, they offer a gateway to a world of culinary delights, making dining more enjoyable, convenient, and fulfilling than ever before.

<div align= "center"><img src="Assets\file_2024-03-15_04.10.43.png" /></div>

### Model developement
The recommendation engine is built using Nearest Neighbors alogrithm which is an unsupervised learner for implementing neighbor searches.

### Dataset
I used Food.com kaggle dataset Data with over 7000+ recipes. Visit this [kaggle](https://www.kaggle.com/datasets/shrutisaxena/food-nutrition-dataset)

### Backend Developement
The application is built using the FastAPI framework, which allows for the creation of fast and efficient web APIs.

### Frontend Developement

The application's front-end is made with Streamlit. Streamlit is an open source app framework in Python language. It helps to create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, NumPy, pandas, Matplotlib etc. 

#### Docker-Compose
My project is composed of different services (frontend,API). Therefore, our application should run on multiple containers. With the help of Docker-compose we can share our application using the yaml file that define the services that runs together.

## Technologies
The project is created with:
* Python: 3.10.8
* fastapi 0.88.0
* uvicorn 0.20.0
* scikit-learn 1.1.3
* Pandas: 1.5.1
* Streamlit: 1.16.0
* streamlit-echarts 1.24.1
* Numpy: 1.21.5
* beautifulsoup4 4.11.1

## Setup

### Run it locally
#### Clone the repo
```
$ git clone https://github.com/aadeshpalpal/Hackathon_PU15-03-24.git
```
### docker-compose
In the project root run:
```
$ docker-compose up -d --build
```
Then open http://localhost:8501

PS: You should have docker and docker-compose
