import aiohttp

async def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Запрос к CoinGecko, статус: {response.status}")  # Проверяем статус запроса
            if response.status == 200:
                data = await response.json()
                print(f"Ответ API: {data}")  # Смотрим, что вернул API
                return data["bitcoin"]["usd"]
            else:
                return None
