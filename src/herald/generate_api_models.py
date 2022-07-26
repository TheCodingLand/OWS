from typing import List
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from devtools import debug
#import sqlalchemy
from sqlalchemy.orm import Session, relationship, sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
engine = create_engine("sqlite://", echo=True)
import db_schema
from glob import glob
LocalSession = sessionmaker(bind=engine)
from db_schema import Base

tables = Base.__subclasses__()

items = dict([(cls.__name__, cls) for cls in tables if isinstance(cls, type)])
for item, value in items.items():
    print (value.__class__)
    if str(value.__class__) == "<class 'sqlalchemy.orm.decl_api.DeclarativeMeta'>":
        pydantic_model = sqlalchemy_to_pydantic(value)
        with open(f'./class_schema/{item}.json', 'w') as f:
            f.write(pydantic_model.schema_json(indent=2))


from datamodel_code_generator.parser.openapi import JsonSchemaParser
for item in glob('./class_schema/*.json'):
    with open(item) as f:
        parser= JsonSchemaParser(f.read())
        code = parser.parse()
        filename = item.replace('./class_schema\\','').replace('.json','')
        with open(f'./api_models/{filename}.py', 'w') as f:
            f.write (code)