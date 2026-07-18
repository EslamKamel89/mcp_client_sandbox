from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather given a location

    Args:
        location (str): location can be city , state , etc..

    Returns:
        str: returns the weather description like the `weather is hot and dry` or `weather is rainy and cloudy`
    """
    return "The weather is hot and dry"


if __name__ == "__main__":
    mcp.run()
