from odp.client import Client
import os

api_key = os.getenv("ODP_KEY")
client = Client(api_key=api_key)

ds = client.dataset("1d801817-742b-4867-82cf-5597673524eb")

df = ds.table.select().all().dataframe()
print(df.head())