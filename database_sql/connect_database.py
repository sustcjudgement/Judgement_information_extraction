from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.Age import AgeBean

localhost = "127.0.0.1"
engine = create_engine(
    'mysql+mysqlconnector://root:halo1998@localhost:3306/judgement',echo=True)

metadata = MetaData(engine)

# JudgementTable = Table('total_info', metadata,
#                        Column('Judgement_ID', Integer,primary_key=True),
#                        Column('Area', TEXT),
#                        Column('Job',TEXT),
#                        Column('Age',TEXT),
#                        Column('Time',TEXT),
#                        Column('Money',TEXT),
#                        )
#
# Base = declarative_base()
#
#
# class Judgement(Base):
#     __tablename__ = 'total_info'
#     Judgement_ID = Column(Integer, primary_key=True)
#     Area = Column(TEXT)
#     Job = Column(TEXT)
#     Age = Column(TEXT)
#     Time = Column(TEXT)
#     Money = Column(TEXT)
#
#
# metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
#
#
# def insert_DB(judgements=JudgementBean()):
#     session = DBSession()
#     # 创建新User对象: id自增
#     new_judgement = Judgement(
#
#         # Judgement_ID=judgements.judgement_id,
#         Area=judgements.area,
#         Job=judgements.job,
#         Age=judgements.age,
#         Time=judgements.time,
#         Money=judgements.money
#     )
#     # 添加到session:
#     session.add(new_judgement)
#     # 提交即保存到数据库:
#     session.commit()
#     # 关闭session:
#     session.close()

AreaTable = Table('Age_info', metadata,
                       Column('Judgement_ID', Integer,primary_key=True),
                       # Column('Area', TEXT),
                       # Column('Job',TEXT),
                       Column('Age',TEXT),
                       # Column('Time',TEXT),
                       # Column('Money',TEXT),
                       )

Base = declarative_base()


class Judgement(Base):
    __tablename__ = 'Age_info'
    Judgement_ID = Column(Integer, primary_key=True)
    # Area = Column(TEXT)
    # Job = Column(TEXT)
    Age = Column(TEXT)
    # Time = Column(TEXT)
    # Money = Column(TEXT)


metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


def insert_DB(judgements=AgeBean()):
    session = DBSession()
    # 创建新User对象: id自增
    new_judgement = Judgement(

        # Judgement_ID=judgements.judgement_id,
        # Area=judgements.area,
        # Job=judgements.job,
        Age=judgements.age,
        # Time=judgements.time,
        # Money=judgements.money
    )
    # 添加到session:
    session.add(new_judgement)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

