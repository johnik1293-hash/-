import aiosqlite
import os

async def init_db(db_path: str):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    async with aiosqlite.connect(db_path) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                is_premium INTEGER DEFAULT 0,
                used_today INTEGER DEFAULT 0,
                last_used_at TEXT
            );
            """
        )
        await db.commit()

async def get_db(db_path: str):
    return await aiosqlite.connect(db_path)
