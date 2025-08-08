from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

# Timezone keys for creating ZoneInfo objects
zones = (
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi'
)

# Get the current time, in UTC and the in local timezone
# utc_now = datetime.now(tz=timezone.utc)
local_now = datetime.now()
# local_now = local_now.replace(microsecond=0)
local_tz = datetime.now().astimezone().tzinfo
print(f'Today\'s time is: {local_now}')
print(f'The local timezone is: {local_tz}')

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    # required_time = utc_now.astimezone(tz)
    # required_time = datetime.now(tz=tz)
    required_time = local_now.astimezone(tz)
    city = zone.split('/')[-1]
    # print(f'The time in {city} is {required_time.strftime('%Y-%d-%m %H:%M:%S %Z')}')
    print(f'The time in {city} is {required_time.strftime('%m/%d/%Y %H:%M:%S %z %Z')}')

# Alt program, searches through all available time zones
# cities = ['Paris', 'London', 'Hong_Kong', 'Nairobi']
# print()
# print('Available timezone keys')
# print('-' * 23)
#
# for zone_key in sorted(zoneinfo.available_timezones()):
#     if '/' in zone_key:
#         city = zone_key.split('/')
#         # print(city)
#         if city[1] in cities:
#             print(zone_key)
#             tz = zoneinfo.ZoneInfo(zone_key)
#             print(utc_now.astimezone(tz).strftime('%Y-%d-%m %H:%M:%S %Z'))
