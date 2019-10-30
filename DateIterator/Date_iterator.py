from datetime import timedelta, date

today = date.today()
today_year = today.year
today_month = today.month
today_day = today.day

YYYY = int(input("pick a year"))
while True:
	if ((today_year < YYYY ) or (YYYY < 1971)):
		print("Enter a valid year before " + str(today_year) + ", and after 1971")
		YYYY = int(input("pick a year"))
	else:
		break


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(YYYY, 1, 1)
end_date = date(YYYY, 12, 31)
for single_date in daterange(start_date, end_date):
    time = single_date.strftime("%Y-%m-%d")
    print(time)

