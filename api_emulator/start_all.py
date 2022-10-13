import asyncio

from uvicorn import Server, Config

from app_1.main import app as app1
from app_10.main import app as app10
from app_11.main import app as app11
from app_12.main import app as app12
from app_13.main import app as app13
from app_14.main import app as app14
from app_2.main import app as app2
from app_3.main import app as app3
from app_4.main import app as app4
from app_5.main import app as app5
from app_6.main import app as app6
from app_7.main import app as app7
from app_8.main import app as app8
from app_9.main import app as app9

apps = [
    app1,
    app2,
    app3,
    app4,
    app5,
    app6,
    app7,
    app8,
    app9,
    app10,
    app11,
    app12,
    app13,
    app14,
]


class MyServer(Server):
    async def run(self, sockets=None):
        self.config.setup_event_loop()
        return await self.serve(sockets=sockets)


async def run():
    u_apps = []
    for i in range(len(apps)):
        config = Config(f"app_{i + 1}.main:app", host="0.0.0.0",
                        port=8001 + i)
        server = MyServer(config=config)
        u_apps.append(server.run())
    return await asyncio.gather(*u_apps)


if __name__ == '__main__':
    asyncio.run(run())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run())
