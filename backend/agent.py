from __future__ import annotations
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import (
    JobContext,
    WorkerOptions,
    cli,
    llm,
    function_tool,
    Agent,
    AgentSession,
    RunContext
)
from livekit.plugins import openai, silero
from api import AssistantFnc
from prompts import WELCOME_MESSAGE, INSTRUCTIONS, LOOKUP_VIN_MESSAGE
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Global assistant function context
assistant_fnc = AssistantFnc()

@function_tool
async def lookup_car(context: RunContext, vin: str) -> str:
    """Lookup a car by its VIN"""
    logger.info(f"Looking up car with VIN: {vin}")
    return await assistant_fnc.lookup_car(vin)

@function_tool
async def get_car_details(context: RunContext) -> str:
    """Get the details of the current car"""
    logger.info("Getting current car details")
    return await assistant_fnc.get_car_details()

@function_tool
async def create_car(context: RunContext, vin: str, make: str, model: str, year: int) -> str:
    """Create a new car entry"""
    logger.info(f"Creating car: {make} {model} {year} with VIN: {vin}")
    return await assistant_fnc.create_car(vin, make, model, year)

class CarAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions=INSTRUCTIONS,
            tools=[lookup_car, get_car_details, create_car],
            # Use OpenAI Realtime API
            llm=openai.realtime.RealtimeModel(
                model="gpt-4o-mini-realtime-preview",
                voice="shimmer",
                temperature=0.8
            )
        )

async def entrypoint(ctx: JobContext):
    logger.info("Agent entrypoint started")
    
    # Connect to the room
    await ctx.connect()
    logger.info("Connected to room")

    # Create the agent
    car_assistant = CarAssistant()
    
    logger.info("Creating AgentSession...")
    
    # Create AgentSession for Realtime API
    session = AgentSession(
        vad=silero.VAD.load()
    )
    
    logger.info("Starting session...")
    
    # Start the session with the agent and room
    await session.start(
        room=ctx.room,
        agent=car_assistant
    )
    
    logger.info("Session started, generating welcome message...")
    
    # Generate initial greeting
    await session.generate_reply(instructions=WELCOME_MESSAGE)
    
    logger.info("Agent is ready and connected!")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))