from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_person(self):
        sql = """
        CREATE TABLE IF NOT EXISTS person (                                                
        id BIGSERIAL NOT NULL PRIMARY KEY,
        last_name VARCHAR(50) NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        father_name VARCHAR(50) NOT NULL,
        date_of_birth VARCHAR(50) NOT NULL,
        email VARCHAR(150), 
        phone_number VARCHAR(50) NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def select_phone(self, phone_number):
        sql = "SELECT * FROM person WHERE person.phone_number LIKE $1;"

        return await self.execute(sql, phone_number, fetch=True)

