from ninja import Schema


class FaqsSchema(Schema):
    id: int
    question: str
    answer: str

class FaqCreateSchema(Schema):
    question: str
    answer: str


