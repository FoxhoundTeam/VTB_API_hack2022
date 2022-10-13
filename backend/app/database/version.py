from beanie import Document


class Version(Document):
    name: str
    code: str

    class Settings:
        name = "version_collection"
