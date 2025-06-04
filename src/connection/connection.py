import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

url = os.getenv("EXPO_PUBLIC_SUPABASE_URL")
key = os.getenv("EXPO_PUBLIC_SUPABASE_ANON_KEY")

supabase: Client = create_client(url, key)


