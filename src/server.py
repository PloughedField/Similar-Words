import json
import time
import logging
logging.basicConfig(level=logging.ERROR,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

class Data:
    def __init__(self):
        try:
            self.txt = open('words_clean.txt', 'r')
            self.file_prime = open('convert_prime_numbers.json', 'r')
            self.dict_prime = json.load(self.file_prime)
            self.file_stats = open('stats.json', 'r')
            self.stats = json.load(self.file_stats)
            self.sort_dict ={}
            self.count_words = 0
        except Exception as err:
            logging.error(err)
            return err

    #get word from file.
    def read_words(self):
        for word in self.txt:
            self.count_words += 1
            self.word_to_json(word.rstrip())
        self.stats["totalWords"] = self.count_words # total word in DB for stats.
        with open('stats.json', 'w')as json_file:
            json.dump(self.stats, json_file, indent=4)
    #calculate the sum of each word and write to the dictionary
    def word_to_json(self,word):
        sum_l = 1
        try:
            for l in word:
                sum_l *= self.dict_prime[l]
        except Exception as err:
            logging.error(err)
            return "Please enter a valid word"

        if sum_l  not in self.sort_dict:
            self.sort_dict[sum_l] = [word]
        else:
            self.sort_dict[sum_l] += [word]

    #save new dictionary in JSON file.
    def save_sorted_words(self):
        with open('new_db.json', 'w')as json_file:
            json.dump(self.sort_dict, json_file)


class Server:

    def __init__(self):
        try:
            self.data_file = open('new_db.json', 'r')
            self.db_words = json.load(self.data_file)
            self.file_prime = open('convert_prime_numbers.json', 'r')
            self.dict_prime = json.load(self.file_prime)
            self.file_stats = open('stats.json', 'r')
            self.stats = json.load(self.file_stats)
            self.sum_letter = 1
            self.totalRequests = 0
        except Exception as err:
            logging.error(err)
            return  err

    # check if the word sum exists in the dictionary
    def similar_words(self,word,start_time):
        self.totalRequests += 1 # total Requests for stats.
        self.stats["totalRequests"] += self.totalRequests
        try:
            for letter in word:
                self.sum_letter *= self.dict_prime[letter]
        except Exception as err:
            logging.error(err)
            return "Please enter a valid word"
        end_time = (time.time_ns() - start_time)
        self.stats["avgProcessingTimeNs"] += [end_time] # avg run time for stats.
        with open('stats.json', 'w')as json_file:
            json.dump(self.stats, json_file, indent=4)
        try:
            # response to client.
            self.db_words[str(self.sum_letter)].remove(word)
            return {"similar": self.db_words[str(self.sum_letter)]}
        except Exception as err:
            logging.error(err)
            return {"similar": []}

    # get statistic
    def metrics(self):
        self.stats["avgProcessingTimeNs"] = [sum(self.stats["avgProcessingTimeNs"])/ len(self.stats["avgProcessingTimeNs"])]

        with open('stats.json', 'w')as json_file:
            json.dump(self.stats, json_file, indent=4)

        return self.stats


