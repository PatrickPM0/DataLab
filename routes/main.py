from flask import Blueprint, render_template
import pandas as pd
import json
import plotly.express as px

# Define a Blueprint
main_bp = Blueprint("main", __name__)


# Load the dataset
df = pd.read_csv("data\Student_Mental_Stress_and_Coping_Mechanisms.csv")


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/about")
def about():
    return render_template("about.html")
