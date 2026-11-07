"""Late-fee calculation for the campus library desk."""


def late_fee(days_late: int, daily_rate: float, grace_days: int = 0) -> float:
    """Return the late fee in dollars for an item returned ``days_late`` days late.

    The first ``grace_days`` days late are free; only the days beyond that are charged.
    Items returned on time or early are never charged.
    """
    if days_late <= 0:
        return 0.0
    chargeable_days = max(0, days_late - grace_days)
    return round(chargeable_days * daily_rate, 2)
