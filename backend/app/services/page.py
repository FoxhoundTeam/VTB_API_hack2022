from beanie import PydanticObjectId

from app import database, schemes


class PageService:
    async def get_pages(self, version: PydanticObjectId) -> list[schemes.Page]:
        return (
            await database.Page.find(
                database.Page.version == version, projection_model=schemes.Page
            )
            .sort(database.Page.order)
            .to_list()
        )

    async def get_pages_tree(self, version: PydanticObjectId) -> list[schemes.PageTree]:
        pages = (
            await database.Page.find(
                database.Page.version == version, projection_model=schemes.PageTree
            )
            .sort(database.Page.order)
            .to_list()
        )
        tree: list[schemes.PageTree] = []
        parent_indexes: dict[PydanticObjectId, list[int]] = {}
        for page in pages:
            page.disabled = not bool(page.parent)
            if page.parent not in parent_indexes:
                tree.append(page)
                parent_indexes[page.id] = [len(tree) - 1]
            else:
                root = tree[parent_indexes[page.parent][0]]
                parent = root
                for i in parent_indexes[page.parent][1:]:
                    parent = parent.children[i]
                parent.children.append(page)
                parent_indexes[page.id] = parent_indexes[page.parent].copy()
                parent_indexes[page.id].append(len(parent.children) - 1)
        return tree
