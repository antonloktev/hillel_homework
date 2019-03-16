import asyncio
import time
import aiohttp


async def get_request(session, url):
    async with session.get(url) as response:
        print('Code {} from {}'.format(response.status, url))


async def download_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(get_request(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = ['https://httpbin.org/get'] * 5
    start = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(urls))
    print('Completed in {} seconds'.format(time.time() - start))
    
# ---------------------
import asyncio
import requests
import time


async def get_request(url):
    requests.get(url)
    print('Request {} completed'.format(url))


if __name__ == "__main__":
	urls = ['https://httpbin.org/get'] * 5
    start = time.time()
    asyncio.get_event_loop().run_until_complete(asyncio.gather(*[get_request(url) for url in urls]))
    print('Completed in {} seconds'.format(time.time() - start))


