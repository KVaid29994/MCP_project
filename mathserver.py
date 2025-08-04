from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool(name="add", description="add two numbers together")
def add(a: int, b:int) -> int:
    '''
    add two numbers together
    '''
    return a + b

@mcp.tool(name="multiply", description="multiply two numbers together")
def multiply(a: int, b:int) -> int:
    '''
    multiply two numbers together
    '''
    return a * b
#std io is the default transport for mcp used to communicate with the mcp server using standard input and output

if __name__ == "__main__":
    mcp.run(transport = "stdio")






