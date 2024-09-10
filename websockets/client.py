import asyncio
import websockets

async def handle_message(message):
    print(message)

async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send("hello")
        try:
            while True:
                message = await websocket.recv()
                await handle_message(message)
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            
asyncio.get_event_loop().run_until_complete(test())