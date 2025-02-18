from dotenv import load_dotenv
# from flask import Flask, render_template, request
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city=" Walasmulla City"):

     request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'