import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("JIRA_API_TOKEN"))
