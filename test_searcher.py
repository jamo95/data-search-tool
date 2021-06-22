"""
Testing file
"""

from io import StringIO
import unittest
from unittest.mock import patch
from searcher import Searcher
import test_expected_outputs

class TestSearcher(unittest.TestCase):

    """Class for testing Searcher"""

    def test_quit(self):

        """test quitting"""

        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=StringIO()) as mock_output:
                with patch('builtins.input', return_value=None) as mock_input:
                    mock_input.side_effect = ['quit']
                    Searcher().run()
        # pylint: disable=C0103
        self.maxDiff = None
        self.assertEqual(mock_output.getvalue(), test_expected_outputs.test_quit_output)

    def test_view_search_fields(self):

        """test viewing searchable fields"""

        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=StringIO()) as mock_output:
                with patch('builtins.input', return_value=None) as mock_input:
                    mock_input.side_effect = ['2', 'quit']
                    Searcher().run()
        self.maxDiff = None
        self.assertEqual(mock_output.getvalue(), test_expected_outputs.test_view_search_fields_output)

    def test_search_user(self):

        """test searching users data"""

        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=StringIO()) as mock_output:
                with patch('builtins.input', return_value=None) as mock_input:
                    mock_input.side_effect = ['1','1', '_id', '19', 'quit']
                    Searcher().run()
        self.maxDiff = None
        self.assertEqual(mock_output.getvalue(), test_expected_outputs.test_search_user_output)

    def test_search_tickets(self):

        """test searching tickets data"""

        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=StringIO()) as mock_output:
                with patch('builtins.input', return_value=None) as mock_input:
                    mock_input.side_effect = ['1','2', 'submitter_id', '35', 'quit']
                    Searcher().run()
        self.maxDiff = None
        self.assertEqual(mock_output.getvalue(), test_expected_outputs.test_search_tickets_output)

    def test_search_organizations(self):

        """test searching organizations data"""

        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=StringIO()) as mock_output:
                with patch('builtins.input', return_value=None) as mock_input:
                    mock_input.side_effect = ['1','3', 'shared_tickets', 'False', 'quit']
                    Searcher().run()
        self.maxDiff = None
        self.assertEqual(mock_output.getvalue(), test_expected_outputs.test_search_organizations_output)

if __name__ == '__main__':
    unittest.main()
