'''
github.py contains a handful of methods
for interacting with Github data.
'''

import requests
import simplejson as json

########################
# GITHUB API CONSTANTS #
########################

API_BASE_URL = 'https://api.github.com/users/DrkSephy'

def getUserData(clientID, clientSecret):
	'''Get generic Github User data.'''
	url = API_BASE_URL + '?' + clientID + '&' + clientSecret
	req = requests.get(url)
	jsonList = []
	jsonList.append(json.loads(req.content))
	parsedData = []
	userData = {}
	for data in jsonList: 
		userData['name'] = data['name']
		userData['blog'] = data['blog']
		userData['email'] = data['email']
		userData['public_gists'] = data['public_gists']
		userData['public_repos'] = data['public_repos']
		userData['avatar_url'] = data['avatar_url']
		userData['followers'] = data['followers']
		userData['following'] = data['following']
	parsedData.append(userData)

	return parsedData
	

def getUserRepositories(clientID, clientSecret):
	'''Get a list of all repositories owned by a User.'''

	pageNumber = 1


	jsonList = []
	repositories = []

	while True:
		req = requests.get('https://api.github.com/users/DrkSephy/repos?page=' + str(pageNumber) + '&' + clientID + '&' + clientSecret)
		jsonList.append(json.loads(req.content))
		if len(json.loads(req.content)) < 30:
			break
		elif len(json.loads(req.content)) >= 30:
			pageNumber += 1

	
	for data in jsonList:
		for datum in data:
			repositories.append(datum['name'])
			
	return repositories

def getForkedRepositories(clientID, clientSecret):
	'''Get a list of all forked repositories by a user.'''
	
	pageNumber = 1

	
	jsonList = []

	
	forkedRepositories = []
 
	while True:
		req = requests.get('https://api.github.com/users/DrkSephy/repos?page=' + str(pageNumber) + '&' + clientID + '&' + clientSecret)
		jsonList.append(json.loads(req.content))
		if len(json.loads(req.content)) < 30:
			break
		elif len(json.loads(req.content)) >= 30:
			pageNumber += 1


	forkedRepos = {}
	for data in jsonList:
		for datum in data:
			if datum['fork'] == True:
				forkedRepos['name'] = datum['name']
				forkedRepositories.append(forkedRepos)
				forkedRepos = {}

	return forkedRepositories

def getTopContributedRepositories(repos, clientID, clientSecret):
	'''Get a list of all commits for each repository owned.'''

	jsonList = []
	for repo in repos:
		req = requests.get('https://api.github.com/repos/DrkSephy/' + repo + '/stats/contributors' + '?' + clientID + '&' + clientSecret)
		jsonList.append(json.loads(req.content))

	parsedData = []

	indexNumber = -1
	for item in jsonList:
		indexNumber += 1
		commits = {}
		for data in item:
			if data['author']['login'] == 'DrkSephy':
				commits['author'] = data['author']['login']
				commits['total'] = data['total']
				commits['repo_name'] = repos[indexNumber]
				parsedData.append(commits)

	return parsedData

def filterCommits(data):
	'''Returns the top 10 committed repositories.'''

	maxCommits = []
	for i in range(1, 10):
		maxCommitedRepo = max(data, key=lambda x:x['total'])
		maxCommits.append(maxCommitedRepo)
		index = data.index(maxCommitedRepo)
		data.pop(index)
	return maxCommits
	
	
def getStarGazerCount(clientID, clientSecret):
	'''Get Stargazer counts for all repositories.'''
	
	pageNumber = 1
	jsonList = []
	stargazers = []
	while True:
		req = requests.get('https://api.github.com/users/DrkSephy/repos?page=' + str(pageNumber) + '&' + clientID + '&' + clientSecret)
		jsonList.append(json.loads(req.content))
		if len(json.loads(req.content)) < 30:
			break
		elif len(json.loads(req.content)) >= 30:
			pageNumber += 1


	for data in jsonList:
		for datum in data:
			starData = {}
			starData['stargazers_count'] = datum['stargazers_count']
			starData['name'] = datum['name']
			stargazers.append(starData)
			
	return stargazers

def filterStarGazerCount(data):
	'''Return top 10 starred repositories.'''
	maxStars= []
	for i in range(1, 10):
		maxStarGazers = max(data, key=lambda x:x['stargazers_count'])
		maxStars.append(maxStarGazers)
		index = data.index(maxStarGazers)
		data.pop(index)
	return maxStars




