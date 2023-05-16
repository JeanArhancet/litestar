from __future__ import annotations

from dataclasses import dataclass

from litestar import Litestar, post
from litestar.dto.factory import DTOConfig
from litestar.dto.factory.stdlib.dataclass import DataclassDTO


@dataclass
class Person:
    name: str
    age: int
    email: str
    id: int


class ReadDTO(DataclassDTO[Person]):
    config = DTOConfig(exclude={"email"})


class WriteDTO(DataclassDTO[Person]):
    config = DTOConfig(exclude={"id"})


@post("/person", dto=WriteDTO, return_dto=ReadDTO, sync_to_thread=False)
def create_person(data: Person) -> Person:
    # Logic for persisting the person goes here
    return data


app = Litestar(route_handlers=[create_person])
