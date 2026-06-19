import csv
from functools import reduce

def load_users(path):
  users = []
  with open(path, newline='') as f:
    reader= csv.DictReader(f)
    for row in reader:
      users.append({
          "name": row["Name"],
          "email": row["Email"],
          "age": int(row["Age"]),                       
          "city": row["City"],
          "purchase_amount": float(row["Purchase_Amount"]),
      })
    return users


def get_high_spending_adult_emails(data):

    big_spenders = list(filter(lambda u: u["age"] > 30 and  u["purchase_amount"] > 100, data))
    big_spender_emails = list(map(lambda u: u["email"], big_spenders))

    return big_spender_emails, big_spenders

def get_new_york_users(data):

    New_York_Users = [f"{user['name']}: {user['age']}" for user in data if user["city"] == "New York"]

    return New_York_Users


def total_spent(data):

  return reduce(lambda acc, u: acc + u["purchase_amount"], data, 0.0)


def get_top_5_oldest(data):
  
  sorted_users = sorted(data, key = lambda u: int(u["age"]), reverse=True)[:5]
  return [u["name"] for u in sorted_users]



def main():
    #Loading data
    raw_data = load_users("user_data.csv")
    
    #Running analyses
    big_spender_emails, big_spenders = get_high_spending_adult_emails(raw_data)
    ny_strings = get_new_york_users(raw_data)
    total_sales = total_spent(raw_data)
    top_oldest = get_top_5_oldest(raw_data)
    
    #Printting outputs
    print("=" * 40)
    print("       WEB SCRAPER FINAL REPORT   ")
    print("=" * 40)

    print("Number of users loaded: ", len(raw_data), "users")  
    print("sample:", raw_data[0])

    print(f"\nUsers over 30 years who spent more than $100: {len(big_spenders)} users")
    print(f"\nBig Spender Emails(sample 10):\n {big_spender_emails[:10]}")
    sample_big_spenders = big_spenders[:10]
    print("\nBig Spenders(sample 10):")
    for spender in sample_big_spenders:
        print(spender)

    print(f"\nName and Age of users from New York: {len(ny_strings)}")
    ny_sample = ny_strings[:10]
    for index, user in enumerate(ny_sample, start=1):
       print(f"{index}. {user}")

    print(f"\nTotal purchase amount: {total_sales:.2f}")

    print("\nTop oldest users: ")
    print(top_oldest)
    print("\n")




if __name__ == "__main__":
    main()