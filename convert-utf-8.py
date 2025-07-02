def convert_to_utf8(input_path, output_path, source_encoding='utf-16le'):
    with open(input_path, 'r', encoding=source_encoding, errors='ignore') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(line)

if __name__ == "__main__":
    input_file = "all_resources_app-routing-system 1.yaml"  # Replace with your file path
    output_file = "converted_utf8.yaml"
    convert_to_utf8(input_file, output_file)
    print(f"File converted and saved as: {output_file}")

