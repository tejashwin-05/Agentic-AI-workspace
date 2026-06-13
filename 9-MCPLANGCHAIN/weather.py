from mcp.server import fastmcp 

mcp = fastmcp("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """
    Get the weather for a given location
    """
    return f"The weather in California is sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

