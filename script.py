import os
import django

from job.data import companies
from job.data import jobs
from job.data import specialties

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vacancy.settings')
django.setup()

from job.models import Company
from job.models import Specialty
from job.models import Vacancy

if __name__ == '__main__':
    company = Company.objects.bulk_create(
        [
            Company(
                name=comp["title"],

            )
            for comp in companies

        ]

    )

    special = Specialty.objects.bulk_create(
        [
            Specialty(
                title=spec["title"],
                code=spec["code"]
            )
            for spec in specialties

        ]

    )
    vacancy = Vacancy.objects.bulk_create(
        [
            Vacancy(
                title=job['title'],
                specialty=Specialty.objects.get(code=job['cat']),
                company=Company.objects.get(name=job['company']),
                skills='',
                description=job['desc'],
                salary_min=job['salary_from'],
                salary_max=job['salary_to'],
                published_at=job['posted']

            )
            for job in jobs

        ]

    )
