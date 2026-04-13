from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError
from cfg import DB_CONNSTR


def create_table_spotify_recently_playlist():
    """
    Create the 'spotify_recently_playlist' table in the database if it doesn't exist.

    This function first checks if the table already exists to avoid errors
    and provides clear messages regarding the operation status.

    Returns:
        bool: True if the table exists or was successfully created, False if an error occurred.
        Examples of messages:
        ℹ️ Table 'spotify_recently_playlist' already exists, no creation needed
        True

        📝 Creating table 'spotify_recently_playlist'...
        ✅ Table 'spotify_recently_playlist' created successfully
        True

        ❌ Error creating/verifying table: [error_message]
        False
    """
    engine = None
    try:
        engine = create_engine(DB_CONNSTR)

        inspector = inspect(engine)
        table_exists = inspector.has_table("spotify_recently_playlist")

        if table_exists:
            print("ℹ️ Table 'spotify_recently_playlist' already exists, no creation needed")
            return True

        print("📝 Creating table 'spotify_recently_playlist'...")
        create_table_query = """
        CREATE TABLE spotify_recently_playlist (
            played_at TIMESTAMP PRIMARY KEY,
            artist TEXT,
            track TEXT,
            url TEXT
        );
        """

        with engine.begin() as conn:
            conn.execute(text(create_table_query))

        print("✅ Table 'spotify_recently_playlist' created successfully")
        return True

    except SQLAlchemyError as e:
        print(f"❌ Error creating/verifying table: {e}")
        print(f"   Tipo de error: {type(e).__name__}")

        error_msg = str(e).lower()
        if "password" in error_msg:
            print("   → Posible error: Contraseña incorrecta en DB_CONNSTR")
        elif "connection refused" in error_msg:
            print("   → Posible error: PostgreSQL no está corriendo")
        elif "database" in error_msg and "does not exist" in error_msg:
            print("   → Posible error: La base de datos no existe")
        elif "permission denied" in error_msg:
            print("   → Posible error: El usuario no tiene permisos suficientes")

        return False

    except Exception as e:
        print(f"❌ Error creating/verifying table: {e}")
        return False

    finally:
        if engine:
            engine.dispose()