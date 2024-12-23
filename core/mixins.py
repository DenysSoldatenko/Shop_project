from django.core.cache import cache

class CacheMixin:
    def set_get_cache(self, query, cache_name, cache_time):
        data = cache.get(cache_name)
        if not data:
            cache.set(cache_name, query, cache_time)
            return query
        return data
