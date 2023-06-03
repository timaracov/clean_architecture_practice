import typing as t
from dataclasses import dataclass
from random import randint, uniform, choices


## BAD BAD CODE


ALPH = "qwerypisadfaksjdvmncapdorieqwr"
ALPH += ALPH.upper()


@dataclass
class User:
    id: int

    name: str
    second_name: str
    third_namee: str

    address: str

    wage_per_month: float
    taxes_percent: float
    daily_income: float


    @staticmethod
    def create_fake_user():
        return User(
            randint(0, 100),
            "".join(choices(ALPH, k=5)),
            "".join(choices(ALPH, k=5)),
            "".join(choices(ALPH, k=5)),
            "".join(choices(ALPH, k=5)),
            uniform(200.0, 2000.0),
            uniform(200.0, 2000.0),
            uniform(200.0, 2000.0),
        )


class UserLogic:
    def __init__(self, db_path: str, user: t.Optional[User] = None) -> None:
        self._user = user
        self._db_path = db_path

    def calc_years_wage(self) -> float:
        if self._user is not None:
            return self._user.wage_per_month * 12
        raise ValueError("No user provided")
    
    def calc_monthly_rest_of_wage(self) -> float:
        if self._user is not None:
            return self._user.wage_per_month*(1-self._user.taxes_percent)
        raise ValueError("No user provided")

    def calc_monthly_income(self) -> float:
        if self._user is not None:
            return self._user.daily_income * 30
        raise ValueError("No user provided")
    
    def calc_monthly_rest_of_wage_with_income(self) -> float:
        if self._user is not None:
            return (
                (self._user.wage_per_month + self.calc_monthly_income())
                *(1-self._user.taxes_percent)
            )
        raise ValueError("No user provided")

    def save_to_db(self) -> None:
        with open(self._db_path, "w") as db:
            db.write(User.__dict__.__str__())

    def load_from_db(self) -> User:
        with open(self._db_path) as db:
            _ = db.read()
        return User.create_fake_user()


## GOOD CODE???


@dataclass
class Config:
    DB_PATH: str = "fancy_project.db"



class UserDB:
    @staticmethod
    def save(user: User) -> None:
        with open(Config.DB_PATH, "a") as db_file:
            db_file.write(str(user.__dict__))

    @staticmethod
    def load() -> User:
        with open(Config.DB_PATH) as db_file:
            user_data = db_file.read()
        ...
        return User.create_fake_user()
    

class UserCalculator:
    def __init__(self, user: User) -> None:
        self._user = user

    def calc_years_wage(self) -> float:
        return self._user.wage_per_month * 12
    
    def calc_monthly_rest_of_wage(self):
        return self._user.wage_per_month*(1-self._user.taxes_percent)

    def calc_monthly_income(self):
        return self._user.daily_income * 30
    
    def calc_monthly_rest_of_wage_with_income(self):
        return (
            (self._user.wage_per_month + self.calc_monthly_income())
            *(1-self._user.taxes_percent)
        )

