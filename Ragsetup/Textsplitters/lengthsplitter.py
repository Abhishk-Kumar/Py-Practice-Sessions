from langchain_text_splitters import CharacterTextSplitter
from langchain_groq import ChatGroq

from dotenv import load_dotenv

import os

load_dotenv()

model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

text="""
abhishek@MacBookAir Ragsetup % uv add dotenv,langchain,langchain-community,langchain-groq,langchain-core,langchain-classic 
error: Failed to parse: dotenv,langchain,langchain-community,langchain-groq,langchain-core,langchain-classic
  Caused by: Expected one of @, (, <, =, >, ~, !, ;, found ,
dotenv,langchain,langchain-community,langchain-groq,langchain-core,langchain-classic
      ^
abhishek@MacBookAir Ragsetup % 

uv add does not use commas between package names.
Add packages separated by spaces.

Use this:

uv add python-dotenv langchain langchain-community langchain-groq langchain-core langchain-classic

You also wrote dotenv, but the correct package name is:

python-dotenv

After installing, your pyproject.toml dependencies will update automatically.

abhishek@MacBookAir Docloaders % uv run pypdfloader.py 
/Users/abhishek/Desktop/Abworks/Ragsetup/Docloaders/pypdfloader.py:4: DeprecationWarning: langchain-community is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.
  from langchain_community.document_loaders import PyPdfLoader
Traceback (most recent call last):
  File "/Users/abhishek/Desktop/Abworks/Ragsetup/Docloaders/pypdfloader.py", line 4, in <module>
    from langchain_community.document_loaders import PyPdfLoader
ImportError: cannot import name 'PyPdfLoader' from 'langchain_community.document_loaders' (/Users/abhishek/Desktop/Abworks/Ragsetup/.venv/lib/python3.14/site-packages/langchain_community/document_loaders/__init__.py)
abhishek@MacBookAir Docloaders % 

The class name is wrong.
It should be PyPDFLoader (capital PDF), not PyPdfLoader.

Use:

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("yourfile.pdf")

docs = loader.load()

print(docs)

You may also need to install pypdf:

uv add pypdf

The deprecation warning is only a warning, not the main error.

Yes, langchain-community is being phased out gradually.
Now LangChain is moving integrations into separate dedicated packages.

Earlier:

from langchain_community.document_loaders import PyPDFLoader

New recommended approach is standalone integration packages like:

uv add langchain-pdf

or other provider-specific packages.

But currently, many loaders still work through langchain-community, and PyPDFLoader is still commonly used there. The warning is mainly informing developers about future migration.

Your code is working correctly now since the PDF content and metadata printed successfully.

Current practical setup most developers still use:

"""
splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

# if pdf so split_documents will be used and if text so split_text will be used
result=splitter.split_text(text)
print(result)