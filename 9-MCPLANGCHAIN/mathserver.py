from mcp.server import fastmcp 

mcp = fastmcp("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """
    Add two numbers together
    """
    return a + b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    """
    Multiply two numbers together
    """
    return a * b

#The transport="stdio" argument tells the server to:

#Use standard input/output (stdin and stdout) to receive and respond to tool function calls

if __name__ == "__main__":
    mcp.run(transport="stdio")

