import pytest
import uuid

from uuid import UUID
from category import Category


class TestCategory:

    def test_name_is_required(self):
        with pytest.raises(
            TypeError,
            match="missing 1 required positional argument: 'name'"
        ):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(
            ValueError,
            match="name must have less than 255 characters"
        ):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="O Aranha")

        assert type(category.id) == UUID

    def test_created_category_with_default_values(self):
        category = Category(name="Aranha")

        assert category.name == "Aranha"
        assert category.description == ""
        assert category.is_active is True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Aranha")

        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        cat_id = uuid.uuid4()

        category = Category(
            id=cat_id,
            name="Aranha",
            description="Filmes em Geral",
            is_active=False,
        )

        assert category.id == cat_id
        assert category.name == "Aranha"
        assert category.description == "Filmes em Geral"
        assert category.is_active is False