from setuptools import setup

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

AUTHOR_USER_NAME = "santhosh102002"
REPO_NAME = "Text-Summarizer"
setup(
    name="textsummarizer",
    version="0.0.0",
    author="Santhosh Kumar Kadiyam",
    author_email="santhosh102002@gmail.com",
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github/com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"

    },

    
)