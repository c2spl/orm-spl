import pytest

from app import model
from app import schema


@pytest.fixture
def text() -> str:
    return "hello world."


@pytest.fixture(autouse=True)
@pytest.mark.asyncio
async def init(text: str):
    # all tables
    await model.models.create_all()

    # insert
    note = await model.Note.objects.create(text=text)

    yield

    # delete
    await note.delete()


@pytest.mark.asyncio
async def test_get(text: str):
    """get"""
    note = await model.Note.objects.first()
    assert note.text == text


@pytest.mark.asyncio
async def test_update(text):
    """update"""
    note = schema.Note(text=text)
    default_completed = False

    # select where first
    note = await model.Note.objects.filter(text=note.text).first()
    assert note.completed == default_completed

    # update and object updated
    updated_completed = True
    await note.update(completed=updated_completed)
    assert note.completed == updated_completed
