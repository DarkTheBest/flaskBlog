import os
from dotenv import load_dotenv

load_dotenv()


token = os.environ.get('BOT_API_TOKEN')
admin_id = os.environ.get('ADMIN_ID')
