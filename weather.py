from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool(name="get_weather", description="Get the weather for a location")
async def get_weather(location:str)->str:
    """Get the weather location."""
    return "It's always raining in California"

if __name__=="__main__":
    mcp.run(transport="streamable-http") ## runs as a server that can be accessed by a client
    # what is streamable-http?
    #it is a transport that allows the mcp server to be accessed by a client over http
    # why?
    #mcp is a protocol for building agents that can use tools to interact with the world
    # what is a tool?
    #a tool is a function that can be used to interact with the world
    # what is a tool in mcp?
    #a tool is a function that can be used to interact with the world