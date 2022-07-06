import aiohttp
import asyncio
import time
import requests
import random

start_time = time.time()
apis = ["100", "200", "300", "400", "500", "600", "700"]


# async def main():

#     async with aiohttp.ClientSession() as session:

#         for number in range(1, 5):
#             url = "http://43.204.96.121:80/test"
#             # url = "http://34.125.24.74:9174/character/list"
#             randomAPI = random.choice(apis)
#             print("API: ", randomAPI)
#             async with session.post(url, json={
#                 "api": randomAPI
#             }) as resp:
#                 output = await resp.json()
#                 print(
#                     "Index: {} --> Output: {}".format(number, output["status"]))


# asyncio.run(main())
# print("--- %s seconds ---" % (time.time() - start_time))
# print("==================================================")
# start_time = time.time()

for number in range(1, 5):
    url = "http://43.204.96.121:80/test"
    randomAPI = random.choice(apis)
    print("API: ", randomAPI)
    resp = requests.post(url, json={
        "api": randomAPI
    })
    output = resp.json()
    print(output["status"])

print("--- %s seconds ---" % (time.time() - start_time))
