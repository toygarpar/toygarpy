import asyncio


async def fetch_data(delay):
    
    print("veri alınıyor")

    await asyncio.sleep(delay)

    print("veri alındı!")


    return {"data" : "bazı_veriler"}





async def main(msg):
    
    print("start")

    task = fetch_data(2)   #asenkron bir fonku başka fonk içinde çağırmak, başına await yazmak veya task= kullanmak lazım

    result = await task

    print(f"alınan data: {result}")

    print("end")





asyncio.run(main())