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
#     gh_api_url = "https://api.github.com/search/repositories"
#     param = { "q": "stars:>50000"}
#     response = requests.get(gh_api_url, params=param)
#     print(response.text)

#? solution 2: Searching the Github API

def create_query(language, min_stars=50000):
	query = f"stars:>{min_stars} "
	for lang in language:
		query += f"language:{lang} "
	return query

def response_with_most_stars(languages, sort = "stars", order = "desc"):
	gh_api_url = "https://api.github.com/search/repositories"
	query = create_query(languages)

	#? Define the parameters we want to be part of our URL
	param = { "q": query, "sort": sort, "order": order}

	#? Pass in the query and the parameters as part of the request.
	response = requests.get(gh_api_url, params=param)
	status_code = response.status_code

	#? Check if the rate limit was hit. Applies only for students running this code
	#? in the in-person course.
	if status_code == 403:
		raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
	if status_code != 200:
		raise RuntimeError(f"An error occurred. HTTP Status Code was: {status_code}.")
	else:
		response_json = response.json()["items"]
		return response_json

if __name__ == "__main__":
	languages = ["python", "Javascript", "Ruby"]
	result = response_with_most_stars(languages)
	for res in result:
		language = res["language"]
		stars = res["stargazers_count"]
		name = res["name"]

		print(f"{name} is a {language} repo with {stars} stars\n")

#! solution 2: Searching the Github API -> 2:38
