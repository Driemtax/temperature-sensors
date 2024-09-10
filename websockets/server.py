import asyncio
import websockets
import temp
import datetime# create handler for each connection
async def handler(websocket, path):
   now = datetime.datetime.now()
   print(f"{now.strftime('%H:%M:%S')}: New Client Connection")
   await websocket.recv()
   first_data = str(temp.get_first_data())
   await websocket.send(first_data)
   average_data = str(temp.get_average_data())
   await websocket.send(average_data)
   
   # close connection to client
   await websocket.close()

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()