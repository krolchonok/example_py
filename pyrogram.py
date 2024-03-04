import asyncio
from pyrogram import Client

api_id = test
api_hash = "test"

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        ...

            
asyncio.run(main())
