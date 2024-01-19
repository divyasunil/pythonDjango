import asyncio
from elasticsearch import AsyncElasticsearch

es = AsyncElasticsearch("localhost")


async def main():
    resp = await es.search(
        index="webinars",
        body={
            "query": {
                "match": {
                    "title": "Python"
                }
            }
        }
    )
    print(resp)


asyncio.run(main())
