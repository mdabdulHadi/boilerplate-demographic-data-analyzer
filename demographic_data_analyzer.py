import pandas as pd


def calculate_demographic_data(data, print_data=True):
  # Convert the data to a DataFrame-like structure (list of dictionaries)
  columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
    'salary'
  ]
  df = pd.DataFrame(data, columns=columns)

  # Convert 'hours-per-week' column to numeric with errors='coerce' to handle non-numeric values
  df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = df[df['sex'] == 'Male']['age'].astype(int).mean()

  # What is the percentage of people who have a Bachelor's degree?
  total_people = df.shape[0]
  percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] /
                          total_people) * 100

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?
  higher_education = df[df['education'].isin(
    ['Bachelors', 'Masters', 'Doctorate'])]
  lower_education = df.drop(higher_education.index)

  higher_education_rich_percentage = (
    higher_education[higher_education['salary'] == '>50K'].shape[0] /
    higher_education.shape[0]) * 100
  lower_education_rich_percentage = (
    lower_education[lower_education['salary'] == '>50K'].shape[0] /
    lower_education.shape[0]) * 100

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = df[df['hours-per-week'] == min_work_hours]
  rich_percentage = (
    num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] /
    num_min_workers.shape[0]) * 100

  # What country has the highest percentage of people that earn >50K?
  country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
  highest_earning_country = country_counts.idxmax()
  highest_earning_country_percentage = (country_counts.max() /
                                        total_people) * 100

  # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupation = df[(df['salary'] == '>50K') & (
    df['native-country'] == 'India')]['occupation'].mode()[0]

  # Round the decimals to the nearest tenth
  average_age_men = round(average_age_men, 1)
  percentage_bachelors = round(percentage_bachelors, 1)
  higher_education_rich_percentage = round(higher_education_rich_percentage, 1)
  lower_education_rich_percentage = round(lower_education_rich_percentage, 1)
  rich_percentage = round(rich_percentage, 1)
  highest_earning_country_percentage = round(
    highest_earning_country_percentage, 1)

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich_percentage}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich_percentage}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich_percentage': higher_education_rich_percentage,
    'lower_education_rich_percentage': lower_education_rich_percentage,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
