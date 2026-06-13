from langchain_mcp_adapters.client import MultipleMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
load_dotenv()
import asyncio 

async def main():
    client = MultipleMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"],
                "transport":"stdio"
            },
            "weather":{
                "url":"http://localhost:8000/mcp",
                "transport":"streamable-http"
            }
        }
    )
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.3-70b-versatile")
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages":[
            {"role":"user", "content":"What is (3+5)*12?"}
        ]}
    )

    weather_response = await agent.ainvoke(
        {"messages":[
            {"role":"user", "content":"What is the weather in California?"}
        ]}
    )

    print("Math Response:", math_response["messages"][-1].content)
    print("Weather Response:", weather_response["messages"][-1].content)

asyncio.run(main())