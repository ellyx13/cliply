from core.services import BaseServices
from db.base import BaseCRUD
from db.engine import app_engine

from .model import Articles as ArticlesModel
from .object import Articles


class ArticleServices(BaseServices):
    def __init__(self, service_name, crud=None):
        super().__init__(service_name, crud)

    async def create(self, article: Articles):
        data = article.to_dict()
        data["created_at"] = self.get_current_datetime()
        data_save = ArticlesModel(**data).model_dump()
        return await self.save(data=data_save)

    async def get_by_url(self, url: str) -> ArticlesModel | None:
        result = await self.get_by_field(data=url, field_name="url", ignore_error=True)
        if result:
            return ArticlesModel(**result)
        return None


article_crud = BaseCRUD(database_engine=app_engine, collection="articles")
article_services = ArticleServices(service_name="articles", crud=article_crud)
