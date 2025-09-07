import datetime as dt
from aiosqlite import Connection

DAILY_FREE_LIMIT = 20  # операций в сутки для free

async def check_and_inc(db: Connection, user_id: int) -> bool:
    today = dt.date.today().isoformat()
    async with db.execute("SELECT used_today, last_used_at FROM users WHERE user_id=?", (user_id,)) as cur:
        row = await cur.fetchone()
    if not row:
        await db.execute("INSERT INTO users(user_id, used_today, last_used_at) VALUES(?,?,?)", (user_id, 1, today))
        await db.commit()
        return True
    used, last_date = row
    if last_date != today:
        used = 0
    if used >= DAILY_FREE_LIMIT:
        return False
    await db.execute("UPDATE users SET used_today=?, last_used_at=? WHERE user_id=?", (used+1, today, user_id))
    await db.commit()
    return True
