from aiomirai import Event, WsReceiver, MessageChain, SessionApi

api = SessionApi('http://localhost:8080', 'authKey', 10000)
rec = WsReceiver(api)


@rec.on('FriendMessage')
async def _(ev: Event):
    async with api:
        await api.send_friend_message(
            target=ev['sender']['id'],
            message_chain=MessageChain('qwq'),
        )


async def main():
    try:
        await api.auth()
        await api.verify()
        await api.config(enable_websocket=True)
        await rec.run()
    finally:
        await api.release()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
