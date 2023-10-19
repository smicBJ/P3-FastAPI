

class Helper:

    def __init__(self):
        self.raw_data = self.read_a_file(filename="class_info/data/mock_data.txt")
        self.data = self.clean_up_data()

    @staticmethod
    def read_a_file(filename):
        with open(filename) as file:
            all_lines = file.readlines()
            return all_lines

    def clean_up_data(self):
        data = []
        for athlete in self.raw_data:
            athlete_data = athlete.replace("\n", "")
            athlete_data_list = athlete_data.split(", ")
            data.append({
                "name": athlete_data_list[0],
                "games": athlete_data_list[1],
                "points": athlete_data_list[2]
            })
        return data
