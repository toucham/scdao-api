#!/usr/bin/env python3

from app.crud.user_crud import create_user
from app.schemas.user_schemas import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="admin@scdao-api.org",
            password="password",
            is_active=True,
            is_superuser=True,
            is_county_authorized=True
        ),
    )


if __name__ == "__main__":
    print("Creating superuser admin@scda-api.org")
    init()
    print("Superuser created")
