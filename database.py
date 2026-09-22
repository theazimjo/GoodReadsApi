from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("postgresql://postgres:xiFnU/fe6@ZPsNs@db.lkzhkvcwaifrvkvztftz.supabase.co:5432/postgres")


Base = declarative_base()
Session = sessionmaker()