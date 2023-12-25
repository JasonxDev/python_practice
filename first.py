from datetime import datetime, timezone


def create_utc_datetime(year, month, day, hour=0, minute=0, second=0, millisecond=0):
    # Create a datetime object with the provided parameters
    dt = datetime(year, month, day, hour, minute, second, millisecond * 1000)

    # Assuming the provided datetime is in local time, convert it to UTC
    # Note: This assumes your local time is the system's current timezone
    dt_utc = dt.astimezone(timezone.utc)

    # Format the datetime in the specified format
    formatted_utc_datetime = dt_utc.strftime(
        "%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"  # Trim to milliseconds and add 'Z'
    return formatted_utc_datetime


# Example usage
print(create_utc_datetime(2023, 12, 25))  # 2023-12-25T05:00:00.000Z
print(create_utc_datetime(2023, 8, 7))  # 2023-08-07T04:00:00.000Z
