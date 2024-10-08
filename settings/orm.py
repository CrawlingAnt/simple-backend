from sqlmodel import create_engine,SQLModel,Session

engine = create_engine("mysql://root:a198man204@127.0.0.1:3306/study_system")

def init_db():
    SQLModel.metadata.create_all(engine, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
