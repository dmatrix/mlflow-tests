import asyncio
import time
from datetime import datetime


async def custom_sleep(n):
    """
    Custom sleep that uses synchronous sleep

    Parameters
    ----------
    n : int
        Sleep for n seconds
    """
    print('SLEEP', datetime.now())
    await asyncio.sleep(n)


async def factorial(name, number):
    """
    A courtine to compute a factorial

    Parameters
    ----------
    name: str
        A label to indicate which coroutine is currently running
    """

    f = 1
    for i in range(2, number + 1):
        print('Task: {}: Compute factorial for: {}'.format(name, i))
        # invoke custom sleep to yield to the next task
        await custom_sleep(2)
        f *= i
    # Print the result after having awakened after sleep
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))


if __name__ == '__main__':

    # Main event loop here that queues the tasks
    start = time.time()
    loop = asyncio.get_event_loop()

    # Create a queue of tasks
    tasks = [
        asyncio.ensure_future(factorial("A", 3)),
        asyncio.ensure_future(factorial("B", 4))
    ]

    # loop until all tasks within the coroutines have been
    # scheduled and completed
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    print("Total time: {}".format(end - start))

