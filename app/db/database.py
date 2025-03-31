from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_settings
from datetime import datetime

from app.models.user import User

settings = get_settings()

# MongoDB client instance
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

# Collections
users = db.users


# Initialize indexes
async def init_db():
    """Initialize database indexes."""
    # Create unique index on browser_id
    await users.create_index("browser_id", unique=True)


async def close_db_connection():
    """Close database connection."""
    client.close()


async def get_or_create_user(browser_id: str) -> dict:
    """Get or create a user with the given browser_id."""
    # Try to find existing user
    user = await users.find_one({"browser_id": browser_id})

    if user:
        return User(browser_id=user["browser_id"], credits=user["credits"])

    # Create new user with 10 free credits
    new_user = {"browser_id": browser_id, "credits": 10, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()}

    await users.insert_one(new_user)
    return User(browser_id=browser_id, credits=10)


async def update_user_credits(browser_id: str, credits_to_add: int) -> dict:
    """Update user credits."""
    result = await users.find_one_and_update(
        {"browser_id": browser_id}, {"$inc": {"credits": credits_to_add}, "$set": {"updated_at": datetime.utcnow()}}, return_document=True
    )
    return User(browser_id=browser_id, credits=result["credits"])


async def consume_credit(browser_id: str) -> bool:
    """
    Consume one credit from user's account.
    Returns True if successful, False if not enough credits.
    """
    user = await users.find_one({"browser_id": browser_id})
    if not user or user["credits"] < 1:
        return False

    await update_user_credits(browser_id, -1)
    return True
