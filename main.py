import argparse
import pandas as pd

# Function to preprocess the dataset (you can customize this as needed)
def preprocess_dataset(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)

    # Perform preprocessing operations (example: removing duplicates)
    df.drop_duplicates(inplace=True)

    # Save the preprocessed dataset
    df.to_csv(output_file, index=False)

    print("Dataset preprocessed and saved successfully.")

def main():
    parser = argparse.ArgumentParser(description="Dataset Preprocessing CLI")

    # Add arguments for input and output file paths
    parser.add_argument("input_file", help="Input CSV file for preprocessing")
    parser.add_argument("output_file", help="Output CSV file to save preprocessed data")

    # Parse the arguments
    args = parser.parse_args()

    # Preprocess the dataset
    preprocess_dataset(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
