import csv
import json

class TrainingDataFormatter:

    def format_all_data(self) -> None:
        labeled_data = self.format_labeled_data('data/training_dataset.csv')
        seed_data = self.convert_seed_data_to_finetuning_format()
        all_data = labeled_data + seed_data

        with open('data/final_finetuning_data.jsonl', 'w', encoding='utf-8') as file:
            for case in all_data:
                json_line = json.dumps(case)
                file.write(json_line + '\n')

    def format_labeled_data(self, file_path) -> list[dict]:
        data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for i, row in enumerate(reader):
                
                print(f'\n\ncase {i+1}:\n')
                print(f'raw data: {row}')

                if row['use'] == '1':                
                    structured_case = self.convert_data_to_finetuning_format(row)
                    print(f'\ntransformed result: {structured_case}')
                    data.append(structured_case)
                else:
                    print('\ncase was labeled to not be used')

        return data

    def convert_data_to_finetuning_format(self, data: dict) -> dict:
        system_data = {"role": "system", "content": "You are Benn Stancil."}
        input_data = "Answer the following question in the style of Benn Stancil: " + data["input"]

        user_data = {"role": "user", "content": input_data}
        assistant_data = {"role": "assistant", "content": data["output"]}
        
        messages_data = {"messages": [system_data, user_data, assistant_data]}
        return messages_data

    def convert_seed_data_to_finetuning_format(self) -> list[dict]:
        with open('seed_examples.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        print(data)

        formatted_data = []
        for case in data:
            formatted_case = self.convert_data_to_finetuning_format(case)
            formatted_data.append(formatted_case)
        
        return formatted_data

TrainingDataFormatter().format_all_data()