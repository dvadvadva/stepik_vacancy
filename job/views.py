from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError
from .models import Vacancy, Specialty, Company

specialty = Specialty.objects.all()
all_vacancy = Vacancy.objects.all()
companies = Company.objects.all()


class MainView(View):
    def get(self, request):

        specialty_dict = {}
        for special in specialty:
            count_special = Vacancy.objects.filter(specialty=special.id)
            specialty_dict[special.title] = {'count': count_special.count(), 'code': special.code}

        vacancy_company = {}
        company_id = {}
        for company in companies:
            count_vacancy = Vacancy.objects.filter(company=company.id)
            vacancy_company[company.name] = {'count': count_vacancy.count(), 'id': company.id}
        context = {
            'specialty': specialty_dict,
            'company': vacancy_company,
            'title': 'Джуманджи',
            'company_id': company_id

        }
        return render(request, 'index.html', context=context)


class VacanciesView(View):
    def get(self, request, specialty=None):
        if specialty is not None:
            try:
                category = Specialty.objects.get(code=specialty)
            except Specialty.DoesNotExist:
                raise Http404
        if specialty:
            context = {
                'category': category,
                'vacancy': Vacancy.objects.filter(specialty__code=specialty),
                'title': 'Вакансии | Джуманджи',
                'count': Vacancy.objects.filter(specialty__code=specialty).count()

            }
        else:
            context = {
                'vacancy': all_vacancy,
                'category': 'Все вакансии',
                'title': 'Вакансии | Джуманджи',
                'count': Vacancy.objects.count()
            }
        return render(request, 'vacancies.html', context=context)


class VacancyView(View):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            raise Http404
        context = {
            'vacancy': vacancy,
            'title': 'Вакансия | Джуманджи'
        }
        return render(request, 'vacancy.html', context=context)


class CompanyView(View):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist:
            raise Http404

        count_vacancy = company.vacancies.count()
        context = {
            'company': company,
            'count_vacancy': count_vacancy,
            'vacancies': company.vacancies.all(),
            'title': 'Компания | Джуманджи'

        }
        return render(request, 'company.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('<center><h2> что то сломалось</h2></center>')


def custom_handler500(request):
    return HttpResponseServerError('Внутрення ошибка сервера')
