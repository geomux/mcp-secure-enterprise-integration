# MCP server handling registration of tools, tooling requests from AI agent, and Identity and Access auth per request
# Uses mcp 4.0 (stateless) for scaleability options (i.e. server running behind a load balancer)

from fastmcp import FastMCP

server = FastMCP("enterprise-integration-mcp-server")


def main():
    server.run(
        transport="http",
        host="0.0.0.0",
        port=9000
    )


if __name__ == "__main__":
    main()
