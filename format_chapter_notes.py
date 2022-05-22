import os
from dotenv import load_dotenv
import glob

from classes.application import Application

app = Application()
app.insert_hyperlinks()