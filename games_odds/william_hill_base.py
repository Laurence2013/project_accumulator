import datetime
from django.core.urlresolvers import resolve
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill
from games_odds.models import TimeOfRefreshWilliamHill0, TimeOfRefreshWilliamHill1, TimeOfRefreshWilliamHill2, TimeOfRefreshWilliamHill3, TimeOfRefreshWilliamHill4

class WilliamHillBase(ScrapingWilliamHill):

    def get_web_details_0(self, request_info, william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link):
        current_url = resolve(request_info).url_name
        get_refresh_date = self.get_date(current_url)
        is_refresh = self.empty_csv_files(tbody_ids_link, span_ids_link, get_match_odds_link)
        if is_refresh is True:
            context = self.get_context(william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link, get_refresh_date)
            return context
        return None

    def get_web_details_1(self, william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link, TimeOfRefreshWilliamHill):
        get_refresh_date = self.get_refresh(TimeOfRefreshWilliamHill)
        get_file_count = self.get_empty_files(tbody_ids_link, span_ids_link, get_match_odds_link)
        if get_file_count[0] == 3:
            context = {
                'games': self.combine_matches_odds_2(span_ids_link, get_match_odds_link),
                'get_refresh_date': get_refresh_date,
            }
            return context
        if get_file_count[1] == 3:
            context = self.get_context(william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link, get_refresh_date)
            return context
        if get_file_count[1] < 3 or get_file_count[0] < 3:
            is_empty = self.empty_csv_files(tbody_ids_link, span_ids_link, get_match_odds_link)
            if is_empty is True:
                context = self.get_context(william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link, get_refresh_date)
                return context

    def get_refresh(self, TimeOfRefreshWilliamHill):
        if str(TimeOfRefreshWilliamHill) is str('TimeOfRefreshWilliamHill0'):
            get_refresh_date = TimeOfRefreshWilliamHill0.objects.last()
        if TimeOfRefreshWilliamHill is 'TimeOfRefreshWilliamHill1':
            get_refresh_date = TimeOfRefreshWilliamHill1.objects.last()
        if TimeOfRefreshWilliamHill is 'TimeOfRefreshWilliamHill2':
            get_refresh_date = TimeOfRefreshWilliamHill2.objects.last()
        if TimeOfRefreshWilliamHill is 'TimeOfRefreshWilliamHill3':
            get_refresh_date = TimeOfRefreshWilliamHill3.objects.last()
        if TimeOfRefreshWilliamHill is 'TimeOfRefreshWilliamHill4':
            get_refresh_date = TimeOfRefreshWilliamHill4.objects.last()
        return get_refresh_date

    def get_date(self, current_url):
        refresh_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        if current_url is str('william_hill_0'):
            TimeOfRefreshWilliamHill0.objects.all()
            refresh = TimeOfRefreshWilliamHill0(william_hill_id=current_url, date_of_refresh=refresh_time)
            refresh.save()
            get_refresh_date = TimeOfRefreshWilliamHill0.objects.last()
        if current_url is str('william_hill_1'):
            TimeOfRefreshWilliamHill1.objects.all()
            refresh = TimeOfRefreshWilliamHill1(william_hill_id=current_url, date_of_refresh=refresh_time)
            refresh.save()
            get_refresh_date = TimeOfRefreshWilliamHill1.objects.last()
        if current_url is str('william_hill_2'):
            TimeOfRefreshWilliamHill2.objects.all()
            refresh = TimeOfRefreshWilliamHill2(william_hill_id=current_url, date_of_refresh=refresh_time)
            refresh.save()
            get_refresh_date = TimeOfRefreshWilliamHill2.objects.last()
        if current_url is str('william_hill_3'):
            TimeOfRefreshWilliamHill3.objects.all()
            refresh = TimeOfRefreshWilliamHill3(william_hill_id=current_url, date_of_refresh=refresh_time)
            refresh.save()
            get_refresh_date = TimeOfRefreshWilliamHill3.objects.last()
        if current_url is str('william_hill_4'):
            TimeOfRefreshWilliamHill4.objects.all()
            refresh = TimeOfRefreshWilliamHill4(william_hill_id=current_url, date_of_refresh=refresh_time)
            refresh.save()
            get_refresh_date = TimeOfRefreshWilliamHill4.objects.last()
        return get_refresh_date

    def get_empty_files(self, tbody_ids_link, span_ids_link, get_match_odds_link):
        not_empty_files = 0
        empty_files = 0
        for files in self.get_list_file_size(tbody_ids_link, span_ids_link, get_match_odds_link):
            if files != int(0):
                not_empty_files += 1
            if files == int(0):
                empty_files += 1
        return [not_empty_files, empty_files]

    def empty_csv_files(self, tbody_id_links, span_ids_link, get_match_odds_link):
        set_list_empty = list()
        set_list_empty.append(tbody_id_links)
        set_list_empty.append(span_ids_link)
        set_list_empty.append(get_match_odds_link)
        is_empty = self.empty_files(set_list_empty)
        if is_empty is True:
            return True

    def combine_matches_odds(self, william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link):
        links_0 = self.get_tbody(tbody_ids_link, william_hill_link)
        if len(links_0) > 0:
            empty1 = self.save_check_empty(tbody_ids_link, links_0)
        if empty1 is True:
            self.get_span_ids(william_hill_link, tbody_ids_link)
            empty2 = self.save_check_empty(span_ids_link, self.span_id_lists)
            self.clear_list()
        if empty2 is True:
            match_odds = self.get_all_odds_for_match(william_hill_link, tbody_ids_link)
            empty3 = self.save_check_empty(get_match_odds_link, match_odds)
        if empty3 is True:
            context = self.combine_matches_odds_2(span_ids_link, get_match_odds_link)
        return context

    def combine_matches_odds_2(self, span_ids_link, get_match_odds_link):
        get_match = self.get_match(span_ids_link)
        get_odds = self.convert_fraction_to_decimal(get_match_odds_link)
        get_converts = self.create_new_list(get_odds)
        get_combined = self.combine_odds_match(get_match, get_converts)
        return get_combined

    def get_list_file_size(self, tbody_ids_link, span_ids_link, get_match_odds_link):
        file_sizes = []
        get_file_size0 = self.get_file_size(tbody_ids_link)
        get_file_size1 = self.get_file_size(span_ids_link)
        get_file_size2 = self.get_file_size(get_match_odds_link)

        file_sizes.append(get_file_size0)
        file_sizes.append(get_file_size1)
        file_sizes.append(get_file_size2)
        return file_sizes

    def get_context(self, william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link, get_refresh_date):
        return {
            'games': self.combine_matches_odds(william_hill_link, tbody_ids_link, span_ids_link, get_match_odds_link),
            'get_refresh_date': get_refresh_date,
        }
