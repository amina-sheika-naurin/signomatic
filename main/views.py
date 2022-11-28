from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

#for main program
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
# Create your views here.
def index(request):
    return(render(request,"index.html"))


def create(request):
    
    os.system('source ~/miniconda/bin/activate')
    os.system('python3 "/Users/aminasheikanaurin/Documents/sign/djangoSign/main.py"')


    return(render(request,"index.html"))

def train(request):
    
    os.system('source ~/miniconda/bin/activate')
    os.system('python3 "/Users/aminasheikanaurin/Documents/sign/djangoSign/model.py"')


    return(render(request,"index.html"))


def predict(request):
    
    os.system('source ~/miniconda/bin/activate')
    os.system('python3 "/Users/aminasheikanaurin/Documents/sign/djangoSign/predict.py"')


    return(render(request,"index.html"))

def home(request):

    return(render(request,"home.html"))

    

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



#backend codes


