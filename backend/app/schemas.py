from pydantic import BaseModel


class LogBase(BaseModel):
    user_agent: str


class LogCreate(LogBase):
    pass


class Log(LogBase):
    id: int
    target_id: int

    class Config:
        orm_mode = True


class TargetBase(BaseModel):
    redirect_by: str


class TargetCreate(TargetBase):
    pass


class DeleteTarget(BaseModel):
    url: str


class Target(TargetBase):
    id: int
    url: str
    is_activate: bool
    logs: list[Log] = []

    class Config:
        orm_mode = True

class UrlError(BaseModel):
    status: str
    problem: str

class DeleteError(BaseModel):
    status: str
    problem: str


