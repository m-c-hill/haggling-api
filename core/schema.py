# Pydantic models
from pydantic import BaseModel, Field


# https://stackoverflow.com/questions/70694605/i-want-to-change-api-response-json-in-fastapi-pydantic


class UserSchema(BaseModel):
    pass


class OfferSchema(BaseModel):
    class Config:
        schema_extra = {}  # https://fastapi.tiangolo.com/tutorial/schema-extra-example/


class UserIn(BaseModel):
    pass


class UserOut(BaseModel):
    pass


class UserDB(BaseModel):
    pass


# class State(str, Enum):
#     awaiting_my_acceptance = "AwaitingMyAcceptance"
#     awaiting_their_acceptance = "AwaitingTheirAcceptance"
#     withdrawn_by_me = "WithdrawnByMe"
#     withdrawn_by_them = "WithdrawnByThem"
#     accepted = "Accepted"
#     Cancelled = "cancelled"

# class Action(str, Enum):
#     submit = "Submit"
#     accept = "Accept"
#     cancel = "Cancel"
#     propose_update = "ProposeUpdate"
#     withdraw = "Withdraw"
#     update_private_data = "UpdatePrivateData"
