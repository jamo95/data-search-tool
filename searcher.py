"""
Provide searcher to search through data
"""

import sys
import json
import constants

class Searcher():

    """Searcher class for searching data from json files"""

    def __init__(self):
        self.user_command = None
        self.json_data_set = {}

        self.user_choices = set([
            constants.SEARCH,
            constants.VIEW_SEARCH_FIELDS
        ])

        self.user_search_terms = {
            "_id": int,
            "url": str,
            "external_id": str,
            "name": str,
            "alias": str,
            "created_at": str,
            "active": bool,
            "verified": bool,
            "shared": bool,
            "locale": str,
            "timezone": str,
            "last_login_at": str,
            "email": str,
            "phone": str,
            "signature": str,
            "organization_id": int,
            "tags": list,
            "suspended": bool,
            "role": str
        }

        self.ticket_search_terms = {
            "_id": str,
            "url": str,
            "external_id": str,
            "created_at": str,
            "type": str,
            "subject": str,
            "description": str,
            "priority": str,
            "status": str,
            "submitter_id": int,
            "assignee_id": int,
            "organization_id": int,
            "tags": list,
            "has_incidents": bool,
            "due_at": str,
            "via": str,
            "requester_id": str
        }

        self.organization_search_terms = {
            "_id": int,
            "url": str,
            "external_id": str,
            "name": str,
            "domain_names": list,
            "created_at": str,
            "details": str,
            "shared_tickets": bool,
            "tags": list
        }

        self.search_options = {
            constants.USER_SEARCH: self.user_search_terms,
            constants.TICKET_SEARCH: self.ticket_search_terms,
            constants.ORGANIZATION_SEARCH: self.organization_search_terms
        }

    # pylint: disable=R0912
    # pylint: disable=R0915
    def run(self):

        """Run search program"""

        # pylint: disable=R1702
        while self.user_command != constants.QUIT:
            try:
                # input user choice
                self.print_instructions()
                self.user_command = input()
                if self.user_command == constants.QUIT:
                    sys.exit(1)
                if self.user_command not in self.user_choices:
                    raise ValueError("Search option does not exist")

                if self.user_command == constants.SEARCH:

                    # user inputs search option
                    print("Select 1) Users or 2) Tickets or 3) Organizations")
                    search_option = input()
                    if search_option == constants.QUIT:
                        sys.exit(1)
                    if search_option not in self.search_options:
                        raise ValueError("Search option does not exist")
                    self.access_data(search_option)

                    # user inputs search term
                    print("Enter search term")
                    search_term = input()
                    if search_term == constants.QUIT:
                        sys.exit(1)
                    if search_term not in self.search_options[search_option]:
                        raise ValueError("Search term does not exist")

                    # user inputs search value
                    print("Enter search value")
                    search_value = input()
                    if search_value == constants.QUIT:
                        sys.exit(1)

                    # boolean for whether search value exists
                    search_value_exists = False

                    # loop through json data set to find match in term and value
                    for json_object in self.json_data_set:
                        search_value_type = self.search_options[search_option][search_term]

                        # handle case of empty values
                        # i.e. no requester_id key and values in ticket data
                        if search_term not in json_object:
                            if not search_value:
                                for key, value in json_object.items():
                                    print("%-*s     %s" % (20, key,value))
                                print("\n")
                                search_value_exists = True

                        # if search value type is a list then input ony needs to
                        # match one value in list
                        elif search_value_type == list:
                            if search_value in json_object[search_term]:
                                for key, value in json_object.items():
                                    print("%-*s     %s" % (20, key,value))
                                print("\n")
                                search_value_exists = True

                        # remaining cases are int or str
                        else:
                            adj_search_value = None
                            # convert to int type if search value type is int
                            if search_value_type == int and search_value.isdigit():
                                adj_search_value = int(search_value)
                            # convert to bool type if search value type is bool
                            elif search_value_type == bool:
                                if search_value == "false" or search_value == "False":
                                    adj_search_value = False
                                elif search_value == "true" or search_value == "True":
                                    adj_search_value = True
                            # rename search_value variable regardless if str
                            else:
                                adj_search_value = search_value

                            if json_object[search_term] == adj_search_value:
                                for key, value in json_object.items():
                                    print("%-*s     %s" % (20, key,value))
                                print("\n")
                                search_value_exists = True

                    # print no results found if key exists but value doesn't
                    if not search_value_exists:
                        print("No results found")

                # display view of searchable fields
                elif self.user_command == constants.VIEW_SEARCH_FIELDS:
                    self.show_searchable_fields()

            # when exception is from quitting
            except SystemExit:
                sys.exit()

            # when exception is an input error
            except ValueError as error_message:
                print("Input error: ", error_message)

            # Enter random input to restart. Inputting quit will exit however.
            print("Enter any input to restart or enter quit to exit")
            self.user_command = input()
            #print extra lines to make output cleaner
            print("\n")

        sys.exit()

    # pylint: disable=R0201
    def print_instructions(self):

        """Display welcome message"""

        print("Welcome to Search")
        print("Type 'quit' to exit at any time, Press 'Enter' to continue")
        print("\n")
        print("    Select search options:")
        print("    * Press 1 to search")
        print("    * Press 2 to view a list of searchable fields")
        print("    Type 'quit' to exit")
        print("    Select search options:")
        print("\n")

    def show_searchable_fields(self):

        """Display searchable fields"""

        print("---------------------------------------------")
        print("Search Users with")
        for user_search_term in self.user_search_terms:
            print(user_search_term)
        print("\n")
        print("---------------------------------------------")
        print("Search Tickets with")
        for ticket_search_term in self.ticket_search_terms:
            print(ticket_search_term)
        print("\n")
        print("---------------------------------------------")
        print("Search Organizations with")
        for organization_search_term in self.organization_search_terms:
            print(organization_search_term)
        print("\n")

    def access_data(self, search_option):

        """Access and return data from relevant json files"""

        if search_option == constants.USER_SEARCH:
            with open("./data/users.json", "r") as file_handle:
                self.json_data_set = json.load(file_handle)
        elif search_option == constants.TICKET_SEARCH:
            with open("./data/tickets.json", "r") as file_handle:
                self.json_data_set = json.load(file_handle)
        elif search_option == constants.ORGANIZATION_SEARCH:
            with open("./data/organizations.json", "r") as file_handle:
                self.json_data_set = json.load(file_handle)

if __name__ == "__main__":
    Searcher().run()
