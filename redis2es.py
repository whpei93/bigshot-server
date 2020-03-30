import json

from elasticsearch import Elasticsearch

from utils import init_logger, load_config, init_redis_conn, init_es_conn


def main():
    config = load_config('config.yml')

    log_config = config.get('log')
    log_file = log_config.get('log_file')
    log_level = log_config.get('log_level')
    log_formatter = log_config.get('log_formatter')
    logger = init_logger(log_file, log_level, log_formatter)

    redis_conn = init_redis_conn(config.get('redis'), logger)
    es_conn = init_es_conn(config.get('es'), logger)

    movie_key_list = redis_conn.keys('movie_*')
    for movie_key in movie_key_list:
        if redis_conn.hget(movie_key, "insert2es") == "1":
            continue
        movie_info = redis_conn.hgetall(movie_key)
        movie_url_en = movie_info.get("url")
        movie_url_ch = movie_info.get("movie_url_ch")
        movie_url_ja = movie_info.get("movie_url_ja")
        movie_id = movie_info.get("id")

        if not movie_info.get("movie_info"):
            print(movie_key)
            continue
        movie_detail = json.loads(movie_info.get("movie_info"))
        genres = movie_detail.get('genre')
        genre_list = []
        for k, v in genres.items():
            v.update({'id': k})
            genre_list.append(v)
        movie_detail['genre'] = genre_list

        stars = movie_detail.get('stars')
        star_list = []
        for k, v in stars.items():
            v.update({'id': k})
            star_list.append(v)
        movie_detail['stars'] = star_list

        magnets = movie_detail.get('magnets')
        magnet_list = []
        for k, v in magnets.items():
            magnet_list.append(v)
        movie_detail['magnets'] = magnet_list

        # series = movie_detail.get('series')
        # serie_list = []
        # if series:
        #     for k, v in series.items():
        #         print(movie_key, v)
        #         v.update({'id': k})
        #         serie_list.append(v)
        # movie_detail['series'] = serie_list

        movie_detail['url_ja'] = movie_url_ja
        movie_detail['url_ch'] = movie_url_ch

        if movie_detail['release_date']['value'] == '0000-00-00':
            movie_detail['release_date']['value'] = '1970-01-01'

        es.index("movies", id=movie_id, body=movie_detail)

if __name__ == "__main__":
    main()

