from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Aishu namdev",
    author_email="ancktd99@gmail.com",
    packages=find_packages(),
    install_requires=[
        "google-genai",
        "langchain",
        "langchain-google-genai",
        "python-dotenv",
        "pypdf",
        "pandas"
    ]
)