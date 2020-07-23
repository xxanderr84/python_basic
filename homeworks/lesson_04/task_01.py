from sys import argv
from sys import exit


def salary(work_hours: float, work_rate: float, work_bonus: float) -> float:
    return work_hours*work_rate + work_bonus


if len(argv) < 4:
    exit('Не хватает параметров для расчета')

_, salary_param, rate_param, bonus_param, *__ = argv

try:
    salary_param = float(salary_param)
except ValueError:
    print('Не верно указано количесвто рабочих часов')

try:
    rate_param = float(rate_param)
except ValueError:
    print('Не верно указан оклад')

try:
    bonus_param = float(bonus_param)
except ValueError:
    print('Не верно указаан премия')
print(f'Зарплата сотрудника состовляет: {salary(salary_param, rate_param, bonus_param)}')
