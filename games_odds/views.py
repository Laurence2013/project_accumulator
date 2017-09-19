import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill
from games_odds.webScraping.decimalToFractionAndStoreInDb import DecimalToFractionAndStoreInDb
from games_odds.webScraping.combineOddsWithItsMatch import CombineOddsWithItsMatch
from games_odds.mainViewsApi.main_views_api import MainViewsApi
from games_odds.models import TimeOfRefresh

class Bookies(TemplateView):
    template_name = 'accumulator/bookies.html'

    def get_context_data(self, **kwargs):
        context = super(Bookies, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class Main_William_Hill(TemplateView, ScrapingWilliamHill):
    template_name = 'accumulator/william_hill/main_william_hill.html'

    def get_context_data(self, **kwargs):
        context = super(Main_William_Hill, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        get_match_dates = str('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/Football.html')

        get_matches = self.get_daily_matches_dates(get_match_dates)
        context = { 'get_matches': get_matches, }
        return render(request, self.template_name, self.get_context_data(**context))

class William_Hill_Games_0(TemplateView, MainViewsApi, ScrapingWilliamHill, DecimalToFractionAndStoreInDb, CombineOddsWithItsMatch):
    template_name = 'accumulator/william_hill/william_hill_0.html'
    base_dir = settings.BASE_DIR

    tbody_ids_link_0 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_0.csv'
    span_ids_link_0 = base_dir + '/games_odds/williamHillFiles/tag_name_span_attr_ids/ids_for_tag_span_link_0.csv'
    get_match_odds_link_0 = base_dir + '/games_odds/williamHillFiles/get_match_odds/get_match_odds_link_0.csv'

    def get_context_data(self, **kwargs):
        context = super(William_Hill_Games_0, self).get_context_data(**kwargs)
        return context

    def get(self, request, refresh_no, *args, **kwargs):
        if int(refresh_no) is int(1):
            refresh_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
            TimeOfRefresh.objects.all()
            refresh = TimeOfRefresh(date_of_refresh=refresh_time)
            refresh.save()
            get_refresh_date = TimeOfRefresh.objects.last()
            is_refresh = self.empty_csv_files()
            if is_refresh is True:
                context = {
                    'games': self.combine_matches_odds('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html'),
                    'get_refresh_date': get_refresh_date,
                }
            return render(request, self.template_name, self.get_context_data(**context))
        else:
            not_empty_files = 0
            empty_files = 0
            for files in self.get_list_file_size():
                if files != int(0):
                    not_empty_files += 1
                if files == int(0):
                    empty_files += 1

            if not_empty_files == 3:
                get_refresh_date = TimeOfRefresh.objects.last()
                context = {
                    'games': self.combine_matches_odds_2(),
                    'get_refresh_date': get_refresh_date,
                }
                return render(request, self.template_name, self.get_context_data(**context))
            if empty_files == 3:
                get_refresh_date = TimeOfRefresh.objects.last()
                context = {
                    'games': self.combine_matches_odds('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html'),
                    'get_refresh_date': get_refresh_date,
                }
                return render(request, self.template_name, self.get_context_data(**context))
            if empty_files < 3 or not_empty_files < 3:
                is_empty = self.empty_csv_files()
                get_refresh_date = TimeOfRefresh.objects.last()
                if is_empty is True:
                    context = {
                        'games': self.combine_matches_odds('http://sports.williamhill.com/bet/en-gb/betting/y/5/tm/0/Football.html'),
                        'get_refresh_date': get_refresh_date,
                    }
            return render(request, self.template_name, self.get_context_data(**context))

    def empty_csv_files(self):
        set_list_empty = list()
        set_list_empty.append(self.tbody_ids_link_0)
        set_list_empty.append(self.span_ids_link_0)
        set_list_empty.append(self.get_match_odds_link_0)
        is_empty = self.empty_files(set_list_empty)
        if is_empty is True:
            return True

    def combine_matches_odds(self, url_link):
        links_0 = self.get_tbody(self.tbody_ids_link_0, url_link)
        if len(links_0) > 0:
            empty1 = self.save_check_empty(self.tbody_ids_link_0, links_0)
        if empty1 is True:
            self.get_span_ids(url_link, self.tbody_ids_link_0)
            empty2 = self.save_check_empty(self.span_ids_link_0, ScrapingWilliamHill.span_id_lists)
            self.clear_list()
        if empty2 is True:
            match_odds = self.get_all_odds_for_match(url_link, self.tbody_ids_link_0)
            empty3 = self.save_check_empty(self.get_match_odds_link_0, match_odds)
        if empty3 is True:
            context = self.combine_matches_odds_2()
        return context

    def combine_matches_odds_2(self):
        get_match = self.get_match(self.span_ids_link_0)
        get_odds = self.convert_fraction_to_decimal(self.get_match_odds_link_0)
        get_converts = self.create_new_list(get_odds)
        get_combined = self.combine_odds_match(get_match, get_converts)
        # context = {'games': list(get_combined),}
        return get_combined

    def get_list_file_size(self):
        file_sizes = []
        get_file_size0 = self.get_file_size(self.tbody_ids_link_0)
        get_file_size1 = self.get_file_size(self.span_ids_link_0)
        get_file_size2 = self.get_file_size(self.get_match_odds_link_0)

        file_sizes.append(get_file_size0)
        file_sizes.append(get_file_size1)
        file_sizes.append(get_file_size2)
        return file_sizes


# tbody_ids_link_1 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_1.csv'
# tbody_ids_link_2 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_2.csv'
# tbody_ids_link_3 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_3.csv'
# tbody_ids_link_4 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_4.csv'
# tbody_ids_link_5 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_5.csv'
# tbody_ids_link_6 = base_dir + '/games_odds/williamHillFiles/tag_name_tbody_attr_ids/ids_for_tag_tbody_link_6.csv'
