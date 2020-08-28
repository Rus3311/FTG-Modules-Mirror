




@register(outgoing=True, pattern=r"^\.snow$")
async def moon(event):
    deq = deque(list("☁️🌦🌧⛈🌩"))
   
   try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return
    deq = deque(list("💨❄️💧⚡️💦"))
    
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return

