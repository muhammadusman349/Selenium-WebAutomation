"""
Task 1:
• Navigate to https://staging.zoneomics.com.
• Get the Title of the page.
• Define a Function which takes Title as an argument and split each character
individually e.g. Test into T, e, s, t and add them to a List and print it.
• Verify that Title of the page contains “Zoneomics” and the size of the List is
greater than or equal to than 51.

"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://staging.zoneomics.com.")

title = driver.title
print(title)


def split_title(title_):
    l = []
    for i in title_:
        l.append(i)
    # t_list = list(title_)
    return l


def verify_title(title_, t_list):
    if "Zoneomics" in title_ and len(t_list)>= 51:
        print("title have Zoneomics")
    else:
        print("Not in failed")


list_of = split_title(title)
verify_title(title, list_of)

driver.quit()