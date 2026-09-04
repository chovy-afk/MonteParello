"""Wires scenario_generator output into TradingAgents.propagate().

Steps 3-4 of the build order: start with a plain sequential loop,
then add asyncio/ThreadPoolExecutor concurrency with a semaphore.
"""
