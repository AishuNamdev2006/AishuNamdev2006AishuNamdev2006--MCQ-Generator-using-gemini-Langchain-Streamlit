import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from pypdf import PdfReader
from pydantic import BaseModel, Field
from pypdf import PdfReader
load_dotenv()
key=os.getenv("genai_api_key")
print(key)