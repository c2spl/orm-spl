import databases
import orm

database = databases.Database("sqlite:///data/db.sqlite")
models = orm.ModelRegistry(database=database)


class Note(orm.Model):
    tablename = "notes"
    registry = models
    fields = dict(
        id=orm.Integer(primary_key=True),
        text=orm.String(max_length=80),
        completed=orm.Boolean(default=False),
    )
