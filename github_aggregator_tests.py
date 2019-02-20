""" The goal of this file is to demonstrate the implementation of the functions
in the github_aggregator file. """

# Modules
import requests
import json
import unittest

# File Imports
from github_aggregator import gather_repos, gather_commits, gather_github_info

class TestGitHubAggregator(unittest.TestCase):
    """ This class contains all of the unit tests for the GitHub Aggregator """

    def test_gather_repos(self):
        self.assertEqual(gather_repos('kylerozanitis'), ['DSA', 'expressionevaluator', 'gedcom-parser', 'GitHubApi567', 'hello-world', 'Personal-Website', 'school-data-management-system', 'SSW-567', 'Triangle567'])
        self.assertNotEqual(gather_repos('kylerozanitis'), ['expressionevaluator', 'gedcom-parser', 'GitHubApi567', 'hello-world', 'Personal-Website', 'school-data-management-system', 'SSW-567', 'Triangle567'])
        # self.assertEqual(gather_repos('Asupkay'), ['agar.io-clone', 'asupkay.github.io', 'Chirp', 'Code-Jam-Parody', 'Cryptocurrency-Tracker-Vector', 'CryptoPortfolio', 'CS-546-Final-Project', 'CS-546-Web-Programming-I', 'CS-554-Web-Programming-II', 'DiceRoll', 'enlistment', 'friendly-js-primer', 'GameJam7', 'GCP-App-Engine-Node-Tutorial', 'Github-Monitor', 'GitHubApi567', 'Google-Chrome-Extensions', 'Homeless-Shelter-Finder', 'Interview-Practice', 'Interview-Prep', 'NodeJSPractice', 'Raffler', 'React-Redux-Demo', 'Smart-Home', 'SSW-567', 'SSW-567-HW-02a', 'Stock-Tracker', 'ToDone-App', 'ud851-Exercises', 'ud851-Sunshine'])

    def test_gather_commits(self):
        self.assertEqual(gather_commits('kylerozanitis', 'Triangle567'), ('Triangle567', 11))
        self.assertNotEqual(gather_commits('kylerozanitis', 'Triangle567'), ('Triangle567', 13))
        # self.assertEqual(gather_commits('Asupkay', 'Chirp'), ('Chirp', 2))

    def test_gather_github_info(self):
        self.assertEqual(gather_github_info('kylerozanitis'), [('DSA', 9), ('expressionevaluator', 6), ('gedcom-parser', 30), ('GitHubApi567', 16), ('hello-world', 3), ('Personal-Website', 11), ('school-data-management-system', 7), ('SSW-567', 9), ('Triangle567', 11)])
        self.assertNotEqual(gather_github_info('kylerozanitis'), [('expressionevaluator', 6), ('gedcom-parser', 30), ('GitHubApi567', 12), ('hello-world', 3), ('Personal-Website', 11), ('school-data-management-system', 7), ('SSW-567', 9), ('Triangle567', 11)])
        # self.assertEqual(gather_github_info('Asupkay'), [('agar.io-clone', 30), ('asupkay.github.io', 30), ('Chirp', 2), ('Code-Jam-Parody', 29), ('Cryptocurrency-Tracker-Vector', 30), ('CryptoPortfolio', 15), ('CS-546-Final-Project', 30), ('CS-546-Web-Programming-I', 30), ('CS-554-Web-Programming-II', 30), ('DiceRoll', 18), ('enlistment', 2), ('friendly-js-primer', 6), ('GameJam7', 2), ('GCP-App-Engine-Node-Tutorial', 5), ('Github-Monitor', 30), ('GitHubApi567', 8), ('Google-Chrome-Extensions', 13), ('Homeless-Shelter-Finder', 30), ('Interview-Practice', 11), ('Interview-Prep', 30), ('NodeJSPractice', 7), ('Raffler', 30), ('React-Redux-Demo', 1), ('Smart-Home', 30), ('SSW-567', 9), ('SSW-567-HW-02a', 8), ('Stock-Tracker', 8), ('ToDone-App', 8), ('ud851-Exercises', 30), ('ud851-Sunshine', 30)])

if __name__ == '__main__':
    print("Running Unit Tests...")
    unittest.main(exit=False,verbosity=2)