import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()
    await nc.connect(servers=["nats://demo.nats.io:4222"])

    async def message_handler(msg):
        subject = msg.subject
        data = msg.data.decode()
        print(f"[Avalanche] {subject}: {data}")

    await nc.subscribe("trinity.events", cb=message_handler)
    print("[+] Avalanche Node Listening...")
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(run())
