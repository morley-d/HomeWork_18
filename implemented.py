# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)
