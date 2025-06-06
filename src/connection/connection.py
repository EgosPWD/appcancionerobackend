import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client | None = None 
def get_connection() -> Client:
    global supabase

    if not supabase:
        try:
            supabase = create_client(url, key)
        except Exception as e:
            print(f"Error creating Supabase client: {e}")
            supabase = None
    return supabase