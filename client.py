import asyncio
import traceback

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(command="uv", args=["run", "weather.py"])


async def main():
    print("Starting stdio_client ....................")
    try:
        async with stdio_client(server_params) as (read, write):
            print("Client connecting, creating session")
            async with ClientSession(read, write) as session:
                print("Initializing session")
                await session.initialize()
                print("Listing tools:")
                tools = await session.list_tools()
                print("Available Tools: ", tools)
                print("Calling tool:")
                result = await session.call_tool("get_weather", {"location": "cairo"})
                print("Result: ", result)
    except Exception as ex:
        print("An Error occurred")
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
