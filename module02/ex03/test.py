import requests

# api_url = "http://shibe.online/api/shibes?count=1
# param = {"count": 2}
# response = requests.get(api_url, params=param)
# statuscode = response.status_code
# print("status code = ", statuscode)
# response_json = response.json()
# print(response_json)
#################################

# #? solution 1: Fetching the Github API
# def response_with_most_stars():
#     gh_api_url = “https://api.github.com/search/repositories"
#     param = { "q": "stars:>50000"}
#     response = requests.get(gh_api_url, params=param)
#     print(response.text)

#? solution 2: Searching the Github API
def response_with_most_stars():
    gh_api_url = "https://api.github.com/search/repositories"
    param = { "q": "stars:>50000"}
    response = requests.get(gh_api_url, params=param)
    response_json = response.json()["items"]
    print(response_json)
    return response_json



if __name__ == "__main__":
    result = response_with_most_stars()
    print(len(result))
    for res in result:
        language = res["language"]
        stars = res["stargazers_count"]
        name = res["name"]

        print(f"name -> {name}\tlanguage -> {language}\tstars -> {stars}\n")

