class DetmirCategoryURL:

    @staticmethod
    def get(city: str = 'MOW', offset: int = 0):
        return f'https://api.detmir.ru/v2/products?filter=categories[].alias:zdorovyj_perekus_pp;promo:false;withregion:RU-{city}&expand=meta.facet.ages.adults,meta.facet.gender.adults,webp&meta=*&limit=100&offset={offset}&sort=popularity:desc'

