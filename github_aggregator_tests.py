""" The goal of this file is to demonstrate the implementation of the functions
in the github_aggregator file. """

# Modules
import requests
import json
import unittest

# File Imports
from github_aggregator import gather_repos

class TestGitHubAggregator(unittest.TestCase):
    """ This class contains all of the unit tests for the GitHub Aggregator """

    def test_gather_repos(self):
        self.assertEqual(gather_repos('kylerozanitis'), ['DSA', 'expressionevaluator', 'gedcom-parser', 'GitHubApi567', 'hello-world', 'Personal-Website', 'school-data-management-system', 'SSW-567', 'Triangle567'])
        self.assertNotEqual(gather_repos('kylerozanitis'), ['expressionevaluator', 'gedcom-parser', 'GitHubApi567', 'hello-world', 'Personal-Website', 'school-data-management-system', 'SSW-567', 'Triangle567'])
        self.assertEqual(gather_repos('Asupkay'), ['agar.io-clone', 'asupkay.github.io', 'Chirp', 'Code-Jam-Parody', 'Cryptocurrency-Tracker-Vector', 'CryptoPortfolio', 'CS-546-Final-Project', 'CS-546-Web-Programming-I', 'CS-554-Web-Programming-II', 'DiceRoll', 'enlistment', 'friendly-js-primer', 'GameJam7', 'GCP-App-Engine-Node-Tutorial', 'Github-Monitor', 'GitHubApi567', 'Google-Chrome-Extensions', 'Homeless-Shelter-Finder', 'Interview-Practice', 'Interview-Prep', 'NodeJSPractice', 'Raffler', 'React-Redux-Demo', 'Smart-Home', 'SSW-567', 'SSW-567-HW-02a', 'Stock-Tracker', 'ToDone-App', 'ud851-Exercises', 'ud851-Sunshine'])

if __name__ == '__main__':
    unittest.main(exit=False,verbosity=2)