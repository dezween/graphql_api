# schema.py
import graphene
from models import Character, characters_data

class CharacterType(graphene.ObjectType):
    name = graphene.String(description="The name of the character")
    faculty = graphene.String(description="The faculty of the character")
    description = graphene.String(description="A brief description of the character")
    wand = graphene.String(description="The wand of the character")
    boggart = graphene.String(description="The boggart of the character")
    patronus = graphene.String(description="The patronus of the character")

class Query(graphene.ObjectType):
    character = graphene.List(CharacterType, 
                                name=graphene.String(),
                                faculty=graphene.String(),
                                wand=graphene.String(),
                                boggart=graphene.String(),
                                patronus=graphene.String())

    characters = graphene.List(CharacterType)

    def resolve_character(self, info, **kwargs):
        filtered_characters = characters_data.items()
        for field, value in kwargs.items():
            if value:
                filtered_characters = [(key, char) for key, char in filtered_characters if getattr(char, field) == value]
        return [char for _, char in filtered_characters]

    def resolve_characters(self, info):
        return list(characters_data.items())

schema = graphene.Schema(query=Query)