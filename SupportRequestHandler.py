from collections.abc import Mapping
from typing import List
import re

#simplified input
incoming_support_request = (input("Welcome to AirHelp! How may we help you?") or "THIS IS A DEFAULT, EXEMPLARY REQUEST")

class SupportRequest(Mapping):

    def __init__(self, input_support_request):

        self.input_support_request = input_support_request
        self.tags = []
        self.support_request_word_list = []
        self._storage = self.create_support_request(self.input_support_request)

    def __getitem__(self, key):

        return self._storage[key]

    def __iter__(self):

        return iter(self._storage)

    def __len__(self):

        return len(self._storage)

    def create_support_request(self, input_support_request):

        #rule 1: check if the input contains queries (as opposed to checking if sentence only ENDS in '?')
        if '?' in input_support_request:
            self.tags.append("needs answer")

        # ***other tag rules would go here***

        self.support_request_word_list = self.input_to_word_list(input_support_request)
        create_support_request = {"message" : input_support_request, "tags" : self.tags, "words" : self.support_request_word_list}
        return create_support_request

    def input_to_word_list(self, input_support_request):

        #here we can add different delimiters for splitting text in to words
        input_to_word_list: List[str] = [word for word in re.split(r"[-.?!,|\s]+", input_support_request)]
        return input_to_word_list

r = SupportRequest(incoming_support_request)

#debugging
print(r.get("message"))
print(r.get("tags"))
print(r.get("words"))
print(r)