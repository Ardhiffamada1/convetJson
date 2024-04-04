import json

def text_to_json(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    data = {}
    for i, line in enumerate(lines):
        data[f"line_{i+1}"] = line.strip()
        data[f"line_{i+1}"] = line.strip()

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON Sukses di convert{output_file}")

def main():
    input_file = input("Pilih file yang mau diconvert (.txt): ")
    output_file = input("Enter the path for the output JSON file: ")
    try:
        text_to_json(input_file, output_file)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
