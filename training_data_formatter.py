import csv
import json

class TrainingDataFormatter:

    def format_all_data(self, output_path: str) -> None:
        labeled_data = self.format_labeled_data('data/training_dataset.csv')
        seed_data = self.convert_seed_data_to_finetuning_format('data/seed_examples.json')
        all_data = labeled_data + seed_data

        with open(output_path, 'w', encoding='utf-8') as file:
            for example in all_data:
                json_line = json.dumps(example, ensure_ascii=False)
                file.write(json_line + '\n')

    def format_labeled_data(self, file_path: str) -> list[dict]:
        data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row['use'] == '1':                
                    formatted_example = self.convert_data_to_finetuning_format(row)
                    data.append(formatted_example)

        return data

    def convert_seed_data_to_finetuning_format(self, file_path: str) -> list[dict]:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        formatted_data = []
        for example in data:
            formatted_example = self.convert_data_to_finetuning_format(example)
            formatted_data.append(formatted_example)
        
        return formatted_data

    def convert_data_to_finetuning_format(self, data: dict) -> dict:
        system_data = {"role": "system", "content": "You are Benn Stancil."}
        input_data = "Answer the following question in the style of Benn Stancil: " + data["input"]
        user_data = {"role": "user", "content": input_data}
        assistant_data = {"role": "assistant", "content": data["output"]}
        
        messages_data = {"messages": [system_data, user_data, assistant_data]}
        return messages_data

TrainingDataFormatter().format_all_data('data/final_finetuning_data.jsonl')