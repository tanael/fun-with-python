# Fun with python coroutines - asyncio

The preferred way of writing `asyncio` applications using `async`/`await`.

## Coroutines

### Sample `simple.py`

A simple demonstration of `asyncio`, rather useless...

### Sample `sequential.py`

A sequential implementation of `asyncio`, still useless...

### Sample `asynchronous.py`

A truly asynchronous implementation of `asyncio`, at last!

## Awaitables

There are three main types of awaitable objects:

  * `coroutines`
  * `Tasks`
  * `Futures`

### Awaitable coroutine

`Coroutines` can be awaited.

### Awaitable Task

`Tasks` schedule `coroutines` concurrently.

### Awaitable Future

A `Future` is an **eventual result** of an asynchronous operation.

`Futures` are needed to allow callback-based code.
