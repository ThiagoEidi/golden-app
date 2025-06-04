from sqlalchemy.orm import Mapped, mapped_column, registry, validates

from app.utils import sanitizar_name

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    cpf: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]

    @validates('username')
    def validar_username(self, key, name: str) -> str:
        self._ = 'xpto'
        return sanitizar_name(name)
