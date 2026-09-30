from fastmcp import FastMCP
import random
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

@mcp.tool()
def flip_coin() -> str:
    """Flips a coin"""
    return random.choice(["Heads", "Tails"])

@mcp.tool()
def roll_dice() -> int:
    """Rolls a dice"""
    return random.randint(1, 6)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=6969)
