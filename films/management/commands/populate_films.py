import csv
from django.core.management.base import BaseCommand
from films.models import Film


class Command(BaseCommand):
    help = "Populates the Film model with initial data from a TSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "file",
            type=str,
            help="Path to the TSV file"
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs["file"]

        try:
            with open(file_path, newline="", encoding="utf-8") as tsvfile:
                reader = csv.DictReader(tsvfile, delimiter=",")

                for row in reader:
                    try:
                        film, created = Film.objects.get_or_create(
                            title=row["English Title"],
                            release_year=int(row["Release Year"])
                        )

                        if created:
                            self.stdout.write(
                                self.style.SUCCESS(f"Created film: {film.title}")
                            )
                        else:
                            self.stdout.write(
                                self.style.WARNING(f"Film already exists: {film.title}")
                            )

                    except Exception as e:
                        self.stdout.write(
                            self.style.WARNING(f"Could not create film: {e}")
                        )

        except FileNotFoundError:
            self.stderr.write(
                self.style.ERROR(f"File not found: {file_path}")
            )

        except Exception as e:
            self.stderr.write(
                self.style.ERROR(f"An error occurred: {e}")
            )